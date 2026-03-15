# Prosjektstyringsplan
for
Finansiell logistikk og beslutningstøtte ved hjelp av KI

**Dato:** 2026-03-14

**Utarbeidet av:** Magnus Ødegård

**Autorisert av:** 

---

## Innhold

1. [Sammendrag](#sammendrag)
2. [Omfang](#omfang)
3. [Fremdrift](#fremdrift)
4. [Risiko](#risiko)
6. [Saker](#saker)
7. [Interessenter](#interessenter)
8. [Ressurser](#ressurser)
9. [Kommunikasjon](#kommunikasjon)
10. [Kvalitet](#kvalitet)
11. [Anskaffelser](#anskaffelser)
12. [Endringskontrollprosess](#endringskontrollprosess)

---

## Sammendrag

Dette dokumentet utgjør prosjektstyringsplanen for prosjektet «Finansiell logistikk og beslutningstøtte ved hjelp av KI». Det dokumenterer planbaselines for omfang, fremdrift og risiko, og gir tilleggsinformasjon for å støtte prosjektleder i vellykket gjennomføring.

Dette prosjektet støtter følgende mål: Å forbedre Bedriftens evne til å identifisere fakturaer med høy risiko for sen betaling gjennom datadrevet prediksjon og beslutningsstøtte.

Dette er et levende dokument, og skal oppdateres av prosjektleder ved behov gjennom prosjektets løpetid.

### Behov

Bedriften håndterer et stort volum av fakturaer, og sen betaling etter forfallsdato medfører ineffektiv ressursbruk og redusert kontroll over likviditet og leverandørforhold. Det finnes i dag ikke et systematisk og datadrevet verktøy for å forutsi hvilke fakturaer som er i risikosonen for forsinkelse. Prosjektet svarer på behovet for bedre prioritering og oppfølging av fakturaer.

### Sponsor

[Veileder ved Handelshøyskolen BI / Bedriften] er sponsor for dette prosjektet, ansvarlig for prosjektbudsjettet og myndighet for godkjenning av denne prosjektplanen og eventuelle endringer under gjennomføringen.

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
- Klassifisering av fakturaer i risikoategorier.
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

| Feature                   | Beskrivelse                                                         |
|---------------------------|---------------------------------------------------------------------|
| GjennomsnittDagerForsinket | Gjennomsnittlig antall dager forsinket på tidligere fakturaer       |
| AntallFakturerITide       | Antall tidligere fakturaer betalt innen forfall                     |
| AntallFakturerForsinket   | Antall tidligere fakturaer betalt etter forfall                     |
| AndelITide                | Andel av tidligere fakturaer betalt i tide                          |
| DagerSidenSisteBetaling   | Antall dager siden forrige betaling                                 |
| BetalingsdagIMåned        | Gjennomsnittlig dag i måneden betaling skjer                        |
| UteståendeFaktura         | Binær: 1 hvis leverandør har utestående faktura, 0 ellers           |
| GlobalTrend               | Gjennomsnittlig økning/reduksjon i forsinkelse siste måned          |

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

| ID  | Leveranse                          | Eier            |
|-----|------------------------------------|-----------------|
| 1.0 | Fase 1 – Proposal                  | Magnus Ødegård  |
| 2.0 | Fase 2 – Prosjektstyringsplan      | Magnus Ødegård  |
| 3.0 | Datainnsamling og forberedelse     | Magnus Ødegård  |
| 3.1 | Anonymisering og datarensing       | Magnus Ødegård  |
| 3.2 | Eksplorativ dataanalyse (EDA)      | Magnus Ødegård  |
| 4.0 | Modellutvikling                    | Magnus Ødegård  |
| 4.1 | Feature engineering – fakturadata  | Magnus Ødegård  |
| 4.2 | Feature engineering – historiske betalingsvariabler | Magnus Ødegård  |
| 4.3 | Trening av kandidatmodeller        | Magnus Ødegård  |
| 4.4 | Evaluering og modellvalg           | Magnus Ødegård  |
| 5.0 | Fase 3 – Review                    | Magnus Ødegård  |
| 6.0 | Fase 4 – Rapport og presentasjon   | Magnus Ødegård  |

### Omfangsverifikasjon

Alle leveranser skal verifiseres av prosjektleder (Magnus Ødegård) og gjennomgås av veileder. Leveranser anses godkjent etter tilbakemelding fra veileder.

---

## Fremdrift

### Avhengighetsdiagram

Prosjektarbeidet følger en sekvensiell struktur der hver fase bygger på forrige:

Proposal → Prosjektstyringsplan → Datainnsamling → EDA → Modellutvikling → Review → Rapport

### Gantt-plan

| Fase / Leveranse                   | Start      | Slutt      |
|------------------------------------|------------|------------|
| Fase 1 – Proposal                  | 2026-01-13 | 2026-02-23 | Ferdig
| Fase 2 – Prosjektstyringsplan      | 2026-02-23 | 2026-03-27 | Jobbes med
| Datainnsamling og forberedelse     | 2026-02-23 | 2026-04-11 | Behov for data fra veileder
| Eksplorativ dataanalyse (EDA)      | 2026-04-04 | 2026-04-18 |
| Modellutvikling og evaluering      | 2026-04-18 | 2026-05-09 |
| Fase 3 – Review                    | 2026-05-09 | 2026-05-16 |
| Fase 4 – Rapport og presentasjon   | 2026-05-16 | 2026-05-30 |

Siste first 1.Juni

### Kritisk linje

Den kritiske linjen er:

**Proposal → Prosjektstyringsplan → Datainnsamling → EDA → Modellutvikling → Rapport**

Forsinkelse i noen av disse fasene vil direkte påvirke sluttleveransen.

### Milepæler

| Milepæl                              | Planlagt dato |
|--------------------------------------|---------------|
| Godkjent proposal (Fase 1)           | 2026-02-23    |
| Godkjent prosjektstyringsplan        | 2026-03-27    |
| Ferdig datagrunnlag                  | 2026-04-11    | Behov for data fra veileder
| Ferdig EDA og feature engineering    | 2026-04-18    |
| Ferdig og evaluert modell            | 2026-05-09    |
| Innlevert endelig rapport (Fase 4)   | 2026-05-30    |

---

## Risiko

### Prosess for risikostyring

Risikoer identifiseres og vurderes av prosjektleder (Magnus Ødegård) gjennom hele prosjektet. Risikoregisteret gjennomgås jevnlig og oppdateres ved behov.

### Risikoregister

| ID  | Risiko                                   | Sannsynlighet | Konsekvens | Tiltak                                               |
|-----|------------------------------------------|---------------|------------|------------------------------------------------------|
| R1  | Utilstrekkelig datakvalitet              | Middels       | Høy        | Grundig datarensing og simulering av manglende data  |
| R2  | Manglende tilgang til data               | Lav           | Høy        | Anonymisere og tilpasse datasett tidlig i prosjektet |
| R3  | Modellen gir lav prediksjonsyteevne      | Middels       | Middels    | Teste flere modeller og tuning av hyperparametere    |
| R4  | Tidspress mot innleveringsfrist          | Middels       | Middels    | Følge Gantt-plan; justere omfang ved behov           |
| R5  | Konfidensialitetsproblemer med data      | Lav           | Høy        | Full anonymisering; bruk av syntetiske data ved behov|
| R6  | Konseptdrift – relasjon mellom variabler og utfall endrer seg over tid | Middels | Middels | Tidsbasert datadeling; periodisk retrening av modell; overvåke ytelsesmål |

---

## Saker

Ingen åpne saker per oppstart av prosjektet. Saker vil registreres og følges opp løpende.

| ID  | Sak | Status | Ansvarlig | Frist |
|-----|-----|--------|-----------|-------|
| –   | –   | –      | –         | –     |

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

- **Historisk fakturadata (Bedriften):** Nødvendig for modelltrening. Må anonymiseres og klargjøres tidlig.
- **Tid:** Individuelt prosjekt – alt avhenger av studentens tilgjengelige tid og arbeidskapasitet.

---

## Kommunikasjon

### Veiledermøter

Veiledermøter gjennomføres etter behov for å sikre faglig kvalitet og fremdrift. Spørsmål og leveranser sendes til veileder i forkant av møter.

### Statusoppdateringer

Prosjektleder (Magnus Ødegård) oppdaterer Gantt-plan og risikoregister jevnlig gjennom prosjektet.

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

### Omfangsverifikasjon

Modellens ytelse evalueres med standardmål: presisjon, recall, F1-score og AUC-ROC. Terskler fastsettes basert på bruksscenarioet (prioritering av oppfølging vs. automasjon).

Appel et al. (2020) oppnådde 77 % nøyaktighet i et tilsvarende prediksjonsproblem for fakturabetaling. Dette brukes som referansepunkt (benchmark) for prosjektets modell. Målnivå settes til AUC-ROC ≥ 0.75 og F1-score ≥ 0.70 på hold-out testsettet. Alle kandidatmodeller dokumenteres og sammenlignes i rapporten.

---

## Anskaffelser

Prosjektet benytter kun åpen kildekode-programvare (Python, scikit-learn, pandas m.fl.) og internt datasett fra Bedriften. Ingen eksterne anskaffelser er planlagt.

---

## Endringskontrollprosess

Alle vesentlige endringer i omfang, fremdriftsplan eller metode etter at denne planen er godkjent, skal:

1. Dokumenteres med begrunnelse av prosjektleder.
2. Diskuteres med veileder.
3. Oppdateres i prosjektstyringsplanen og Gantt-plan ved godkjenning.

Mindre justeringer som ikke påvirker prosjektmålet eller sluttleveransen kan gjennomføres av prosjektleder uten formell godkjenning, men skal loggføres.

---

## Vedlegg

### Vedlegg A – Kravliste

*(Utfylles under gjennomføringen)*

### Vedlegg B – WBS-ordliste

*(Se tabell under Omfang)*

### Vedlegg C – Saksliste

| Sak | Status | Ansvarlig | Frist |
|-----|--------|-----------|-------|
| –   | –      | –         | –     |

### Vedlegg D – Mal for månedlig rapport

*(Ikke aktuelt for individuelt studentprosjekt – erstattes av statusoppdatering til veileder)*

### Vedlegg E – Mal for brukerreview

*(Ikke aktuelt – gjennomføres som egenvurdering og veiledertilbakemelding)*

### Vedlegg F – Skjema for endringsforespørsel

| Felt                        | Beskrivelse |
|-----------------------------|-------------|
| Dato                        |             |
| Beskrivelse av endring      |             |
| Begrunnelse                 |             |
| Konsekvens for omfang       |             |
| Konsekvens for fremdrift    |             |
| Beslutning / Godkjenning    |             |
