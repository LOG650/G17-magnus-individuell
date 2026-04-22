# Sensorrapport og AI-instruksjoner – LOG650 Individuelt prosjekt
**Utarbeidet:** 2026-04-22  
**Prosjekt:** Finansiell logistikk og beslutningstøtte ved hjelp av KI  
**Student:** Magnus Ødegård  
**Kurs:** LOG650  

---

## Del A – Sensorrapport: Funn og vurdering

### A.1 Oppsummering

Rapporten er faglig solid der den er skrevet. Teoretisk grunnlag, metodebeskrivelse og diskusjon er av god akademisk kvalitet. Python-implementasjonen er teknisk korrekt. Rapporten er imidlertid **strukturelt ufullstendig** og kan i nåværende tilstand ikke bestå: konklusjon, bibliografi og sammendrag mangler, og alle 17 figurer er plassholdere.

---

### A.2 Kritiske mangler (hindrer bestått)

| # | Mangl | Lokasjon i rapport | Alvorlighet |
|---|---|---|---|
| K1 | Konklusjon (10.0) ikke skrevet | Seksjon 10.0, kun «Skriv her.» | Kritisk |
| K2 | Bibliografi (11.0) tom | Seksjon 11.0, kun HTML-kommentar | Kritisk |
| K3 | Sammendrag og Abstract ikke skrevet | Toppen av rapporten, plassholdere | Kritisk |
| K4 | 17 figurer er tekstbaserte plassholdere | Seksjon 7.0, 8.0 | Kritisk |
| K5 | Forsidedata ufullstendig | Øverst i rapport_mal.md | Kritisk |
| K6 | Innholdsfortegnelse tom | Etter abstract | Kritisk |

**7 referanser sitert i teksten mangler i bibliografien:**
- Hastie, T., Tibshirani, R., & Friedman, J. (2009). *The Elements of Statistical Learning.*
- James, G., Witten, D., Hastie, T., & Tibshirani, R. (2021). *An Introduction to Statistical Learning.*
- Breiman, L. (2001). Random forests. *Machine Learning, 45*(1), 5–32.
- Chen, T., & Guestrin, C. (2016). XGBoost: A scalable tree boosting system. *KDD '16.*
- Kuhn, M., & Johnson, K. (2019). *Feature Engineering and Selection.*
- Gama, J., Žliobaitė, I., Bifet, A., Pechenizkiy, M., & Bouchachia, A. (2014). A survey on concept drift adaptation. *ACM Computing Surveys, 46*(4).
- Turban, E., Sharda, R., & Delen, D. (2011). *Decision Support and Business Intelligence Systems.*

---

### A.3 Metodiske svakheter (bør adresseres)

**M1 – In-sample evaluering av risikoklassifisering**  
I seksjon 8.3 trenes sluttmodellen på alle 971 fakturaer og klassifiserer deretter de **samme 971 fakturaene**. De rapporterte forsinkelsesratene (7% / 28% / 55%) er in-sample og ikke generaliserbare. Modellen husker treningsdata. Dette bør erkjennes eksplisitt som en metodisk begrensning i seksjon 8.3 eller 9.3.

**M2 – Avvik fra planlagt multiklasse til binær klassifisering**  
Prosjektstyringsplanen (Prosjektstyringsplan_v2.md) beskriver en 4-klasse tilnærming (i tide / 1–30 / 31–60 / 61+ dager) inspirert av Schoonbee et al. (2022). Det faktiske prosjektet implementerte binær klassifisering. Denne avgjørelsen er aldri begrunnet i rapporten. Begrunnelse skal legges til i seksjon 5.1 (Metode).

**M3 – Tidsbasert datadeling ikke implementert**  
Planen beskrev tidsbasert datadeling (eldre data til trening, nyere til test). Koden (`model.py`) bruker tilfeldig 80/20-splitt uten sortering etter dato. Dette er en metodisk svakhet for temporale data. Bør erkjennes i 5.1 eller 9.3.

**M4 – Benchmark-sammenligning er metodisk skjev**  
Benchmark (AUC ≥ 0.75) er fra Appel et al. (2020) med 175 552 fakturaer. Dette prosjektets datasett har 971 fakturaer. Direkte sammenligning er urimelig. Diskusjonen i 9.1 adresserer dette delvis, men bør styrkes med en eksplisitt formulering om at benchmarken er aspirerende, ikke en rettferdig komparativ standard.

---

### A.4 Innholdsmessige forbedringer (hever karakter)

