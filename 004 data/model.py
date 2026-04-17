"""
Modellering – KI-basert prediksjon av sene fakturarbetalinger
Prosjekt: LOG650 – Magnus Ødegård
Datasett:  features.csv  (produsert av eda.py)
"""

import sys
import warnings
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from pathlib import Path

from sklearn.model_selection import train_test_split, RandomizedSearchCV, StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    roc_auc_score, f1_score, precision_score, recall_score,
    accuracy_score, classification_report, confusion_matrix, roc_curve
)
from xgboost import XGBClassifier

warnings.filterwarnings("ignore")

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

# ── Stier ─────────────────────────────────────────────────────────────────────
BASE    = Path(__file__).parent
CSV     = BASE / "features.csv"
RAW_CSV = BASE / "table.csv"
OUTDIR  = BASE / "modell_figurer"
OUTDIR.mkdir(exist_ok=True)

SEED = 42
CV_FOLDS = 5

# ══════════════════════════════════════════════════════════════════════════════
# 1. LAST INN OG FORBERED DATA
# ══════════════════════════════════════════════════════════════════════════════
print("=" * 65)
print("1. DATA – INNLASTING OG SPLITTING")
print("=" * 65)

df = pd.read_csv(CSV)

# Bool-kolonner → int (nødvendig for XGBoost)
bool_cols = df.select_dtypes(include="bool").columns
df[bool_cols] = df[bool_cols].astype(int)

# Ekskluder «Ubetalt»-fakturaer – de har ukjent utfall og er feilmerket
# som klasse 0 (i tide) i features.csv. Les Betalingsstatus fra råfilen.
raw = pd.read_csv(RAW_CSV)
gyldig_idx = raw[raw["Betalingsstatus"] != "Ubetalt"].index
df = df.iloc[gyldig_idx].reset_index(drop=True)
print(f"  29 «Ubetalt»-fakturaer ekskludert – {len(df)} rader brukes til modellering.")

X = df.drop(columns=["er_forsinket"])
y = df["er_forsinket"]

n_pos   = int(y.sum())
n_neg   = int((y == 0).sum())
ratio   = n_neg / n_pos        # brukes som scale_pos_weight i XGBoost

print(f"  Totalt antall fakturaer  : {len(df)}")
print(f"  Betalt i tide  (klasse 0): {n_neg}  ({n_neg/len(df)*100:.1f} %)")
print(f"  Forsinket      (klasse 1): {n_pos}  ({n_pos/len(df)*100:.1f} %)")
print(f"  Antall features          : {X.shape[1]}")
print(f"  Klassevekt XGBoost       : scale_pos_weight = {ratio:.2f}")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=SEED, stratify=y
)
print(f"\n  Treningssett : {len(X_train)} rader  |  Testsett: {len(X_test)} rader")

# Skaler numeriske kolonner (LogReg trenger dette)
num_cols = ["Fakturabeløp (NOK)", "netto_dager", "betalingsfrist_dager",
            "faktura_maned", "faktura_kvartal",
            "Gj.snitt dager forsinket (leverandør)", "Antall fakturaer (leverandør)"]

scaler = StandardScaler()
X_train_sc = X_train.copy()
X_test_sc  = X_test.copy()
X_train_sc[num_cols] = scaler.fit_transform(X_train[num_cols])
X_test_sc[num_cols]  = scaler.transform(X_test[num_cols])

cv = StratifiedKFold(n_splits=CV_FOLDS, shuffle=True, random_state=SEED)

# ══════════════════════════════════════════════════════════════════════════════
# 2. BASELINE-MODELLER  (uten hyperparameterjustering)
# ══════════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 65)
print("2. BASELINE-MODELLER")
print("=" * 65)

baseline_models = {
    "Logistisk regresjon": LogisticRegression(
        class_weight="balanced", max_iter=1000, random_state=SEED
    ),
    "Random Forest": RandomForestClassifier(
        n_estimators=100, class_weight="balanced", random_state=SEED
    ),
    "XGBoost": XGBClassifier(
        n_estimators=100, scale_pos_weight=ratio,
        eval_metric="logloss", random_state=SEED, verbosity=0
    ),
}

