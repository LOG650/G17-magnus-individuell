# Prosjektstatus – Finansiell logistikk og beslutningstøtte ved hjelp av KI
**Sist oppdatert:** 2026-04-16 (arbeidsøkt 4)
**Prosjektleder:** Magnus Ødegård | **Kurs:** LOG650

---

## Nåværende fase
**FASE 3 – Gjennomføring** (9. mar – 27. apr 2026)

> Neste milepæl: **Ferdig EDA og feature engineering — 2026-04-18** (EDA og feature engineering fullført 2026-04-16)

---

## Milepæler

| #  | Milepæl                               | Dato       | Status        |
|----|---------------------------------------|------------|---------------|
| M1 | Godkjent proposal (Fase 1)            | 2026-02-09 | ✅ Fullført   |
| M2 | Godkjent prosjektstyringsplan (Fase 2)| 2026-03-17 | ✅ Fullført   |
| M3 | Ferdig datagrunnlag (Fase 3)          | 2026-04-11 | ✅ Fullført   |
| M4 | Ferdig EDA og feature engineering     | 2026-04-18 | ✅ Fullført   |
| M5 | Ferdig og evaluert modell             | 2026-05-09 | ⏳ Kommende  |
| M6 | Innlevert endelig rapport (Fase 4)    | 2026-05-31 | ⏳ Kommende  |

---

## WBS – Oppgavestatus

### Fase 1 & 2 – Proposal og Plan
| ID  | Oppgave                                         | Status        | Notat |
|-----|-------------------------------------------------|---------------|-------|
| 1.0 | Fase 1 – Proposal                               | ✅ Fullført   |       |
| 2.0 | Fase 2 – Prosjektstyringsplan                   | ✅ Fullført   |       |
| 2.1 | Utarbeide og strukturere prosjektstyringsplan   | ✅ Fullført   |       |
| 2.2 | Gjennomgang og godkjenning av veileder          | ✅ Fullført   |       |

### Fase 3 – Gjennomføring (aktiv)
| ID    | Oppgave                                                         | Status         | Notat |
|-------|-----------------------------------------------------------------|----------------|-------|
| 3.1   | Introduksjon og problemstilling – første utkast                 | ✅ Fullført    | Innledning (1.0), problemstilling (1.1), delproblemer (1.2), avgrensinger (1.3) og antagelser (1.4) skrevet inn i rapport_mal.md |
| 3.2   | Teori og litteratursøk                                          | ✅ Fullført    | Seksjon 2.0 og 3.0 skrevet inn i rapport_mal.md |
| 3.2.1 | Søk og gjennomgang av relevante artikler                        | ✅ Fullført    | Appel et al. (2020) og Schoonbee et al. (2022) gjennomgått og oppsummert |
| 3.2.2 | Oppsummering av teorigrunnlag for rapporten                     | ✅ Fullført    | 2.0 Litteratur og 3.0 Teori (6 delkapitler) skrevet inn i rapporten |
| 3.3   | Casebeskrivelse og datainnsamling                               | ✅ Fullført    | Datasett mottatt fra veileder – 1 000 fakturaer, 15 kolonner |
| 3.3.1 | Anonymisering og klargjøring av fakturadatasett                 | ✅ Fullført    | 29 fakturaer med status «Ubetalt» identifisert og dokumentert |
| 3.3.2 | Eksplorativ dataanalyse (EDA)                                   | ✅ Fullført    | eda.py – 9 figurer, leverandørprofil og features.csv produsert |
| 3.4   | Data, metode og modellering (KI-implementasjon)                 | ⚠️ Pågår       |       |
| 3.4.1 | Feature engineering – fakturaspesifikke variabler               | ✅ Fullført    | betalingsfrist_dager, netto_dager, faktura_maned, faktura_kvartal |
| 3.4.2 | Feature engineering – historiske betalingsvariabler             | ✅ Fullført    | Leverandørrisikoscore, one-hot-enkoding av kategoriske variabler |
| 3.4.3 | Trening av kandidatmodeller                                     | ✅ Fullført    | model.py – Log.reg (AUC 0.695), RF (0.691), XGBoost (0.720) – ingen når benchmark ennå |
| 3.4.4 | Hyperparameterjustering og modellvalg                           | ⬜ Ikke startet |       |
| 3.5   | Analyse og resultater – kjøre modeller og dokumentere funn      | ⬜ Ikke startet |       |
| 3.5.1 | Evaluering av modellytelse (AUC-ROC, F1-score, presisjon/recall)| ⬜ Ikke startet |       |
| 3.5.2 | Klassifisering av fakturaer i risikokategorier                  | ⬜ Ikke startet |       |
| 3.6   | Diskusjon – tolke funn mot teori og problemstilling             | ⬜ Ikke startet |       |
| 3.7   | Peer-to-peer review av annen gruppes utkast                     | ⬜ Ikke startet |       |

