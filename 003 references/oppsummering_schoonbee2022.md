# Oppsummering: Schoonbee et al. (2022)

**Tittel:** A Machine-Learning Approach Towards Solving the Invoice Payment Prediction Problem

**Forfattere:** L. Schoonbee, W.R. Moore, J.H. van Vuuren

**Utgiver:** South African Journal of Industrial Engineering, Vol. 33(4), pp. 126–146 (2022)

---

## Problemstilling

Artikkelen tar for seg **Invoice Payment Prediction Problem (IPPP)** – problemet med å predikere når, eller om, kunder vil betale utstedte fakturaer. Tradisjonelle reaktive tiltak (rabatter, ekstern innkreving, direktebetaling) har varierende suksess. Artikkelen foreslår i stedet en **preventiv tilnærming** basert på maskinlæring, integrert i et beslutningsstøttesystem (DSS).

**Mål:** Predikere betalingsintervall for en faktura på utstedelsestidspunktet, slik at innkrevingsressurser kan prioriteres mot fakturaer med høyest risiko for sen betaling.

**Klassifisering (multiklasse):**

| Klasse | Beskrivelse                    |
|--------|--------------------------------|
| 0      | Betalt i tide (0 dager forsinket) |
| 1      | 1–30 dager forsinket           |
| 2      | 31–60 dager forsinket          |
| 3      | 61+ dager forsinket            |

---

## Kontekst og datasett

- **Casepartner:** Curro Holdings Ltd – et for-profit skoleselskap i Sør-Afrika
- **Datasett:** 1 068 620 fakturaoppføringer, januar 2016 – april 2021
- **Features i rådata:** 20 deskriptive variabler (10 kategoriske, 10 kontinuerlige) + 1 målvariabel
- **To merker analysert separat:** Curro Schools og Curro Academy

**Tidsbasert datadeling:**

| Datasett        | Periode                    | Andel |
|-----------------|----------------------------|-------|
| Trening         | 2016–2019                  | 56%   |
| Test            | 2020 (månedlig rullerende)  | 32%   |
| Hyperpar.-tuning| Oktober 2020               | –     |
| Hold-out        | November 2020              | –     |

Modellen retreneres månedlig (ved begynnelsen av hver måned) for å håndtere endringer i kundeadferd.

---

## ML-utviklingsveikart (CRISP-DM-basert)

Artikkelen presenterer et strukturert 10-stegs veikart for maskinlæringsutvikling:

| Steg | Beskrivelse                                                                 |
|------|-----------------------------------------------------------------------------|
| 1.0  | Formulere IPPP-instansen og forstå forretningsspørsmålet                    |
| 2.0  | Feature engineering – historiske variabler basert på kundeadferd            |
| 3.0  | Datadeling i trenings-, test- og hold-out-sett (tidsbasert)                 |
| 4.0  | Datavask og forbehandling (håndtere manglende verdier, uteliggere, koding)  |
| 5.0  | Baseline algoritmeevaluering (uten engineered features)                     |
| 6.0  | Feature-seleksjon (filtrer, wrapper, embedded metoder)                      |
| 7.0  | Optimal subset av prediktive features                                        |
| 8.0  | Hyperparameterjustering (grid search)                                        |
| 9.0  | Feature importance-analyse                                                   |
| 10.0 | Endelig modellabsorpsjon i DSS                                               |

---

## Feature engineering

### Historiske features (beregnet per konto)

| Nr | Feature                | Beskrivelse                                                       |
|----|------------------------|-------------------------------------------------------------------|
| 1  | AveDaysLate            | Gjennomsnittlig antall dager forsinket på alle tidligere fakturaer |
| 2  | NumInvOnTime           | Antall fakturaer betalt i tide                                    |
| 3  | NumInvLate             | Antall fakturaer betalt etter forfall                             |
| 4  | RatioOnTime            | Andel fakturaer betalt i tide                                     |
| 5  | DayPayInMonth          | Gjennomsnittlig dag i måneden betaling skjer                      |
| 6  | NumPaymentsPerMonth    | Antall betalinger per måned                                       |
| 7  | DaysSinceLastPayment   | Antall dager siden forrige betaling                               |
| 8  | AnyInvoicesLate        | Binær: 1 hvis utestående faktura finnes, 0 ellers                 |
| 9  | GlobalTrend            | Gjennomsnittlig økning/reduksjon i forsinkelse siste måned        |

### Beregningsmetode for historiske features

Tre metoder ble testet:
1. Gjennomsnitt over alle tidligere fakturaer
2. Gjennomsnitt over et fast antall (window size 2–5)
3. **Eksponentiell vekting over siste 10 fakturaer** (beste resultat)

**Vektfaktor 1.5** ga best prediksjonsytelse: nyere fakturaer vektes 1.5× mer enn den nest nyeste, osv.