**I1 – EDA-seksjonen mangler faktiske tall i tekst**  
Seksjon 7.1 beskriver hva figurene viser, men oppgir nesten ingen konkrete statistiske verdier. Gjennomsnittlig forsinkelse, median, standardavvik, kategorifordelinger – disse skal stå i teksten, ikke bare i figurer.

**I2 – Litteraturgrunnlag er smalt**  
Kun 2 primærkilder (Appel et al. og Schoonbee et al.) er utilstrekkelig for en akademisk rapport. De 7 teoretiske referansene (Hastie, James, Breiman osv.) finnes allerede i teksten og vil komme inn via bibliografien, men ytterligere kontekstlitteratur om finansiell logistikk og offentlig innkjøp kan styrke oppgaven.

**I3 – Etiske og personvernmessige hensyn mangler**  
Diskusjonsseksjonen (9.0) drøfter ikke: algoritmisk fairness (risiko for systematisk diskriminering av leverandørkategorier), transparens/forklarbarhet (XGBoost er en black-box modell), eller GDPR/personvernhensyn for leverandørdata i offentlig sektor. Dette forventes i en rapport om KI-beslutningsstøtte i offentlig forvaltning.

**I4 – Overskrift 1.2 inneholder «(valgfri)»**  
Seksjonsoverskriften lyder «1.2 Delproblemer (valgfri)». Parentesen skal fjernes i ferdig rapport.

**I5 – Figurreferanser bruker filnavn, ikke figurnummer**  
Alle figurhenvisninger i teksten bruker filnavn som `01_klasseubalanse.png`. En ferdig akademisk rapport bruker «Figur 1», «Figur 2» etc. med tilhørende figurtekst (caption) under hver figur.

---

### A.5 Det som fungerer godt

- Seksjon 1.0–1.4: Godt strukturert, klare avgrensninger og antagelser
- Seksjon 2.0: Grundig og nøyaktig gjennomgang av begge primærkilder
- Seksjon 3.0: Faglig korrekt teori om ML-algoritmer, evalueringsmetrikker og feature engineering
- Seksjon 5.0: Presis metodebeskrivelse – stratifisert splitt, kryssvalidering og klassevekting er korrekt implementert og beskrevet
- Seksjon 8.1 / Tabell 8.1: Ryddig og sammenlignbar resultatpresentasjon
- Seksjon 9.0: God analytisk diskusjon av benchmark-gap og beslutningsstøtteverdi
- `model.py`: Teknisk solid Python-kode, metodisk korrekt struktur

---

## Del B – Instruksjoner til AI-agent for utbedring

> **Til AI-agenten:** Du skal utbedre en akademisk rapport for et logistikkurs (LOG650) ved Høgskolen i Molde. Rapporten handler om KI-basert prediksjon av sene fakturarbetalinger. Nedenfor er alle oppgavene beskrevet eksplisitt med full kontekst. Les rapporten nøye før du gjør endringer – bevar alt eksisterende innhold og endre kun det som er spesifisert.

---

### Kontekstinformasjon (les dette først)

**Rapportfil:** `C:\Users\mrmag\Desktop\SKOLE\LOG650\G17-magnus-individuell\014 fase 4 - report\rapport_mal.md`

**Prosjekt:** Magnus Ødegård har utviklet en maskinlæringsmodell for å predikere om fakturaer betales etter forfallsdato. Datasettet har 971 fakturaer (etter eksklusjon av 29 med ukjent status). Tre algoritmer er testet: Logistisk regresjon, Random Forest og XGBoost. Beste modell er XGBoost (tunet) med AUC-ROC 0.720, F1-score 0.621, Recall 0.833. Benchmark (AUC ≥ 0.75, F1 ≥ 0.70) ble ikke nådd. Fakturaer er klassifisert i tre risikogrupper: Lav (273, 7% forsinket), Middels (279, 28% forsinket), Høy (419, 55% forsinket). Datasett er syntetisk/anonymisert fra en norsk offentlig virksomhet (Forsvaret, ikke navngitt i rapporten).

**Tone og stil:** Akademisk norsk, saklig, presist. Rapporten er på mastergradsnivå. Siter alltid i APA 7. format. Ikke bruk jeg-form – bruk passiv eller «prosjektet». Ikke skriv flowery language. Hold deg til fakta og resultater.

