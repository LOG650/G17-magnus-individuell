# Prosjektstatus – Finansiell logistikk og beslutningstøtte ved hjelp av KI
**Sist oppdatert:** 2026-04-16
**Prosjektleder:** Magnus Ødegård | **Kurs:** LOG650

---

## Nåværende fase
**FASE 3 – Gjennomføring** (9. mar – 27. apr 2026)

> Neste milepæl: **Ferdig EDA og feature engineering — 2026-04-18** (om 2 dager!)

---

## Milepæler

| #  | Milepæl                               | Dato       | Status        |
|----|---------------------------------------|------------|---------------|
| M1 | Godkjent proposal (Fase 1)            | 2026-02-09 | ✅ Fullført   |
| M2 | Godkjent prosjektstyringsplan (Fase 2)| 2026-03-17 | ✅ Fullført   |
| M3 | Ferdig datagrunnlag (Fase 3)          | 2026-04-11 | ⚠️ Oppdater  |
| M4 | Ferdig EDA og feature engineering     | 2026-04-18 | 🔴 Kritisk   |
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
| 3.1   | Introduksjon og problemstilling – første utkast                 | ⬜ Ikke startet |       |
| 3.2   | Teori og litteratursøk                                          | ⬜ Ikke startet |       |
| 3.2.1 | Søk og gjennomgang av relevante artikler                        | ⬜ Ikke startet |       |
| 3.2.2 | Oppsummering av teorigrunnlag for rapporten                     | ⬜ Ikke startet |       |
| 3.3   | Casebeskrivelse og datainnsamling                               | ⚠️ Pågår       | Avhenger av data fra veileder |
| 3.3.1 | Anonymisering og klargjøring av fakturadatasett                 | ⚠️ Pågår       |       |
| 3.3.2 | Eksplorativ dataanalyse (EDA)                                   | ⬜ Ikke startet |       |
| 3.4   | Data, metode og modellering (KI-implementasjon)                 | ⬜ Ikke startet |       |
| 3.4.1 | Feature engineering – fakturaspesifikke variabler               | ⬜ Ikke startet |       |
| 3.4.2 | Feature engineering – historiske betalingsvariabler             | ⬜ Ikke startet |       |
| 3.4.3 | Trening av kandidatmodeller                                     | ⬜ Ikke startet |       |
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

1. **[KRITISK]** Bekrefte status på datagrunnlag fra veileder (M3 – forfalt 2026-04-11)
2. **[KRITISK]** Fullføre EDA (3.3.2) innen 2026-04-18
3. **[KRITISK]** Fullføre feature engineering (3.4.1, 3.4.2) innen 2026-04-18
4. Starte trening av baseline-modell (logistisk regresjon) (3.4.3)
5. Skrive første utkast av introduksjon og problemstilling (3.1)
6. Gjennomføre litteratursøk og oppsummere teorigrunnlag (3.2.1, 3.2.2)

---

## Åpne saker

| ID  | Sak                                         | Status   | Ansvarlig      | Frist      |
|-----|---------------------------------------------|----------|----------------|------------|
| S1  | Avklare datatilgang fra veileder            | 🔴 Åpen  | Magnus Ødegård | Snarest    |

---

## Aktive risikoer å følge opp

| ID | Risiko                               | Nivå    | Tiltak/Kommentar                              |
|----|--------------------------------------|---------|-----------------------------------------------|
| R1 | Utilstrekkelig datakvalitet          | Middels | Grundig datarensing – sjekk etter EDA         |
| R2 | Manglende tilgang til data           | Høy     | **Uavklart** – avventer datasett fra veileder |
| R4 | Tidspress mot innleveringsfrist      | Høy     | EDA-frist om 2 dager – krever prioritering    |

---

## Modellmål (benchmark)

| Mål            | Terskel | Referanse              |
|----------------|---------|------------------------|
| AUC-ROC        | ≥ 0.75  | Appel et al. (2020)    |
| F1-score       | ≥ 0.70  | Appel et al. (2020)    |

**Kandidatmodeller:** Logistisk regresjon (baseline) → Random Forest → Gradient Boosting (XGBoost/LightGBM) → Survival analysis

---

## Endringslogg

| Dato       | Endring                                     | Grunn |
|------------|---------------------------------------------|-------|
| 2026-04-16 | Statusfil opprettet og populert fra prosjektstyringsplanen | Initiell oppstart |

---

*Oppdater denne filen ved hver arbeidsøkt: endre status, legg til saker, og oppdater neste steg.*