### Feature-seleksjon

Fire metoder ble brukt; features som ble valgt av minst 3 av 4 metoder ble inkludert:

| Prioritert feature      | Spearman-korrelasjon |
|-------------------------|----------------------|
| AveDaysLate             | 0.55                 |
| RatioOnTime             | 0.54                 |
| PreviousBalance         | 0.54                 |
| DaysSinceLastPayment    | 0.44                 |
| CreditScore             | 0.29                 |
| DayPayInMonth           | 0.10                 |
| AnyInvoicesLate         | 0.47                 |
| GlobalTrend             | 0.08                 |
| NumPaymentsPerMonth     | 0.05                 |

**Viktigste features:** AveDaysLate, RatioOnTime og PreviousBalance er mest prediktive på tvers av alle modeller.

---

## Datavask og forbehandling

- **Manglende verdier:** Gjennomsnitt-imputering eller fjerning av rader (9% av fakturaer manglet betalingsdato og ble fjernet)
- **Uteliggere:** Klamp-transformasjon
- **Klasseimbalanse:** Tomek links (beste metode) – resulterte i 50/26/24% fordeling
- **Kategoriske variabler:** One-hot encoding
- **Normalisering:** Standardisering og robust skalering (valgt per modell)
- **Forhåndsbetaling:** Fakturaer betalt før forfall (45,19%) fjernet – trivielle å predikere

---

## Modeller og resultater

### Baseline AUC (uten engineered features) vs. enriched AUC

| Modell               | Baseline AUC | Enriched AUC | Forbedring |
|----------------------|--------------|--------------|------------|
| Random Forest        | 79.25%       | 82.33%       | +3.08%     |
| Neural Network       | 75.22%       | 81.44%       | +6.22%     |
| Logistic Regression  | 74.78%       | 79.55%       | +4.77%     |
| k-NN                 | 69.61%       | 75.31%       | +5.70%     |
| Naive Bayes          | 69.81%       | 79.26%       | +9.45%     |
| Decision Tree        | 64.87%       | 66.94%       | +2.06%     |

### Endelige AUC-resultater (etter hyperparameterjustering)

| Rang | Modell               | Curro   | Curro Academy | Snitt   |
|------|----------------------|---------|---------------|---------|
| 1    | **Random Forest**    | 83.72%  | 83.51%        | **83.61%** |
| 2    | Neural Network       | 83.23%  | 82.83%        | 83.03%  |
| 3    | Decision Tree        | 81.64%  | 81.71%        | 81.67%  |
| 4    | k-NN                 | 80.98%  | 81.14%        | 81.06%  |
| 5    | Logistic Regression  | 79.71%  | 82.40%        | 81.05%  |
| 6    | Naive Bayes          | 78.53%  | 79.99%        | 79.26%  |

**Valgt modell:** Random Forest – best ytelse og god tolkbarhet. Ensemble ble ikke valgt pga. økt beregningsbyrde.

**Hold-out resultater:** AUC 79.01% (Curro) og 82.5% (Curro Academy).

---

## Beslutningsstøttesystem (DSS)

DSS-en ble implementert i Python med Dash-grensesnitt og inkluderer:

1. **Dataopplasting** – automatisk feature engineering og datavask
2. **Visualisering** – scatter-plott, fordelinger, betalingshistorikk per konto
3. **Prediksjoner** – tabell med klasse, sannsynlighet per klasse, sorteringsmuligheter
4. **Feature importance** – visualisering av viktigste variabler

Systemet valideres av fageksperter (SMEs) og bekreftes å representere reelle innkrevingsscenarioer.

---

## Konklusjon og relevans for dette prosjektet

| Aspekt                     | Funn / anbefaling                                                              |
|----------------------------|--------------------------------------------------------------------------------|
| Problemformulering         | Multiklasse-klassifisering (0/1–30/31–60/61+ dager) er best egnet             |
| Beste modell               | Random Forest anbefales som primærmodell                                       |
| Feature engineering        | Historiske features er avgjørende – gir 3–9% AUC-forbedring                   |
| Beregningsmetode           | Eksponentiell vekting med faktor 1.5 over siste 10 fakturaer                  |
| Viktigste features         | AveDaysLate, RatioOnTime, PreviousBalance                                      |
| Datadeling                 | Tidsbasert splitt – aldri tilfeldig splitt                                     |
| Datavask                   | Tomek links for klasseimbalanse; fjerning av forhåndsbetalte fakturaer        |
| Ytelsesmål (benchmark)     | AUC 79–83% som referansepunkt                                                  |
| Retrening                  | Månedlig retrening anbefales for å følge endringer i betalingsadferd          |
| Metodikk                   | CRISP-DM-basert 10-stegs veikart gir strukturert tilnærming                   |

---

*Oppsummering utarbeidet av Magnus Ødegård, mars 2026*