baseline_results = {}
for name, model in baseline_models.items():
    if "Logistisk" in name:
        model.fit(X_train_sc, y_train)
        y_pred  = model.predict(X_test_sc)
        y_proba = model.predict_proba(X_test_sc)[:, 1]
    else:
        model.fit(X_train, y_train)
        y_pred  = model.predict(X_test)
        y_proba = model.predict_proba(X_test)[:, 1]

    baseline_results[name] = {
        "AUC-ROC" : round(roc_auc_score(y_test, y_proba), 3),
        "F1-score": round(f1_score(y_test, y_pred), 3),
        "Presisjon": round(precision_score(y_test, y_pred), 3),
        "Recall"  : round(recall_score(y_test, y_pred), 3),
        "Nøyaktighet": round(accuracy_score(y_test, y_pred), 3),
        "model"   : model,
        "y_proba" : y_proba,
        "y_pred"  : y_pred,
    }
    print(f"\n  {name}")
    print(f"    AUC-ROC    : {baseline_results[name]['AUC-ROC']:.3f}   (mål ≥ 0.75)")
    print(f"    F1-score   : {baseline_results[name]['F1-score']:.3f}   (mål ≥ 0.70)")
    print(f"    Presisjon  : {baseline_results[name]['Presisjon']:.3f}")
    print(f"    Recall     : {baseline_results[name]['Recall']:.3f}")
    print(f"    Nøyaktighet: {baseline_results[name]['Nøyaktighet']:.3f}")

# ══════════════════════════════════════════════════════════════════════════════
# 3. HYPERPARAMETERJUSTERING – Random Forest
# ══════════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 65)
print("3. HYPERPARAMETERJUSTERING – Random Forest (RandomizedSearchCV)")
print("=" * 65)

rf_param_grid = {
    "n_estimators"    : [100, 200, 300, 500],
    "max_depth"       : [None, 5, 10, 15, 20],
    "min_samples_split": [2, 5, 10],
    "min_samples_leaf" : [1, 2, 4],
    "class_weight"    : ["balanced", "balanced_subsample"],
}

rf_search = RandomizedSearchCV(
    RandomForestClassifier(random_state=SEED),
    param_distributions=rf_param_grid,
    n_iter=40,
    scoring="roc_auc",
    cv=cv,
    random_state=SEED,
    n_jobs=-1,
    verbose=0,
)
rf_search.fit(X_train, y_train)
best_rf = rf_search.best_estimator_

print(f"  Beste parametre:\n    {rf_search.best_params_}")
print(f"  CV AUC-ROC (trening): {rf_search.best_score_:.3f}")

y_pred_rf  = best_rf.predict(X_test)
y_proba_rf = best_rf.predict_proba(X_test)[:, 1]
rf_tuned = {
    "AUC-ROC"    : round(roc_auc_score(y_test, y_proba_rf), 3),
    "F1-score"   : round(f1_score(y_test, y_pred_rf), 3),
    "Presisjon"  : round(precision_score(y_test, y_pred_rf), 3),
    "Recall"     : round(recall_score(y_test, y_pred_rf), 3),
    "Nøyaktighet": round(accuracy_score(y_test, y_pred_rf), 3),
    "model"      : best_rf,
    "y_proba"    : y_proba_rf,
    "y_pred"     : y_pred_rf,
}
print(f"\n  Random Forest (tunet) – testsett:")
print(f"    AUC-ROC    : {rf_tuned['AUC-ROC']:.3f}   (mål ≥ 0.75)")
print(f"    F1-score   : {rf_tuned['F1-score']:.3f}   (mål ≥ 0.70)")
print(f"    Presisjon  : {rf_tuned['Presisjon']:.3f}")
print(f"    Recall     : {rf_tuned['Recall']:.3f}")

# ══════════════════════════════════════════════════════════════════════════════
# 4. HYPERPARAMETERJUSTERING – XGBoost
# ══════════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 65)
print("4. HYPERPARAMETERJUSTERING – XGBoost (RandomizedSearchCV)")
print("=" * 65)

xgb_param_grid = {
    "n_estimators"    : [100, 200, 300, 500],
    "max_depth"       : [3, 5, 7, 9],
    "learning_rate"   : [0.01, 0.05, 0.1, 0.2, 0.3],
    "subsample"       : [0.6, 0.7, 0.8, 1.0],
    "colsample_bytree": [0.6, 0.7, 0.8, 1.0],
    "scale_pos_weight": [1, round(ratio, 1), round(ratio * 1.5, 1)],
    "min_child_weight": [1, 3, 5],
}

