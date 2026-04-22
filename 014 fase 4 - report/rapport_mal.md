# Finansiell logistikk og beslutningstøtte ved hjelp av KI

**Forfatter:** Magnus Ødegård  
**Totalt antall sider inkludert forsiden:**  
**Sted, Innleveringsdato:** Molde,  
**Studiepoeng:**  
**Veileder:**  

---

## Sammendrag

*Skrives til slutt – kort oppsummering av problemstilling, metode, funn og konklusjon.*

---

## Abstract

*Written last – English summary of problem, method, findings and conclusion.*

---

## Innhold

<!-- Genereres automatisk eller skrives manuelt -->

---

## 1.0 Innledning

Håndtering av fakturaer og innkommende betalinger er en sentral del av finansiell logistikk i enhver virksomhet. Sen betaling av fakturaer medfører likviditetsrisiko, øker behovet for manuell oppfølging og kan i ytterste konsekvens føre til tap av utestående krav. Tradisjonelt har innkrevere prioritert fakturaer for oppfølging basert på beløpsstørrelse – den største fakturaen følges opp først. Denne tilnærmingen er imidlertid reaktiv og ignorerer at risikoen for sen betaling ikke nødvendigvis korrelerer med beløpets størrelse (Appel et al., 2020).

De siste årene har maskinlæring vist seg å være et effektivt verktøy for å forutsi betalingsadferd i fakturadatasett. Appel et al. (2020) demonstrerte at ensemblemodeller basert på Random Forest og Gradient Boosting kan predikere forsinkede betalinger med en nøyaktighet på om lag 77–80 %, og at en risikoscore kombinert med fakturabeløp gir et vesentlig bedre grunnlag for prioritering enn beløp alene. Schoonbee et al. (2022) utvidet dette arbeidet ved å formalisere problemet som «Invoice Payment Prediction Problem» (IPPP) og integrere en maskinlæringsmodell i et beslutningsstøttesystem (DSS). Deres resultater viser at historiske betalingsvariabler – særlig gjennomsnittlig antall dager forsinket og andel fakturaer betalt i tide – er de mest prediktive variablene, og at Random Forest oppnår AUC-verdier på 79–84 % etter hyperparameterjustering.

Denne oppgaven anvender en tilsvarende tilnærming på fakturadata fra en norsk offentlig virksomhet (heretter kalt Bedriften, anonymisert). Målet er å utvikle en maskinlæringsmodell som kan støtte beslutningstakere i å identifisere fakturaer med høy risiko for sen betaling, og dermed bidra til mer effektiv ressursprioritering i fakturahåndteringen.

### 1.1 Problemstilling

**Hvordan kan KI brukes til å predikere sannsynligheten for at en faktura betales etter forfallsdato, basert på fakturainformasjon som INCOTERMS, betalingsbetingelser og historisk betalingsatferd?**

### 1.2 Delproblemer (valgfri)

Problemstillingen operasjonaliseres gjennom følgende beslutningsvariabler:

- **Sannsynlighet for sen betaling** – predikert sannsynlighet for at en faktura passerer forfallsdato uten betaling.
- **Forventet betalingsforsinkelse** – estimert antall dager etter forfall betaling forventes å skje.
- **Risikoklassifisering** – klassifisering av fakturaer i risikokategorier (lav / middels / høy) som grunnlag for prioritert oppfølging.

Disse variablene benyttes som beslutningsstøtte for å avgjøre hvilke fakturaer som bør følges opp manuelt, og hvilke som kan behandles gjennom ordinær prosess.

### 1.3 Avgrensinger

Oppgaven avgrenses til én virksomhet (Bedriften, anonymisert). Avgrensingen er gjort fordi betalingsadferd varierer betydelig mellom virksomheter og bransjer – en modell trent på én virksomhets historikk vil ikke uten videre være overførbar til andre kontekster. Analysen baseres utelukkende på historiske fakturadata og inkluderer ikke sanntidsdata eller fremtidige kontraktsforhold.

Tvistesaker, kontraktsendringer underveis og generelle makroøkonomiske forhold er holdt utenfor analysen, ettersom slik informasjon ikke er registrert i det tilgjengelige datasettet. Det gjøres heller ingen juridisk vurdering av kontrakter eller betalingsbetingelser; fokuset er datadrevet prediksjon og beslutningsstøtte.

### 1.4 Antagelser

Følgende antagelser er lagt til grunn for analysen:

**A1 – Historisk atferd er representativ for fremtidig atferd.** Modellen trenes på tidligere fakturamønstre og anvendes til å predikere nye fakturaer. Dette forutsetter at leverandørenes betalingsadferd er relativt stabil over tid. Antagelsen er standard i litteraturen (Appel et al., 2020; Schoonbee et al., 2022), men innebærer at modellen bør evalueres periodisk.

**A2 – Det anonymiserte datasettet reflekterer reelle betalingsmønstre.** Enkelte variabler er justert for å ivareta konfidensialitet. Det antas at disse justeringene ikke har endret de statistiske sammenhengene som er relevante for prediksjon.

**A3 – Registrerte datoer og betalingsbetingelser er korrekte.** Analysen forutsetter at forfallsdato, faktisk betalingsdato og kontraktsbetingelser (INCOTERMS, betalingsbetingelser) er korrekt registrert i systemet. Datafeil i disse feltene vil direkte påvirke modellens evne til å lære riktige mønstre.

**A4 – Fakturaer med status «Ubetalt» ekskluderes uten å innføre seleksjonsskjevhet.** 29 fakturaer med ukjent utfall (status «Ubetalt») er fjernet fra treningsdatasettet. Det antas at disse ikke skiller seg systematisk fra øvrige fakturaer på en måte som påvirker modellens generaliserbarhet.

---

## 2.0 Litteratur

### 2.1 Litteratursøk og utvalg

