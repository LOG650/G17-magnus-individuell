"""
EDA – Eksplorativ dataanalyse
Prosjekt: LOG650 – KI-basert prediksjon av sene fakturarbetalinger
Datasett:  table.csv  (1 000 fakturaer, 15 kolonner)
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
from pathlib import Path

# Tving UTF-8 output på Windows-terminal
if sys.stdout.encoding.lower() != "utf-8":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

# ── Stier ────────────────────────────────────────────────────────────────────
BASE   = Path(__file__).parent
CSV    = BASE / "table.csv"
OUTDIR = BASE / "eda_figurer"
OUTDIR.mkdir(exist_ok=True)

sns.set_theme(style="whitegrid", palette="muted")
pd.set_option("display.float_format", "{:.2f}".format)

# ── 1. Last inn data ──────────────────────────────────────────────────────────
df = pd.read_csv(CSV, parse_dates=["Fakturadato", "Forfallsdato", "Faktisk betalingsdato"])

print("=" * 60)
print("1. GRUNNLEGGENDE OVERSIKT")
print("=" * 60)
print(f"  Antall fakturaer  : {len(df):,}")
print(f"  Antall kolonner   : {df.shape[1]}")
print(f"\nKolonner:\n  {list(df.columns)}")

# ── 2. Manglende verdier ──────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("2. MANGLENDE VERDIER")
print("=" * 60)
missing = df.isnull().sum()
if missing.sum() == 0:
    print("  Ingen manglende verdier – datasett er komplett.")
else:
    print(missing[missing > 0])
    # Fakturaer uten betalingsdato er trolig ennå ikke betalt (åpne)
    apne = df[df["Faktisk betalingsdato"].isnull()]
    print(f"\n  Fakturaer uten betalingsdato: {len(apne)}")
    print(f"  Betalingsstatus for disse: {apne['Betalingsstatus'].value_counts().to_dict()}")
    # Fyll inn manglende Dager forsinket = 0 for fakturaer uten forsinket-status
    df["Dager forsinket"] = df["Dager forsinket"].fillna(0)

# ── 3. Lag binær målvariabel ──────────────────────────────────────────────────
df["er_forsinket"] = (df["Betalingsstatus"] == "Forsinket").astype(int)

# ── 4. Klasseubalanse ─────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("3. KLASSEUBALANSE (målvariabel)")
print("=" * 60)
klasse = df["er_forsinket"].value_counts()
print(f"  Betalt i tide : {klasse[0]:4d}  ({klasse[0]/len(df)*100:.1f} %)")
print(f"  Forsinket     : {klasse[1]:4d}  ({klasse[1]/len(df)*100:.1f} %)")

fig, ax = plt.subplots(figsize=(5, 4))
ax.bar(["Betalt i tide", "Forsinket"], [klasse[0], klasse[1]], color=["steelblue", "tomato"])
ax.set_ylabel("Antall fakturaer")
ax.set_title("Klasseubalanse – Betalingsstatus")
for bar in ax.patches:
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 5,
            f"{bar.get_height():.0f}", ha="center", va="bottom", fontsize=10)
plt.tight_layout()
plt.savefig(OUTDIR / "01_klasseubalanse.png", dpi=150)
plt.close()
print("  → Figur lagret: 01_klasseubalanse.png")

# ── 5. Deskriptiv statistikk ──────────────────────────────────────────────────
print("\n" + "=" * 60)
print("4. DESKRIPTIV STATISTIKK – numeriske kolonner")
print("=" * 60)
num_cols = ["Fakturabeløp (NOK)", "Dager forsinket",
            "Gj.snitt dager forsinket (leverandør)", "Antall fakturaer (leverandør)"]
print(df[num_cols].describe().to_string())

# ── 6. Distribusjon av forsinkelse ────────────────────────────────────────────
forsinket = df[df["er_forsinket"] == 1]["Dager forsinket"]
print("\n" + "=" * 60)
print("5. FORSINKELSE – kun sene fakturaer")
print("=" * 60)
print(f"  Min     : {forsinket.min()} dager")
print(f"  Maks    : {forsinket.max()} dager")
print(f"  Median  : {forsinket.median():.0f} dager")
print(f"  Snitt   : {forsinket.mean():.1f} dager")

fig, ax = plt.subplots(figsize=(7, 4))
sns.histplot(forsinket, bins=20, kde=True, ax=ax, color="tomato")
ax.set_xlabel("Dager forsinket")
ax.set_ylabel("Antall fakturaer")
ax.set_title("Distribusjon av forsinkelse (kun forsinkede fakturaer)")
plt.tight_layout()
plt.savefig(OUTDIR / "02_distribusjon_forsinkelse.png", dpi=150)
plt.close()
print("  → Figur lagret: 02_distribusjon_forsinkelse.png")

# ── 7. Andel forsinkede per leverandørkategori ────────────────────────────────
print("\n" + "=" * 60)
print("6. ANDEL FORSINKEDE PER LEVERANDØRKATEGORI")
print("=" * 60)
kat = (df.groupby("Leverandørkategori")["er_forsinket"]
         .agg(["sum", "count"])
         .rename(columns={"sum": "forsinket", "count": "totalt"}))
kat["andel_%"] = (kat["forsinket"] / kat["totalt"] * 100).round(1)
kat = kat.sort_values("andel_%", ascending=False)
print(kat.to_string())

fig, ax = plt.subplots(figsize=(9, 4))
sns.barplot(data=kat.reset_index(), x="Leverandørkategori", y="andel_%", ax=ax, palette="muted")
ax.set_ylabel("Andel forsinkede (%)")
ax.set_title("Andel forsinkede fakturaer per leverandørkategori")
ax.yaxis.set_major_formatter(mticker.FormatStrFormatter("%.0f%%"))
plt.xticks(rotation=20, ha="right")
plt.tight_layout()
plt.savefig(OUTDIR / "03_andel_per_kategori.png", dpi=150)
plt.close()
print("  → Figur lagret: 03_andel_per_kategori.png")

# ── 8. Andel forsinkede per betalingsbetingelse ───────────────────────────────
print("\n" + "=" * 60)
print("7. ANDEL FORSINKEDE PER BETALINGSBETINGELSE")
print("=" * 60)
bet = (df.groupby("Betalingsbetingelser")["er_forsinket"]
         .agg(["sum", "count"])
         .rename(columns={"sum": "forsinket", "count": "totalt"}))
bet["andel_%"] = (bet["forsinket"] / bet["totalt"] * 100).round(1)
bet = bet.sort_values("andel_%", ascending=False)
print(bet.to_string())

fig, ax = plt.subplots(figsize=(8, 4))
sns.barplot(data=bet.reset_index(), x="Betalingsbetingelser", y="andel_%", ax=ax, palette="muted")
ax.set_ylabel("Andel forsinkede (%)")
ax.set_title("Andel forsinkede fakturaer per betalingsbetingelse")
ax.yaxis.set_major_formatter(mticker.FormatStrFormatter("%.0f%%"))
plt.tight_layout()
plt.savefig(OUTDIR / "04_andel_per_betingelse.png", dpi=150)
plt.close()
print("  → Figur lagret: 04_andel_per_betingelse.png")

# ── 9. Andel forsinkede per risikokategori ────────────────────────────────────
print("\n" + "=" * 60)
print("8. ANDEL FORSINKEDE PER RISIKOKATEGORI (leverandør)")
print("=" * 60)
ris = (df.groupby("Risikokategori leverandør")["er_forsinket"]
         .agg(["sum", "count"])
         .rename(columns={"sum": "forsinket", "count": "totalt"}))
ris["andel_%"] = (ris["forsinket"] / ris["totalt"] * 100).round(1)
order = ["Medium", "Høy", "Kritisk"]
ris = ris.reindex([o for o in order if o in ris.index])
print(ris.to_string())

fig, ax = plt.subplots(figsize=(6, 4))
colors = {"Medium": "steelblue", "Høy": "orange", "Kritisk": "tomato"}
bars = ax.bar(ris.index, ris["andel_%"],
              color=[colors.get(k, "gray") for k in ris.index])
ax.set_ylabel("Andel forsinkede (%)")
ax.set_title("Andel forsinkede fakturaer per risikokategori (leverandør)")
ax.yaxis.set_major_formatter(mticker.FormatStrFormatter("%.0f%%"))
for bar in bars:
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5,
            f"{bar.get_height():.1f}%", ha="center", va="bottom", fontsize=10)
plt.tight_layout()
plt.savefig(OUTDIR / "05_andel_per_risiko.png", dpi=150)
plt.close()
print("  → Figur lagret: 05_andel_per_risiko.png")

# ── 10. Korrelasjonsmatrise (numeriske features) ──────────────────────────────
print("\n" + "=" * 60)
print("9. KORRELASJON MED MÅLVARIABEL (er_forsinket)")
print("=" * 60)
num_features = ["Fakturabeløp (NOK)", "Gj.snitt dager forsinket (leverandør)",
                "Antall fakturaer (leverandør)", "er_forsinket"]
corr = df[num_features].corr()
print(corr["er_forsinket"].drop("er_forsinket").sort_values(ascending=False).to_string())

fig, ax = plt.subplots(figsize=(7, 5))
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", ax=ax,
            linewidths=0.5, vmin=-1, vmax=1)
ax.set_title("Korrelasjonsmatrise – numeriske variabler")
plt.tight_layout()
plt.savefig(OUTDIR / "06_korrelasjonsmatrise.png", dpi=150)
plt.close()
print("  → Figur lagret: 06_korrelasjonsmatrise.png")

# ── 11. Feature engineering – variabler som brukes i modell ──────────────────
print("\n" + "=" * 60)
print("10. FEATURE ENGINEERING")
print("=" * 60)

# Datobaserte features
df["betalingsfrist_dager"] = (df["Forfallsdato"] - df["Fakturadato"]).dt.days
df["faktura_maned"]        = df["Fakturadato"].dt.month
df["faktura_kvartal"]      = df["Fakturadato"].dt.quarter

# Betalingsbetingelse som tall (trekk ut netto-antall)
df["netto_dager"] = (df["Betalingsbetingelser"]
                       .str.extract(r"(\d+)")[0]
                       .astype(int))

# One-hot encode kategoriske variabler
cat_cols = ["Leverandørkategori", "Kontrakttype", "INCOTERMS", "Risikokategori leverandør"]
df_encoded = pd.get_dummies(df, columns=cat_cols, drop_first=False)

feature_cols = (
    ["Fakturabeløp (NOK)", "netto_dager", "betalingsfrist_dager",
     "faktura_maned", "faktura_kvartal",
     "Gj.snitt dager forsinket (leverandør)", "Antall fakturaer (leverandør)"]
    + [c for c in df_encoded.columns if any(c.startswith(p) for p in cat_cols)]
)

X = df_encoded[feature_cols]
y = df_encoded["er_forsinket"]

print(f"  Antall features  : {X.shape[1]}")
print(f"  Antall rader     : {X.shape[0]}")
print(f"\n  Nye datofeatures:")
print(f"    betalingsfrist_dager  – antall dager fra faktura til forfall")
print(f"    faktura_maned         – måneden fakturaen ble utstedt")
print(f"    faktura_kvartal       – kvartal fakturaen ble utstedt")
print(f"    netto_dager           – betalingsbetingelse som heltall (10/14/30/…)")
print(f"\n  One-hot-enkodede kolonner ({len([c for c in feature_cols if '_' in c and not c.startswith('Faktura')])}):")
for c in feature_cols:
    if any(c.startswith(p) for p in cat_cols):
        print(f"    {c}")

# Lagre ferdig dataset til modellering
out_csv = BASE / "features.csv"
df_encoded[feature_cols + ["er_forsinket"]].to_csv(out_csv, index=False)
print(f"\n  → Ferdig datasett lagret: features.csv  ({X.shape[0]} rader, {X.shape[1]+1} kolonner)")

print("\n" + "=" * 60)
print("EDA FERDIG – figurer i mappen 'eda_figurer/'")
print("=" * 60)

# ══════════════════════════════════════════════════════════════
# LEVERANDØRANALYSE – sannsynlighet for sen betaling per leverandør
# ══════════════════════════════════════════════════════════════

print("\n\n" + "=" * 60)
print("LEVERANDØRANALYSE – RISIKOPROFIL PER LEVERANDØR")
print("=" * 60)

# ── A. Aggreger nøkkeltall per leverandør ─────────────────────
lev = (
    df.groupby("Leverandør-ID")
    .agg(
        antall_fakturaer        = ("Faktura-ID",               "count"),
        andel_forsinket_pct     = ("er_forsinket",             lambda x: round(x.mean() * 100, 1)),
        snitt_dager_forsinket   = ("Dager forsinket",          lambda x: round(x[x > 0].mean(), 1) if (x > 0).any() else 0),
        median_dager_forsinket  = ("Dager forsinket",          lambda x: round(x[x > 0].median(), 1) if (x > 0).any() else 0),
        snitt_belop_nok         = ("Fakturabeløp (NOK)",       lambda x: round(x.mean(), 0)),
        total_belop_nok         = ("Fakturabeløp (NOK)",       "sum"),
        kategori                = ("Leverandørkategori",       "first"),
        risikokategori          = ("Risikokategori leverandør","first"),
        kontrakttype            = ("Kontrakttype",             "first"),
    )
    .reset_index()
)

# Sannsynlighet for forsinkelse (0–1, brukes som score)
lev["p_forsinket"] = lev["andel_forsinket_pct"] / 100

# Risikoscore = p_forsinket vektet med snitt forsinkelse (normalisert 0–1)
max_dager = lev["snitt_dager_forsinket"].max()
lev["risikoscore"] = (
    lev["p_forsinket"] * 0.6
    + (lev["snitt_dager_forsinket"] / max_dager if max_dager > 0 else 0) * 0.4
).round(3)

lev = lev.sort_values("risikoscore", ascending=False).reset_index(drop=True)
lev.index += 1  # Ranger fra 1

print("\n  Topp 10 leverandører – høyest risiko for sen betaling:\n")
topp10 = lev.head(10)[["Leverandør-ID", "kategori", "risikokategori",
                         "antall_fakturaer", "andel_forsinket_pct",
                         "snitt_dager_forsinket", "risikoscore"]]
topp10.columns = ["Leverandør", "Kategori", "Risiko",
                  "Ant.fakt.", "Forsinket %", "Snitt dager", "Risikoscore"]
print(topp10.to_string(index=True))

print("\n  Bunn 10 leverandører – lavest risiko:\n")
bunn10 = lev.tail(10)[["Leverandør-ID", "kategori", "risikokategori",
                         "antall_fakturaer", "andel_forsinket_pct",
                         "snitt_dager_forsinket", "risikoscore"]]
bunn10.columns = ["Leverandør", "Kategori", "Risiko",
                  "Ant.fakt.", "Forsinket %", "Snitt dager", "Risikoscore"]
print(bunn10.to_string(index=True))

# ── B. Figur: Risikoscore topp 15 leverandører ───────────────
topp15 = lev.head(15)
fig, ax = plt.subplots(figsize=(10, 5))
colors = topp15["risikokategori"].map(
    {"Medium": "steelblue", "Høy": "orange", "Kritisk": "tomato"}
).fillna("gray")
bars = ax.barh(topp15["Leverandør-ID"][::-1], topp15["risikoscore"][::-1],
               color=colors[::-1])
ax.set_xlabel("Risikoscore  (0 = ingen risiko, 1 = maksimal risiko)")
ax.set_title("Topp 15 leverandører – risikoscore for sen betaling")
ax.set_xlim(0, 1)
# Legende
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor="tomato",    label="Kritisk"),
    Patch(facecolor="orange",    label="Høy"),
    Patch(facecolor="steelblue", label="Medium"),
]
ax.legend(handles=legend_elements, loc="lower right")
plt.tight_layout()
plt.savefig(OUTDIR / "07_leverandor_risikoscore.png", dpi=150)
plt.close()
print("\n  → Figur lagret: 07_leverandor_risikoscore.png")

# ── C. Figur: Scatter – andel forsinket vs. snitt dager forsinket ─
fig, ax = plt.subplots(figsize=(9, 6))
scatter_colors = lev["risikokategori"].map(
    {"Medium": "steelblue", "Høy": "orange", "Kritisk": "tomato"}
).fillna("gray")
sc = ax.scatter(
    lev["andel_forsinket_pct"],
    lev["snitt_dager_forsinket"],
    c=scatter_colors,
    s=lev["antall_fakturaer"] * 3,
    alpha=0.7,
    edgecolors="white",
    linewidths=0.5,
)
# Merk leverandørene med høyest risikoscore
for _, row in lev.head(8).iterrows():
    ax.annotate(
        row["Leverandør-ID"],
        (row["andel_forsinket_pct"], row["snitt_dager_forsinket"]),
        xytext=(5, 3), textcoords="offset points", fontsize=8
    )
ax.set_xlabel("Andel forsinkede fakturaer (%)")
ax.set_ylabel("Gjennomsnittlig forsinkelse (dager, kun sene fakturaer)")
ax.set_title("Leverandørrisiko – andel forsinket vs. gjennomsnittlig forsinkelse\n"
             "(sirkelstørrelse = antall fakturaer)")
ax.legend(handles=legend_elements, loc="upper left")
plt.tight_layout()
plt.savefig(OUTDIR / "08_leverandor_scatter.png", dpi=150)
plt.close()
print("  → Figur lagret: 08_leverandor_scatter.png")

# ── D. Figur: Betalingsatferd over tid (kvartal) – topp 5 leverandører ──
print("\n" + "-" * 60)
print("  Betalingsatferd over tid – topp 5 risiko-leverandører")
print("-" * 60)

df["år_kvartal"] = df["Fakturadato"].dt.to_period("Q").astype(str)
topp5_lev = lev.head(5)["Leverandør-ID"].tolist()
df_topp5 = df[df["Leverandør-ID"].isin(topp5_lev)]

trend = (
    df_topp5.groupby(["Leverandør-ID", "år_kvartal"])["er_forsinket"]
    .mean()
    .reset_index()
)
trend["er_forsinket"] *= 100

fig, ax = plt.subplots(figsize=(11, 5))
for lev_id in topp5_lev:
    data = trend[trend["Leverandør-ID"] == lev_id].sort_values("år_kvartal")
    ax.plot(data["år_kvartal"], data["er_forsinket"], marker="o", label=lev_id)
ax.set_xlabel("Kvartal")
ax.set_ylabel("Andel forsinkede fakturaer (%)")
ax.set_title("Betalingsatferd over tid – topp 5 risiko-leverandører (per kvartal)")
ax.legend(title="Leverandør")
plt.xticks(rotation=30, ha="right")
ax.yaxis.set_major_formatter(mticker.FormatStrFormatter("%.0f%%"))
plt.tight_layout()
plt.savefig(OUTDIR / "09_leverandor_trend.png", dpi=150)
plt.close()
print("  → Figur lagret: 09_leverandor_trend.png")

# ── E. Lagre leverandørprofil til CSV ─────────────────────────
lev_out = BASE / "leverandor_risikoprofil.csv"
lev.to_csv(lev_out, index=True)
print(f"\n  → Leverandørprofil lagret: leverandor_risikoprofil.csv  ({len(lev)} leverandører)")

# ── F. Oppsummering for rapport ───────────────────────────────
print("\n" + "=" * 60)
print("OPPSUMMERING – LEVERANDØRANALYSE")
print("=" * 60)
kritiske = lev[lev["risikokategori"] == "Kritisk"]
hoje      = lev[lev["andel_forsinket_pct"] >= 50]

print(f"  Totalt unike leverandører   : {len(lev)}")
print(f"  Leverandører med >= 50 %    : {len(hoje)} stk")
print(f"    {', '.join(hoje['Leverandør-ID'].tolist())}")
print(f"  Risikokategori 'Kritisk'    : {len(kritiske)} leverandør(er)")
print(f"    {', '.join(kritiske['Leverandør-ID'].tolist())}")
print(f"\n  Høyest risikoscore          : {lev.iloc[0]['Leverandør-ID']}  "
      f"({lev.iloc[0]['andel_forsinket_pct']} % forsinket, "
      f"snitt {lev.iloc[0]['snitt_dager_forsinket']} dager)")
print(f"  Lavest risikoscore           : {lev.iloc[-1]['Leverandør-ID']}  "
      f"({lev.iloc[-1]['andel_forsinket_pct']} % forsinket)")

print("\n" + "=" * 60)
print("ALT FERDIG – figurer i 'eda_figurer/', profil i 'leverandor_risikoprofil.csv'")
print("=" * 60)