xgb_search = RandomizedSearchCV(
    XGBClassifier(eval_metric="logloss", random_state=SEED, verbosity=0),
    param_distributions=xgb_param_grid,
    n_iter=50,
    scoring="roc_auc",
    cv=cv,
    random_state=SEED,
    n_jobs=-1,
    verbose=0,
)
xgb_search.fit(X_train, y_train)
best_xgb = xgb_search.best_estimator_

print(f"  Beste parametre:\n    {xgb_search.best_params_}")
print(f"  CV AUC-ROC (trening): {xgb_search.best_score_:.3f}")

y_pred_xgb  = best_xgb.predict(X_test)
y_proba_xgb = best_xgb.predict_proba(X_test)[:, 1]
xgb_tuned = {
    "AUC-ROC"    : round(roc_auc_score(y_test, y_proba_xgb), 3),
    "F1-score"   : round(f1_score(y_test, y_pred_xgb), 3),
    "Presisjon"  : round(precision_score(y_test, y_pred_xgb), 3),
    "Recall"     : round(recall_score(y_test, y_pred_xgb), 3),
    "Nøyaktighet": round(accuracy_score(y_test, y_pred_xgb), 3),
    "model"      : best_xgb,
    "y_proba"    : y_proba_xgb,
    "y_pred"     : y_pred_xgb,
}
print(f"\n  XGBoost (tunet) – testsett:")
print(f"    AUC-ROC    : {xgb_tuned['AUC-ROC']:.3f}   (mål ≥ 0.75)")
print(f"    F1-score   : {xgb_tuned['F1-score']:.3f}   (mål ≥ 0.70)")
print(f"    Presisjon  : {xgb_tuned['Presisjon']:.3f}")
print(f"    Recall     : {xgb_tuned['Recall']:.3f}")

# ══════════════════════════════════════════════════════════════════════════════
# 5. SAMMENLIGNING – alle modeller
# ══════════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 65)
print("5. SAMMENLIGNING – ALLE MODELLER")
print("=" * 65)

alle_modeller = {
    "Log.reg (baseline)"  : baseline_results["Logistisk regresjon"],
    "RF (baseline)"       : baseline_results["Random Forest"],
    "XGBoost (baseline)"  : baseline_results["XGBoost"],
    "RF (tunet)"          : rf_tuned,
    "XGBoost (tunet)"     : xgb_tuned,
}

header = f"  {'Modell':<25}  {'AUC-ROC':>8}  {'F1-score':>8}  {'Presisjon':>9}  {'Recall':>8}  {'Nøyaktighet':>11}"
print(header)
print("  " + "-" * (len(header) - 2))
for name, r in alle_modeller.items():
    naa  = "✓" if r["AUC-ROC"] >= 0.75 else " "
    naf  = "✓" if r["F1-score"] >= 0.70 else " "
    print(f"  {name:<25}  {r['AUC-ROC']:>7.3f}{naa}  {r['F1-score']:>7.3f}{naf}  "
          f"{r['Presisjon']:>9.3f}  {r['Recall']:>8.3f}  {r['Nøyaktighet']:>11.3f}")

print(f"\n  (✓ = når benchmark: AUC-ROC ≥ 0.75 og F1-score ≥ 0.70)")

# Velg beste modell basert på AUC-ROC
beste_navn  = max(alle_modeller, key=lambda n: alle_modeller[n]["AUC-ROC"])
beste       = alle_modeller[beste_navn]
print(f"\n  → Beste modell: {beste_navn}  (AUC-ROC = {beste['AUC-ROC']:.3f})")

# ══════════════════════════════════════════════════════════════════════════════
# 6. FIGURER
# ══════════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 65)
print("6. FIGURER")
print("=" * 65)

