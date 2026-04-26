---
Sensor: AI-agent (skill_sensur.md – Høgskolen i Molde, LOG650)
Student: Magnus Ødegård
Rapport: Finansiell logistikk og beslutningstøtte ved hjelp av KI
Dato: 2026-04-25
---

## Tilbakemelding: Fullstendig sensorvurdering

---

### Styrker

- **Innledning (1.0–1.4)** er gjennomarbeidet og faglig presis. Problemstillingen er klart avgrenset, antagelsene er eksplisitt formulert (A1–A4) og koblet til konkrete metodiske valg. Avgrensningene er realistiske og godt begrunnet. Dette er på B/A-nivå.

- **Litteraturgjennomgang (2.0)** er solid. Begge primærkilder (Appel et al. og Schoonbee et al.) er gjengitt nøyaktig, med korrekt gjengivelse av datasettkarakteristika, metodiske bidrag og ytelsestall. Sammenstillingstabellen (Tabell 2.1) er pedagogisk og faglig riktig.

- **Teori (3.0)** dekker alle relevante konsepter for oppgaven: lineær og ikke-lineær klassifisering, evalueringsmetrikker, feature engineering, konseptdrift og DSS. Begrepsbruk er korrekt. Forklaringen av hvorfor accuracy er misvisende ved klasseubalanse (3.3) er særlig god.

- **Metodebeskrivelse (5.0)** er presis og reproduserbar. CRISP-DM-forankringen er eksplisitt, stratifisert splitt og klassevekting er korrekt implementert og beskrevet. Testsettet er holdt tilbake – ingen datalekkasje i evalueringsprosessen.

- **Resultatpresentasjon (8.1, Tabell 8.1)** er ryddig og sammenlignbar. Alle fem modeller er rapportert med samme sett av metrikker. Benchmark-avviket er erkjent og forklart uten å overdrive eller underdrive funnene.

- **Diskusjon (9.0)** er analytisk sterk. Forklaringen av benchmark-gapet (lite datasett + syntetisk data) er faglig korrekt og balansert. Beslutningsstøtteverdien argumenteres godt via risikoklassifiseringens separasjon (7 % / 28 % / 55 %) og recall-tall (0,833).

- **Kode og metodikk:** RandomizedSearchCV med StratifiedKFold (k=5) og AUC som optimaliseringskriterium er korrekt valg. Klassevekting fremfor SMOTE er et akseptabelt og velbegrunnet valg.

---

### Svakheter

#### Kritiske mangler (hindrer bestått i nåværende tilstand)

**K1 – Konklusjon (10.0) mangler.**
Seksjonen inneholder kun «Skriv her.» Problemstillingen er aldri eksplisitt besvart. En akademisk rapport uten konklusjon kan ikke bestå.

**K2 – Bibliografi (11.0) er ufullstendig.**
Kun to kilder er listet (Appel et al. og Schoonbee et al.), men rapporten siterer ytterligere referanser implisitt via teoridelen (Random Forest, XGBoost, feature engineering, konseptdrift, DSS). Alle siterte verk må med.

**K3 – Sammendrag og Abstract er ikke skrevet.**
Begge seksjoner inneholder kun instruksjonsplassholdere. Dette er obligatorisk innhold.

---

#### Metodiske svakheter (bør adresseres)

**M1 – In-sample evaluering av risikoklassifisering (8.3).**
Sluttmodellen er trent på alle 971 fakturaer og deretter klassifiserer de samme 971 fakturaene. De rapporterte forsinkelsesratene (7 % / 28 % / 55 %) er in-sample-estimater og ikke generaliserbare. Dette er en vesentlig metodisk svakhet som ikke erkjennes i teksten. En sensor vil spørre direkte om dette.

**M2 – Valget av binær fremfor multiklasse klassifisering er ikke begrunnet.**
Prosjektet bruker binær klassifisering, men Schoonbee et al. (2022) – som er primær metodereferanse – bruker fire klasser. Avviket er aldri kommentert i rapporten. Begrunnelsen er tilgjengelig (lite datasett) men skal stå i teksten.

**M3 – Tidsbasert datadeling ikke implementert eller erkjent.**
For temporale fakturadata er tilfeldig splitt en svakere metodikk enn tidsbasert splitt. Dette er ikke kommentert i metodeseksjonen.

**M4 – Benchmark-sammenligning er ikke kvalifisert tilstrekkelig.**
Diskusjonen (9.1) adresserer datasettstørrelse, men understreker ikke eksplisitt at AUC ≥ 0,75 er en aspirerende, ikke komparativ, standard for et datasett 180× mindre enn primærkildenes.

---

#### Innholdsmessige forbedringer (hever karakter)

**I1 – EDA-seksjonen (7.1) mangler konkrete tall.**
Teksten beskriver hva figurene *viser*, men oppgir nesten ingen statistiske verdier: gjennomsnittlig forsinkelse, median, standardavvik, forsinkelsesrate per kategori. Tallene er tilgjengelige fra analysen og skal stå i teksten.

