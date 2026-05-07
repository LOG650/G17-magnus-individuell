---
lang: nb-NO
documentclass: article
geometry: a4paper, margin=2.5cm
fontsize: 11pt
header-includes: |
  \usepackage{titling}
  \usepackage{tabularx}
  \usepackage{newunicodechar}
  \newunicodechar{≈}{\ensuremath{\approx}}
  \AtBeginDocument{\hypersetup{pdftitle={Peer-review av G17},pdfauthor={G19 (nettstudent kveld)}}}
---

\begin{titlepage}
\thispagestyle{empty}
\vspace*{2cm}
\begin{center}
{\Huge\textbf{Peer-review av G17}}\\[0.5cm]
{\Large LOG650 -- Vår 2026}\\[3cm]

\renewcommand{\arraystretch}{1.6}
\begin{tabular}{p{5cm}p{9cm}}
\textbf{Vurderende gruppe} & G19 (nettstudent kveld) \\
\textbf{Vurdert gruppe} & G17 \\
\textbf{Tittel på rapporten} & \textit{Finansiell logistikk og beslutningstøtte ved hjelp av KI} \\
\textbf{Forfatter av rapporten} & Magnus Ødegård \\
\textbf{Dato} & 2026-05-04 \\
\end{tabular}

\vspace{1.5cm}
{\small\textit{Vurderingen gjelder versjonen av rapporten som var tilgjengelig mandag 4. mai 2026. Senere endringer er ikke vurdert.}}
\end{center}
\vfill
\end{titlepage}

## Helhetsinntrykk

Rapporten er metodisk solid og forankret i Appel et al. (2019) og Schoonbee et al. (2022). CRISP-DM-strukturen, datadelingen og hyperparameterjusteringen er ryddig dokumentert, og diskusjonen er ærlig om at benchmarkene ikke nås – forklart med datasettets størrelse og syntetiske natur. Den praktiske beslutningsstøtteverdien fremstår tydelig gjennom risikotredelingen og recall-prioriteringen. Hovedutfordringene er at sammendrag, abstract, innholdsfortegnelse og forsideopplysninger ennå ikke er ferdige, at datasettets syntetiske natur først avsløres i §9.1, at risikoklassifiseringen i §8.3 evalueres på treningsdataene, og at §7 inneholder mye tolkning som hører hjemme i §9. Litteraturgrunnlaget er smalt (to artikler) og veiledningens krav om validitet, reliabilitet og etiske hensyn er ikke direkte adressert. Hovedinntrykket er likevel et ryddig fagarbeid – de fleste forbedringspunktene gjelder *plassering* og *eksplisittering* mer enn faglige feilgrep.

---

## 1 Innledning ✅

Innledningen er kort og effektiv, forankret i primærlitteraturen fra første avsnitt. Avgrensingene i §1.3 er faglig begrunnet, og §1.4 lister fire eksplisitte antagelser med konsekvenser.

**Forbedringspunkter**

- Eksplisitt forskningsmål mangler – målet er gjemt i siste avsnitt av §1.0.
- Spenning mellom A2 (anonymisert ekte data) og §9.1 (syntetisk data) – avklares for sent.
- §1.2 delproblem 2 («Forventet betalingsforsinkelse») leveres ikke i analysen.
- «KI» i problemstillingen er bredere enn metoden faktisk dekker (tre tabular-ML-algoritmer).

**Foreslåtte endringer**

1. ✅ Skill ut et eksplisitt forskningsmål eller -spørsmål i §1.1.
2. ✅ Avklar i §1.4 (eller §5.2) at datasettet er syntetisk, og oppdater A2.
3. ✅ Stryk eller parker delproblem 2 i §1.2 med begrunnelse, og erstatt «KI» med «maskinlæring» i problemstillingen.

---

## 2 Litteraturgjennomgang og teoretisk forankring ✅

Primærlitteraturen er nøye gjengitt og brukes systematisk videre i metode, resultat og diskusjon. Tabell 2.1 gir en effektiv sammenstilling, og kanoniske referanser for algoritmene (Breiman, 2001; Chen & Guestrin, 2016) er på plass.