# ── Figur 10: ROC-kurve – alle modeller ──────────────────────────────────────
fig, ax = plt.subplots(figsize=(8, 6))
colors_map = {
    "Log.reg (baseline)": "steelblue",
    "RF (baseline)"     : "gray",
    "XGBoost (baseline)": "orange",
    "RF (tunet)"        : "green",
    "XGBoost (tunet)"   : "tomato",
}
for name, r in alle_modeller.items():
    fpr, tpr, _ = roc_curve(y_test, r["y_proba"])
    ax.plot(fpr, tpr, label=f"{name}  (AUC = {r['AUC-ROC']:.3f})",
            color=colors_map[name], linewidth=1.8)
ax.plot([0, 1], [0, 1], "k--", linewidth=1, label="Tilfeldig (AUC = 0.50)")
ax.axvline(x=0, color="gray", linewidth=0.5)
ax.set_xlabel("Falskt positiv rate (FPR)")
ax.set_ylabel("Sant positiv rate (TPR  /  Recall)")
ax.set_title("ROC-kurver – alle kandidatmodeller")
ax.legend(fontsize=9)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1.02)
plt.tight_layout()
plt.savefig(OUTDIR / "10_roc_kurver.png", dpi=150)
plt.close()
print("  → Figur lagret: 10_roc_kurver.png")

# ── Figur 11: Stolpediagram – AUC-ROC sammenligning ──────────────────────────
fig, ax = plt.subplots(figsize=(8, 4))
navnene = list(alle_modeller.keys())
auc_verdier = [alle_modeller[n]["AUC-ROC"] for n in navnene]
bar_colors = [colors_map[n] for n in navnene]
bars = ax.bar(navnene, auc_verdier, color=bar_colors, edgecolor="white")
ax.axhline(y=0.75, color="red", linestyle="--", linewidth=1.5, label="Benchmark (0.75)")
ax.set_ylabel("AUC-ROC")
ax.set_title("Modellsammenligning – AUC-ROC")
ax.set_ylim(0.5, 1.0)
ax.legend()
for bar, val in zip(bars, auc_verdier):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.005,
            f"{val:.3f}", ha="center", va="bottom", fontsize=9)
plt.xticks(rotation=15, ha="right")
plt.tight_layout()
plt.savefig(OUTDIR / "11_auc_sammenligning.png", dpi=150)
plt.close()
print("  → Figur lagret: 11_auc_sammenligning.png")

# ── Figur 12: Konfusjonsmatrise – beste modell ───────────────────────────────
cm = confusion_matrix(y_test, beste["y_pred"])
fig, ax = plt.subplots(figsize=(5, 4))
im = ax.imshow(cm, cmap="Blues")
plt.colorbar(im, ax=ax)
ax.set_xticks([0, 1]); ax.set_yticks([0, 1])
ax.set_xticklabels(["Pred: I tide", "Pred: Forsinket"])
ax.set_yticklabels(["Faktisk: I tide", "Faktisk: Forsinket"])
for i in range(2):
    for j in range(2):
        ax.text(j, i, str(cm[i, j]), ha="center", va="center",
                color="white" if cm[i, j] > cm.max() / 2 else "black", fontsize=14)
ax.set_title(f"Konfusjonsmatrise – {beste_navn}")
plt.tight_layout()
plt.savefig(OUTDIR / "12_konfusjonsmatrise.png", dpi=150)
plt.close()
print("  → Figur lagret: 12_konfusjonsmatrise.png")

# ── Figur 13: Feature importance – beste tre-baserte modell ──────────────────
tree_model = (
    beste["model"]
    if hasattr(beste["model"], "feature_importances_")
    else rf_tuned["model"]
)
importances = pd.Series(tree_model.feature_importances_, index=X.columns)
topp15 = importances.nlargest(15)

fig, ax = plt.subplots(figsize=(9, 5))
topp15[::-1].plot(kind="barh", ax=ax, color="steelblue")
ax.set_xlabel("Feature importance")
ax.set_title(f"Topp 15 viktigste features – {beste_navn}")
plt.tight_layout()
plt.savefig(OUTDIR / "13_feature_importance.png", dpi=150)
plt.close()
print("  → Figur lagret: 13_feature_importance.png")

# ── Figur 14: Presisjon / Recall / F1 – sammenligning ────────────────────────
fig, ax = plt.subplots(figsize=(8, 4))
x_pos = np.arange(len(navnene))
w = 0.25
ax.bar(x_pos - w, [alle_modeller[n]["Presisjon"] for n in navnene], w,
       label="Presisjon", color="steelblue")