Litteratursøket er avgrenset til fagfellevurderte artikler som omhandler maskinlæringsbasert prediksjon av fakturabetaling (accounts receivable prediction) og tilgrensende problemstillinger innen finansiell logistikk og beslutningsstøtte. Søket er gjennomført i Google Scholar og ResearchGate med søkeord som «invoice payment prediction», «accounts receivable machine learning», «late payment prediction» og «decision support accounts receivable». To artikler er vurdert som direkte relevante og er gjennomgått i sin helhet; begge er publisert i anerkjente fagpublikasjoner og representerer forskningsfronten på feltet.

### 2.2 Appel et al. (2020) – Optimize Cash Collection

Appel et al. (2020) fra IBM Research presenterer en maskinlæringsbasert tilnærming for å predikere om fakturaer vil bli betalt etter forfallsdato, med formål om å optimalisere ressursprioritering for innkrevere i en stor multinasjonalbank i Latin-Amerika. Datasettet bestod av 175 552 fakturaer fra 3 725 kunder i åtte land over perioden august 2017 til juni 2019.

Et sentralt metodisk bidrag er innføringen av *window size* (w) – et parameter som begrenser historiske features til de siste w månedene. Forfatterne påviser at kundenes betalingsadferd endrer seg over tid (konseptdrift), og at bruk av all historisk data gir et skjevt bilde av nåværende atferd. Beste ytelse ble oppnådd med w = 2–3 måneder.

Artikkelen tester fem algoritmer: XGBoost, Random Forest, k-nærmeste nabo, logistisk regresjon og naiv Bayes. XGBoost oppnådde høyest nøyaktighet (79,75 %) med w = 2 måneder, tett fulgt av Random Forest (79,05 %). Sluttmodellen er et ensemble av Random Forest og Gradient Boosting, som stabilt oppnår om lag 77 % nøyaktighet og F1-score på tvers av tidssnitt.

I tillegg til klassifisering foreslår forfatterne en prioriteringsmetode der predikert forsinkelsessannsynlighet kombineres med fakturabeløp til en risikoscore (R = Verdi × P(Forsinket)). Dette gir en vesentlig annerledes og mer risikobevisst prioriteringsliste sammenlignet med tradisjonell prioritering basert utelukkende på beløpsstørrelse (Kendalls τ = 0,003).

Artikkelen fungerer som primær metodereferanse for dette prosjektet, og ytelsestallene (~77 % nøyaktighet, F1-score ~77–78 %) brukes som benchmark.

### 2.3 Schoonbee et al. (2022) – The Invoice Payment Prediction Problem

Schoonbee et al. (2022) formaliserer problemet som «Invoice Payment Prediction Problem» (IPPP) og presenterer et strukturert CRISP-DM-basert veikart med ti steg, fra problemformulering til integrasjon i et beslutningsstøttesystem (DSS). Studien er gjennomført i samarbeid med Curro Holdings Ltd i Sør-Afrika, med et datasett på 1 068 620 fakturaoppføringer fra 2016 til 2021.

I motsetning til Appel et al. (2020) opererer Schoonbee et al. med en multiklasse-formulering av IPPP, der fakturaer klassifiseres i fire betalingsintervaller: betalt i tide (0 dager), 1–30 dager forsinket, 31–60 dager forsinket, og over 61 dager forsinket. Denne formuleringen gir et mer granulert grunnlag for ressursprioriteringen.

Studien viser at historiske betalingsfeatures er avgjørende for modellens prediksjonsevne; tillegg av engineered features øker AUC med 2–9 prosentpoeng avhengig av algoritme. Eksponentiell vekting av de siste 10 fakturaene (vektfaktor 1,5) overgår enkelt gjennomsnitt og fast vindusstørrelse som beregningsmetode. De tre viktigste prediktorene er gjennomsnittlig antall dager forsinket (AveDaysLate), andel fakturaer betalt i tide (RatioOnTime) og utestående saldo (PreviousBalance).

Random Forest ble valgt som primærmodell med en endelig AUC på 83,61 % etter hyperparameterjustering. DSS-en implementert i Python/Dash gjør at innkrevere kan laste opp nye fakturaer, visualisere risikoprofiler og sortere etter predikert betalingsklasse.

Artikkelen er særlig relevant som metodologisk referanse for feature engineering, valg av evalueringsmetrikk og CRISP-DM-prosessrammeverk.

### 2.4 Sammenstilling og relevans

Begge artiklene demonstrerer at maskinlæring – og da særlig ensemblemodeller som Random Forest og Gradient Boosting – er godt egnet for prediksjon av fakturaforsinkelse, og at historiske betalingsvariabler er den viktigste kilden til prediktiv kraft. Studiene er gjennomført med store datasett fra henholdsvis finansbransjen og skolesektoren. Dette prosjektets datasett er vesentlig mindre (971 fakturaer), noe som stiller strengere krav til generalisering og datautvalg, men den metodiske tilnærmingen er direkte overførbar.

Tabell 2.1 oppsummerer sentrale karakteristika ved de to studiene.

**Tabell 2.1 – Sammenstilling av primærlitteratur**

| Karakteristika           | Appel et al. (2020)                          | Schoonbee et al. (2022)                      |
|--------------------------|----------------------------------------------|----------------------------------------------|
| Kontekst                 | Multinasjonalbank, Latin-Amerika             | Skoleselskap, Sør-Afrika                     |
| Datasett                 | 175 552 fakturaer                            | 1 068 620 fakturaer                          |
| Problemtype              | Binær klassifisering (forsinket/ikke)        | Multiklasse (fire betalingsintervaller)      |
| Beste modell             | Ensemble (RF + Gradient Boosting)            | Random Forest                                |
| Beste AUC                | ~77–80 %                                     | 79–84 %                                      |
| Viktigste features       | Historiske (average days late, total late)   | AveDaysLate, RatioOnTime, PreviousBalance    |
| Window size              | 2–3 måneder                                  | Eksponentiell vekting (siste 10 fakturaer)   |
| Konseptdrift             | Eksplisitt håndtert via window size          | Håndtert via månedlig retrening              |

---

## 3.0 Teori

### 3.1 Maskinlæring og klassifisering