### Fase 4 – Avslutning (27. apr – 31. mai)
| ID  | Oppgave                                        | Status         | Notat |
|-----|------------------------------------------------|----------------|-------|
| 4.1 | Konklusjon – besvar problemstillingen eksplisitt| ⬜ Ikke startet |       |
| 4.2 | Ferdigstille introduksjon                       | ⬜ Ikke startet |       |
| 4.3 | Kvalitetssikring, korrektur og referanseliste   | ⬜ Ikke startet |       |

---

## Neste steg (prioritert)

1. **[NESTE]** Hyperparameterjustering – GridSearchCV/RandomizedSearchCV for RF og XGBoost (3.4.4)
2. Modellvalg og endelig evaluering (3.4.4)
3. Kjøre beste modell – klassifisere fakturaer i risikokategorier (3.5.2)
2. Modellvalg og endelig evaluering (3.4.4)
3. Kjøre beste modell – klassifisere fakturaer i risikokategorier (3.5.2)

---

## Åpne saker

| ID  | Sak                                                              | Status      | Ansvarlig      | Frist      |
|-----|------------------------------------------------------------------|-------------|----------------|------------|
| S1  | Avklare datatilgang fra veileder                                 | ✅ Løst     | Magnus Ødegård | 2026-04-16 |
| S2  | Avklare håndtering av 29 «Ubetalt»-fakturaer (ekskludere/label) | ✅ Løst     | Magnus Ødegård | 2026-04-16 |

---

## Aktive risikoer å følge opp

| ID | Risiko                               | Nivå    | Tiltak/Kommentar                              |
|----|--------------------------------------|---------|-----------------------------------------------|
| R1 | Utilstrekkelig datakvalitet          | Lav     | EDA gjennomført – datasett komplett bortsett fra 29 ubetalte fakturaer |
| R2 | Manglende tilgang til data           | Lukket  | Datasett mottatt og bekreftet 2026-04-16                               |
| R3 | Håndtering av «Ubetalt»-klasse       | Lukket  | Ekskludert fra trening (971 fakturaer brukes) – S2 løst 2026-04-16    |
| R4 | Tidspress mot innleveringsfrist      | Middels | EDA fullført – neste kritiske frist: modell ferdig 2026-05-09          |

---

## Modellmål (benchmark)

| Mål            | Terskel | Referanse              |
|----------------|---------|------------------------|
| AUC-ROC        | ≥ 0.75  | Appel et al. (2020)    |
| F1-score       | ≥ 0.70  | Appel et al. (2020)    |

**Kandidatmodeller:** Logistisk regresjon (baseline) → Random Forest → Gradient Boosting (XGBoost/LightGBM) → Survival analysis

---

## Endringslogg

| Dato       | Endring                                                                          | Grunn |
|------------|----------------------------------------------------------------------------------|-------|
| 2026-04-16 | Statusfil opprettet og populert fra prosjektstyringsplanen                       | Initiell oppstart |
| 2026-04-16 | Datasett bekreftet mottatt (1 000 fakturaer, 15 kolonner) – S1 lukket            | Arbeidsøkt 2 |
| 2026-04-16 | EDA fullført: klasseubalanse, forsinkelsesdist., kategori- og leverandøranalyse  | Arbeidsøkt 2 |
| 2026-04-16 | Feature engineering fullført: 34 features, features.csv produsert               | Arbeidsøkt 2 |
| 2026-04-16 | Leverandørrisikoprofil laget: risikoscore per leverandør, 9 figurer generert     | Arbeidsøkt 2 |
| 2026-04-16 | M3 og M4 markert fullført – ny åpen sak S2 (Ubetalt-klassen)                    | Arbeidsøkt 2 |
| 2026-04-16 | S2 løst: 29 Ubetalt-fakturaer ekskludert fra trening (971 brukes)               | Arbeidsøkt 3 |
| 2026-04-16 | model.py opprettet: Log.reg (AUC 0.695), RF (0.691), XGBoost (0.720) – 3.4.3 ✅ | Arbeidsøkt 3 |
| 2026-04-16 | 5 figurer generert (10–14), modell_resultater.csv produsert                     | Arbeidsøkt 3 |
| 2026-04-16 | 3.1 påbegynt: første utkast av innledning, avgrensinger og antagelser (rapport.md) | Arbeidsøkt 4 |
| 2026-04-16 | 3.1 fullført: seksjon 1.0–1.4 skrevet inn i rapport_mal.md (014 fase 4 - report)   | Arbeidsøkt 4 |
| 2026-04-16 | 3.2 fullført: seksjon 2.0 Litteratur og 3.0 Teori skrevet inn i rapport_mal.md     | Arbeidsøkt 4 |

---

*Oppdater denne filen ved hver arbeidsøkt: endre status, legg til saker, og oppdater neste steg.*