ax.bar(x_pos,      [alle_modeller[n]["Recall"]    for n in navnene], w,
       label="Recall", color="tomato")
ax.bar(x_pos + w,  [alle_modeller[n]["F1-score"]  for n in navnene], w,
       label="F1-score", color="green")
ax.axhline(y=0.70, color="black", linestyle="--", linewidth=1, label="F1-benchmark (0.70)")
ax.set_xticks(x_pos)
ax.set_xticklabels(navnene, rotation=15, ha="right")
ax.set_ylabel("Score")
ax.set_title("Presisjon, Recall og F1-score – alle modeller")
ax.set_ylim(0, 1.05)
ax.legend()
plt.tight_layout()
plt.savefig(OUTDIR / "14_presisjon_recall_f1.png", dpi=150)
plt.close()
print("  → Figur lagret: 14_presisjon_recall_f1.png")

# ══════════════════════════════════════════════════════════════════════════════
# 7. LAGRE RESULTATER
# ══════════════════════════════════════════════════════════════════════════════
rows = []
for name, r in alle_modeller.items():
    rows.append({
        "Modell"      : name,
        "AUC-ROC"     : r["AUC-ROC"],
        "F1-score"    : r["F1-score"],
        "Presisjon"   : r["Presisjon"],
        "Recall"      : r["Recall"],
        "Nøyaktighet" : r["Nøyaktighet"],
        "Når AUC-mål" : "Ja" if r["AUC-ROC"] >= 0.75 else "Nei",
        "Når F1-mål"  : "Ja" if r["F1-score"] >= 0.70 else "Nei",
    })
res_df = pd.DataFrame(rows)
res_df.to_csv(BASE / "modell_resultater.csv", index=False)
print(f"\n  → Resultater lagret: modell_resultater.csv")

# ══════════════════════════════════════════════════════════════════════════════
# 8. RISIKOKATEGORISERING – 3.5.2
#    Beste modell trenes på hele datasettet og klassifiserer alle 971 fakturaer
# ══════════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 65)
print("8. RISIKOKATEGORISERING AV FAKTURAER  (WBS 3.5.2)")
print("=" * 65)

# Bruk parametrene fra beste søk – tren på hele datasettet for full dekning
final_model = XGBClassifier(
    **{k: v for k, v in xgb_search.best_params_.items()},
    eval_metric="logloss", random_state=SEED, verbosity=0
)
final_model.fit(X, y)
alle_proba = final_model.predict_proba(X)[:, 1]

# Terskler for risikokategorier
# Lav: p < 0.30 | Middels: 0.30–0.55 | Høy: ≥ 0.55
TERSKEL_LAV  = 0.30
TERSKEL_HOY  = 0.55

def kategoriser(p):
    if p < TERSKEL_LAV:
        return "Lav"
    elif p < TERSKEL_HOY:
        return "Middels"
    else:
        return "Høy"

risiko_df = df.copy()
risiko_df["p_forsinket"]       = alle_proba.round(4)
risiko_df["risikoklasse"]      = [kategoriser(p) for p in alle_proba]
risiko_df["faktisk_forsinket"] = y.values

# Oppsummering
kat_fordeling = risiko_df["risikoklasse"].value_counts().reindex(["Lav", "Middels", "Høy"])
print(f"\n  Terskler: Lav < {TERSKEL_LAV}  |  Middels {TERSKEL_LAV}–{TERSKEL_HOY}  |  Høy ≥ {TERSKEL_HOY}")
print(f"\n  {'Risikoklasse':<12}  {'Antall':>8}  {'Andel':>7}  {'Faktisk forsinket %':>20}")
for kat in ["Lav", "Middels", "Høy"]:
    gruppe = risiko_df[risiko_df["risikoklasse"] == kat]
    n      = len(gruppe)
    pct    = n / len(risiko_df) * 100
    faktisk_pct = gruppe["faktisk_forsinket"].mean() * 100 if n > 0 else 0
    print(f"  {kat:<12}  {n:>8}  {pct:>6.1f}%  {faktisk_pct:>19.1f}%")