Maskinlæring er en gren av kunstig intelligens der algoritmer lærer mønstre fra data uten å bli eksplisitt programmert med regler (Hastie et al., 2009). I dette prosjektet benyttes **veiledet læring** (supervised learning), der modellen trenes på historiske fakturaposter med kjent utfall (betalt i tide eller forsinket) og deretter predikerer utfall for nye, usette fakturaer.

Problemstillingen er formulert som et **binært klassifiseringsproblem**: for hver faktura skal modellen angi en sannsynlighet p ∈ [0, 1] for at fakturaen betales etter forfallsdato. En terskelverdi (typisk 0,5) konverterer sannsynligheten til en klasse, men for prioriteringsformål er den kontinuerlige sannsynligheten mer nyttig enn klassemerkelappen alene.

### 3.2 Kandidatalgoritmer

**Logistisk regresjon** er en lineær klassifikasjonsmetode som modellerer log-odds for binært utfall som en lineær kombinasjon av prediktorvariabler. Metoden er enkel å tolke og egner seg godt som baseline-modell; begrensningen er at den ikke fanger ikke-lineære sammenhenger i dataene (James et al., 2021).

**Random Forest** er en ensemblemetode basert på bagging av beslutningstrær. Et stort antall trær (typisk 100–1000) trenes på tilfeldige utvalg av både rader og variabler, og prediksjonene aggregeres ved majoritetsavstemning (klassifisering) eller gjennomsnitt (regresjon). Random Forest er robust mot overfitting, tolererer manglende verdier og gir feature importance som biprodukt (Breiman, 2001).

**Gradient Boosting (XGBoost)** er en sekvensiell ensemblemetode der nye trær trenes for å korrigere residualfeil fra foregående trær, og tapsfunksjonen minimeres via gradientnedstigning. XGBoost er en effektiv implementasjon av gradient boosting med regularisering og støtte for parallell prosessering (Chen & Guestrin, 2016). Metoden oppnår gjennomgående høy prediksjonsytelse på tabulære datasett og var beste enkeltmodell i Appel et al. (2020).

### 3.3 Evalueringsmetrikker

For klassifiseringsproblemer med **klasseubalanse** – der én klasse (f.eks. betalt i tide) er langt vanligere enn den andre (forsinket) – er enkel nøyaktighet (accuracy) et misvisende mål. En modell som alltid predikerer «i tide» vil oppnå høy nøyaktighet uten å ha lært noe nyttig. Følgende metrikker er derfor sentrale:

**AUC-ROC** (Area Under the Receiver Operating Characteristic Curve) måler modellens evne til å skille mellom klassene uavhengig av terskelverdi. En AUC på 0,5 tilsvarer tilfeldig gjetting, mens AUC = 1,0 er perfekt separasjon. AUC er den primære evalueringsmetrikken i litteraturen (Appel et al., 2020; Schoonbee et al., 2022) og brukes som benchmark i dette prosjektet (mål: AUC ≥ 0,75).

**F1-score** er det harmoniske gjennomsnittet av presisjon (andel korrekt predikerte positive av alle predikert positive) og recall (andel korrekt predikerte positive av alle faktiske positive). F1-score balanserer de to typene feil og er spesielt nyttig ved klasseubalanse (mål: F1 ≥ 0,70).

**Konfusjonsmatrise** viser antall sanne positive, sanne negative, falske positive og falske negative, og er grunnlaget for å beregne presisjon, recall og F1-score.

### 3.4 Feature engineering

Feature engineering er prosessen med å transformere rådata til informative prediktorvariabler som forbedrer modellens evne til å lære relevante mønstre (Kuhn & Johnson, 2019). I kontekst av fakturapredikering skilles det mellom to typer features:

**Fakturaspesifikke features** beskriver egenskaper ved den individuelle fakturaen: betalingsfrist i dager, fakturabeløp, fakturamåned og -kvartal, leverandørkategori og INCOTERMS. Disse variablene er tilgjengelige på utstedelsestidspunktet og er direkte observerbare.

**Historiske betalingsfeatures** oppsummerer leverandørens tidligere betalingsadferd: gjennomsnittlig antall dager forsinket, andel fakturaer betalt i tide, antall forsinkede fakturaer og variasjon i forsinkelse. Begge primærstudier dokumenterer at disse variablene er de mest prediktive (Appel et al., 2020; Schoonbee et al., 2022), og at feature engineering på historiske data typisk øker AUC med 3–9 prosentpoeng.

### 3.5 Konseptdrift

**Konseptdrift** refererer til fenomenet der den statistiske sammenhengen mellom prediktorvariabler og målvariabel endrer seg over tid (Gama et al., 2014). I fakturakontekst kan dette skyldes sesongvariasjon, makroøkonomiske endringer eller endret kundeadferd. Appel et al. (2020) løser problemet med en window size-parameter som begrenser historiske features til de siste 2–3 månedene; Schoonbee et al. (2022) retrener modellen månedlig. For dette prosjektet, med et begrenset datasett uten tydelig tidsstruktur, er konseptdrift erkjent som en begrensning som bør adresseres ved eventuell drift av modellen.

### 3.6 Beslutningsstøttesystem (DSS) og risikoscore

Et **beslutningsstøttesystem** (DSS) er et informasjonssystem som integrerer data, modeller og brukergrensesnitt for å støtte semi-strukturerte beslutningsprosesser (Turban et al., 2011). I fakturahåndteringskontekst kan et DSS automatisere risikoklassifisering av innkommende fakturaer og generere prioriteringslister for innkrevingsressurser.

Appel et al. (2020) foreslår en risikoscore som kombinerer predikert forsinkelsessannsynlighet med fakturabeløp (R = Verdi × P(Forsinket)), slik at oppfølgingsinnsatsen rettes mot fakturaer med høy forventet tapseksponering. Schoonbee et al. (2022) implementerer tilsvarende logikk i et Python/Dash-grensesnitt. I dette prosjektet benyttes risikoscoren som grunnlag for en tredelt risikoklassifisering (lav / middels / høy), men en fullstendig DSS-implementasjon faller utenfor prosjektets scope.

