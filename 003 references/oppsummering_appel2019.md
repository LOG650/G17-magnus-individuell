# Oppsummering: Appel et al. (2020)

**Tittel:** Optimize Cash Collection: Use Machine Learning to Predicting Invoice Payment

**Forfattere:** Ana Paula Appel, Victor Oliveira, Bruno Lima, Gabriel Louzada Malfatti, Vagner Figueredo de Santana, Rogerio de Paula

**Utgiver:** IBM Research / SIAM (2020)

---

## Problemstilling

Artikkelen tar for seg utfordringen med å predikere om en faktura vil bli betalt i tide eller forsinket (accounts receivable – AR). Innkrevere («collectors») håndterer daglig et stort antall fakturaer og prioriterer tradisjonelt kunder basert utelukkende på beløpets størrelse – ikke på sannsynligheten for forsinkelse. Dette er ineffektivt fordi den største fakturaen ikke nødvendigvis er den med høyest risiko for sen betaling.

**Hovedmål:** Utvikle en maskinlæringsmodell som predikerer sannsynligheten for at en faktura betales etter forfall, og bruke dette til å lage en bedre prioriteringsliste for innkrevere.

---

## Kontekst og datasett

- **Samarbeidspartner:** En multinasjonalbank i Latin-Amerika (anonymisert)
- **Datasett:** 175 552 fakturaer fra 8 land (primært Brasil, Mexico, Colombia, Chile og Peru), 3 725 kunder, perioden august 2017 – juni 2019
- **Klassedefinisjon:** En faktura anses som forsinket hvis betaling skjer mer enn 5 dager etter forfallsdato (p.g.a. behandlingstid i betalingssystemet)

**Datadeling (tidsbasert – for å unngå datalekkasje):**

| Datasett      | Periode               | Andel |
|---------------|-----------------------|-------|
| Trening       | Aug 2017 – Jul 2018   | ~70%  |
| Validering    | Aug 2018 – Nov 2018   | ~15%  |
| Test          | Des 2018 – Jun 2019   | ~15%  |

---

## Feature engineering

Artikkelen fremhever at fakturavariabler alene gir en dårlig modell. Historiske betalingsvariabler er avgjørende for god ytelse.

**Historiske features (beregnet per kunde med «window size» w måneder tilbake):**

| Feature                                  | Beskrivelse                                                    |
|------------------------------------------|----------------------------------------------------------------|
| paid invoice                             | Om siste faktura ble betalt (1 = ja, 0 = nei, -1 = ukjent)   |
| total paid invoices                      | Antall betalte fakturaer før ny faktura                        |
| sum amount paid invoices                 | Totalt beløp betalt på tidligere fakturaer                     |
| total invoices late                      | Antall fakturaer betalt etter forfall                          |
| sum amount late invoices                 | Totalt beløp på forsinkede fakturaer                           |
| total outstanding invoices               | Antall utestående fakturaer                                    |
| total outstanding late                   | Antall utestående fakturaer som er forsinket                   |
| sum total outstanding                    | Totalt beløp utestående                                        |
| sum late outstanding                     | Totalt beløp utestående og forsinket                           |
| average days late                        | Gjennomsnittlig antall dager forsinket på betalte fakturaer    |
| average days outstanding late            | Gjennomsnittlig forsinkelse på utestående fakturaer            |
| standard deviation invoices late         | Standardavvik på antall dager forsinket (betalte fakturaer)    |
| standard deviation invoices outstanding late | Standardavvik på forsinkelse (utestående fakturaer)        |
| payment frequency difference             | Antall ganger kunden har gjort en betaling                     |

---

## Konseptdrift (Concept Drift)

Et sentralt funn er at den statistiske fordelingen av features endrer seg over tid – kalt **konseptdrift**. Kundene i datasettet betalte fakturaer raskere mot slutten av perioden enn i starten. Bruk av all historisk data for å beregne features gir derfor et skjevt bilde av nåværende atferd.

**Løsning:** En parameter kalt *window size* (w) begrenser hvor langt tilbake i tid historiske features beregnes. Beste resultat ble oppnådd med w = 2–3 måneder.

---

## Modeller og resultater

**Testede algoritmer:**

| Algoritme               | Beste nøyaktighet (w=2) |
|-------------------------|-------------------------|
| XGBoost (Gradient Boosting) | **79,75 %**         |
| Random Forest           | 79,05 %                 |
| k-Nearest Neighbors     | 75,40 %                 |
| Logistisk regresjon     | 74,91 %                 |
| Naive Bayes             | 72,00 %                 |

- **Beste modeller:** XGBoost og Random Forest, begge med w = 2 måneder
- **Sluttmodell:** Ensemble av Random Forest og Gradient Boosting
- **Stabilt resultat på tvers av tidssnitt:** ~77 % nøyaktighet og F1-score ~77–78 %
- **AUC:** Høyest for ensemble-modellene (dokumentert via ROC-kurver)

---

## Prioriteringsliste

I tillegg til klassifisering foreslår artikkelen en ny prioriteringsmetode som kombinerer sannsynligheten for sen betaling med fakturabeløpet:

**Risikoscore per faktura:**
> R = Verdi × P(Forsinket)

**Risikoscore per kunde:**
> R_kunde = gjennomsnitt av R over alle kundens fakturaer

Dette gir en mer realistisk rangering enn den tradisjonelle «grådige» tilnærmingen (kun basert på beløpsstørrelse). Kendalls τ = 0,003 viser at rangeringen endrer seg betydelig (~50 %) sammenlignet med gammel metode.

---

## Konklusjon og relevans for dette prosjektet

| Aspekt                    | Funn / anbefaling                                                        |
|---------------------------|--------------------------------------------------------------------------|
| Modelltype                | Ensemble av Random Forest og Gradient Boosting anbefales                 |
| Feature engineering       | Historiske features er avgjørende – fakturavariabler alene er utilstrekkelig |
| Window size               | Bruk 2–3 måneder tilbake for historiske features (konseptdrift)          |
| Datadeling                | Tidsbasert splitt – aldri tilfeldig splitt ved tidsseriedata             |
| Ytelsesmål (benchmark)    | ~77 % nøyaktighet og F1-score som referansepunkt                         |
| Konseptdrift              | Modellen bør evalueres og retrenes periodisk                             |
| Prioritering              | Kombiner predikert sannsynlighet med fakturabeløp for oppfølgingsliste   |

---

*Oppsummering utarbeidet av Magnus Ødegård, mars 2026*
