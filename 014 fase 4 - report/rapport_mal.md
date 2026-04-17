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

*Skriv her.*

---

## 5.0 Metode og data

### 5.1 Metode

*Skriv her.*

### 5.2 Data

*Skriv her.*

---

## 6.0 Modellering

*Skriv her.*

---

## 7.0 Analyse

*Skriv her.*

---

## 8.0 Resultat

*Skriv her.*

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