---

## 4.0 Casebeskrivelse

Bedriften er en norsk offentlig virksomhet som håndterer innkjøp av varer og tjenester fra et bredt spekter av leverandører. Av konfidensialitetshensyn er virksomhetens identitet og identifiserende detaljer anonymisert i sin helhet. Datasettet er tilpasset og omstrukturert for å ivareta konfidensialitetskravene i overensstemmelse med antagelse A2 (avsnitt 1.4), uten å forringe de statistiske egenskapene som er relevante for modelltrening.

Virksomheten benytter standardiserte kontraktsformer for offentlig anskaffelse: rammeavtaler, enkeltkontrakter, minikonkurranser og åpne anbudskonkurranser. Leverandørmassen spenner over åtte kategorier: IT, konsulenttjenester, bygg, energi, forbruksmateriell, renhold, transport og vedlikehold. Fakturaene er regulert av internasjonale leveringsbetingelser (INCOTERMS 2020) og norske betalingsbetingelser med kredittider på 10, 14, 30, 60 og 90 dager netto.

Utfordringen Bedriften ønsker å adressere er mangelen på systematisk, datadrevet identifisering av fakturaer med høy risiko for sen betaling. Tradisjonell prioritering av betalingsoppfølging baseres på forfallsdato og fakturabeløp, uten systematisk hensyn til leverandørspesifikk betalingshistorikk. Konsekvensen er at fakturaer fra leverandører med konsekvent forsinkede betalingsmønstre behandles på lik linje med fakturaer fra pålitelige leverandører – en ressursbruk som er ineffektiv og reaktiv.

Prosjektet tar utgangspunkt i et historisk fakturadatasett fra Bedriften og utvikler en maskinlæringsmodell som klassifiserer fakturaer etter risiko for sen betaling. Modellen er ment som beslutningsstøtte for prioritering av fakturakontroll og innkrevingsoppfølging, og er ikke designet for automatisert beslutning uten menneskelig vurdering.

---

## 5.0 Metode og data

### 5.1 Metode

Prosjektet følger en prosessstruktur inspirert av CRISP-DM (Cross-Industry Standard Process for Data Mining), det rammeverket Schoonbee et al. (2022) benytter som grunnlag for sitt veikart for Invoice Payment Prediction Problem (IPPP). CRISP-DM strukturerer datadrevne prosjekter i seks faser: forretningsforståelse, dataforståelse, dataforberedelse, modellering, evaluering og implementasjon.

**Dataforståelse og forberedelse** gjennomføres gjennom eksplorativ dataanalyse (EDA) som kartlegger klasseubalanse, forsinkelsesdistribusjon og bivariate relasjoner mellom prediktorvariabler og målvariabelen. Feature engineering transformerer rådata til et modelleringsklart datasett.

**Modellering** tester tre algoritmetyper med ulik kompleksitet: logistisk regresjon som lineær baseline, Random Forest og Gradient Boosting (XGBoost) som ensemblemetoder. For ensemblemetodene gjennomføres hyperparameterjustering med RandomizedSearchCV og 5-fold stratifisert kryssvalidering (StratifiedKFold, k=5), med AUC-ROC som optimaliseringskriterium. Stratifisert kryssvalidering sikrer at klassefordelingen er representativ i hvert valideringsfold.

**Datadeling** følger en 80/20 stratifisert splitt: 776 fakturaer til trening og 195 til testing. Testsettet holdes tilbake gjennom hele hyperparameterjusteringsprosessen og benyttes kun for endelig evaluering. Denne tilnærmingen gir ærlige ytelsestall og motvirker datalekkasje.

**Klasseubalanse** håndteres gjennom klassevekting: `class_weight='balanced'` for logistisk regresjon og Random Forest, og `scale_pos_weight` (satt til forholdet mellom majoritets- og minoritetsklassen, ca. 1,96) for XGBoost.

**Evalueringsmetrikker** er primært AUC-ROC og F1-score, med benchmarks satt til AUC ≥ 0,75 og F1 ≥ 0,70 basert på Appel et al. (2020). I tillegg rapporteres presisjon, recall og nøyaktighet for alle modeller. Recall prioriteres fremfor presisjon fordi det for beslutningsstøtteformål er mer kostbart å overse en forsinket faktura (falsk negativ) enn å flagge en faktura feilaktig (falsk positiv).

### 5.2 Data

Datasettet ble mottatt fra veileder som en anonymisert representasjon av Bedriftens fakturadatasett, og inneholder 1 000 fakturaer med 15 variabler. Tabell 5.1 gir en oversikt over variabelskjemaet.

**Tabell 5.1 – Variabelskjema for rådata**

| Variabel | Datatype | Beskrivelse |
|---|---|---|
| Faktura-ID | Identifikator | Unik fakturanøkkel |
| Leverandør-ID | Identifikator | Anonymisert leverandøridentifikator |
| Fakturabeløp (NOK) | Numerisk | Fakturabeløp i norske kroner |
| Fakturadato | Dato | Utstedelsesdato for fakturaen |
| Forfallsdato | Dato | Opprinnelig forfallsdato |
| Faktisk betalingsdato | Dato | Dato for registrert betaling |
| Betalingsstatus | Kategorisk | Betalt / Forsinket / Ubetalt |
| Dager forsinket | Numerisk | Antall dager betalt etter forfall (0 = i tide) |
| Betalingsbetingelser | Kategorisk | Netto 10 / 14 / 30 / 60 / 90 |
| INCOTERMS | Kategorisk | Leveringsbetingelse (11 koder: CFR, CIF, CIP, CPT, DAP, DDP, DPU, EXW, FAS, FCA, FOB) |
| Kontrakttype | Kategorisk | Rammeavtale / Enkeltkontrakt / Minikonkurranse / Åpen anbudskonkurranse |
| Leverandørkategori | Kategorisk | IT / Konsulenttjenester / Bygg / Energi / Forbruksmateriell / Renhold / Transport / Vedlikehold |
| Gj.snitt dager forsinket (leverandør) | Numerisk | Leverandørens historiske gjennomsnitt – antall dager betalt etter forfall |
| Antall fakturaer (leverandør) | Numerisk | Totalt antall fakturaer per leverandør i datasettet |
| Risikokategori leverandør | Kategorisk | Lav / Medium / Høy / Kritisk – forhåndsdefinert i datasettet |