# Lagre klassifisering
risiko_df[["p_forsinket", "risikoklasse", "faktisk_forsinket",
           "Fakturabeløp (NOK)", "netto_dager", "Gj.snitt dager forsinket (leverandør)"]
         ].to_csv(BASE / "risiko_klassifisering.csv", index=False)
print(f"\n  → Klassifisering lagret: risiko_klassifisering.csv")

# ── Figur 15: Fordeling risikokategorier ─────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(11, 4))

# Søylediagram – antall per kategori
kat_farger = {"Lav": "steelblue", "Middels": "orange", "Høy": "tomato"}
bars = axes[0].bar(kat_fordeling.index, kat_fordeling.values,
                   color=[kat_farger[k] for k in kat_fordeling.index])
axes[0].set_ylabel("Antall fakturaer")
axes[0].set_title("Fordeling av risikokategorier")
for bar, val in zip(bars, kat_fordeling.values):
    axes[0].text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 3,
                 str(val), ha="center", va="bottom", fontsize=11)

# Andel faktisk forsinkede per risikoklasse
faktisk_per_kat = (risiko_df.groupby("risikoklasse")["faktisk_forsinket"]
                   .mean() * 100).reindex(["Lav", "Middels", "Høy"])
bars2 = axes[1].bar(faktisk_per_kat.index, faktisk_per_kat.values,
                    color=[kat_farger[k] for k in faktisk_per_kat.index])
axes[1].set_ylabel("Andel faktisk forsinkede (%)")
axes[1].set_title("Faktisk forsinkelsesrate per risikoklasse")
axes[1].yaxis.set_major_formatter(mticker.FormatStrFormatter("%.0f%%"))
for bar, val in zip(bars2, faktisk_per_kat.values):
    axes[1].text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5,
                 f"{val:.1f}%", ha="center", va="bottom", fontsize=11)
plt.tight_layout()
plt.savefig(OUTDIR / "15_risikokategorier.png", dpi=150)
plt.close()
print("  → Figur lagret: 15_risikokategorier.png")

# ── Figur 16: Histogram – fordeling av predikert sannsynlighet ───────────────
fig, ax = plt.subplots(figsize=(8, 4))
ax.hist(risiko_df[risiko_df["faktisk_forsinket"] == 0]["p_forsinket"],
        bins=30, alpha=0.6, color="steelblue", label="Faktisk: I tide")
ax.hist(risiko_df[risiko_df["faktisk_forsinket"] == 1]["p_forsinket"],
        bins=30, alpha=0.6, color="tomato", label="Faktisk: Forsinket")
ax.axvline(TERSKEL_LAV, color="orange", linestyle="--", linewidth=1.5,
           label=f"Terskel Lav/Middels ({TERSKEL_LAV})")
ax.axvline(TERSKEL_HOY, color="red", linestyle="--", linewidth=1.5,
           label=f"Terskel Middels/Høy ({TERSKEL_HOY})")
ax.set_xlabel("Predikert sannsynlighet for sen betaling")
ax.set_ylabel("Antall fakturaer")
ax.set_title("Fordeling av predikert risikosannsynlighet")
ax.legend(fontsize=9)
plt.tight_layout()
plt.savefig(OUTDIR / "16_sannsynlighet_fordeling.png", dpi=150)
plt.close()
print("  → Figur lagret: 16_sannsynlighet_fordeling.png")

# ── Figur 17: Risikoprofil etter fakturabeløp ─────────────────────────────────
fig, ax = plt.subplots(figsize=(8, 4))
for kat, farge in kat_farger.items():
    sub = risiko_df[risiko_df["risikoklasse"] == kat]
    ax.scatter(sub["Fakturabeløp (NOK)"] / 1000, sub["p_forsinket"],
               alpha=0.4, s=20, color=farge, label=kat)
ax.axhline(TERSKEL_LAV, color="orange", linestyle="--", linewidth=1)
ax.axhline(TERSKEL_HOY, color="red",    linestyle="--", linewidth=1)
ax.set_xlabel("Fakturabeløp (TNOK)")
ax.set_ylabel("Predikert sannsynlighet for forsinkelse")
ax.set_title("Risiko vs. fakturabeløp – alle fakturaer")
ax.legend(title="Risikoklasse")
plt.tight_layout()
plt.savefig(OUTDIR / "17_risiko_vs_belop.png", dpi=150)
plt.close()
print("  → Figur lagret: 17_risiko_vs_belop.png")