**Forbedringspunkter**

- Smalt grunnlag: kun to artikler gjennomgått i sin helhet, lite triangulering mot tilgrensende felt (kredittrisiko, B2B trade credit).
- Eksplisitt forskningsgap mangler i §2.4 – studien posisjoneres ikke mot et tydelig hull.
- Litteratursøkets prosess er underdokumentert (ingen inklusjonskriterier, antall treff, screening).
- Teori-til-metode-koblingen er løs: algoritmebegrunnelse og recall-prioritering kommer først i §5.1.

**Foreslåtte endringer**

1. ✅ Utvid §2.1 med inklusjons-/eksklusjonskriterier, tidsvindu og antall treff.
2. ✅ Tilføy 1–2 avsnitt i §2.4 (eller ny §2.5) som formulerer det forskningsgapet prosjektet adresserer.
3. ✅ Flytt argumentet om recall som primærmetrikk fra §5.1 til §3.3.

---

## 3 Metode

CRISP-DM-rammeverket er eksplisitt forankret i Schoonbee, datadelingen er korrekt med beskyttet holdout, og klassevektingen er differensiert per algoritme. Tabell 5.1 (variabelskjema) er ryddig, og avsnittet om bruk av KI-verktøy er åpent og redelig.

**Forbedringspunkter**

- Validitet, reliabilitet og etiske hensyn er ikke eksplisitt forklart (eget veiledningskriterium).
- Datagrunnlagets syntetiske natur avsløres først i §9.1 – burde vært i §5.2.
- Stratifisert random split begrunnes ikke i §5.1 der splitten faktisk gjøres; argumentet i §3.5 («uten tydelig tidsstruktur») kunne vært gjentatt og koblet eksplisitt til konseptdrift-diskusjonen.
- §4.0 er deskriptivt tynt: fire korte avsnitt uten figurer/tabeller eller nøkkeltall om Bedriften.

**Foreslåtte endringer**

1. ✅ Legg til §5.3 «Validitet, reliabilitet og etiske hensyn» som dekker datagrunnlagets natur, splittstrategi, kryssvalidering, konfidensialitet og KI-bruk.
2. ✅ Begrunn valg av binær framfor multiklasse-formulering og random framfor tidsbasert split eksplisitt i §5.1.
3. ✅ Utvid §4.0 med deskriptive nøkkeltall, og flytt deskriptive figurer fra §7.1 dit.

---

## 4 Analyse og resultater

Modelleringsløpet er metodisk gjennomført (baseline → tuning → holdout, jf. Tabell 8.1), featureviktigheten kobles eksplisitt til Schoonbees *AveDaysLate*, og risikoscoren operasjonaliseres som tredeling. Visualiseringen er rik (ROC, AUC, presisjon/recall/F1, konfusjonsmatrise, featureviktighet, risiko-mot-beløp).

**Forbedringspunkter**

- §8.3 evaluerer risikoklassifiseringen på treningsdataene (modell retrent på alle 971): «åtte ganger separasjon» er per definisjon optimistisk og bør erstattes med out-of-fold eller holdout-tall.
- §7 og §8 inneholder tolkning som hører hjemme i §9 – f.eks. «overraskende sterk baseline», «konsistent med Appel et al.», «bekrefter at variabelen er valid».
- Dobbel «Figur 1» mellom §5.2 og §7.1 (samme bilde) – kryssreferansen er tvetydig.
- Risikotersklene 0,30 / 0,55 i §8.3 er ad-hoc og ubegrunnet.

**Foreslåtte endringer**

1. ✅ Re-evaluer risikoklassifiseringen på out-of-fold- eller holdout-prediksjoner, eller gjør eksplisitt at tallene gjelder treningsdataene.
2. ✅ Flytt tolkningssetninger fra §7 og §8 til §9, og slett dupliseringen av Figur 1.
3. ✅ Begrunn risikotersklene (lik gruppestørrelse, presisjons-/recall-mål, eller sammenligning med Appel et al.).