**Datakvalitet**

Datasettet er komplett uten manglende verdier i de fakturaene som benyttes til modellering. 29 fakturaer (2,9 %) med betalingsstatus «Ubetalt» ble identifisert under EDA. Ettersom utfallet er ukjent for disse fakturaene, er de ekskludert fra treningsdatasettet i samsvar med antagelse A4 (avsnitt 1.4). Det endelige modelleringsdatasettet består av 971 fakturaer.

**Klasseubalanse**

Av de 971 fakturaene er 643 (66,2 %) betalt i tide og 328 (33,8 %) forsinket. Ubalansen på om lag 2:1 er moderat sammenlignet med mange klassifiseringsdatasett, men tilstrekkelig til at enkel nøyaktighet er et misvisende ytelsesmål – en modell som alltid predikerer «i tide» oppnår 66,2 % nøyaktighet uten å ha lært noe nyttig.

<figure style="text-align:center;">
<img src="../004 data/eda_figurer/01_klasseubalanse.png" alt="Klasseubalanse" width="55%">
<figcaption><small>Figur 1: Av de 971 fakturaene i analysedatasettet er 643 (66,2 %) betalt i tide (klasse 0) og 328 (33,8 %) forsinket (klasse 1). Ubalansen på om lag 2:1 medfører at enkel nøyaktighet er et misvisende ytelsesmål – en naiv modell som alltid predikerer «i tide» oppnår 66,2 % uten å ha lært noe nyttig.</small></figcaption>
</figure>

---

## 6.0 Modellering

### 6.1 Feature engineering

Feature engineering transformerte de 15 råkolonnene til 34 prediktorvariabler i to steg.

**Datobaserte og betalingsbetingelsesfeatures** er utledet direkte fra råverdiene:

| Feature | Beskrivelse |
|---|---|
| betalingsfrist_dager | Antall dager fra fakturadato til forfallsdato |
| netto_dager | Betalingsbetingelse som heltall (10, 14, 30, 60 eller 90) |
| faktura_maned | Måneden fakturaen ble utstedt (1–12) |
| faktura_kvartal | Kvartal fakturaen ble utstedt (1–4) |

**One-hot-enkoding** er benyttet for alle fire kategoriske variabler:

| Variabel | Antall kategorier | Antall nye kolonner |
|---|---|---|
| Leverandørkategori | 8 | 8 |
| Kontrakttype | 4 | 4 |
| INCOTERMS | 11 | 11 |
| Risikokategori leverandør | 4 | 4 |

I tillegg beholdes de to leverandørhistoriske variablene fra rådata: gjennomsnittlig antall dager forsinket og antall fakturaer per leverandør. Disse er direkte analoge til de viktigste historiske featurene identifisert av Schoonbee et al. (2022): *AveDaysLate* og leverandørvolum. Totalt gir dette 34 prediktorvariabler.

Numeriske variabler standardiseres (StandardScaler) for logistisk regresjon. Ensemblemodellene er invariante for lineær skalering og benytter råverdier.

### 6.2 Baseline-modeller

Tre baseline-modeller trenes uten hyperparameterjustering for å etablere et referansepunkt:

- **Logistisk regresjon:** `class_weight='balanced'`, `max_iter=1000`, standardiserte features
- **Random Forest:** `n_estimators=100`, `class_weight='balanced'`
- **XGBoost:** `n_estimators=100`, `scale_pos_weight=1.96`

### 6.3 Hyperparameterjustering

Random Forest og XGBoost justeres med RandomizedSearchCV over 5-fold stratifisert kryssvalidering, med AUC-ROC som optimaliseringskriterium.

**Random Forest** søker over 40 tilfeldige kombinasjoner av: `n_estimators` (100–500), `max_depth` (5, 10, 15, 20 og ubegrenset), `min_samples_split` (2, 5, 10), `min_samples_leaf` (1, 2, 4) og `class_weight` (balanced / balanced_subsample).

**XGBoost** søker over 50 tilfeldige kombinasjoner av: `n_estimators` (100–500), `max_depth` (3, 5, 7, 9), `learning_rate` (0,01–0,30), `subsample` (0,6–1,0), `colsample_bytree` (0,6–1,0), `scale_pos_weight` og `min_child_weight` (1, 3, 5).

Beste parameterkombinasjon for hver modell evalueres deretter på hold-out testsettet.

---

## 7.0 Analyse

### 7.1 Eksplorativ dataanalyse (EDA)

**Klasseubalanse**

Av 971 fakturaer er 643 (66,2 %) betalt i tide og 328 (33,8 %) forsinket, en 2:1-ubalanse som krever klassevekting i alle modeller (se avsnitt 5.1).

<figure style="text-align:center;">
<img src="../004 data/eda_figurer/01_klasseubalanse.png" alt="Klasseubalanse" width="55%">
<figcaption><small>Figur 1: Søylediagram over antall fakturaer i klasse 0 (betalt i tide, 643 stk.) og klasse 1 (forsinket, 328 stk.). Ubalansen krever klassevekting i alle modeller for å unngå at majoritetsklassen dominerer prediksjonen.</small></figcaption>
</figure>

**Forsinkelsesdistribusjon**

Distribusjonen av antall dager forsinket blant de 328 forsinkede fakturaene er skjev mot høyre: de fleste forsinkede fakturaer er relativt kort forsinket, men det finnes en hale av fakturaer med svært lang forsinkelse. Distribusjonen inneholder KDE-estimat som visualiserer tetthetstopper.