# ══════════════════════════════════════════════════════════════════════════════
# 9. FORKLARINGER – YTELSESMÅL, ALGORITMER OG BEGREPER
# ══════════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 65)
print("9. FORKLARINGER – YTELSESMÅL, ALGORITMER OG BEGREPER")
print("=" * 65)

forklaringer = """
  ── YTELSESMÅL ────────────────────────────────────────────────────

  AUC-ROC (Area Under the Receiver Operating Characteristic Curve)
  ─────────────────────────────────────────────────────────────────
  Måler modellens evne til å skille mellom «Forsinket» og «I tide»
  på tvers av ALLE mulige klassifiseringsgrenser (ikke bare én).
  ROC-kurven plotter TPR (recall) mot FPR for alle terskler.
  • 1.0 = perfekt modell  |  0.5 = tilfeldig gjetting
  • Benchmark i dette prosjektet: ≥ 0.75  (Appel et al., 2020)
  • Fordel: robust mot klasseubalanse – påvirkes ikke av at de fleste
    fakturaer er «I tide».
  • I dette prosjektet: beste AUC = 0.720 (XGBoost tunet) → noe
    under benchmark, men meningsfull evne til å skille klassene.

  F1-score
  ─────────────────────────────────────────────────────────────────
  Harmonisk gjennomsnitt av presisjon og recall.
  F1 = 2 × (Presisjon × Recall) / (Presisjon + Recall)
  • 1.0 = perfekt  |  0.0 = verdiløs modell  |  Benchmark: ≥ 0.70
  • Nyttig når både falske positive og falske negative er kostbare.
  • I dette prosjektet: beste F1 = 0.621 → modellen fanger opp
    83 % av forsinkede fakturaer, men genererer også en del
    falske alarmer (presisjon 0.495).

  Presisjon
  ─────────────────────────────────────────────────────────────────
  Av alle fakturaer modellen flagget som «Forsinket», hvor mange
  var faktisk forsinkede?  →  Presisjon = TP / (TP + FP)
  • Høy presisjon → færre falske alarmer.
  • I dette prosjektet: ~0.49–0.53 – omtrent annenhver flagget
    faktura er faktisk forsinket.

  Recall (sensitivitet / sant positiv rate – TPR)
  ─────────────────────────────────────────────────────────────────
  Av alle fakturaer som faktisk ble forsinket, hvor mange fanget
  modellen opp?  →  Recall = TP / (TP + FN)
  • Høy recall → færre forsinkede fakturaer som «glipper» gjennom.
  • I dette prosjektet: ~0.80–0.83 – modellen fanger opp 4 av 5
    forsinkede fakturaer (høy verdi for beslutningsstøtte).

  Nøyaktighet (accuracy)
  ─────────────────────────────────────────────────────────────────
  Andel korrekt klassifiserte fakturaer totalt.
  →  Nøyaktighet = (TP + TN) / (TP + TN + FP + FN)
  • Kan være misvisende ved klasseubalanse: en modell som alltid
    svarer «I tide» vil ha ~66 % nøyaktighet, men null nytteverdi.

  Konfusjonsmatrise
  ─────────────────────────────────────────────────────────────────
  Oppsummerer alle utfall i én tabell:
    TP – forsinket, korrekt flagget av modellen
    TN – i tide, korrekt klassifisert som i tide
    FP – i tide, men feilaktig flagget (falsk alarm)
    FN – forsinket, men ikke fanget opp («glapp igjennom»)

  ── ALGORITMER ────────────────────────────────────────────────────

  Beslutningstre (basis for RF og XGBoost)
  ─────────────────────────────────────────────────────────────────
  En trestruktur av ja/nei-spørsmål om features (f.eks.
  «er Gj.snitt dager forsinket > 15?»). Bladnodene gir
  klassifisering. Et enkelt tre overfit lett; RF og XGBoost
  løser dette ved å kombinere mange trær.

  Random Forest (RF)
  ─────────────────────────────────────────────────────────────────
  Trener hundrevis av beslutningstrær på tilfeldige utvalg av
  treningsdata og features. Sluttprediksjon er gjennomsnittet
  av alle trærnes sannsynligheter («ensemble»).
  • Sterk mot støy og overfitting.
  • «balanced_subsample»: hvert tre trenes med balansert
    klasse-fordeling → kompenserer for klasseubalansen.
  • I dette prosjektet: AUC 0.698 (tunet) – solid men slår ikke
    XGBoost.

  XGBoost (eXtreme Gradient Boosting)
  ─────────────────────────────────────────────────────────────────
  Bygger trær sekvensielt der hvert nytt tre korrigerer feilene
  fra forrige tre («gradient boosting»). «eXtreme» refererer til
  optimaliseringer for hastighet og regularisering.
  Nøkkelparametere brukt i dette prosjektet:
    n_estimators      – antall trær i sekvensen
    max_depth         – maks dybde per tre (lavere = enklere modell)
    learning_rate     – hvor mye hvert tre korrigerer (lave verdier
                        gir langsommere men mer stabil læring)
    subsample         – andel av treningsdata per tre (reduserer
                        overfitting)
    colsample_bytree  – andel features per tre (tilsv. RF)
    scale_pos_weight  – klassevekt for «Forsinket»-klassen
    min_child_weight  – minimum sum av vekter i en bladnode
                        (høyere verdi → mer konservativ modell)
  • I dette prosjektet: beste modell med AUC 0.720 etter tuning.

  Logistisk regresjon (baseline)
  ─────────────────────────────────────────────────────────────────
  Lineær modell som estimerer log-odds for klassifisering.
  Gir en sannsynlighet P(forsinket) = 1 / (1 + e^(-z))
  der z = vektet sum av features.
  • Enkel og tolkbar, men fanger ikke opp ikke-lineære sammenhenger.
  • Brukes her som baseline for sammenligning.
  • I dette prosjektet: AUC 0.706 – overraskende sterk baseline,
    noe som indikerer at lineære sammenhenger forklarer mye.

  ── METODER ───────────────────────────────────────────────────────

  Hyperparameterjustering (RandomizedSearchCV)
  ─────────────────────────────────────────────────────────────────
  Søker etter de beste innstillingene for algoritmen ved å prøve
  et tilfeldig utvalg kombinasjoner (her: 40–50 kombinasjoner) og
  velge den som gir høyest CV-AUC.
  Alternativ: GridSearchCV prøver alle kombinasjoner (mye tregere).

  Kryssvalidering (StratifiedKFold, k=5)
  ─────────────────────────────────────────────────────────────────
  Treningssettet deles i 5 like deler. Modellen trenes 5 ganger –
  hver gang brukes 4 deler til trening og 1 til validering.
  «Stratified» sikrer at klasse-fordelingen er lik i alle fold.
  CV-score er gjennomsnittet over alle 5 valideringssett.

  Train/test-splitting (80/20 stratifisert)
  ─────────────────────────────────────────────────────────────────
  80 % av data brukes til trening (776 fakturaer), 20 % holdes
  tilbake for endelig evaluering (195 fakturaer). «Stratifisert»
  sikrer at begge sett har samme andel forsinkede fakturaer.
  Testsettet røres ikke under trening – gir ærlige ytelsestall.

  scale_pos_weight (XGBoost) / class_weight='balanced' (sklearn)
  ─────────────────────────────────────────────────────────────────
  Kompenserer for klasseubalansen (66 % i tide / 34 % forsinket).
  Gir feilklassifisering av forsinkede fakturaer høyere straff,
  slik at modellen ikke bare velger majoritetsklassen konsekvent.

  Risikokategorisering – terskler
  ─────────────────────────────────────────────────────────────────
  Modellen gir en sannsynlighet (0–1) for forsinkelse per faktura.
  Disse konverteres til tre risikoklasser:
    Lav     – p < 0.30  → lav oppmerksomhet nødvendig
    Middels – 0.30–0.55 → bør følges opp etter behov
    Høy     – p ≥ 0.55  → prioritert oppfølging anbefales
  Valg av terskler er en avveining mellom presisjon og recall –
  lavere terskel for «Høy» fanger opp flere, men gir flere falske
  alarmer.
"""
print(forklaringer)

print("=" * 65)
print("MODELLERING FERDIG – figurer i 'modell_figurer/'")
print("=" * 65)