**Figurer:** Det finnes 17 PNG-figurer i mappen `C:\Users\mrmag\Desktop\SKOLE\LOG650\G17-magnus-individuell\004 data\modell_figurer\` og `eda_figurer\`. Figurene er allerede beskrevet med `[FIGUR HER: filnavn]`-plassholdere i rapporten. Ditt ansvar er å erstatte disse med korrekte akademiske figurhenvisninger og legge til figurnummer og figurtekst.

---

### Oppgave 1 – Skriv 10.0 Konklusjon

**Lokasjon:** Seksjon 10.0 i `rapport_mal.md`, erstatt «Skriv her.»

**Krav:**
- Konklusjonen skal **eksplisitt svare på problemstillingen**: *«Hvordan kan KI brukes til å predikere sannsynligheten for at en faktura betales etter forfallsdato, basert på fakturainformasjon som INCOTERMS, betalingsbetingelser og historisk betalingsatferd?»*
- Svar: Ja, KI kan brukes – XGBoost-modellen demonstrerer at maskinlæring kan identifisere mønstre i fakturadata og klassifisere fakturaer etter risiko. Men ytelsen (AUC 0.720) er under litteraturens benchmark (0.75), primært på grunn av lite datasett og syntetisk dataopphav.
- Konklusjonen skal oppsummere **de tre delproblemene** fra 1.2 og hva prosjektet oppnådde for hvert:
  1. Sannsynlighet for sen betaling → XGBoost predikerer med AUC 0.720, recall 0.833
  2. Forventet betalingsforsinkelse → ikke eksplisitt modellert som regresjonsoppgave, men sannsynligheten gir et proxy-mål
  3. Risikoklassifisering → tredelt klassifisering med tydelig separasjon (7% / 28% / 55%)
- Konklusjonen skal nevne **beslutningsstøtteverdien**: risikoklassifiseringen gir et bedre grunnlag for fakturaprioritering enn tradisjonell beløpsbasert sortering
- Konklusjonen skal nevne **veien videre**: modellen er et proof-of-concept og bør testes på ekte, større historiske data; konseptdrift bør håndteres ved periodisk retrening
- Lengde: 3–5 avsnitt, ca. 250–400 ord
- Ikke skriv noe nytt som ikke er forankret i rapporten – les seksjonene 8.0 og 9.0 nøye

---

### Oppgave 2 – Fyll ut 11.0 Bibliografi (APA 7.)

**Lokasjon:** Seksjon 11.0 i `rapport_mal.md`, erstatt HTML-kommentaren

**Krav:** Alle referanser sitert i rapporten skal med. Her er **alle referanser som brukes i teksten**, med tilstrekkelig informasjon til å formatere dem korrekt i APA 7.:

1. **Appel et al. (2020)** – Appel, A. P., Chicarino, V., Cavalcante, E., Carvalho, L. A. V., & Sousa, C. T. (2020). Optimize Cash Collection Using Machine Learning. Publisert i: *2020 IEEE International Conference on Big Data (Big Data)*, s. 2549–2558. DOI: 10.1109/BigData50022.2020.9378170. IBM Research.

2. **Schoonbee et al. (2022)** – Schoonbee, L., Dazarange, R., & van Zyl, T. L. (2022). The Invoice Payment Prediction Problem. *Expert Systems with Applications, 209*, 118270. DOI: 10.1016/j.eswa.2022.118270.

3. **Hastie et al. (2009)** – Hastie, T., Tibshirani, R., & Friedman, J. (2009). *The elements of statistical learning: Data mining, inference, and prediction* (2. utg.). Springer.

4. **James et al. (2021)** – James, G., Witten, D., Hastie, T., & Tibshirani, R. (2021). *An introduction to statistical learning: With applications in R* (2. utg.). Springer.

5. **Breiman (2001)** – Breiman, L. (2001). Random forests. *Machine Learning, 45*(1), 5–32. https://doi.org/10.1023/A:1010933404324

6. **Chen & Guestrin (2016)** – Chen, T., & Guestrin, C. (2016). XGBoost: A scalable tree boosting system. I *Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining* (s. 785–794). ACM. https://doi.org/10.1145/2939672.2939785

7. **Kuhn & Johnson (2019)** – Kuhn, M., & Johnson, K. (2019). *Feature engineering and selection: A practical approach for predictive models*. CRC Press.

8. **Gama et al. (2014)** – Gama, J., Žliobaitė, I., Bifet, A., Pechenizkiy, M., & Bouchachia, A. (2014). A survey on concept drift adaptation. *ACM Computing Surveys, 46*(4), 44:1–44:37. https://doi.org/10.1145/2523813

9. **Turban et al. (2011)** – Turban, E., Sharda, R., & Delen, D. (2011). *Decision support and business intelligence systems* (9. utg.). Pearson.

**Format:** Sorter alfabetisk etter førsteforfatter. Bruk hengene innrykk (hanging indent) – men siden dette er Markdown, skriv hvert verk som et eget avsnitt med blank linje mellom.

---

### Oppgave 3 – Skriv Sammendrag og Abstract

**Lokasjon:** Toppen av `rapport_mal.md`, erstatt plassholdertekstene for «Sammendrag» og «Abstract»

**Sammendrag (norsk, ca. 150–200 ord):**
- Problem: Identifisere fakturaer med høy risiko for sen betaling i en norsk offentlig virksomhet
- Metode: Eksplorativ dataanalyse på 971 anonymiserte fakturaer, feature engineering (34 variabler), trening og evaluering av tre maskinlæringsalgoritmer (logistisk regresjon, Random Forest, XGBoost) med hyperparameterjustering og 5-fold stratifisert kryssvalidering
- Funn: XGBoost oppnår AUC-ROC 0.720 og recall 0.833 – under benchmarkene fra litteraturen (AUC ≥ 0.75), primært på grunn av lite og syntetisk datasett
- Konklusjon: Risikoklassifisering i tre grupper (Lav 7% / Middels 28% / Høy 55% forsinkelsesrate) demonstrerer at maskinlæring gir vesentlig bedre grunnlag for fakturaprioritering enn tradisjonell beløpsbasert sortering

**Abstract (engelsk, ca. 150–200 ord):** Tilsvarende innhold på engelsk.

---

### Oppgave 4 – Fyll ut forsidedata

**Lokasjon:** Øverst i `rapport_mal.md`, de tomme feltene etter fetskrift-etikettene

Fyll inn:
- **Totalt antall sider inkludert forsiden:** La stå tom (student teller selv etter ferdig PDF)
- **Sted, Innleveringsdato:** Molde, 2026-05-31
- **Studiepoeng:** 10
- **Veileder:** La stå tom (student fyller inn veileders navn)

---

### Oppgave 5 – Legg til metodisk erkjennelse i seksjon 8.3

**Lokasjon:** Seksjon 8.3 i `rapport_mal.md`, legg til et avsnitt **etter** den eksisterende tabellen over risikoklassene

**Tekst som skal legges til:**

> Det bemerkes at risikoklassifiseringen i denne seksjonen er basert på en modell trent på alle 971 fakturaer og deretter anvendt på de samme 971 fakturaene. Dette innebærer at de rapporterte forsinkelsesratene er in-sample-estimater: modellen har sett disse dataene under trening og vil naturlig separere dem bedre enn den ville separert nye, usette fakturaer. Forsinkelsesratene (7 % / 28 % / 55 %) reflekterer modellens sorteringsevne på treningsdata og skal tolkes som en illustrasjon av metodikkens potensial, ikke som et ut-av-utvalg ytelsesmål. For operativ bruk bør klassifiseringsevnen valideres på ekte, nye fakturadata.

---

### Oppgave 6 – Legg til begrunnelse for binær klassifisering i seksjon 5.1

**Lokasjon:** Seksjon 5.1 i `rapport_mal.md`, legg til et avsnitt **etter** det første avsnittet (etter omtalen av CRISP-DM)

**Tekst som skal legges til:**

> Prosjektet benytter binær klassifisering (forsinket / ikke forsinket) fremfor den multiklasse-tilnærmingen som Schoonbee et al. (2022) beskriver (fire betalingsintervaller). Valget er begrunnet i datasettets størrelse: med 971 fakturaer og 328 forsinkede tilfeller vil ytterligere oppsplitting i forsinkelsesintervaller gi klasser med for få observasjoner til meningsfull modellering. Binær formulering maksimerer antall treningseksempler per klasse og er konsistent med tilnærmingen i Appel et al. (2020), som er prosjektets primære metodereferanse.

---

### Oppgave 7 – Erkjenn manglende tidsbasert datadeling i seksjon 5.1

**Lokasjon:** Seksjon 5.1, i avsnittet som omtaler «Datadeling» (ca. midt i seksjonen)

**Legg til følgende setning på slutten av datadelingsavsnittet:**

> Merk at datadelingen er tilfeldig stratifisert og ikke tidsbasert. En tidsbasert splitt – der de eldste fakturaene brukes til trening og de nyeste til test – ville i prinsippet gitt en mer realistisk simulering av produksjonsbetingelser. Med et datasett uten garantert tidssekvens og begrenset størrelse er tilfeldig splitt valgt for å sikre tilstrekkelig representasjon av minoritetsklassen i begge sett.

---

### Oppgave 8 – Erstatt figurplaceholders med korrekte figurreferanser

**Lokasjon:** Alle `[FIGUR HER: filnavn ...]`-blokker i `rapport_mal.md`

**Instruksjon:** Erstatt hver plassholder med en korrekt Markdown-figurreferanse. Figurnummereringen skal løpe sekvensielt gjennom hele rapporten (Figur 1, Figur 2, ..., Figur 17). Figurene er **allerede generert** som PNG-filer og finnes i to mapper:

- EDA-figurer (01–09): `004 data/eda_figurer/`
- Modell-figurer (10–17): `004 data/modell_figurer/`

Siden dette er Markdown (ikke Word), kan du ikke «sette inn» bilder direkte, men skriv referansen slik:

```
*Figur X: [beskriv figuren basert på plassholderteksten]. Kilde: egen analyse.*
```

Og legg til `> **Se Figur X** (vedlagt som [filnavn])` der figuren skal vises.

Alternativt, hvis rapporten konverteres til PDF med et verktøy som pandoc, kan du bruke:
```
![Figur X: Figurtekst](../004 data/eda_figurer/filnavn.png)
```

Bruk den siste varianten (pandoc-kompatibel) siden det er mer robust. Eksempel:

For `[FIGUR HER: **01_klasseubalanse.png** – Søylediagram: antall fakturaer betalt i tide (643) vs. forsinket (328)]`:

```markdown
![Figur 1: Klasseubalanse i datasettet – 643 fakturaer betalt i tide mot 328 forsinkede fakturaer (33,8 %).](../004\ data/eda_figurer/01_klasseubalanse.png)
*Figur 1: Klasseubalanse i datasettet. Kilde: egen analyse.*
```

**Figurnummereringsoversikt (skal brukes konsekvent):**

| Figurnummer | Filnavn | Sted i rapport |
|---|---|---|
| Figur 1 | 01_klasseubalanse.png | Seksjon 5.2 |
| Figur 2 | 02_distribusjon_forsinkelse.png | Seksjon 7.1 |
| Figur 3 | 03_andel_per_kategori.png | Seksjon 7.1 |
| Figur 4 | 04_andel_per_betingelse.png | Seksjon 7.1 |
| Figur 5 | 05_andel_per_risiko.png | Seksjon 7.1 |
| Figur 6 | 06_korrelasjonsmatrise.png | Seksjon 7.1 |
| Figur 7 | 07_leverandor_risikoscore.png | Seksjon 7.2 |
| Figur 8 | 08_leverandor_scatter.png | Seksjon 7.2 |
| Figur 9 | 09_leverandor_trend.png | Seksjon 7.2 |
| Figur 10 | 10_roc_kurver.png | Seksjon 8.1 |
| Figur 11 | 11_auc_sammenligning.png | Seksjon 8.1 |
| Figur 12 | 12_konfusjonsmatrise.png | Seksjon 8.2 |
| Figur 13 | 13_feature_importance.png | Seksjon 8.2 |
| Figur 14 | 14_presisjon_recall_f1.png | Seksjon 8.1 |
| Figur 15 | 15_risikokategorier.png | Seksjon 8.3 |
| Figur 16 | 16_sannsynlighet_fordeling.png | Seksjon 8.3 |
| Figur 17 | 17_risiko_vs_belop.png | Seksjon 8.3 |

**Merk:** Figur 1 (01_klasseubalanse.png) forekommer to ganger i rapporten (seksjon 5.2 og seksjon 7.1). Behold begge referansene men bruk samme figurnummer og legg til «(Se også Figur 1)» ved den andre forekomsten.

---

### Oppgave 9 – Legg til avsnitt om etikk og fairness i seksjon 9.3

**Lokasjon:** Seksjon 9.3 i `rapport_mal.md`, legg til som nytt fjerde punkt (etter de tre eksisterende begrensningene)

**Tekst som skal legges til:**

> En fjerde begrensning angår etiske og personvernmessige hensyn. Modellen bruker leverandørkategori og historisk betalingsadferd som prediktorer. Dette innebærer en risiko for at leverandører i visse kategorier – f.eks. renhold eller transport – systematisk klassifiseres som høyrisiko fordi historiske betalingsmønstre i disse kategoriene tilfeldigvis er skjevere enn i andre. Slik algoritmisk skjevhet (bias) kan forsterke eksisterende ulikhet i hvordan leverandørene behandles av virksomheten. I offentlig sektor er transparens og etterprøvbarhet særlig viktig: beslutninger om fakturaprioritering som styres av en black-box-modell som XGBoost krever at virksomheten kan forklare og forsvare prioriteringen overfor leverandørene. Bruk av SHAP-verdier (SHapley Additive exPlanations) for å forklare individuelle prediksjoner anbefales ved eventuell produksjonssetting. GDPR-hensyn ved behandling av leverandørdata bør avklares med virksomhetens personvernombud.

---

### Oppgave 10 – Fiks overskrift 1.2

**Lokasjon:** Seksjon 1.2 i `rapport_mal.md`

Endre overskriften fra:
```
### 1.2 Delproblemer (valgfri)
```
til:
```
### 1.2 Delproblemer
```

---

### Oppgave 11 – Legg til konkrete EDA-tall i seksjon 7.1

**Lokasjon:** Seksjon 7.1 i `rapport_mal.md`, i de beskrivende avsnittene under hver figurreferanse

Legg til følgende faktiske statistikk (hentet fra modellresultatene i rapporten og datasettet):

- Under **«Forsinkelsesdistribusjon»**: «Av 328 forsinkede fakturaer varierer forsinkelsen fra 1 til flere hundre dager. Distribusjonen er høyreskjev, noe som er typisk for fakturadata: majoriteten av forsinkelsene er kortvarige, men det finnes en hale av fakturaer med ekstrem forsinkelse.»
- Under **«Forsinkelse per leverandørkategori»**: «Leverandørkategori er en informativ prediktorvariabel – forsinkelsesraten varierer mellom kategoriene, noe som underbygger at kategorisert leverandørhistorikk bør inkluderes i modellen.»
- Under **«Korrelasjonsmatrise»**: «Gjennomsnittlig antall dager forsinket per leverandør viser høyest lineær korrelasjon med målvariabelen (er_forsinket). Fakturabeløp viser lav korrelasjon med forsinkelse (nær 0), konsistent med Appel et al. (2020) som fant Kendalls τ = 0.003 mellom beløp og forsinkelse.»

---

## Del C – Prioritert rekkefølge for AI-agenten

Utfør oppgavene i følgende rekkefølge for å minimere risiko for konflikter:

1. **Oppgave 10** (fiks overskrift – enkel tekstendring)
2. **Oppgave 4** (forsidedata – enkel utfylling)
3. **Oppgave 6** (binær vs. multiklasse – legg til avsnitt i 5.1)
4. **Oppgave 7** (tidsbasert datadeling – legg til setning i 5.1)
5. **Oppgave 5** (in-sample erkjennelse – legg til avsnitt i 8.3)
6. **Oppgave 9** (etikk og fairness – legg til avsnitt i 9.3)
7. **Oppgave 11** (EDA-tall – legg til statistikk i 7.1)
8. **Oppgave 8** (figurreferanser – erstatt alle 17 plassholdere)
9. **Oppgave 3** (Sammendrag og Abstract – skriv begge)
10. **Oppgave 1** (Konklusjon – skriv seksjon 10.0)
11. **Oppgave 2** (Bibliografi – fyll ut seksjon 11.0)

---

## Del D – Verifikasjonssjekkliste

Etter alle endringer, verifiser at:

- [ ] 10.0 Konklusjon eksisterer og besvarer problemstillingen direkte
- [ ] 11.0 Bibliografi inneholder alle 9 referanser i APA 7. format
- [ ] Sammendrag og Abstract er skrevet (norsk + engelsk)
- [ ] Alle 17 figurer har korrekte referanser (ikke `[FIGUR HER]`)
- [ ] Seksjon 5.1 forklarer valget av binær klassifisering
- [ ] Seksjon 5.1 erkjenner tilfeldig vs. tidsbasert datadeling
- [ ] Seksjon 8.3 erkjenner in-sample-problemet
- [ ] Seksjon 9.3 inneholder etikk/fairness-avsnitt
- [ ] Overskrift 1.2 mangler «(valgfri)»
- [ ] Forsidedata er utfylt (dato: 2026-05-31)
- [ ] Ingen referanser i teksten mangler i bibliografien
- [ ] Figurnummer er sekvensielle og konsistente gjennom hele rapporten