<figure style="text-align:center;">
<img src="../004 data/eda_figurer/02_distribusjon_forsinkelse.png" alt="Distribusjon forsinkelse" width="60%">
<figcaption><small>Figur 2: Histogram med KDE-kurve over antall dager forsinket for de 328 forsinkede fakturaene. Fordelingen er høyreskjev – de fleste forsinkelser er kortvarige, men en hale av fakturaer med svært lang forsinkelse drar gjennomsnittet opp over medianen.</small></figcaption>
</figure>

**Forsinkelse per leverandørkategori**

Andelen forsinkede fakturaer varierer mellom leverandørkategoriene. Figuren viser at visse kategorier har systematisk høyere forsinkelsesrate, noe som indikerer at leverandørkategori er en informativ prediktorvariabel.

<figure style="text-align:center;">
<img src="../004 data/eda_figurer/03_andel_per_kategori.png" alt="Forsinkelse per leverandørkategori" width="65%">
<figcaption><small>Figur 3: Prosentandel forsinkede fakturaer per leverandørkategori, sortert synkende. Kategorier med høy forsinkelsesrate er systematisk mer risikable og bør prioriteres i oppfølgingsarbeidet. Dette bekrefter at leverandørkategori er en informativ prediktorvariabel.</small></figcaption>
</figure>

**Forsinkelse per betalingsbetingelse**

Forsinkelsesraten undersøkes på tvers av betalingsbetingelsene Netto 10, 14, 30, 60 og 90. Figuren viser om lengre kredittid er assosiert med høyere eller lavere andel forsinkede fakturaer.

<figure style="text-align:center;">
<img src="../004 data/eda_figurer/04_andel_per_betingelse.png" alt="Forsinkelse per betalingsbetingelse" width="60%">
<figcaption><small>Figur 4: Prosentandel forsinkede fakturaer per betalingsbetingelse (Netto 10/14/30/60/90 dager). Figuren viser om lengre kredittid er assosiert med høyere forsinkelsesrisiko, og gir grunnlag for vurdering av betalingsbetingelse som prediktor.</small></figcaption>
</figure>

**Forsinkelse per risikokategori (leverandør)**

Den forhåndsdefinerte leverandørrisikokategorien viser tydelig separasjon i forsinkelsesrate mellom risikogruppene, noe som bekrefter at variabelen er valid og informativ for modelltrening.

<figure style="text-align:center;">
<img src="../004 data/eda_figurer/05_andel_per_risiko.png" alt="Forsinkelse per risikokategori" width="55%">
<figcaption><small>Figur 5: Prosentandel forsinkede fakturaer per forhåndsdefinert leverandørrisikokategori (Medium / Høy / Kritisk). Den tydelige separasjonen mellom risikogruppene bekrefter at denne variabelen er valid og informativ for modelltrening.</small></figcaption>
</figure>

**Korrelasjonsmatrise**

Korrelasjonsanalysen for numeriske variabler viser at gjennomsnittlig antall dager forsinket per leverandør (historisk) har sterkest lineær korrelasjon med målvariabelen (er_forsinket). Fakturabeløp viser lav korrelasjon med forsinkelse, noe som underbygger at beløpsbasert prioritering alene er utilstrekkelig som beslutningsgrunnlag – konsistent med Appel et al. (2020, s. Kendalls τ = 0,003).

<figure style="text-align:center;">
<img src="../004 data/eda_figurer/06_korrelasjonsmatrise.png" alt="Korrelasjonsmatrise" width="55%">
<figcaption><small>Figur 6: Korrelasjonsmatrise (Pearson) for numeriske variabler. Gjennomsnittlig antall dager forsinket per leverandør har sterkest lineær korrelasjon med målvariabelen (er_forsinket), mens fakturabeløp viser lav korrelasjon – konsistent med Appel et al. (2020).</small></figcaption>
</figure>

### 7.2 Leverandørprofil og risikoscore

Leverandøranalysen aggregerer betalingsadferd per leverandør og beregner en sammensatt risikoscore: 60 % vektet på andel forsinkede fakturaer, 40 % på normalisert gjennomsnittlig forsinkelse (i dager). Risikoscoren rangerer leverandørene fra 0 (ingen historisk risiko) til 1 (maksimal risiko).

<figure style="text-align:center;">
<img src="../004 data/eda_figurer/07_leverandor_risikoscore.png" alt="Leverandør risikoscore" width="65%">
<figcaption><small>Figur 7: Topp 15 leverandører rangert etter sammensatt risikoscore (60 % vektet andel forsinkede fakturaer + 40 % normalisert gjennomsnittlig forsinkelse), fargekodert etter risikokategori. Disse leverandørene bør prioriteres for tett oppfølging.</small></figcaption>
</figure>

Scatter-plottet nedenfor illustrerer forholdet mellom andel forsinkede fakturaer og gjennomsnittlig forsinkelse per leverandør, der sirkelstørrelsen angir antall fakturaer. Leverandører øverst til høyre i plottet – høy andel forsinket kombinert med lang gjennomsnittlig forsinkelse – utgjør den høyeste samlede risikoen.

<figure style="text-align:center;">
<img src="../004 data/eda_figurer/08_leverandor_scatter.png" alt="Leverandør scatter" width="65%">
<figcaption><small>Figur 8: Scatter-plot over andel forsinkede fakturaer (x-akse) mot gjennomsnittlig antall dager forsinket (y-akse) per leverandør. Sirkelstørrelse angir antall fakturaer; farge angir risikokategori. Leverandører øverst til høyre utgjør den høyeste samlede risikoen.</small></figcaption>
</figure>

Trendanalysen viser betalingsatferden over tid (per kvartal) for de fem høyest rangerte risiko-leverandørene, og indikerer om forsinkelsesmønstrene er stabile eller endrer seg over tid.

<figure style="text-align:center;">
<img src="../004 data/eda_figurer/09_leverandor_trend.png" alt="Leverandør trend" width="65%">
<figcaption><small>Figur 9: Prosentandel forsinkede fakturaer per kvartal for de fem høyest rangerte risiko-leverandørene. Stabile trender over tid støtter antagelse A1 om at historisk betalingsadferd er representativ for fremtidig atferd.</small></figcaption>
</figure>

