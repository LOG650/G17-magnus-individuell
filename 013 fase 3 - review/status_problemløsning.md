# Status – Gjenstående utbedringer i rapport_mal.md

**Rapport:** `014 fase 4 - report/rapport_mal.md`
**Agent-kontekst:** `014 fase 4 - report/agent_FLIK.md`
**Sist oppdatert:** 2026-05-05

---

## Allerede utbedret

| Punkt | Seksjon | Beskrivelse |
|---|---|---|
| ✅ | 1.0, 1.3, 1.4 A2, 4.0, 5.2 | Inkonsistens i datasettbeskrivelse: alle referanser til «anonymisert» data og «Bedriften, anonymisert» er erstattet med «syntetisk» og «Bedriften, hypotetisk». Datasettet er fullstendig generert av veileder og baseres ikke på ekte data. |
| ✅ | Linje 1 (dokumenttittel) | Tittelfeil rettet: «beslutningstøtte» → «beslutningsstøtte» (manglende «s»). |
| ✅ | 5.2 | Duplisert Figur 1 fjernet fra seksjon 5.2. Figuren beholdes kun i 7.1 (EDA). Teksten i 5.2 er utvidet med kryssreferanse: «Se Figur 1 i avsnitt 7.1». |

---

## Allerede utbedret (fortsettelse)

| Punkt | Seksjon | Beskrivelse |
|---|---|---|
| ✅ | 9.0–9.3 | Inkonsekvent desimaltegn: alle desimalpunktum i diskusjonskapitlet erstattet med komma (0.720→0,720, 0.621→0,621, 0.833→0,833 (×2), 0.75→0,75, 0.70→0,70, 0.698→0,698, 0.706→0,706, 0.003→0,003). |

---

## Gjenstående utbedringer

### 2 – Inkonsekvent desimaltegn (høy prioritet)
**Seksjon:** 9.0 Diskusjon (9.1, 9.2, 9.3)
**Problem:** Seksjon 9.0 bruker punktum som desimaltegn (f.eks. 0.720, 0.75, 0.70, 0.003), mens resten av rapporten bruker komma (0,720 osv.). Norsk akademisk standard er komma.
**Handling:** Erstatt alle desimalpunktum med komma i seksjon 9.0–9.3. Eksempler som må rettes:
- «AUC-ROC på 0.720» → «0,720»
- «F1-score på 0.621» → «0,621»
- «recall på 0.833» → «0,833»
- «AUC ≥ 0.75» → «AUC ≥ 0,75»
- «F1 ≥ 0.70» → «F1 ≥ 0,70»
- «Kendalls τ = 0.003» → «Kendalls τ = 0,003»
- Alle øvrige desimaltall i 9.1 og 9.2

---

### 3 – Duplisert Figur 1 (høy prioritet)
**Seksjon:** 5.2 og 7.1
**Problem:** Figur 1 (klasseubalanse, samme bilde) vises i begge seksjoner med hvert sitt figurnummer «Figur 1» og ulik figurtekst. Dette er en formell feil – figurnummer skal kun forekomme én gang.
**Handling:** Fjern figuren fra seksjon 5.2 (datakapitlet). Behold figuren i 7.1 (EDA) der den hører faglig hjemme. Den aktuelle figurblokken i 5.2 som skal fjernes:
```html
<figure style="text-align:center;">
<img src="../004 data/eda_figurer/01_klasseubalanse.png" alt="Klasseubalanse" width="55%">
<figcaption><small>Figur 1: Av de 971 fakturaene i analysedatasettet er 643 (66,2 %) betalt i tide (klasse 0) og 328 (33,8 %) forsinket (klasse 1). ...</small></figcaption>
</figure>
```

---

### 4 – Svak setning om forsinkelsesdistribusjon (lav prioritet)
**Seksjon:** 7.1, avsnitt «Forsinkelsesdistribusjon»
**Problem:** Setningen «Distribusjonen inneholder KDE-estimat som visualiserer tetthetstopper.» beskriver figuren teknisk uten å tolke hva distribusjonen viser.
**Eksisterende tekst:**
> «Distribusjonen inneholder KDE-estimat som visualiserer tetthetstopper.»

**Forslag til endring:**
> «Majoriteten av forsinkelsene er kortvarige (< 30 dager), men en lang høyrehavale indikerer at et mindretall fakturaer har svært lang forsinkelse – noe som drar gjennomsnittsforsinkelsen over medianen.»

---

### 5 – Tomme felter på forsiden (må fylles manuelt)
**Seksjon:** Forside
**Problem:** Følgende felter er tomme og kan ikke fylles av en AI-agent uten input fra forfatteren:
- `Totalt antall sider inkludert forsiden:`
- `Veileder:`

**Handling:** Forfatteren fyller inn manuelt.

---

### 6 – Tom innholdsliste (må fylles manuelt)
**Seksjon:** Innhold
**Problem:** Innholdslisten inneholder kun en kommentar: `<!-- Genereres automatisk eller skrives manuelt -->`. Den er ikke utfylt.
**Handling:** Forfatteren eller neste agent fyller inn innholdsfortegnelse manuelt basert på den endelige seksjonslisten.

---

### 7 – Tomt vedlegg (lav prioritet)
**Seksjon:** 12.0 Vedlegg
**Problem:** Seksjonen er tom. Enten bør vedlegg legges til, eller det bør legges inn en setning som forklarer at vedlegg ikke er inkludert.
**Forslag:** Legg til én setning, f.eks.: «Vedlegg er ikke inkludert i denne innleveringen. Python-kode og datasett er tilgjengelig på forespørsel.»

---

## Prioriteringsrekkefølge

1. Desimaltegn i seksjon 9.0 (søk/erstatt)
2. Fjern duplisert Figur 1 fra 5.2
3. Forside og innholdsliste (manuelt av forfatter)
4. Forsinkelsesdistribusjon-setning
5. Vedlegg