---

## 5 Diskusjon

Diskusjonen er ærlig om benchmark-gapet og forklarer det faglig forsvarlig (datasettstørrelse, syntetisk data). Koblingen til primærlitteraturen er gjennomgående, og den praktiske beslutningsstøtteverdien etableres tydelig i §9.2.

**Forbedringspunkter**

- Eksplisitt kobling tilbake til problemstillingen i §1.1 mangler.
- Implikasjoner er nesten utelukkende praktiske – teoretiske og policy-implikasjoner er ikke berørt.
- Uventede funn (log.reg ≈ XGBoost; RF baseline med lav recall) er underdrøftet.
- Mulig sirkulær validering: datasettet er syntetisk og inneholder forhåndsdefinert «Risikokategori leverandør» – modellen kan «bekrefte» mønstre som er bygget inn i datageneratoren.

**Foreslåtte endringer**

1. ✅ Tilføy et åpningsavsnitt i §9 som siterer problemstillingen og besvarer den punktvis.
2. ✅ Utvid med teoretiske og policy-implikasjoner, og løft frem uventede funn i et eget delkapittel.
3. ✅ Drøft eksplisitt risikoen for sirkulær validering ved syntetisk datasett.

---

## 6 Konklusjon

Konklusjonen besvarer problemstillingen direkte, identifiserer historisk betalingsatferd som sterkeste prediktor, og leverer tre handlingsrettede anbefalinger til Bedriften.

**Forbedringspunkter**

- Begrensningsavsnittet duplikerer §9.3 i utvidet form.
- Studiens teoretiske bidrag formuleres ikke (veiledningskriterium).
- Forslag til videre forskning er i hovedsak praktiske implementeringssteg snarere enn forskningsspørsmål forankret i forskningsbakgrunnen – anbefaling 3 har et metodisk element (window size), men de øvrige er driftsorienterte.
- Påstanden om bransjegeneralisering motsier avgrensingen i §1.3, og presisjon (0,495) nevnes ikke når recall (0,833) fremheves.

**Foreslåtte endringer**

1. ✅ Trim begrensningsavsnittet og bruk plassen på fremoverpekende vurderinger.
2. ✅ Tilføy et delavsnitt om studiens teoretiske bidrag (overførbarhet av IPPP-metodikken, replikasjon av featureviktighet, observasjoner om lineære vs. ensemble-modeller på syntetisk data).
3. ✅ Erstatt deler av «videre forskning» med faktiske forskningsspørsmål (datavolum, klasseubalansetiltak, transfer learning), og modererer generaliseringspåstanden.

---

## 7 Skriveflyt, formelle aspekter og helhetsvurdering

Språket er presist og strukturen følger en logisk progresjon. APA 7-formatet i §11 er konsistent og korrekt, tabellene er ryddige (Tabell 8.1 fremhever beste modell), og forkortelser introduseres med full form ved første bruk.

**Forbedringspunkter**

- Sammendrag, Abstract og Innholdsfortegnelse er ikke skrevet, og forsideopplysninger er ufullstendige (sidetall, dato, studiepoeng, veileder).
- Dobbel «Figur 1» mellom §5.2 og §7.1; tabellene i §6.1 er unummerert.
- §4.0 er svært tynt sammenlignet med §7 og §8; §6 og §7 har overlappende formål.
- Originaliteten er kontekstuell og ikke eksplisitt formulert.

**Foreslåtte endringer**

1. ✅ Skriv Sammendrag og Abstract (8–15 linjer hver) og fyll inn forsideopplysningene.
2. ✅ Slett dupliseringen av Figur 1, nummerer tabellene i §6.1, og samkjør figurnummer mellom captions og filnavn.
3. ✅ Utvid §4.0 og slå sammen overlappende deler av §6 og §7 – bruk frigjort plass på å tydeliggjøre studiens faktiske bidrag i §2.4 og §10.