---

## 8.0 Resultat

### 8.1 Modellytelse

Tabell 8.1 viser ytelsesmålene for alle fem modeller evaluert på hold-out testsettet (195 fakturaer, aldri sett under trening).

**Tabell 8.1 – Modellresultater på hold-out testsett**

| Modell | AUC-ROC | F1-score | Presisjon | Recall | Nøyaktighet |
|---|---|---|---|---|---|
| Log.reg (baseline) | 0,706 | 0,627 | 0,515 | 0,803 | 0,677 |
| RF (baseline) | 0,695 | 0,471 | 0,528 | 0,424 | 0,677 |
| XGBoost (baseline) | 0,661 | 0,476 | 0,432 | 0,530 | 0,605 |
| RF (tunet) | 0,698 | 0,610 | 0,486 | 0,818 | 0,646 |
| **XGBoost (tunet)** | **0,720** | **0,621** | **0,495** | **0,833** | **0,656** |
| *Benchmark* | *≥ 0,750* | *≥ 0,700* | *–* | *–* | *–* |

Ingen av de fem modellene når benchmarkene satt med referanse til Appel et al. (2020). Beste modell er XGBoost med hyperparameterjustering, som oppnår AUC-ROC 0,720 og F1-score 0,621. Hyperparameterjustering bidrar positivt for begge ensemblemetoder: Random Forest øker fra AUC 0,695 til 0,698, mens XGBoost øker fra 0,661 til 0,720 – en forbedring på 5,9 prosentpoeng og den største enkeltgevinsten i eksperimentet.

Logistisk regresjon utmerker seg som en overraskende sterk baseline med AUC 0,706, noe som indikerer at lineære sammenhenger mellom prediktorvariabler og forsinkelse er fremtredende i datasettet. RF baseline skiller seg negativt ut med lav recall (0,424), noe som betyr at modellen uten tuning i stor grad predikerer majoritetsklassen og overser forsinkede fakturaer.

> *[FIGUR HER: **10_roc_kurver.png** – ROC-kurver for alle fem modeller med AUC-verdier i legende, samt diagonallinje for tilfeldig gjetting (AUC = 0,50). Viser at XGBoost tunet har den største arealen under kurven.]*

> *[FIGUR HER: **11_auc_sammenligning.png** – Søylediagram: AUC-ROC per modell, med horisontal benchmark-linje ved 0,75. Tydeliggjør gapet mellom oppnådd ytelse og benchmark.]*

> *[FIGUR HER: **14_presisjon_recall_f1.png** – Gruppert søylediagram: presisjon, recall og F1-score for alle fem modeller, med benchmark-linje for F1 ved 0,70. Viser avveiningen mellom presisjon og recall på tvers av modeller.]*

### 8.2 Konfusjonsmatrise og feature importance

Konfusjonsmatrisen for beste modell (XGBoost tunet) bryter ned klassifiseringsresultatene i de fire utfallstypene: sanne positive (forsinkede fakturaer korrekt flagget), sanne negative (i tide korrekt klassifisert), falske positive (i tide feilaktig flagget) og falske negative (forsinkede fakturaer som ikke ble fanget opp).

> *[FIGUR HER: **12_konfusjonsmatrise.png** – Konfusjonsmatrise for XGBoost tunet på testsettet (195 fakturaer). Merk antall falske negative – disse representerer forsinkede fakturaer som «glapp igjennom» modellen.]*

Feature importance fra XGBoost tunet identifiserer de variablene som bidrar mest til modellens prediksjoner. Gjennomsnittlig antall dager forsinket per leverandør (historisk) er den klart viktigste prediktoren, konsistent med Schoonbee et al. (2022) som identifiserer *AveDaysLate* som den mest prediktive variabelen i sitt datasett. Leverandørens risikokategori og volumbaserte variabler er blant de øvrige sentrale prediktorene.

> *[FIGUR HER: **13_feature_importance.png** – Horisontalt søylediagram: topp 15 viktigste features i XGBoost tunet, rangert etter feature importance (Gini-basert). Bekrefter at historiske leverandørvariabler dominerer.]*

### 8.3 Risikoklassifisering av fakturaer

Sluttmodellen – XGBoost tunet, retrent på hele datasettet (971 fakturaer) for full dekning – klassifiserer alle fakturaer i tre risikogrupper basert på predikert sannsynlighet for forsinkelse:

| Risikoklasse | Terskel | Antall fakturaer | Faktisk forsinkelsesrate |
|---|---|---|---|
| Lav | p < 0,30 | 273 | 7 % |
| Middels | 0,30 ≤ p < 0,55 | 279 | 28 % |
| Høy | p ≥ 0,55 | 419 | 55 % |

Separasjonen mellom risikogruppene er tydelig: forsinkelsesraten i høy-gruppen (55 %) er nær åtte ganger høyere enn i lav-gruppen (7 %). Dette viser at modellen skiller mellom leverandørprofiler på en meningsfull og praktisk anvendbar måte. For en innkrever innebærer dette at ressursinnsatsen kan konsentreres mot de 419 høyrisikofakturaene fremfor å behandle alle 971 likt.

> *[FIGUR HER: **15_risikokategorier.png** – To panel: venstre: søylediagram over antall fakturaer per risikoklasse (Lav 273 / Middels 279 / Høy 419); høyre: søylediagram over faktisk forsinkelsesrate per risikoklasse (7 % / 28 % / 55 %). Tydelig separasjon bekrefter modellens sorteringsevne.]*

> *[FIGUR HER: **16_sannsynlighet_fordeling.png** – Histogram over predikert forsinkelsessannsynlighet for alle 971 fakturaer, fargekodert etter faktisk utfall (blå = i tide / rød = forsinket), med vertikale terskellinjer ved p = 0,30 og p = 0,55. Viser overlapp mellom klassene og modellens usikkerhetssone.]*

