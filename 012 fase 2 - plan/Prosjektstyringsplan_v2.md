# Prosjektstyringsplan
for
Finansiell logistikk og beslutningstøtte ved hjelp av KI

**Dato:** 2026-03-14 | **Sist oppdatert:** 2026-04-20
**Utarbeidet av:** Magnus Ødegård | **Kurs:** LOG650

> **Nåværende fase:** FASE 3 – Gjennomføring (9. mar – 27. apr 2026)

---

## Innhold

1. [Sammendrag](#sammendrag)
2. [Omfang](#omfang)
3. [Fremdrift](#fremdrift)
4. [Risiko](#risiko)
5. [Saker](#saker)
6. [Interessenter](#interessenter)
7. [Ressurser](#ressurser)
8. [Kommunikasjon](#kommunikasjon)
9. [Kvalitet](#kvalitet)
10. [Anskaffelser](#anskaffelser)
11. [Endringskontrollprosess](#endringskontrollprosess)
12. [Endringslogg](#endringslogg)

---

## Sammendrag

Dette dokumentet utgjør prosjektstyringsplanen for prosjektet «Finansiell logistikk og beslutningstøtte ved hjelp av KI». Det dokumenterer planbaselines for omfang, fremdrift og risiko, og gir tilleggsinformasjon for å støtte prosjektleder i vellykket gjennomføring. Dokumentet fungerer også som et levende statusstyringsdokument og oppdateres løpende gjennom prosjektets faser.

Dette prosjektet støtter følgende mål: Å forbedre Bedriftens evne til å identifisere fakturaer med høy risiko for sen betaling gjennom datadrevet prediksjon og beslutningsstøtte.

### Behov

Bedriften håndterer et stort volum av fakturaer, og sen betaling etter forfallsdato medfører ineffektiv ressursbruk og redusert kontroll over likviditet og leverandørforhold. Det finnes i dag ikke et systematisk og datadrevet verktøy for å forutsi hvilke fakturaer som er i risikosonen for forsinkelse. Prosjektet svarer på behovet for bedre prioritering og oppfølging av fakturaer.

### Sponsor

Veileder fra HIM er sponsor for dette prosjektet, ansvarlig for godkjenning av denne prosjektplanen og eventuelle endringer under gjennomføringen.

### Kunde

Bedriften (anonymisert) representerer sluttbrukerne av prosjektet, har deltatt i definisjon av prosjektomfanget og vil være ansvarlig for godkjenning av kravene og aksept av de endelige leveransene.

### Forretningscase

Prosjektet er begrunnet gjennom økt effektivitet i fakturahåndtering, redusert andel forsinkede betalinger og bedre grunnlag for prioritering av fakturakontroll og oppfølging.

#### Alternativer

Følgende alternativer ble vurdert:

- **Status quo:** Manuell gjennomgang av alle fakturaer. Forkastet fordi det er ressurskrevende og ikke skalerbart.
- **Regelbasert system:** Enkle terskelverdier for flagging. Forkastet fordi det ikke tar hensyn til komplekse mønstre i historiske data.
- **KI-basert prediksjon (valgt):** Maskinlæringsmodell basert på historiske fakturadata. Gir best balanse mellom nøyaktighet og gjennomførbarhet.

#### Forutsetninger

- Tilgang til historiske fakturadata fra Bedriften (anonymisert og tilpasset).
- Datasettet er representativt og av tilstrekkelig kvalitet for modelltrening.
- Prosjektet gjennomføres som individuelt studentprosjekt i kurset LOG650.

#### Gevinster

- Redusert andel forsinkede betalinger.
- Bedre grunnlag for prioritering av fakturakontroll og oppfølging.
- Frigjøring av ressurser fra manuell gjennomgang til risikobasert oppfølging.

#### Kostnader

Prosjektet gjennomføres som et akademisk studentprosjekt. Kostnader er primært knyttet til tidsbruk og databehandling.

#### Analyse

Det valgte alternativet (KI-basert prediksjon) forventes å gi størst gevinst i form av reduserte forsinkede betalinger og effektivisering av fakturakontroll.

---

## Omfang

Denne seksjonen beskriver prosjektomfanget, inkludert prosjektmål, forutsetninger, begrensninger, krav og arbeidsnedbrytningsstruktur.

### Mål

Prosjektmålet er å utvikle en KI-modell som predikerer sannsynligheten for at en faktura betales etter forfallsdato, basert på fakturainformasjon som INCOTERMS, betalingsbetingelser og historisk betalingsatferd.

**Prosjektets forutsetninger er:**

- Historiske fakturadata er tilgjengelig og kan anonymiseres.
- Prosjektet gjennomføres innenfor tidsrammen for kurset LOG650.
- Python/R og relevante maskinlæringsbiblioteker er tilgjengelig.

**Prosjektets begrensninger er:**

- Prosjektet avgrenses til én virksomhet (Bedriften).
- Kun historiske fakturadata benyttes – ingen sanntidsdata.
- Ingen juridisk vurdering av kontrakter inngår i analysen.
- Tvistesaker, kontraktsendringer underveis og eksterne økonomiske forhold er ekskludert.

### Krav

Prosjektkravene inkluderer:

- Datahåndtering og anonymisering av fakturadatasett.
- Eksplorativ dataanalyse (EDA) og feature engineering.
- Utvikling og evaluering av prediksjonsmodell(er).
- Klassifisering av fakturaer i risikokategorier.
- Beslutningsstøtterapport med anbefalinger.

### Løsning

Løsningen som skal utvikles er en maskinlæringsbasert prediksjonsmodell som klassifiserer fakturaer etter risiko for sen betaling. Modellen vil bli trent på historiske fakturadata og evaluert med relevante ytelsesmål (f.eks. presisjon, recall, F1-score, AUC-ROC).

Inspirert av Schoonbee et al. (2022) vil prosjektet benytte en multiklasse-tilnærming der fakturaer klassifiseres i følgende utfallskategorier:

| Klasse | Beskrivelse                          |
|--------|--------------------------------------|
| 0      | Betalt innen forfallsdato (i tide)   |
| 1      | 1–30 dager forsinket                 |
| 2      | 31–60 dager forsinket                |
| 3      | 61+ dager forsinket                  |

**Beslutningsvariabler:**

- Sannsynlighet for sen betaling
- Forventet betalingsforsinkelse (antall dager)
- Risikoklassifisering (lav / middels / høy)

### Metodologi

Prosjektet følger et maskinlæringsutviklingsveikart inspirert av Schoonbee et al. (2022) og Appel et al. (2020):

#### Kandidatalgoritmer

Følgende algoritmer vil testes og sammenlignes:

- Logistisk regresjon (baseline)
- Random Forest
- Gradient Boosting (XGBoost / LightGBM)
- Survival analysis (som supplementær tilnærming)

Beste modell velges basert på ytelsesmålene beskrevet under Kvalitet.

#### Feature engineering

Feature engineering er en kritisk del av prosjektet og deles inn i to kategorier:

**Fakturaspesifikke variabler (fra fakturadatasettet):**

| Feature              | Beskrivelse                                      |
|----------------------|--------------------------------------------------|
| Fakturabeløp         | Beløp på fakturaen                               |
| INCOTERMS            | Leveringsbetingelse                              |
| Betalingsbetingelser | Antall dager kreditt (f.eks. netto 30)           |
| Kontrakttype         | Type kontrakt knyttet til fakturaen              |
| Leverandørkategori   | Kategori/type leverandør                         |
| Forfallsdato         | Opprinnelig forfallsdato                         |

**Historiske betalingsvariabler (beregnes per leverandør, inspirert av Schoonbee et al.):**

| Feature                    | Beskrivelse                                                         |
|----------------------------|---------------------------------------------------------------------|
| GjennomsnittDagerForsinket | Gjennomsnittlig antall dager forsinket på tidligere fakturaer       |
| AntallFakturerITide        | Antall tidligere fakturaer betalt innen forfall                     |
| AntallFakturerForsinket    | Antall tidligere fakturaer betalt etter forfall                     |
| AndelITide                 | Andel av tidligere fakturaer betalt i tide                          |
| DagerSidenSisteBetaling    | Antall dager siden forrige betaling                                 |
| BetalingsdagIMåned         | Gjennomsnittlig dag i måneden betaling skjer                        |
| UteståendeFaktura          | Binær: 1 hvis leverandør har utestående faktura, 0 ellers           |
| GlobalTrend                | Gjennomsnittlig økning/reduksjon i forsinkelse siste måned          |

Historiske variabler beregnes med eksponentiell vekting (vektfaktor ~1.5) for å gi nyere atferd større betydning, i tråd med funn fra Schoonbee et al. (2022).

#### Datadeling og validering

For å unngå datalekkasje benyttes tidsbasert datadeling:

- **Treningssett:** Eldre historiske fakturadata
- **Valideringssett:** Nyere data for hyperparameterjustering
- **Testsett:** Siste tilgjengelige periode (hold-out)

Modellen vil retrenenes periodisk for å håndtere konseptdrift (se risikoregister).

#### Ytelsesmål og benchmark

Basert på Appel et al. (2020), som oppnådde 77 % nøyaktighet i tilsvarende problem, settes følgende målnivå:

- Mål: AUC-ROC ≥ 0.75 og F1-score ≥ 0.70 på testsettet
- Resultater fra alle kandidatmodeller dokumenteres og sammenlignes

### Arbeidsnedbrytningsstruktur (WBS)

Tabellen nedenfor viser fullstendig arbeidsnedbrytning med nåværende fremdriftsstatus for alle leveranser.

#### Fase 1 & 2 – Proposal og Plan

| ID  | Leveranse                                       | Eier           | Status        | Notat |
|-----|-------------------------------------------------|----------------|---------------|-------|
| 1.0 | Fase 1 – Proposal                               | Magnus Ødegård | ✅ Fullført   |       |
| 2.0 | Fase 2 – Prosjektstyringsplan                   | Magnus Ødegård | ✅ Fullført   |       |
| 2.1 | Utarbeide og strukturere prosjektstyringsplan   | Magnus Ødegård | ✅ Fullført   |       |
| 2.2 | Gjennomgang og godkjenning av veileder          | Magnus Ødegård | ✅ Fullført   |       |

#### Fase 3 – Gjennomføring (aktiv)

| ID    | Leveranse                                                         | Eier           | Status          | Notat |
|-------|-------------------------------------------------------------------|----------------|-----------------|-------|
| 3.1   | Introduksjon og problemstilling – første utkast                   | Magnus Ødegård | ✅ Fullført     | Seksjon 1.0–1.4 skrevet inn i rapport_mal.md |
| 3.2   | Teori og litteratursøk                                            | Magnus Ødegård | ✅ Fullført     | Seksjon 2.0 og 3.0 skrevet inn i rapport_mal.md |
| 3.2.1 | Søk og gjennomgang av relevante artikler                          | Magnus Ødegård | ✅ Fullført     | Appel et al. (2020) og Schoonbee et al. (2022) gjennomgått |
| 3.2.2 | Oppsummering av teorigrunnlag for rapporten                       | Magnus Ødegård | ✅ Fullført     | 2.0 Litteratur og 3.0 Teori (6 delkapitler) skrevet inn |
| 3.3   | Casebeskrivelse og datainnsamling                                 | Magnus Ødegård | ✅ Fullført     | 1 000 fakturaer, 15 kolonner mottatt fra veileder |
| 3.3.1 | Anonymisering og klargjøring av fakturadatasett                   | Magnus Ødegård | ✅ Fullført     | 29 fakturaer med status «Ubetalt» identifisert og ekskludert |
| 3.3.2 | Eksplorativ dataanalyse (EDA)                                     | Magnus Ødegård | ✅ Fullført     | eda.py – 9 figurer, leverandørprofil og features.csv produsert |
| 3.4   | Data, metode og modellering (KI-implementasjon)                   | Magnus Ødegård | ✅ Fullført     |       |
| 3.4.1 | Feature engineering – fakturaspesifikke variabler                 | Magnus Ødegård | ✅ Fullført     | betalingsfrist_dager, netto_dager, faktura_maned, faktura_kvartal |
| 3.4.2 | Feature engineering – historiske betalingsvariabler               | Magnus Ødegård | ✅ Fullført     | Leverandørrisikoscore, one-hot-enkoding av kategoriske variabler |
| 3.4.3 | Trening av kandidatmodeller                                       | Magnus Ødegård | ✅ Fullført     | Log.reg (AUC 0.706), RF (0.695), XGBoost (0.661) baseline |
| 3.4.4 | Hyperparameterjustering og modellvalg                             | Magnus Ødegård | ✅ Fullført     | RF tunet (AUC 0.698), XGBoost tunet (AUC 0.720) – beste modell |
| 3.5   | Analyse og resultater – kjøre modeller og dokumentere funn        | Magnus Ødegård | ✅ Fullført     |       |
| 3.5.1 | Evaluering av modellytelse (AUC-ROC, F1-score, presisjon/recall)  | Magnus Ødegård | ✅ Fullført     | Beste: XGBoost tunet – AUC 0.720, F1 0.621, Recall 0.833 |
| 3.5.2 | Klassifisering av fakturaer i risikoategorier                     | Magnus Ødegård | ✅ Fullført     | Lav 273 (7 % forsinket) / Middels 279 (28 %) / Høy 419 (55 %) |
| 3.6   | Diskusjon – tolke funn mot teori og problemstilling               | Magnus Ødegård | ✅ Fullført     | Seksjon 9.0 skrevet inn – modellytelse, beslutningsstøtteverdi, begrensninger |
| 3.7   | Peer-to-peer review av annen gruppes utkast                       | Magnus Ødegård | ⬜ Ikke startet |       |
| 3.8   | Godkjent hovedutkast til forskningsrapport (min. 80–90 % ferdig) | Magnus Ødegård | ⏳ Pågår        | Seksjon 1–9 komplett; gjenstår: 10.0 Konklusjon, Sammendrag/Abstract, 11.0 Bibliografi |
| 3.8.1 | Ferdigstille alle rapportseksjoner (seksjon 1–9 komplett)         | Magnus Ødegård | ✅ Fullført     | Seksjon 1–9 skrevet inn i rapport_mal.md; 10.0, Sammendrag/Abstract og 11.0 håndteres i Fase 4 |
| 3.8.2 | Intern gjennomgang og korrektur av hele utkastet                  | Magnus Ødegård | ✅ Fullført     | AI-assistert gjennomgang fullført; funn dokumentert i SENSORRAPPORT_OG_AI_INSTRUKS.md – 6 kritiske mangler og 4 metodiske svakheter identifisert |
| 3.8.3 | Levere utkast til veileder for tilbakemelding                     | Magnus Ødegård | ⬜ Ikke startet |       |
| 3.8.4 | Motta og innarbeide veiledertilbakemelding – oppnå godkjenning    | Magnus Ødegård | ⬜ Ikke startet |       |

#### Fase 4 – Avslutning (27. apr – 31. mai)

| ID  | Leveranse                                       | Eier           | Status          | Notat |
|-----|-------------------------------------------------|----------------|-----------------|-------|
| 4.1 | Konklusjon – besvar problemstillingen eksplisitt| Magnus Ødegård | ⬜ Ikke startet |       |
| 4.2 | Ferdigstille introduksjon                       | Magnus Ødegård | ⬜ Ikke startet |       |
| 4.3 | Kvalitetssikring, korrektur og referanseliste   | Magnus Ødegård | ⬜ Ikke startet |       |

### Omfangsverifikasjon

Alle leveranser skal verifiseres av prosjektleder (Magnus Ødegård) og gjennomgås av veileder. Leveranser anses godkjent etter tilbakemelding fra veileder.

---

## Fremdrift

### Avhengighetsdiagram

Prosjektarbeidet følger en sekvensiell struktur der hver fase bygger på forrige:

Proposal → Prosjektstyringsplan → Datainnsamling → EDA → Modellutvikling → Review → Rapport

### Gantt-plan

Skrives i MS-project og legges ved i TEAMS-delt mappe ved "G-17 - MAGNUS INDIVIDUELL". Oppdateres jevnlig ved nådde tidsfrister og dersom det oppdages ekstra oppgaver som krever planlegging.

### Kritisk linje

**Proposal → Prosjektstyringsplan → Datainnsamling → EDA → Modellutvikling → Rapport**

Forsinkelse i noen av disse fasene vil direkte påvirke sluttleveransen.

### Milepæler

| #  | Milepæl                               | Planlagt dato | Status        |
|----|---------------------------------------|---------------|---------------|
| M1 | Godkjent proposal (Fase 1)            | 2026-02-09    | ✅ Fullført   |
| M2 | Godkjent prosjektstyringsplan (Fase 2)| 2026-03-17    | ✅ Fullført   |
| M3 | Ferdig datagrunnlag (Fase 3)          | 2026-04-11    | ✅ Fullført   |
| M4 | Ferdig EDA og feature engineering     | 2026-04-18    | ✅ Fullført   |
| M5 | Ferdig og evaluert modell             | 2026-04-17    | ✅ Fullført   |
| M6 | Innlevert endelig rapport (Fase 4)    | 2026-05-31    | ⏳ Kommende  |

---

## Risiko

### Prosess for risikostyring

Risikoer identifiseres og vurderes av prosjektleder (Magnus Ødegård) gjennom hele prosjektet. Risikoregisteret gjennomgås jevnlig og oppdateres ved behov.

### Risikoregister

| ID | Risiko                                   | Sannsynlighet | Konsekvens | Nåværende nivå | Tiltak / Kommentar                                                                                                        |
|----|------------------------------------------|---------------|------------|----------------|---------------------------------------------------------------------------------------------------------------------------|
| R1 | Utilstrekkelig datakvalitet              | Middels       | Høy        | Lav            | EDA gjennomført – datasett komplett; 29 ubetalte fakturaer ekskludert, 971 fakturaer brukes til trening                  |
| R2 | Manglende tilgang til data               | Lav           | Høy        | Lukket         | Datasett mottatt og bekreftet 2026-04-16 – S1 løst                                                                       |
| R3 | Modellen gir lav prediksjonsytelse       | Middels       | Middels    | Lukket         | Ubetalt-klassen ekskludert; XGBoost tunet gir beste ytelse (AUC 0.720) – benchmark ≥ 0.75 ikke nådd, tolkes i diskusjon |
| R4 | Tidspress mot innleveringsfrist          | Middels       | Middels    | Middels        | Modell og seksjon 1–9 fullført; neste kritiske frist: ferdig rapport 2026-05-31. Gjenstår: 11 utbedringsoppgaver fra intern gjennomgang |
| R5 | Konfidensialitetsproblemer med data      | Lav           | Høy        | Lav            | Full anonymisering gjennomført; bruk av syntetiske data ved behov                                                         |
| R6 | Konseptdrift – relasjon mellom variabler endrer seg over tid | Middels | Middels | Lav       | Tidsbasert datadeling ble ikke implementert (tilfeldig 80/20-splitt brukt) – erkjent som metodisk begrensning i seksjon 5.1 og 9.3    |

---

## Saker

Saker registreres, følges opp og lukkes løpende gjennom prosjektets levetid.

| ID | Sak                                                              | Status    | Ansvarlig      | Frist      |
|----|------------------------------------------------------------------|-----------|----------------|------------|
| S1 | Avklare datatilgang fra veileder                                 | ✅ Løst   | Magnus Ødegård | 2026-04-16 |
| S2 | Avklare håndtering av 29 «Ubetalt»-fakturaer (ekskludere/label) | ✅ Løst   | Magnus Ødegård | 2026-04-16 |

---

## Interessenter

| Interessent           | Rolle                     | Behov / Prioritering                          | Planlagt kommunikasjon         |
|-----------------------|---------------------------|-----------------------------------------------|--------------------------------|
| Magnus Ødegård        | Prosjektleder / student   | Gjennomføre og levere prosjektet              | Løpende egenoppfølging         |
| Veileder (BI)         | Faglig veileder / sponsor | Kvalitetssikring og akademisk godkjenning     | Veiledermøter etter behov      |
| Bedriften             | Datakunde / interessent   | Nyttig og konfidensielt håndtert resultat     | Ved levering av rapport        |

---

## Ressurser

### Prosjektteam

| Navn            | Rolle                    | Ansvar                                      |
|-----------------|--------------------------|---------------------------------------------|
| Magnus Ødegård  | Prosjektleder / student  | Alt prosjektarbeid, analyse, rapport        |
| Veileder (BI)   | Faglig veileder          | Tilbakemelding, godkjenning av leveranser   |

### Kritiske ressurser

- **Historisk fakturadata (Bedriften):** Nødvendig for modelltrening. Mottatt og anonymisert 2026-04-16 – 1 000 fakturaer, 15 kolonner.
- **Tid:** Individuelt prosjekt – alt avhenger av studentens tilgjengelige tid og arbeidskapasitet.

---

## Kommunikasjon

### Veiledermøter

Veiledermøter gjennomføres etter behov for å sikre faglig kvalitet og fremdrift. Spørsmål og leveranser sendes til veileder i forkant av møter.

### Statusoppdateringer

Prosjektleder (Magnus Ødegård) oppdaterer dette dokumentet, Gantt-plan og risikoregister jevnlig gjennom prosjektet.

### Fase-leveranser

Leveranser for hver fase (proposal, plan, rapport) leveres i henhold til kursets tidsplan og gjennomgås av veileder.

---

## Kvalitet

### Kvalitetsprinsipper

- **Planlegging:** Kvalitet bygges inn i arbeidet, ikke kun inspiseres i etterkant.
- **Egnet for formålet:** Alle leveranser skal faktisk kunne brukes som beslutningsstøtte.
- **Kontinuerlig forbedring:** Erfaringer tas med videre gjennom prosjektet.

### Fagfellevurderinger

Prosjektleder gjennomfører egenvurdering av alle leveranser før innlevering. Veileder gjennomfører formell vurdering.

### Modellytelse og benchmark

Appel et al. (2020) oppnådde 77 % nøyaktighet i et tilsvarende prediksjonsproblem for fakturabetaling. Dette brukes som referansepunkt (benchmark) for prosjektets modell. Målnivå er satt til AUC-ROC ≥ 0.75 og F1-score ≥ 0.70 på hold-out testsettet.

**Oppnådde resultater:**

| Modell                    | AUC-ROC | F1-score | Presisjon | Recall |
|---------------------------|---------|----------|-----------|--------|
| Logistisk regresjon       | 0.706   | –        | –         | –      |
| Random Forest (baseline)  | 0.695   | –        | –         | –      |
| XGBoost (baseline)        | 0.661   | –        | –         | –      |
| Random Forest (tunet)     | 0.698   | –        | –         | –      |
| **XGBoost (tunet)**       | **0.720** | **0.621** | –      | **0.833** |

Beste modell er XGBoost (tunet) med AUC-ROC 0.720. Benchmark på ≥ 0.75 ble ikke nådd, noe som diskuteres i rapportens diskusjonsseksjon (9.0) i lys av datasettets størrelse og klasseubalanse.

**Risikoklassifisering av 971 fakturaer:**

| Klasse  | Antall fakturaer | Andel forsinket |
|---------|-----------------|-----------------|
| Lav     | 273             | 7 %             |
| Middels | 279             | 28 %            |
| Høy     | 419             | 55 %            |

---

## Anskaffelser

Prosjektet benytter kun åpen kildekode-programvare som Python og internt datasett fra Bedriften. Ingen eksterne anskaffelser er planlagt.

---

## Endringskontrollprosess

Alle vesentlige endringer i omfang, fremdriftsplan eller metode etter at denne planen er godkjent, skal:

1. Dokumenteres med begrunnelse av prosjektleder.
2. Diskuteres med veileder.
3. Oppdateres i prosjektstyringsplanen og Gantt-plan ved godkjenning.

Mindre justeringer som ikke påvirker prosjektmålet eller sluttleveransen kan gjennomføres av prosjektleder uten formell godkjenning, men skal loggføres i endringsloggen nedenfor.

---

## Endringslogg

| Dato       | Endring                                                                              | Arbeidsøkt / Grunn       |
|------------|--------------------------------------------------------------------------------------|--------------------------|
| 2026-04-16 | Statussporing lagt til i dokumentet; milepæler og WBS oppdatert med statuskolonne   | Initiell statusintegrasjon |
| 2026-04-16 | Datasett bekreftet mottatt (1 000 fakturaer, 15 kolonner) – S1 lukket               | Arbeidsøkt 2             |
| 2026-04-16 | EDA fullført: klasseubalanse, forsinkelsesdist., kategori- og leverandøranalyse      | Arbeidsøkt 2             |
| 2026-04-16 | Feature engineering fullført: 34 features, features.csv produsert                   | Arbeidsøkt 2             |
| 2026-04-16 | Leverandørrisikoprofil laget: risikoscore per leverandør, 9 figurer generert        | Arbeidsøkt 2             |
| 2026-04-16 | M3 og M4 markert fullført – ny åpen sak S2 (Ubetalt-klassen)                        | Arbeidsøkt 2             |
| 2026-04-16 | S2 løst: 29 Ubetalt-fakturaer ekskludert fra trening (971 brukes)                   | Arbeidsøkt 3             |
| 2026-04-16 | model.py opprettet: Log.reg (AUC 0.706), RF (0.695), XGBoost (0.661) – 3.4.3 ✅    | Arbeidsøkt 3             |
| 2026-04-16 | 5 figurer generert (10–14), modell_resultater.csv produsert                         | Arbeidsøkt 3             |
| 2026-04-16 | 3.1 fullført: seksjon 1.0–1.4 skrevet inn i rapport_mal.md                         | Arbeidsøkt 4             |
| 2026-04-16 | 3.2 fullført: seksjon 2.0 Litteratur og 3.0 Teori skrevet inn i rapport_mal.md     | Arbeidsøkt 4             |
| 2026-04-17 | model.py gjenopprettet og kjørt på nytt; 29 Ubetalt-fakturaer ekskludert korrekt   | Arbeidsøkt 5             |
| 2026-04-17 | 3.4.4 fullført: RF tunet AUC 0.698, XGBoost tunet AUC 0.720 – benchmark ikke nådd | Arbeidsøkt 5             |
| 2026-04-17 | 3.5.1 fullført: alle 5 modeller evaluert med AUC, F1, presisjon, recall, nøyaktighet| Arbeidsøkt 5             |
| 2026-04-17 | 3.5.2 fullført: 971 fakturaer klassifisert – Lav 273 / Middels 279 / Høy 419       | Arbeidsøkt 5             |
| 2026-04-17 | 3.6 fullført: diskusjon skrevet inn i rapport_mal.md (seksjon 9.0)                  | Arbeidsøkt 6             |
| 2026-04-20 | 3.8 lagt til i WBS: Godkjent hovedutkast med deloppgaver 3.8.1–3.8.4               | Planlegging              |
| 2026-04-22 | 3.8.1 markert fullført: seksjon 1–9 skrevet inn i rapport_mal.md; gjenstår i Fase 4: 10.0, Sammendrag/Abstract, 11.0 Bibliografi | Statusoppdatering |
| 2026-04-22 | M5 markert fullført (modell ferdig og evaluert 2026-04-17)                          | Statusoppdatering        |
| 2026-04-22 | 3.8.2 fullført: AI-assistert intern gjennomgang; SENSORRAPPORT_OG_AI_INSTRUKS.md produsert med 6 kritiske mangler og 4 metodiske svakheter | Arbeidsøkt 7 |
| 2026-04-22 | R4 oppdatert: ny kritisk frist er rapport 2026-05-31 (modell ferdig). R6 korrigert: tidsbasert splitt ikke implementert, erkjent i rapporten | Statusoppdatering |

---

## Vedlegg

### Vedlegg A – Kravliste

*(Utfylles under gjennomføringen)*

### Vedlegg B – WBS-ordliste

*(Se WBS-tabeller under Omfang)*