**I2 – Etikk og fairness er ikke drøftet.**
En rapport om KI-beslutningsstøtte i offentlig sektor mangler drøfting av: algoritmisk skjevhet (visse leverandørkategorier kan systematisk flagges som høyrisiko), forklarbarhet (XGBoost er en black-box modell), og GDPR-hensyn. Dette forventes på dette nivået.

**I3 – Litteraturgrunnlaget er smalt (2 primærkilder).**
For en akademisk rapport er to primærkilder utilstrekkelig. Standardreferanser for Random Forest (Breiman, 2001), XGBoost (Chen & Guestrin, 2016), feature engineering og konseptdrift bør inngå i bibliografien.

**I4 – Overskriften «1.2 Delproblemer (valgfri)» inneholder instruksjonstekst.**
Parentesen «(valgfri)» er en malsignatur, ikke en akademisk overskrift. Skal fjernes.

**I5 – Figur 1 (klasseubalanse) er gjengitt to ganger** (seksjon 5.2 og 7.1) uten kommentar. Én av forekomstene bør fjernes eller kryssrefereres eksplisitt.

---

### Forbedringsforslag (prioritert rekkefølge)

1. **Skriv konklusjon (10.0):** Besvar problemstillingen direkte. Oppsummer de tre delproblemene (predikert sannsynlighet → AUC 0,720; forsinkelsesestimering → proxy; risikoklassifisering → 7/28/55 %). Nevn beslutningsstøtteverdien og veien videre. Ca. 300 ord.

2. **Fyll ut bibliografi (11.0):** Legg til minimum: Breiman (2001), Chen & Guestrin (2016), samt de øvrige verk som er implisitt sitert i teoriseksjonen. Sorter alfabetisk i APA 7.

3. **Skriv Sammendrag og Abstract:** Følg IMRaD-strukturen komprimert. Problem → Metode → Funn → Konklusjon. Ca. 150–200 ord per del.

4. **Erkjenn in-sample-problemet i 8.3:** Legg til ett avsnitt som forklarer at forsinkelsesratene per risikoklasse er in-sample og skal tolkes som illustrasjon av metodikkens potensial, ikke som ut-av-utvalg ytelse.

5. **Begrunne binær klassifisering i 5.1:** Legg til én setning om at multiklasse ble fravalgt grunnet datasettets størrelse, og knytt dette til Appel et al. (2020) som primærreferanse.

6. **Legg til konkrete tall i 7.1:** Median og gjennomsnittlig forsinkelse, forsinkelsesrate per kategori, fordelingstall – disse er tilgjengelige og skal inn i teksten.

7. **Legg til etikk/fairness-avsnitt i 9.3:** Kort drøfting av algoritmisk skjevhet, forklarbarhet (SHAP), og GDPR-hensyn.

8. **Fiks overskrift 1.2:** Fjern «(valgfri)».

---

### Tentativ karakter

**Karakter: D (Nokså god) – betinget**

**Begrunnelse:**
Rapportens skrevne seksjoner holder faglig god til meget god kvalitet. Problemstilling, teori, metode og diskusjon er velbegrunnet og akademisk korrekt. Teknisk implementasjon er solid.

Karakteren er holdt på D fordi rapporten i nåværende tilstand er **strukturelt ufullstendig**: konklusjon, sammendrag og fullstendig bibliografi er obligatoriske komponenter som mangler. Uten disse kan rapporten ikke bestå (F).

Med de kritiske manglene utbedret (K1–K3) vil rapporten med høy sannsynlighet ligge på **C–B**. Dersom de metodiske svakhetene (M1–M4) og innholdsmessige forbedringene (I1–I3) også inkorporeres, er **B** et realistisk sluttresultat.

---

### Spørsmål sensor ville stilt (muntlig eksaminasjon)

1. Konklusjonen din sier at KI *kan* brukes. Hva er det sterkeste argumentet for at metoden er anvendbar på ekte fakturadata fra Bedriften, gitt at AUC 0,720 er under benchmark?

2. I seksjon 8.3 klassifiserer du alle 971 fakturaer med en modell trent på de samme 971 fakturaene. Hva er den metodiske konsekvensen av dette, og hva bør gjøres annerledes i produksjon?

3. Du valgte binær klassifisering. Schoonbee et al. (2022) bruker fire klasser. Hva mister du ved å gå fra fire klasser til to, og hva vinner du?

4. Random Forest er beste modell i Schoonbee et al. (2022), men XGBoost er beste modell hos deg. Hva kan forklare dette avviket?

5. Gjennomsnittlig antall dager forsinket per leverandør er den klart viktigste featuren. Hvordan sikrer du at denne featuren ikke introduserer datalekkasje for nye leverandører uten historikk?

6. Datasettets syntetiske natur er nevnt som en sentral begrensning. Hvis du skulle redesigne prosjektet med tilgang til ekte data – hva ville de tre viktigste endringene i metodikken vært?

---

*Merk: Denne evalueringen er basert på rapporten slik den foreligger per 2026-04-25. Vurderingen er veiledende og vil endres i takt med at manglende seksjoner skrives ferdig.*