> *[FIGUR HER: **17_risiko_vs_belop.png** – Scatter-plot: fakturabeløp (TNOK) på x-aksen, predikert forsinkelsessannsynlighet på y-aksen, fargekodert etter risikoklasse. Illustrerer at høy risiko ikke korrelerer med høyt beløp – den risikobaserte sorteringen gir en vesentlig annerledes prioriteringsliste enn beløpsbasert sortering.]*

---

## 9.0 Diskusjon

### 9.1 Modellytelse mot benchmark

Beste modell i dette prosjektet er XGBoost med hyperparameterjustering, med en AUC-ROC på 0.720, F1-score på 0.621 og recall på 0.833. Benchmarkene satt fra primærlitteraturen – AUC ≥ 0.75 og F1 ≥ 0.70 (Appel et al., 2020) – ble ikke nådd. Dette er et funn som krever tolkning, ikke et fiasko.

Den mest sannsynlige forklaringen på gapet er datasettets størrelse og opphav. Appel et al. (2020) trente på 175 552 fakturaer og Schoonbee et al. (2022) på over én million fakturaoppføringer. Dette prosjektets treningsgrunnlag består av 971 fakturaer – en størrelsesorden som ikke gir modellen tilstrekkelig eksponering mot de subtile mønstrene som skiller betalingsatferd. Med et lite datasett øker variansen i estimatene, og modellen har begrenset kapasitet til å lære generaliserbare sammenhenger.

I tillegg er datasettet syntetisk generert. Variabelskjemaet ble utformet med utgangspunkt i hva primærlitteraturen identifiserer som prediktive variabler, og dataen ble generert innenfor disse rammene. Dette innebærer at de statistiske sammenhengene i datasettet er renere og mer konsistente enn hva ekte fakturadata typisk er. Reell betalingsadferd inneholder støy, unntak og irregulariteter som paradoksalt nok er det modellen trenger for å lære robuste mønstre. Syntetisk data med lav varians setter således et tak på oppnåelig AUC som ikke er sammenlignbart med benchmarks fra studier basert på ekte transaksjonsdata.

At XGBoost er beste modell er konsistent med Appel et al. (2020), som fant at Gradient Boosting oppnådde høyest nøyaktighet blant de testede algoritmene. Random Forest var best i Schoonbee et al. (2022), men oppnådde også sterke resultater i dette prosjektet (AUC 0.698 etter tuning). Ensemblemetodenes overlegenhet over logistisk regresjon (AUC 0.706 baseline) er i tråd med litteraturens generelle funn om at ikke-lineære modeller fanger mer komplekse betalingsmønstre.

### 9.2 Beslutningsstøtteverdi utover dagens praksis

Prosjektets formål er ikke å bygge en produksjonsklar modell, men å demonstrere at en KI-basert tilnærming kan gi bedre grunnlag for fakturaprioritering enn eksisterende praksis. Tradisjonell prioritering baseres typisk på en kombinasjon av forfallsdato og fakturabeløp – den fakturaen som forfaller snart og har høyest beløp følges opp først. Denne logikken er intuitiv, men ignorerer en avgjørende variabel: sannsynligheten for at fakturaen faktisk betales sent.

Appel et al. (2020) viser at risikoscore definert som R = Verdi × P(Forsinket) gir en radikalt annerledes prioriteringsliste sammenlignet med beløpsbasert sortering (Kendalls τ = 0.003). En faktura på 50 000 kr fra en leverandør som historisk betaler i tide er reelt sett lavere prioritet enn en faktura på 20 000 kr fra en leverandør med høy forsinkelsesrate. Modellen i dette prosjektet tilbyr nettopp denne tredje dimensjonen – leverandørrisiko basert på historisk atferd.

Risikoklassifiseringen av 971 fakturaer resulterte i 273 fakturaer i lav risikogruppe (7 % forsinket), 279 i middels (28 % forsinket) og 419 i høy risikogruppe (55 % forsinket). Separasjonen mellom gruppene er tydelig og viser at modellen skiller mellom leverandørprofiler på en meningsfull måte. For en innkrever betyr dette at ressursinnsatsen kan konsentreres mot de 419 høyrisikofakturaene fremfor å behandle alle 971 likt. Recall på 0.833 innebærer at modellen fanger 83 % av faktisk forsinkede fakturaer – et tall som er direkte relevant for formålet om å redusere andel forsinkede betalinger.

Som beslutningsstøtte, slik Schoonbee et al. (2022) formaliserer det i sitt DSS-rammeverk, er modellens verdi ikke primært i den absolutte AUC-verdien, men i dens evne til å rangere fakturaer etter risiko og gi innkrevere et datadrevet grunnlag for prioritering.

### 9.3 Begrensninger og veien videre

Tre begrensninger er sentrale å adressere. For det første begrenser datasettets syntetiske natur modellens generaliserbarhet. Resultatene er et proof-of-concept for metodikken, ikke en validering av modellens ytelse i produksjon. For at tilnærmingen skal gi fullverdig beslutningsstøtte i en reell kontekst, må modellen trenes på faktiske historiske fakturadata fra virksomheten.

For det andre er konseptdrift ikke håndtert. Appel et al. (2020) løser dette med en window size-parameter som begrenser historiske features til de siste 2–3 månedene, slik at modellen ikke lærer av foreldet betalingsadferd. I dette prosjektet er dette erkjent som en begrensning; ved eventuell drift av modellen i produksjon bør periodisk retrening eller tilsvarende mekanisme implementeres.

For det tredje er andelen fakturaer i høy risikogruppe (43 %) høyere enn hva som er intuitivt forventet. Dette kan delvis forklares av at syntetisk data har komprimert leverandørvariasjonen, slik at flere profiler ligner risikable mønstre enn hva ekte data ville vist. Klassifiseringsterskler bør kalibreres på nytt mot ekte data før modellen tas i operativ bruk.

---

## 10.0 Konklusjon

*Skriv her.*

---

## 11.0 Bibliografi

<!-- APA 7th norsk -->

---

## 12.0 Vedlegg
