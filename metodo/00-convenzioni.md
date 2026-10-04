# Convenzioni del metodo

Regole comuni a tutti i file di `metodo/` e `applicazioni/`. Le decisioni dell'autore stanno in `DECISIONI.md` (44 schede, decise il 4 ottobre 2026) e in sintesi in `ricerca/decisioni-log.md`. Questo file le traduce in regole di scrittura: non prende decisioni nuove.

**Per chi scrive un file del metodo**
1. Le etichette di ogni strumento si copiano dalla sezione 3 così come sono.
2. Ogni strumento ha una sola scheda, nel file indicato nella sezione 3. Gli altri file lo citano con l'ID.
3. Se questo file e `DECISIONI.md` non concordano, vale `DECISIONI.md`. Il conflitto si segnala, non si risolve da soli.
4. I punti che l'autore non ha deciso (sezione 6) si scrivono come proposta, con la dicitura **Proposta, da confermare con l'autore**.

**Indice**
1. Etichette
2. Scheda dello strumento
3. Strumenti: ID, decisioni, etichette
4. Mappa dei file
5. Regole di scrittura
6. Punti lasciati all'autore
7. Glossario

---

## 1. Etichette

Il metodo è unico (decisione strutturale dell'autore). Ogni strumento, pratica o affermazione porta una o più etichette. Il sistema è lo stesso del progetto QIGONG dell'autore (`/home/user/QIGONG`): quattro colori, ognuno con un nome. Le etichette si combinano quando aspetti diversi dello stesso strumento hanno statuti diversi, come nel progetto QIGONG ("Fonte classica per mappa e terminologia, Tradizione per gli effetti energetici, Evidenza per gli effetti del respiro lento").

### 1.1 Legenda

| Etichetta | Che cosa indica | Che cosa va scritto accanto |
|---|---|---|
| 🟦 **Fonte classica** | L'elemento è attestato nel libro di Lozanov del 2005, la fonte primaria del fondatore | La riga del libro (r. NNNN), presa da `ricerca/modello-canonico-lozanov.md` |
| 🟨 **Tradizione** | Pratica tramandata dalla tradizione suggestopedica e Superlearning (Ostrander e Schroeder, Bancroft, manuali) oppure dallo standard di una disciplina (Health Qigong HQA, tango). Non è stata testata scientificamente come tale | La sigla della fonte (SL1-A T04, MAN A.3, HQA) |
| 🟩 **Evidenza** | Affermazione sostenuta da studi scientifici. Nel testo si specifica sempre **solida** o **parziale** | Il riferimento o il cluster dei file di verifica (VNF, VPS, VTN) |
| 🟥 **Speculativo** | Affermazione **non verificata** oppure **contraddetta** dagli studi. Nel testo si specifica sempre quale delle due | Il cluster dei file di verifica, se c'è |
| 🟥 **Non canonico** | Pratica o spiegazione che Lozanov rifiuta in modo esplicito | La riga del libro (r. NNNN) |

Note.
- 🟦 dice da dove viene un elemento, non che funziona. Una tesi del fondatore è 🟦 per l'attestazione e 🟥 non verificata per l'effetto.
- 🟨 dice da dove viene una pratica, non che funziona. Le corrispondenze del Liu Zi Jue con gli organi sono 🟨 Tradizione: si presentano come teoria tradizionale, senza promesse di salute (SIC-05).
- 🟥 Non canonico non è un giudizio di efficacia: dice solo che Lozanov esclude quella pratica come mezzo o come spiegazione. Uno strumento può essere 🟥 Non canonico e 🟩 Evidenza parziale insieme (per esempio S-23).
- Quando Lozanov non tratta un tema, non c'è un'etichetta di canone. La scheda scrive nella riga "Origine" la dicitura **Non trattato da Lozanov**.
- Regole, criteri e procedure di sicurezza non hanno un'etichetta di evidenza (non c'è un'affermazione di efficacia da valutare). Portano solo l'etichetta d'origine, se c'è.

### 1.2 Corrispondenza con `DECISIONI.md` e con `ricerca/`

`DECISIONI.md` e i file di `ricerca/` usano le lettere A-D e tre gradi di compatibilità con il canone. Si traducono così.

| In `DECISIONI.md` e `ricerca/` | Nel metodo |
|---|---|
| A solida | 🟩 **Evidenza** solida |
| B plausibile-parziale | 🟩 **Evidenza** parziale |
| C debole-non verificata | 🟥 **Speculativo** (non verificato) |
| D smentita-pseudoscienza | 🟥 **Speculativo** (contraddetto dagli studi) |
| Non applicabile (n.a.) | nessuna etichetta di evidenza |
| Coerente (elemento del canone) | 🟦 **Fonte classica** con la riga |
| Coerente (pratica di altra origine compatibile con un principio del canone) | etichetta d'origine (🟨, oppure nessuna per le INT) e, nel testo, "principio affine" con 🟦 e la riga |
| Non trattato | dicitura "Non trattato da Lozanov" |
| Rifiutato | 🟥 **Non canonico** con la riga |

Le schede di `DECISIONI.md` indicano a volte due livelli ("D / B nocciolo"). Nel metodo diventano due etichette, ognuna con il suo oggetto: "🟥 Speculativo (contraddetto) per l'ossigeno al cervello · 🟩 Evidenza parziale per il respiro lento senza apnee".

### 1.3 Formato delle etichette

**Nella scheda.** Una riga subito sotto il titolo, seguita da una riga vuota. Ogni etichetta è formata da quadrato, nome in grassetto, aspetto a cui si riferisce e, tra parentesi, riga o riferimento. Separatore: punto mediano con uno spazio per parte (` · `).

🟦 **Fonte classica** per la procedura (r. 4021-4099) · 🟩 **Evidenza parziale** per la voce variata (VPS T12) · 🟥 **Speculativo** (non verificato) per l'effetto del formato

Regole:
- l'ordine è: 🟦, 🟨, 🟩, 🟥 Speculativo, 🟥 Non canonico;
- "Evidenza" si scrive sempre con "solida" o "parziale" dopo il nome; "Speculativo" sempre con "(non verificato)" o "(contraddetto)";
- l'etichetta non si cambia e non si attenua nel testo della scheda;
- un'etichetta che riguarda solo una variante (per esempio la prova mentale dettata dal docente) lo dice: "🟥 **Non canonico** se dettata dal docente (r. 1440-1441)".

**Nelle tabelle.** Forma breve: quadrato e una parola. `🟦 r. 4021-4099 · 🟩 parziale · 🟥 non verificato`; `🟨 SL1-A T04 · 🟥 non canonico · 🟥 contraddetto`.

**Nel testo continuo.** Per le affermazioni teoriche (in 01, 04, 05, 06) l'etichetta si mette tra parentesi alla fine della frase o del paragrafo: "(🟦 r. 2931 · 🟥 non verificato)".

### 1.4 Statuti delle affermazioni teoriche

Valgono per affermazioni che non sono strumenti. La dicitura di statuto precede le etichette.

| Statuto | Si usa per | Etichette |
|---|---|---|
| **Tesi del fondatore** | Tesi teoriche di Lozanov: riserve, ipermnesia, paraconscio, norma sociale suggestiva, leggi dell'ipermnesia, ricordo spontaneo ritardato | 🟦 **Fonte classica** (r. NNNN) · 🟥 **Speculativo** (non verificato) |
| **Ipotesi teorica** | La cornice predictive coding e metastabilità (D-31) | 🟩 **Evidenza parziale** per i riferimenti e il nucleo cognitivo · 🟥 **Speculativo** (non verificato) per il meccanismo e per il movimento come training di metastabilità |
| **Dichiarato dall'autore** | Risultati riportati da Lozanov (D-32) | 🟦 **Fonte classica** (r. NNNN), con la dicitura "dichiarato dall'autore". Corrisponde al livello C di `DECISIONI.md` |
| **Proposta, da confermare con l'autore** | Punti aperti della sezione 6 | etichette dello strumento a cui la proposta si riferisce |

I fatti storici documentati (date, istituzioni, pubblicazioni) non hanno bisogno di etichetta: corrispondono al livello A.

### 1.5 Riquadro "Cosa dicono le fonti"

Decisione D-30: il testo usa spiegazioni corrette; le spiegazioni delle fonti stanno in un riquadro con la loro etichetta. Vale anche per le pratiche tenute "come nelle fonti" (D-05, D-08, D-10, D-12, D-13, D-15, D-19, D-28): procedura delle fonti, spiegazione corretta nel testo, spiegazione delle fonti nel riquadro.

Formato: citazione Markdown; prima riga con il titolo in grassetto e l'etichetta; una riga `>` vuota; poi il testo.

> **Cosa dicono le fonti** · 🟥 Speculativo (contraddetto)
>
> Le fonti presentano le respirazioni 4-4-4-4 e 8-4-8-4 come un modo per "massimizzare l'apporto di ossigeno al cervello" e "sincronizzare i due emisferi" (MAN A.3, r. 30-34; SL1-B T3, r. 715-716).

Regole:
1. Il riquadro contiene spiegazioni e promesse delle fonti. La procedura sta nel campo "Procedura" della scheda.
2. Ogni affermazione è attribuita: "le fonti", sigla, righe.
3. L'etichetta è quella della spiegazione delle fonti, presa dalla scheda di `DECISIONI.md` o dal cluster dei file di verifica, tradotta con la tabella 1.2.
4. Le cifre delle fonti (percentuali, battiti, hertz, punti di QI) compaiono solo nel riquadro, sempre attribuite.
5. Un riquadro per scheda, dopo la spiegazione corretta. Se le fonti non danno spiegazioni, il riquadro non c'è.
6. Dopo il riquadro non si aggiungono commenti: la spiegazione corretta è già nel testo.
7. Eccezione decisa dall'autore (D-25): la teoria emisferica di Sunbeck compare nel testo della scheda S-35, in un paragrafo intitolato "Teoria di Sunbeck" con l'etichetta 🟥 **Speculativo** (contraddetto).

---

## 2. Scheda dello strumento

Ogni strumento con ID ha una scheda con questo schema.

```markdown
### S-nn Nome dello strumento

🟦 **Fonte classica** per ... (r. NNNN) · 🟩 **Evidenza parziale** per ... · 🟥 **Speculativo** (non verificato) per ...

Origine: ... · Decisione: ... · Fase del ciclo: ... · Sicurezza: SIC-nn

**Scopo.** Una o due frasi.

**Procedura.**
1. ... (2 min)
2. ... (5 min)

**Esempio tango.** ...

**Esempio Liu Zi Jue.** ...

**Spiegazione.** Che cosa dice il canone (con le righe) e che cosa dice la ricerca (con i riferimenti dei file di verifica).

> **Cosa dicono le fonti** · 🟥 Speculativo (contraddetto)
>
> ...

**Precauzioni.** ...

**Collegamenti.** S-nn, S-nn.
```

Regole:
1. **Procedura.** Passi numerati, ognuno con la durata indicativa. Per gli strumenti "come nelle fonti" la procedura segue le estrazioni in `ricerca/estrazioni/` e ne cita sigla e righe; non si modifica. Quando la fonte non dà tempi, la scheda lo dice e propone tempi con la dicitura **Proposta, da confermare con l'autore**. Screening e precauzioni vanno nel campo "Precauzioni".
2. **Fase del ciclo.** Una o più fasi tra: preparazione, introduzione, concerto, elaborazione, performance, fuori aula (02 §1).
3. **Esempi.** Ogni strumento con decisione "nel metodo" ha almeno un esempio di tango e uno di Liu Zi Jue, concreti e praticabili con un gruppo fino a 20 persone (10 coppie). Nel modulo sperimentale gli esempi si danno dove hanno senso.
4. **Spiegazione.** Solo spiegazioni corrette (§5.2). Per gli elementi del canone prima Lozanov, poi la ricerca. Le tesi di Lozanov portano lo statuto "Tesi del fondatore".
5. **Riquadro.** Solo se le fonti danno una spiegazione diversa da quella corretta (§1.5).
6. **Precauzioni.** Quelle della scheda di `DECISIONI.md` (§5.7) e le procedure SIC che si applicano (§3.9).
7. **Collegamenti.** Strumenti affini o in tensione (per esempio S-26 e S-46; S-38 e S-45; S-16 e S-67).

**Regola delle componenti.** Alcune procedure delle fonti combinano elementi che hanno decisioni diverse. Ogni componente segue la propria decisione:
- i dispositivi fuori dal metodo non compaiono: l'AVE che in MAN segue il rilassamento (S-23), gli occhiali Ganzfeld della discesa cromatica (S-24);
- le componenti del modulo sperimentale restano in 07: i cicli di 8 e 12 secondi (S-73) nel concerto in movimento (S-05) e nella respirazione (S-22); l'elettrostimolazione abbinata all'ancoraggio (S-26, S-62); il training autogeno nella prova mentale (S-38, S-64);
- le componenti nel metodo con una scheda propria si citano con l'ID: i tre toni (S-31) e la musica "ad alta frequenza" (S-54) nel concerto in movimento (S-05).

Nei casi dubbi la scheda descrive la procedura delle fonti e segnala in nota la componente con decisione diversa.

**Strumenti del canone.** Si descrivono secondo il canone. Se le fonti li combinano con pratiche non canoniche (per esempio la visualizzazione cromatica durante il concerto passivo, MAN fase 4 della lezione modello), la combinazione si descrive nella scheda della pratica non canonica.

---

## 3. Strumenti: ID, decisioni, etichette

### 3.1 Regole sugli ID

- `S-nn` indica uno strumento o una pratica (76 in tutto). `SIC-nn` indica una procedura di sicurezza (7).
- Gli ID sono stabili. Uno strumento nuovo prende il primo numero libero dopo S-76; nessun ID si rinumera.
- Titolo della scheda: `### S-22 Respirazioni con apnea`, con il nome esatto della tabella.
- Citazione: la prima volta in un file "S-22 Respirazioni con apnea", poi "S-22".
- Colonna "File": sigle della sezione 4 (01-07, 03a, 03b; AT, AQ, AF, AU per le applicazioni) e sezione del file.
- Colonna "Origine": "canone" con le righe di Lozanov 2005 (r. NNNN); "fonti" con le sigle delle estrazioni; "INT" per le integrazioni dalla ricerca attuale.
- Colonna "Decisione": scheda di `DECISIONI.md` e scelta dell'autore. Per gli elementi del canone: "Canone" e la base dell'etichetta di evidenza nei file di verifica.
- Colonna "Etichette": forma breve (§1.3). "n.t." significa "Non trattato da Lozanov".

### 3.2 Ciclo didattico (02)

| ID | Strumento | Origine | Decisione | File | Etichette |
|---|---|---|---|---|---|
| S-01 | Introduzione | canone: r. 3936-3998 (modello §5.4) | Canone. Base: nessuno studio specifico nei file di verifica | 02 §2 | 🟦 r. 3936-3998 · 🟥 non verificato |
| S-02 | Concerto attivo | canone: r. 4021-4099 (modello §5.5) | Canone. Base: VPS C7 (nessuno studio isola il formato) | 02 §2 | 🟦 r. 4021-4099 · 🟥 non verificato |
| S-03 | Concerto passivo | canone: r. 4100-4115 (modello §5.6) | Canone; musica dal programma ufficiale, cap. 31 (nota D-18). Base: VPS C7 | 02 §2 | 🟦 r. 4100-4115 · 🟥 non verificato |
| S-04 | Concerto dimostrato (forma A) | adattamento proposto nel modello (§9.3, r. 761) del concerto canonico | D-27: nel metodo | 02 §2 | 🟦 r. 4021-4115 (concerto da cui deriva) · n.t. (adattamento) · 🟥 non verificato |
| S-05 | Concerto in movimento come nelle fonti (forma C) | fonti: SL1-A T11; TM T5, T7; SL1-B T7 | D-27: nel metodo come nelle fonti | 02 §2 | 🟨 SL1-A T11, TM T7 · 🟥 non verificato · 🟥 non canonico (r. 1394-1397, 1855-1860) |
| S-06 | Elaborazione primaria e secondaria | canone: r. 4248-4369 (modello §5.8) | Canone. Base: VPS §8 (distanziamento e richiamo) | 02 §2 | 🟦 r. 4248-4369 · 🟩 parziale |
| S-07 | Performance degli allievi | canone: r. 3932-3935, 3958-3965, 4463-4468 | Canone. Base: VPS C3 | 02 §2 | 🟦 r. 3932-3935, 4463-4468 · 🟩 parziale |
| S-08 | Struttura globale-parziale e dettagli sul secondo piano | canone: r. 2932-3077, 3129-3138, 5846-5847 | Canone. Base: nessuno studio specifico nei file di verifica | 02 §3 | 🟦 r. 2932-3077 · 🟥 non verificato |
| S-09 | Conoscenza passiva accolta | canone: r. 3266-3320 | Canone. Base: VPS T8 | 02 §3 | 🟦 r. 3266-3320 · 🟩 parziale |
| S-10 | Alternanza dei tempi e sezione aurea | canone: r. 885-908, 4422-4435 | Canone. Base: VPS T11 | 02 §3 | 🟦 r. 885-908, 4422-4435 · 🟥 non verificato (alternanza) · 🟥 contraddetto (sezione aurea come legge) |
| S-11 | Verifiche facili e soglia del 70-75% | canone: r. 4453-4459, 4986-5084, 5143-5178 | Canone. Base: VPS C5 | 02 §3 | 🟦 r. 4453-4459 · 🟩 parziale |
| S-12 | Lettura informativa facoltativa | canone: r. 4479-4481 | Canone (niente compiti obbligatori). Base: VPS C4 | 02 §3 | 🟦 r. 4479-4481 · 🟩 parziale |
| S-13 | Corsi adattivi | canone: r. 2460-2469 | Canone; contenuto non descritto nel libro (§6, punto 4) | 02 §3 | 🟦 r. 2460-2469 |
| S-14 | Controllo della fatica | canone: r. 561-562; r. 5491-5494 (F. Beer, riportato nel libro) | Canone | 02 §3 | 🟦 r. 561-562 |

### 3.3 Catalogo, parte 1: gioco, stato, suggestione, voce, comunicazione (03a)

| ID | Strumento | Origine | Decisione | File | Etichette |
|---|---|---|---|---|---|
| S-15 | Gioco-progetto | canone: r. 755-759, 3943-3949, 4417-4420 | Canone. Base: prove indirette (VPS C1; pedagogia teatrale in D-29) | 03a §A | 🟦 r. 3943-3949 · 🟩 parziale |
| S-16 | Nuove identità | canone: r. 759-762, 2704-2707 | Canone; distinte da S-67 (D-16). Base: VPS C1 | 03a §A | 🟦 r. 759-762 · 🟩 parziale |
| S-17 | Sistema della risata | canone: r. 2716-2726 | Canone. Base: VNF F8 (nocciolo) | 03a §A | 🟦 r. 2716-2726 · 🟩 parziale |
| S-18 | Giochi didattici | canone: r. 2846-2848, 4283 | Canone. Base: VNF F8 (nocciolo) | 03a §A | 🟦 r. 2846-2848, 4283 · 🟩 parziale |
| S-19 | Percezioni periferiche | canone: r. 2232-2264, 3099-3110 | Canone. Base: VNF F3; VPS §8 (osservazione e imitazione) | 03a §A | 🟦 r. 2232-2264 · 🟩 parziale (osservazione di modelli) · 🟥 non verificato (assimilazione periferica) |
| S-20 | Estetica totale della sala e dei materiali | canone: r. 3104-3110, 3924-3928 | Canone. Base: VNF F3 | 03a §A | 🟦 r. 3924-3928 · 🟥 non verificato |
| S-21 | Teatro e mimo | fonti: SL1-A T26 | D-29: nel metodo | 03a §A | 🟨 SL1-A T26 · 🟦 principio affine r. 4265-4313 · 🟩 parziale · 🟥 non verificato (aneddoti delle fonti) |
| S-22 | Respirazioni con apnea | fonti: SL1-A T04-T07; MAN A.3; SL1-B T3; TM T3; TLT R-T1 | D-05: nel metodo come nelle fonti, screening obbligatorio | 03a §B | 🟨 SL1-A T04-T07 · 🟩 parziale (respiro lento senza apnee) · 🟥 contraddetto (ossigeno) · 🟥 non canonico (r. 1407-1416) |
| S-23 | Rilassamento progressivo e Scan and Relax | fonti: SL1-A T01-T02; MAN A.1; SL1-C sez. 2.4 | D-08: nel metodo come nelle fonti | 03a §B | 🟨 SL1-A T01-T02 · 🟩 parziale (ansia) · 🟥 non canonico (r. 1427-1428, 1626-1632) |
| S-24 | Visualizzazioni guidate (discesa cromatica, viaggio calmante) | fonti: SL1-A T08; MAN A.4; DSS T23-bis | D-10: nel metodo come nelle fonti | 03a §B | 🟨 SL1-A T08 · 🟥 contraddetto · 🟥 non canonico (r. 1440-1441) |
| S-25 | Image Streaming | fonti: SL1-A T21; MAN A.8; SL1-B T10; TM T10 | D-10: nel metodo come nelle fonti | 03a §B | 🟨 SL1-A T21 · 🟩 parziale (verbalizzazione) · 🟥 contraddetto (promesse) · 🟥 non canonico (r. 1407-1416) |
| S-26 | Ancoraggi emotivi | fonti: SL1-A T18; MAN A.6, T6.5; SL1-C T10, T15; DSS T25-T26 | D-15: nel metodo come nelle fonti | 03a §B | 🟨 SL1-A T18 · 🟩 parziale (routine) · 🟥 non verificato (ancora) · 🟥 non canonico (r. 1400-1406, 1824-1849) |
| S-27 | Audio notturni e apprendimento nel sonno | fonti: SL1-A T28, T30; SL1-B T17; MAN A.11, T6.4; DSS T17-T19 | D-13: nel metodo come nelle fonti, consenso informato obbligatorio | 03a §C | 🟨 SL1-A T28 · 🟥 contraddetto · 🟥 non canonico (r. 1600-1624) |
| S-28 | Messaggi subliminali | fonti: SL1-A T29; SL1-B T18; DSS T20 | D-13: come sopra | 03a §C | 🟨 SL1-A T29 · 🟥 contraddetto · 🟥 non canonico (r. 1400-1406, 2232-2264) |
| S-29 | Dial Direct 1-800-SUB | fonti: SL1-A T32 | D-13: come sopra | 03a §C | 🟨 SL1-A T32 · 🟥 contraddetto · 🟥 non canonico (r. 1440-1441) |
| S-30 | Intonazione oscillante | canone: r. 2709-2712, 2740-2741, 4021-4099 | D-24: nel metodo. Base: VPS T12 | 03a §D | 🟦 r. 2709-2712 · 🟩 parziale |
| S-31 | Tre toni fissi | fonti: SL1-A T16; MAN A.5; TM T7, T9; TLT R-T4 | D-24: variante opzionale di S-30 | 03a §D | 🟨 SL1-A T16 · 🟩 parziale (variazione della voce) · 🟥 non verificato (tre toni) · 🟥 non canonico (tono imperativo, r. 4089-4091) |
| S-32 | Conteggio a ruoli alternati | proposta dell'autore (D-27b) | D-27b: nel metodo | 03a §D | n.t. · 🟥 non verificato |
| S-33 | Sistema delle canzoni | canone: r. 2715-2716, 4321, 4469-4470 | Canone. Base: VPS §8 (canto e melodia) | 03a §D | 🟦 r. 2715-2716 · 🟩 parziale |
| S-34 | Filastrocche e canzoni mnemoniche | fonti: SL1-A T17 | D-29: nel metodo | 03a §D | 🟨 SL1-A T17 · 🟦 principio affine r. 2715-2716 · 🟩 parziale |
| S-57 | Doppio piano | canone: r. 2279-2282, 4474 | Canone. Base: nessuno studio specifico nei file di verifica | 03a §E | 🟦 r. 2279-2282 · 🟥 non verificato |
| S-58 | Comunicazione non direttiva | canone: r. 1774-1775, 3971-3974, 4004-4014 | Canone. Base: VPS §8 (clima emotivo, autonomia) | 03a §E | 🟦 r. 1774-1775 · 🟩 parziale |
| S-59 | Correzione indiretta | canone: r. 4275-4276, 4358-4360, 4381-4382 | Canone; eccezione SIC-06 (INT-07). Base: VPS §8 (feedback non continuo) | 03a §E | 🟦 r. 4275-4276 · 🟩 parziale |
| S-60 | Prevenzione dell'induzione ipnotica | canone: r. 1795-1798, 1824-1849; competenza 11 (r. 5753-5773) | Canone | 03a §E | 🟦 r. 1824-1849 |

S-57–S-60 erano assegnati a 05 nella prima versione di questo file. Le schede stanno ora in 03a §E (comunicazione); 05 li tratta dal punto di vista del docente e rimanda alle schede. Gli ID non cambiano.

### 3.4 Catalogo, parte 2: corpo, memoria, integrazioni (03b)

| ID | Strumento | Origine | Decisione | File | Etichette |
|---|---|---|---|---|---|
| S-35 | Infinity Walk | fonti: SL1-A T22; SL1-B T4-T5; MAN A.9; DSS T2; TM T4-T5 | D-25: nel metodo come esercizio motorio, con la teoria emisferica nel testo; l'uso come test è S-74 | 03b §A | 🟨 SL1-A T22, MAN A.9 · 🟩 parziale (esercizio) · 🟥 contraddetto (teoria emisferica) · n.t. |
| S-36 | Tecnica Alexander | fonti: SL1-B T14; DSS T4 | D-28: nel metodo come nelle fonti | 03b §A | 🟨 SL1-B T14 · 🟩 parziale · 🟥 contraddetto (flusso energetico, immunità) · n.t. |
| S-37 | TPR (Total Physical Response) | fonti: SL1-A T23 | D-29: nel metodo | 03b §A | 🟨 SL1-A T23 · 🟩 solida (memoria di azioni) · 🟩 parziale (lessico) · n.t. |
| S-38 | Prova mentale come nelle fonti | fonti: SL1-A T09 | D-12: nel metodo come nelle fonti | 03b §A | 🟨 SL1-A T09 · 🟩 parziale (pratica mentale) · 🟥 non verificato (caso Drapeau) · 🟥 non canonico se dettata (r. 1440-1441) |
| S-39 | Mappe mentali | fonti: SL1-A T20 | D-29: nel metodo | 03b §B | 🟨 SL1-A T20 · 🟥 non verificato · n.t. |
| S-40 | Palazzo della memoria | fonti: SL1-A T20 | D-29: nel metodo | 03b §B | 🟨 SL1-A T20 · 🟩 parziale (metodo dei loci) · 🟥 non verificato (varianti delle fonti) · n.t. |
| S-41 | Istruzione inversa | fonti: SL1-A T24 | D-29: nel metodo | 03b §B | 🟨 SL1-A T24 · 🟦 principio affine r. 2932-2933 · 🟩 parziale (fatto storico) · 🟥 non verificato (tecnica) |
| S-42 | Distanziamento e richiamo attivo | INT-01 | INT-01: approvata | 03b §C | 🟦 principio affine r. 4248-4369 · 🟩 solida |
| S-43 | Focus attentivo esterno | INT-02 | INT-02: approvata | 03b §C | 🟦 principio affine r. 3129-3138 · 🟩 solida-parziale (A-B) |
| S-44 | Pratica variata | INT-03 | INT-03: approvata | 03b §C | 🟦 principio affine r. 3860-3872, 4315-4369 · 🟩 parziale |
| S-45 | Imagery autogestita | INT-04 | INT-04: approvata | 03b §C | 🟩 parziale · 🟥 non canonico se dettata (r. 1440-1441) · n.t. |
| S-46 | Routine pre-esecuzione | INT-05 | INT-05: approvata | 03b §C | 🟩 parziale · n.t. |
| S-47 | Esercizi vestibolo-oculari | INT-06 | INT-06: approvata | 03b §C | 🟩 solida (riabilitazione) · 🟩 parziale (danzatori) · n.t. |
| S-48 | Sicurezza percepita | INT-07 | INT-07: approvata | 03b §C | 🟦 principio affine r. 2802-2845, 3860-3915 · 🟩 solida (ansia e prestazione) · 🟥 non verificato (meccanismo) |
| S-49 | Gesto ed effetto di esecuzione | INT-08 | INT-08: approvata | 03b §C | 🟦 principio affine r. 4283 · 🟩 solida (memoria di azioni) · 🟩 parziale (lessico) |
| S-50 | Canto e coro | INT-09 | INT-09: approvata | 03b §C | 🟦 principio affine r. 2715-2716, 4469-4470 · 🟩 parziale |
| S-51 | Misure validate | INT-10 | INT-10: approvata | 03b §C | 🟦 principio affine r. 4453-4459 · 🟩 solida (strumenti) |
| S-52 | Pause brevi nella pratica motoria | INT-11 | INT-11: approvata | 03b §C | 🟩 parziale · n.t. |

### 3.5 Musica (04)

| ID | Strumento | Origine | Decisione | File | Etichette |
|---|---|---|---|---|---|
| S-53 | Effetto Mozart | fonti: SL1-B r. 876-880; MAN r. 136-139; TM D:L122-123, M:L192-198 | D-19: nel metodo come nelle fonti | 04 §4 | 🟨 SL1-B, MAN · 🟩 solida (resoconto di Rauscher 1993) · 🟥 contraddetto · 🟥 non canonico (r. 5805) |
| S-54 | Alte frequenze e gregoriano come "ricarica" | fonti: SL1-A T11; SL1-B T11; TM D-2, M1, T7, T12 | D-19: come sopra | 04 §4 | 🟨 SL1-A T11, SL1-B T11 · 🟥 contraddetto · 🟥 non canonico (r. 5805) |
| S-55 | Ascolto filtrato e conduzione ossea (Tomatis, Sound Therapy, Forbrain, Sonic Brain Activator) | fonti: SL1-A T12; SL1-C T4; DSS T9; MAN schede 5-7, A.5, A.7 | D-19: come sopra | 04 §4 | 🟨 SL1-A T12, MAN · 🟥 contraddetto · 🟥 non canonico (r. 1420-1421, 5811-5813) |
| S-56 | Turning Sound | fonti: TM D6 | D-19: come sopra | 04 §4 | 🟨 TM D6 · 🟥 contraddetto · 🟥 non canonico (r. 1420-1421, 5811-5813) |

### 3.6 Docente (05)

Il file 05 non contiene schede. Tratta le condizioni canoniche del docente (prestigio, aspettativa, amore non sentimentale), la voce e il corpo del docente, la correzione, la gestione del gruppo, le 14 competenze e la formazione, con rimandi alle schede S-30, S-31, S-57, S-58, S-59 e S-60 (03a).

### 3.7 Modulo sperimentale (07)

| ID | Strumento | Origine | Decisione | File | Etichette |
|---|---|---|---|---|---|
| S-61 | Integratori e sostanze | fonti: SL1-A T33-T39 | D-01: modulo sperimentale, solo informativo, rinvio obbligatorio al medico | 07 §2 | 🟨 SL1-A T33-T39 · 🟩 parziale (carenze; tirosina in stress estremo) · 🟥 contraddetto · 🟥 non canonico (r. 1420-1421, 5811-5812) |
| S-62 | Elettrostimolazione cranica e microcorrenti | fonti: SL1-A T40-T41; MAN schede 8-10, A.6; TM D11 | D-03: modulo sperimentale, solo su indicazione medica personale | 07 §2 | 🟨 SL1-A T40-T41 · 🟩 parziale (CES e ansia, prove deboli) · 🟥 contraddetto · 🟥 non canonico (r. 1420-1421, 2046-2047) |
| S-63 | Lavoro su memorie traumatiche e riprogrammazione | fonti: SL1-A T31; SL1-B T19; MAN A.12; SL1-C T9; DSS T21, T23 | D-06: modulo sperimentale, solo con un professionista della salute mentale abilitato presente | 07 §2 | 🟨 SL1-A T31, MAN A.12 · 🟩 parziale (imagery rescripting clinico) · 🟥 contraddetto · 🟥 non canonico (r. 1400-1406, 2046-2047) |
| S-64 | Training autogeno | fonti: SL1-A T03; MAN A.2 | D-09: modulo sperimentale | 07 §3 | 🟨 SL1-A T03 · 🟩 parziale · 🟥 contraddetto ("azzera l'ansia") · 🟥 non canonico (r. 1626-1632, 1807-1812) |
| S-65 | Battiti binaurali e Hemi-Sync | fonti: SL1-A T43; SL1-B T1, T21; MAN A.3, A.11; TM T1, T11, D7 | D-11: modulo sperimentale | 07 §3 | 🟨 SL1-A T43 · 🟩 parziale · 🟥 non verificato (B-C) · 🟥 non canonico (r. 2077-2080, 5811-5813) |
| S-66 | Autoconvalida di Altorfer e affermazioni | fonti: SL1-A T27; SL1-B T16; MAN A.10, PR7, T6.3; DSS T14-T16 | D-14: modulo sperimentale | 07 §3 | 🟨 SL1-A T27 · 🟩 parziale (rischio delle affermazioni) · 🟥 contraddetto · 🟥 non canonico (r. 1400-1406) |
| S-67 | Reincarnazione artificiale di Raikov (Borrowed Genius) | fonti: SL1-A T19; SL1-B T9, T15; MAN A.7; DSS T22, T24; TM T6 | D-16: modulo sperimentale; distinta da S-16 | 07 §3 | 🟨 SL1-A T19 · 🟩 parziale (gioco di ruolo) · 🟥 contraddetto · 🟥 non canonico (r. 1392, 5815) |
| S-68 | Biofeedback ed EEG come training | fonti: SL1-A T44; MAN scheda 14; SL1-C T5; DSS T10-T11 | D-17: modulo sperimentale | 07 §3 | 🟨 SL1-A T44 · 🟩 parziale (EMG clinico) · 🟥 contraddetto (colori QEEG) · 🟥 non canonico (r. 1420-1421, 2417-2419) |
| S-69 | Barocco lento a 60 BPM | fonti: SL1-A T10; SL1-B T8; MAN P9; TM D1-D3, M-3, T8 | D-18: modulo sperimentale, playlist separata dal concerto canonico | 07 §4 | 🟨 SL1-A T10 · 🟥 non verificato / contraddetto (C/D) · 🟥 non canonico (r. 1446-1448, 1460, 5805) |
| S-70 | Accordature planetarie, 136,10 Hz, Schumann, diapason | fonti: SL1-B T12; TM D10, M-6; MAN r. 69, 115, 155 | D-20: modulo sperimentale | 07 §4 | 🟨 SL1-B T12 · 🟩 solida (dato geofisico) · 🟥 contraddetto · n.t. |
| S-71 | Musica di tango o cinese nei concerti | nessuna fonte per i concerti (D-21); tango nel movimento: MAN A.9 | D-21: modulo sperimentale, variante dichiarata non canonica | 07 §4 | 🟩 parziale (dati di tempo) · n.t. (modifica del canone, r. 2923-2926, 5853) |
| S-72 | Musiche commerciali per l'apprendimento | fonti: SL1-A r. 75-77; SL1-B T22; MAN A.2, A.4, A.8; TM M2, M-5, D8, D9 | D-22: modulo sperimentale | 07 §4 | 🟨 SL1-A, MAN · 🟩 parziale (musica gradita in generale) · 🟥 non verificato · 🟥 non canonico (r. 1433-1435, 5811-5813) |
| S-73 | Cicli ritmici di 8 e 12 secondi, unità di 7-9 parole, sessioni di 13 minuti | fonti: SL1-A T13-T15; MAN A.5, PR2; SL1-B T6; TM T9, D1 | D-23: modulo sperimentale (nocciolo in S-52) | 07 §5 | 🟨 SL1-A T13-T15 · 🟩 parziale (pause motorie) · 🟥 contraddetto · 🟥 non canonico (r. 1830-1832, 4037-4060) |
| S-74 | Infinity Walk come test | fonti: DSS T3; SL1-C T3 | D-25: modulo sperimentale | 07 §5 | 🟨 DSS T3 · 🟥 contraddetto · n.t. (tensione con r. 2046-2047) |
| S-75 | Mappature diagnostiche | fonti: SL1-C T1-T5; DSS T7-T10; MAN scheda 5 | D-26: modulo sperimentale, autosservazione e non diagnosi | 07 §5 | 🟨 SL1-C T1-T5 · 🟥 non verificato (ciclo nasale) · 🟥 contraddetto · n.t. (contrasto con r. 2046-2047, 2417-2419) |
| S-76 | Contesto olfattivo | fonti: SL1-A T25 | D-29: modulo sperimentale | 07 §5 | 🟨 SL1-A T25 · 🟩 parziale · n.t. |

### 3.8 Note di decisione da rispettare nelle schede

- **S-03, S-69 (D-18).** Il concerto passivo usa il programma ufficiale (Lozanov 2005, cap. 31, r. 4118-4246). Il barocco lento a 60 BPM è una playlist separata, nel modulo sperimentale.
- **S-04, S-05 (D-27).** L'autore ha messo nel metodo la forma A e la forma C. La forma B proposta dall'analista (movimento libero) non è stata scelta e non compare. La forma C porta l'etichetta 🟥 Non canonico perché il movimento è sincronizzato e guidato dalla voce.
- **S-22 (D-05).** Screening delle controindicazioni obbligatorio (SIC-01). Il ciclo di 12 secondi legato alla lettura appartiene a S-73.
- **S-26, S-46 (D-15, INT-05).** Convivono. S-46 si chiama "routine", non "ancora".
- **S-27, S-28, S-29 (D-13).** Consenso informato obbligatorio, con i contenuti dichiarati ai partecipanti (SIC-02).
- **S-30, S-31 (D-24).** Specifica dell'autore: voce variabile, mai di comando; lo stesso passo proposto in tre qualità dinamiche. I tre toni fissi sono una variante opzionale **nel metodo**, non nel modulo sperimentale; il tono imperativo contrasta con il canone (r. 4089-4091).
- **S-32 (D-27b).** Proposta dell'autore: il docente canta la melodia e gli allievi contano i tempi, o viceversa. Il conteggio prodotto dagli allievi è attivo e non è induzione da voce monotona. Nella scheda si cita il segnale d'allarme canonico del conteggio costante (r. 1845-1849) e la risposta dell'autore.
- **S-35 (D-25).** Teoria emisferica nel testo con etichetta 🟥 Speculativo (contraddetto) (§1.5, regola 7). Uso come test: solo S-74.
- **S-36 (D-28).** "Flusso energetico" e "immunità" portano l'etichetta 🟥 Speculativo (contraddetto).
- **S-38, S-45 (D-12, INT-04).** Convivono. Nella scheda S-38 va la nota dell'autore: la prova mentale al posto della pratica fisica rende meno della pratica fisica (Driskell, Copper, Moran 1994).
- **S-16, S-67 (D-16).** Le nuove identità del canone sono nel metodo; la reincarnazione artificiale di Raikov è nel modulo sperimentale. Le due schede si distinguono in modo esplicito.
- **S-21, S-34, S-37, S-39, S-40, S-41 (D-29).** L'autore chiede esempi concreti di tango e di Liu Zi Jue per ciascuna tecnica.
- **S-42 (INT-01).** Richiamo a coppie o in gioco, mai come interrogazione individuale.
- **S-47 (INT-06).** Precauzioni per vertigini e disturbi vestibolari.
- **S-50 (INT-09).** Tango: tanghi cantati. Qigong: i suoni del Liu Zi Jue.
- **S-51 (INT-10).** Pensata per il corso universitario. Lo STAI-Y richiede una licenza d'uso.
- **S-61 (D-01).** Solo informativo: nessuna dose, nessuna istruzione d'uso, avvertenza di rischio esplicita per perossido di idrogeno, ozono per bocca e germanio, rinvio obbligatorio al medico.
- **S-62 (D-03).** Solo su indicazione medica personale; il docente non lo somministra.
- **S-63 (D-06).** Solo con un professionista della salute mentale abilitato presente.
- **S-71 (D-21).** Variante dichiarata non canonica. La musica di tango e del Liu Zi Jue resta nel metodo come contenuto delle discipline (04 §3).
- **S-75 (D-26).** Avvertenza obbligatoria: autosservazione, non diagnosi.

### 3.9 Procedure di sicurezza

Le procedure non sono strumenti didattici: si descrivono in 06 §2 e le schede le citano nel campo "Sicurezza".

| ID | Procedura | Base | Si applica a |
|---|---|---|---|
| SIC-01 | Screening delle controindicazioni | D-05; gruppi a rischio delle schede di `DECISIONI.md` | S-22 (obbligatorio). Le schede S-23, S-24, S-25, S-26, S-35, S-47 riportano i gruppi a rischio indicati in `DECISIONI.md` |
| SIC-02 | Consenso informato | D-13; D-10 (precauzioni); INT-10; `DECISIONI.md` §3.4 | S-27, S-28, S-29 (obbligatorio, contenuti dichiarati); S-24 e versione guidata di S-25 (precauzioni D-10); S-51 (raccolta di dati); modulo sperimentale (07 §1) |
| SIC-03 | Libertà di non partecipare e di interrompere | r. 1774-1775; INT-07 | tutti gli strumenti |
| SIC-04 | Consenso al contatto e scelta del partner | D-31 (precauzioni); INT-07 | lavoro in coppia, tango |
| SIC-05 | Il docente non è un terapeuta: dichiarazione e invio | r. 2046-2047, 3334-3336; D-31; D-06 | tutto il metodo; S-63 |
| SIC-06 | Correzione diretta degli errori pericolosi | INT-07 | eccezione a S-59 |
| SIC-07 | Condizioni della sala (spazio, pavimento, luci, volume) | INT-06, INT-07, D-25 (precauzioni); §6, punto 18 | S-02, S-03 (volume), S-05, S-35, S-47, tango |

### 3.10 Elementi senza ID

**Fuori dal metodo**, documentati in `ricerca/`: D-02 luci stroboscopiche AVE, D-04 dispositivi rotanti, D-07 generatori ELF, magneti e Bio-Battery. Nessun file del metodo li descrive; 07 §6 li elenca soltanto.

**Elementi delle fonti senza scheda propria** (`DECISIONI.md` §6). Seguono la scheda indicata lì: per esempio la "Danza dei canali semicircolari" va in S-47, l'esercizio Sì/No in S-22, lo specchio con le affermazioni in S-66. Quelli che non rimandano a una decisione (la centratura sul Tanden come immagine per l'asse, gli esercizi con la palla di Dalcroze) non entrano nei file del metodo finché l'autore non apre una scheda.

**Elementi non strumentali**

| Elemento | Dove si tratta |
|---|---|
| Decisione strutturale (metodo unico, etichette su ogni strumento) | 00 §1 |
| D-30 Linguaggio e neuromiti | 00 §1.5 e §5.2; vale per tutti i file |
| D-31 Predictive coding e metastabilità | 01 §3 (fondamento centrale, ipotesi teorica); 06 §1; AF, AU |
| D-32 Storia | 01 §6; AU |
| D-33 Lezione modello ricostruita sul ciclo canonico | 02 §5, con la scaletta di 2 ore delle fonti come confronto |
| Fondamenti, principi, leggi, cinque fattori indispensabili, mezzi, complesso di riserva | 01 §2 |
| Rifiuti espliciti di Lozanov (base dell'etichetta 🟥 Non canonico) | 01 §5 |
| Prestigio, aspettativa, amore non sentimentale; 14 competenze; formazione | 05; raccordo operativo in 03a §E |
| Parametri: gruppi fino a 20 persone (10 coppie), formati, Liu Zi Jue | 02 §4; applicazioni |

---

## 4. Mappa dei file

| Sigla | File | Tratta | Schede |
|---|---|---|---|
| 00 | `metodo/00-convenzioni.md` | etichette, ID, mappa, regole di scrittura, glossario | nessuna |
| 01 | `metodo/01-fondamenti-e-principi.md` | che cos'è il metodo; canone di Lozanov tradotto per la didattica corporea; predictive coding e metastabilità come fondamento centrale; come si incontrano; che cosa esclude il canone; storia | nessuna |
| 02 | `metodo/02-ciclo-didattico.md` | ciclo (preparazione e quattro fasi canoniche); regia della lezione; formati e gruppi con scalette; lezione modello | S-01–S-14 |
| 03a | `metodo/03a-catalogo-strumenti-stato-suggestione-voce.md` | gioco, ruolo e ambiente; stato; sonno e subliminale; voce e canto; comunicazione | S-15–S-34, S-57–S-60 |
| 03b | `metodo/03b-catalogo-strumenti-corpo-memoria-integrazioni.md` | corpo; memoria; integrazioni dalla ricerca (INT) | S-35–S-52 |
| 04 | `metodo/04-musica.md` | criteri; programma dei concerti; musica delle discipline e canzoni; strumenti musicali delle fonti; rimandi al modulo sperimentale | S-53–S-56 |
| 05 | `metodo/05-il-docente.md` | condizioni; posizione comunicativa; voce e corpo del docente; correzione; gruppo; che cosa il docente non fa; 14 competenze; formazione | nessuna (rimandi a S-30, S-31, S-57–S-60) |
| 06 | `metodo/06-sicurezza-ed-etica.md` | principi; procedure; screening e consenso; precauzioni per strumento; invio; privacy e ricerca | SIC-01–SIC-07 |
| 07 | `metodo/07-modulo-sperimentale.md` | regole del modulo; schede; elenco degli elementi fuori dal metodo | S-61–S-76 |
| AT | `applicazioni/tango.md` | ciclo, esempi e lezioni per il tango | nessuna |
| AQ | `applicazioni/qigong-liu-zi-jue.md` | ciclo, esempi e lezioni per il Liu Zi Jue | nessuna |
| AF | `applicazioni/formazione-insegnanti.md` | percorso per docenti | nessuna |
| AU | `applicazioni/corso-universitario.md` | syllabus, laboratori, valutazione | nessuna |

### 4.1 Sezioni dei file

Le sezioni indicate qui sono quelle citate nella colonna "File" della sezione 3. Chi scrive può aggiungere sottosezioni, non spostare le schede.

- **01.** §1 Che cos'è il Superapprendimento · §2 Il canone di Lozanov tradotto per la didattica corporea · §3 Predictive coding e metastabilità (fondamento centrale, ipotesi teorica) · §4 Due fondamenti, un metodo · §5 Che cosa esclude il canone · §6 Storia essenziale
- **02.** §1 Il ciclo · §2 Le fasi (S-01–S-07) · §3 Regia della lezione (S-08–S-14) · §4 Formati e gruppi (lezione settimanale, workshop intensivo, corso universitario; fino a 20 persone) · §5 Lezione modello (D-33)
- **03a.** §A Gioco, ruolo e ambiente (S-15–S-21) · §B Stato (S-22–S-26) · §C Sonno e subliminale (S-27–S-29) · §D Voce e canto (S-30–S-34) · §E Comunicazione (S-57–S-60; raccordo sul prestigio)
- **03b.** §A Corpo (S-35–S-38) · §B Memoria (S-39–S-41) · §C Integrazioni dalla ricerca (S-42–S-52)
- **04.** §1 Criteri · §2 Programma dei concerti (cap. 31) · §3 Musica delle discipline e canzoni (tango, Liu Zi Jue) · §4 Strumenti musicali delle fonti (S-53–S-56) · §5 Rimandi al modulo sperimentale (S-69–S-72)
- **05.** §1 Condizioni (prestigio, aspettativa, amore) · §2 Posizione comunicativa · §3 Voce e corpo del docente · §4 Correzione · §5 Il gruppo fino a 20 · §6 Che cosa il docente non fa · §7 Le 14 competenze · §8 Formazione e certificazione
- **06.** §1 Principi (il docente non è un terapeuta; sicurezza percepita, S-48) · §2 Procedure (SIC-01–SIC-07) · §3 Precauzioni per strumento · §4 Segnali d'allarme e invio · §5 Privacy e ricerca universitaria
- **07.** §1 Regole del modulo · §2 Salute e clinica (S-61–S-63) · §3 Stato e suggestione (S-64–S-68) · §4 Musica (S-69–S-72) · §5 Formato e diagnosi (S-73–S-76) · §6 Fuori dal metodo
- **AT, AQ** (struttura indicativa). §1 Parametri e sala · §2 Gioco-progetto · §3 Il ciclo applicato · §4 Lezione settimanale · §5 Workshop intensivo · §6 Indice degli esempi per strumento. AQ apre con la sequenza Health Qigong del Liu Zi Jue e la distinzione tra respiro come contenuto e come mezzo.
- **AF, AU** (struttura indicativa). AF: destinatari e formato; contenuti; pratica delle competenze; che cosa resta alla formazione pratica. AU: syllabus; fondamenti; laboratori; valutazione (S-42, S-51); storia.

### 4.2 Chi tratta cosa

| Tema | Scheda o testo principale | Altri file (solo rimandi o applicazioni) |
|---|---|---|
| Concerti | procedura in 02 (S-02–S-05) | musica in 04 §2; esempi in AT, AQ |
| Canzoni e canto | S-33, S-34 in 03a; S-50 in 03b | repertorio in 04 §3 |
| Intonazione | S-30, S-31 in 03a | 05 §3 (competenze 2 e 5) |
| Comunicazione del docente | S-57–S-60 in 03a §E | 05 §2-§4 |
| Prestigio e aspettativa | 05 §1 | raccordo operativo in 03a §E |
| Sicurezza percepita | S-48 in 03b | principio in 06 §1 |
| Valutazione | S-51 in 03b | AU |
| Predictive coding | 01 §3 | 06 §1; AF, AU lo riprendono senza riscriverlo |
| Storia | 01 §6 | AU |
| Lezione modello | 02 §5 | AT, AQ la declinano |
| Precauzioni | campo "Precauzioni" di ogni scheda | 06 §3 le raccoglie in tabella |

**Applicazioni.** Non contengono schede nuove. Gli esempi brevi stanno nelle schede; le applicazioni li sviluppano in sequenze di lezione, senza cambiare procedura né etichette. Gli strumenti del modulo sperimentale non compaiono nelle scalette delle lezioni: si propongono a parte, come prevede 07 §1.

---

## 5. Regole di scrittura

### 5.1 Lingua e forma

- Italiano chiaro e diretto, frasi brevi, registro operativo.
- Niente enfasi pubblicitaria ("rivoluzionario", "potente", "straordinario") e niente promesse di risultati.
- Niente frasi di riempimento ("è importante sottolineare", "in conclusione", "come abbiamo visto").
- Titoli brevi. Tabelle per confronti e riepiloghi. Procedure numerate con i tempi.
- Niente emoji, con un'unica eccezione: i quadrati colorati delle etichette (🟦 🟨 🟩 🟥), sempre seguiti dal nome dell'etichetta.
- Tango: termini in spagnolo, senza corsivo (§7.3). Qigong: pinyin senza toni nel testo; caratteri e toni nel glossario.
- Citazioni di Lozanov in inglese, tra virgolette, con la riga.

### 5.2 Spiegazioni (D-30)

- Nel testo solo spiegazioni corrette, con i riferimenti dei file di verifica. Testi già pronti: VNF §4.1, VPS §6, VTN §6.
- Onde alfa, emisferi, ossigeno al cervello, alte frequenze, "ricarica" della corteccia, "subconscio", "4% del potenziale": solo nei riquadri.
- "Ipermnesia", "riserve", "norma sociale suggestiva", "paraconscio" sono termini del canone: si usano con lo statuto "Tesi del fondatore" (🟦 · 🟥 non verificato).
- Nessuna percentuale sul "potenziale". "Emisfero" mai come stile cognitivo ("cervello destro", "persona a cervello sinistro"); unica eccezione la teoria di Sunbeck in S-35 (D-25).
- Non si usano "supermemoria" né altri composti con "super" riferiti a memoria o capacità; il termine canonico è ipermnesia (r. 1504-1507). Il nome del metodo è scelta dell'autore.
- Ogni dato numerico ha la sua fonte.

### 5.3 Predictive coding (D-31)

- È fondamento centrale accanto a Lozanov e porta sempre lo statuto "Ipotesi teorica" (§1.4).
- Riferimenti: quelli primari dei file di verifica (VNF H1, H4, H6, H8, H9, H11), tra cui Kotler, Mannino, Fox, Friston 2026 (articolo d'opinione), Ehlers e Clark 2000, Kube et al. 2020, Linson e Friston 2019, Sarasso et al. 2022, Friston 2010. Niente blog, social o newsletter (VNF H5).
- Correzioni obbligatorie: muscoli e fasce sono riccamente innervati (VNF H7); l'EMDR è una psicoterapia; niente "tutte le terapie efficaci" (D-31).
- Il riferimento sulla C-PTSD (VNF H2) non si usa finché non è identificato.
- Nessuna promessa terapeutica sul trauma. Il corso non è una terapia (SIC-05).
- La traduzione operativa è S-48 Sicurezza percepita.

### 5.4 Storia (D-32)

- Storia senza critiche, in tutti i file, compreso il corso universitario. Le critiche restano in `ricerca/`.
- I risultati di Lozanov sono "dichiarati dall'autore" (§1.4). Riguardano i corsi descritti nel libro, soprattutto di lingua, e non si presentano come risultati attesi per tango, Qigong o corso universitario (modello §8.4).
- UNESCO 1978: raccomandazioni di un gruppo di esperti (riunione di Sofia, dicembre 1978; r. 5651-5745).
- Baba Vanga non compare.
- Nessuna narrazione in prima persona al posto di Lozanov.

### 5.5 Riferimenti e citazioni

- Solo riferimenti presenti nei file di ricerca (`ricerca/verifica-*.md`, `ricerca/modello-canonico-lozanov.md`, `DECISIONI.md`). Nessun riferimento nuovo.
- Forma breve nel testo, come nei file di verifica: Autore anno, *Rivista* volume:pagine.
- Marcatori: "(da ricontrollare)" quando il file di verifica lo segnala così; "[fuori dai file di verifica, da ricontrollare]" per Wulf 2013, Magill e Hall 1990, Engelkamp 1998, Schmidt e Lee (`DECISIONI.md` §3.6); "[da verificare]" per ogni dubbio di chi scrive.
- Lozanov: "Lozanov 2005, r. NNNN" la prima volta in un file, poi "r. NNNN". Le righe sono quelle di `fonti/testo/Lozanov_2005_Suggestopaedia_Desuggestive_Teaching.txt`. Il modello canonico si cita come "modello §5.5" o "modello r. NNN".
- Brani musicali: titoli del programma canonico come nel modello §5.7; brani di tango scelti dal docente, con il tempo misurato (VPS M9). Un titolo o un'esecuzione su cui chi scrive ha dubbi porta "[da verificare]".
- Prima di pubblicare, ogni riferimento va ricontrollato sull'originale (`DECISIONI.md` §3.6).

| Sigla | File |
|---|---|
| SL1-A, SL1-B, SL1-C | `ricerca/estrazioni/superlearning1-A.md`, `-B.md`, `-C.md` |
| MAN | `ricerca/estrazioni/manuale.md` |
| DSS | `ricerca/estrazioni/didattica-super-suggesto.md` |
| TM | `ricerca/estrazioni/tango-musica.md` (T = Tango-Mind, D = didattica, M = musiche) |
| TLT | `ricerca/estrazioni/teoria-lozanov-trauma.md` (R = ricerca globale su Lozanov, T = trauma e predictive coding) |
| L05-1, L05-2, L05-3 | `ricerca/estrazioni/lozanov2005-parte1.md`, `-parte2.md`, `-parte3.md` |
| modello | `ricerca/modello-canonico-lozanov.md` |
| VNF | `ricerca/verifica-neuro-fisiologia.md` |
| VTN | `ricerca/verifica-tecnologie-nutrizione-clinica.md` |
| VPS | `ricerca/verifica-pedagogia-storia-musica.md` |
| HQA | Standard Health Qigong del Liu Zi Jue (Chinese Health Qigong Association, 2003; ed. inglese Foreign Languages Press 2007), come descritto nel progetto QIGONG dell'autore |

### 5.6 Sicurezza ed etica

- Il docente non è un terapeuta (r. 2046-2047, 3334-3336): nessuna diagnosi, nessun trattamento, nessuna promessa di salute. Vale anche per il Liu Zi Jue: le corrispondenze con gli organi si presentano come 🟨 Tradizione.
- Screening delle controindicazioni (SIC-01) obbligatorio per S-22. Consenso informato (SIC-02) obbligatorio per S-27, S-28, S-29.
- Modulo sperimentale: separato dalla lezione, facoltativo, dichiarato non lozanoviano, con precauzioni e, se possibile, una misura prima e dopo (`DECISIONI.md` §3.4, opzione 2).

### 5.7 Precauzioni di `DECISIONI.md`

Ogni scheda di `DECISIONI.md` ha il campo "Precauzioni obbligatorie se l'autore decide di includerlo".
- Per gli strumenti inclusi (nel metodo o nel modulo sperimentale) la scheda dello strumento riporta tutte queste precauzioni nel campo "Precauzioni".
- Se una precauzione cambierebbe una procedura che l'autore ha voluto "come nelle fonti", la procedura resta quella delle fonti e la precauzione si riporta con la dicitura **[da chiarire con l'autore]**. I casi noti sono elencati in §6.2.

---

## 6. Punti lasciati all'autore

### 6.1 Domande aperte (`DECISIONI.md` §7)

| N. | Tema | Stato | Come lo trattano i file |
|---|---|---|---|
| 1 | Nome e certificazione | Deciso: "Superapprendimento, metodo fondato sulla Desuggestopedia di G. Lozanov"; autore certificato | 01 §1; 05 §8 |
| 2 | Numero di allievi | Deciso: fino a 20 persone (10 coppie nel tango) | 02 §4; 05 §5; AT, AQ |
| 3 | Calendario giorno per giorno | Aperto | 02 §4 e applicazioni propongono calendari come proposta |
| 4 | Corsi adattivi | Aperto: il libro non ne descrive il contenuto | S-13 riporta il canone e la domanda |
| 5 | Quarta fase dentro ogni ciclo | Aperto | S-07 come proposta |
| 6 | Secondo livello | Aperto | non trattato |
| 7 | Concerto nelle discipline corporee | In parte deciso: D-27 (forme A e C), D-21 (musica delle discipline nei concerti solo nel modulo sperimentale). Aperto: che cosa sia il "testo" del concerto | 02 §2; 04 §2 |
| 8 | Qigong: confine tra contenuto e induzione (respiro, immagini, occhi chiusi, conteggi) | Aperto | 02 §2 e AQ come proposta |
| 9 | Volume di materiale nel movimento | Aperto | 02 §3; AT, AQ come proposta |
| 10 | Correzione indiretta e sicurezza | Deciso con INT-07: gli errori pericolosi si correggono subito e in modo diretto | SIC-06 |
| 11 | Valutazione e voto nel corso universitario | Aperto (INT-01 e INT-10 approvate) | 02 §4; AU come proposta |
| 12 | Pratica a casa | Aperto (S-12 è il canone) | S-12 e applicazioni come proposta |
| 13 | Contatto, ruoli, cambi di coppia | In parte deciso con INT-07 (libertà di scelta, nessun cambio imposto) | SIC-04; 05 §5; AT |
| 14 | Sezione aurea e durate | Aperto | S-10 come proposta |
| 15 | Gioco-progetto per contesto | Aperto | S-15 e applicazioni come proposta |
| 16 | Lingua madre, schede illustrate e loro ritiro | Aperto | S-04 come proposta |
| 17 | Che cosa sta nel manuale e che cosa nella formazione pratica | Aperto | 05 §8; AF |
| 18 | Aula, luci, volume | Aperto | SIC-07 |
| 19 | Procedura di invio | Aperto; i canali di invio sono obbligatori (precauzioni D-31) | SIC-05; 06 §4 come proposta |

### 6.2 Precauzioni in tensione con "come nelle fonti"

Casi in cui una precauzione di `DECISIONI.md` cambierebbe la procedura delle fonti scelta dall'autore. Nella scheda la procedura resta quella delle fonti e la precauzione si scrive con **[da chiarire con l'autore]** (§5.7).

| Strumento | Precauzione di `DECISIONI.md` | Elemento delle fonti in tensione |
|---|---|---|
| S-22 (D-05) | niente apnee forzate né conteggi rigidi; da seduti o con un appoggio; mai la parola da memorizzare durante una ritenzione | sequenze con apnea; 8-4-8-4 e Aquila in piedi; parola pronunciata nella ritenzione del 2/4/2 |
| S-23 (D-08) | nessuna sensazione dettata; niente rotazioni complete del collo; non sdraiati in sala di ballo | "onda di calore"; rotazioni complete del collo (SL1-A); posizione sdraiata |
| S-24 (D-10) | conduttore con formazione clinica | conduzione del docente in gruppo |
| S-25 (D-10) | occhi aperti, nessuna fonte luminosa | fissare una lampadina e osservare i fosfeni a occhi chiusi |
| S-26 (D-15) | nessuna rievocazione a occhi chiusi di ricordi personali | rievocare "il momento più radioso della propria vita" |
| S-27, S-28, S-29 (D-13) | nessun messaggio subliminale; nessun audio con suggestioni nel sonno; nessuna formula di perdono verso persone reali | la pratica stessa; la "detersione" con il perdono (SL1-A T28). L'autore ha indicato il consenso informato |
| S-38 (D-12) | mai al posto della pratica fisica | il caso Drapeau sostituisce gli allenamenti fisici. L'autore ha indicato una nota (§3.8) |
| S-05 (D-27) | movimento libero, non sincronizzato da comandi vocali | allievi in sincrono con il docente che declama |
| S-35 (D-25) | velocità lenta; appoggi di tallone morbidi; doppio compito solo da soli e in spazio ampio | passo "cadenzato" e "deciso"; appoggi di tallone "massicci"; recitazione di dati durante gli ochos in coppia (MAN A.9) |

---

## 7. Glossario

Le righe sono di Lozanov 2005. Definizioni più ampie nel modello §10.

### 7.1 Termini del canone

| Termine | Definizione | Righe |
|---|---|---|
| Suggestopedia | Sistema di insegnamento che usa "all the possibilities tender suggestion can offer"; nome originale del metodo (1966) | 445-447, 913-916 |
| Desuggestopedia | Sviluppo successivo della Suggestopedia, con più libertà interiore e comunicazione paritaria. Prefisso "de-", non "anti-" | 265-271 |
| Desuggestologia | "a science of spontaneous, not forced release from inhibiting, limiting and impairing influences" | 317-318 |
| Desuggestione | Liberazione dai limiti che la norma sociale suggerisce sulle proprie capacità di apprendere. È l'opposto della "riprogrammazione": il metodo de-programma | 268-271, 1400-1406, 2745-2747 |
| Suggestione | Componente costante di ogni comunicazione: gli stimoli non specifici che rafforzano o indeboliscono le parole | 375-390 |
| Suggestione tenera (comunicativa) | Comunicazione senza comandi e senza obbedienza automatica: "to suggest = to offer, to propose" | 410-423, 1774-1775 |
| Quattro tipi di comunicazione | 1) libera; 2) diretta non manipolativa, quella del metodo; 3) suggestione clinica; 4) ipnosi | 1767-1785 |
| Suggestione clinica | Suggestione con funzione di comando, che condiziona e subordina; esclusa dall'insegnamento | 392-401, 1634-1638 |
| Ipnosi | "manipulative communication accompanied by an almost complete loss of self-control"; esclusa | 1392, 1778-1779 |
| Norma sociale suggestiva | Rete di limiti appresi sulle proprie capacità. Tesi del fondatore | 2752-2800 |
| Barriere antisuggestive | Autoprotezione psichica presente in tutti: emotiva, logica (critico-logica), etica. Non si forzano: "should not be stimulated" | 2802-2845 |
| Riserve | Capacità "unmanifested but genetically predetermined", che operano soprattutto nel paraconscio. Tesi del fondatore | 575-582 |
| Complesso di riserva | Le cinque caratteristiche obbligatorie del risultato: riserve su più piani, assenza di fatica, piacere, effetto educativo, effetto psicoprofilattico | 517-573 |
| Ipermnesia | Memoria a lungo termine superiore, con sette leggi proprie; termine canonico al posto di "supermemoria". Tesi del fondatore. In psicologia sperimentale il termine indica anche un effetto modesto di laboratorio (VPS T1) | 529-548, 1504-1507 |
| Ipercreatività | Produttività creativa elevata, suggerita o autosuggerita | 550-559 |
| Paraconscio | Tutto ciò che in un dato momento è fuori dal campo della coscienza. Non è l'inconscio freudiano | 2195-2227, 1015 |
| Percezioni periferiche | Stimoli sopra soglia che escono dal fuoco dell'attenzione; controllabili, lasciano libertà di scelta. Non sono stimoli subliminali | 2232-2264 |
| Doppio piano | Piano primario (contenuto cosciente) e piano secondario (stimoli non specifici, dettagli) nel comportamento di chi comunica | 2279-2282, 3129-3138 |
| Mezzi comunicativi non specifici | Doppio piano, intonazione e ritmo; credibilità e prestigio, infantilizzazione, pseudo-passività | 2277-2296 |
| Infantilizzazione | "increased trust and receptivity while retaining a critical attitude and self-control": fiducia senza perdita del senso critico | 2289-2293 |
| Pseudo-passività concertistica | Lo stato degli allievi nel concerto passivo: "a calm and relaxed, undisturbed and controlled activity" | 2291-2295, 4023-4024 |
| Calma concentrativa gioiosa e spontanea | Primo principio: rilassamento "cheerful, genuine and highly stimulating", ottenuto con giochi, umorismo e materiali stimolanti | 2931, 2990-2993 |
| Globale-parziale | Secondo principio: la parte nel tutto e il tutto nella parte, con struttura. Non è il metodo per parti né l'olismo | 2932-2933, 2995-3077 |
| Set-up desuggestivo | Terzo principio: disposizione verso le riserve creata dal docente senza alcuna pressione | 2934-2935, 3079-3091 |
| Tre fondamenti | Unità di conscio e paraconscio; ogni stimolo è associato e codificato; dominano gli stati mentali, non gli stimoli | 2871-2880 |
| Cinque fattori indispensabili | Volume ampio; struttura globale-parziale legata alla sezione aurea; docente prestigioso e credibile; aspettativa vera; amore non sentimentale con giochi, canti e arte di tipo classico | 5842-5854 |
| Sette differenze | Ciò che distingue il metodo da ogni altro (sezione aurea, personalità multipla, apprendimento simultaneo di parte e tutto, ipermnesia, suggestione morbida, amore, docente competente) | 594-797 |
| Personalità multipla | Variazioni continue dello stato della persona intera, corpo compreso; si cerca la variante più adatta all'apprendimento | 2409-2432, 2658-2702 |
| Metodologia oscillante | Oscillazione di intonazione e comportamento del docente, contro la monotonia che può indurre ipnosi | 2672-2680, 2740-2741 |
| Orchestrazione | Organizzazione dei mezzi (musica, canti, giochi, prestigio): "only necessary orchestration" rispetto all'amore | 5856-5858 |
| Introduzione | Prima fase: gioco-progetto con presentazione artistica del materiale; sostituisce la "decifrazione" | 478-482, 3936-3998 |
| Concerto attivo | Lettura espressiva del materiale su un'opera classica intera; allievi con testo e traduzione | 4021-4099 |
| Concerto passivo | Lettura colloquiale su un'opera pre-classica intera, a volume da concerto; allievi in ascolto | 4100-4115 |
| Elaborazione | Fase di attivazione nei giorni dopo il concerto: primaria (primo giorno) e secondaria (secondo giorno) | 4248-4369 |
| Performance | Quarta fase: produzione autonoma degli allievi; giorno finale di consolidamento e festa | 3932-3935, 4463-4468 |
| Gioco-progetto | Progetto comune, di solito un film, che dà senso alle attività | 3943-3949, 4417-4420 |
| Nuove identità | Nome, nazionalità, professione e biografia nuovi scelti dall'allievo dentro il gioco-progetto; l'errore appartiene al personaggio | 759-762, 2704-2707 |
| Sistema della risata, sistema delle canzoni | Risata e canti pianificati come "system within the system" | 2715-2726 |
| Estetica totale | "the aesthetics is a teaching, healing and personality harmonising method" | 3924-3928 |
| Sezione aurea | Rapporto di circa 0,618 applicato a durate, intensità e dinamica | 801-908 |
| Corsi adattivi | Introdotti contro la "dissociazione negativa" tra rendimento in corso e fuori; contenuto non descritto | 2460-2469 |
| Iceberg linguistico, conoscenza passiva | Il materiale acquisito senza attenzione focale è più ampio di quello cosciente; la conoscenza passiva è accolta "as warmly as active" | 3266-3320 |
| Ricordo spontaneo ritardato | Il giorno dopo, senza ripasso, si ricorda più materiale. Tesi del fondatore | 3209-3213 |
| Didattogenia | Danno o blocco causato dal modo di insegnare; nella forma di massa, "nevrosi scolastica" | 3780-3782, 3847-3852 |
| Gerarchia delle abitudini | Costruire abitudini elementari da smontare a ogni livello; rifiutata | 3860-3872 |
| Sovracrescita associativa | Lo stimolo si riveste di associazioni ed emozioni e così entra nella memoria a lungo termine | 2900-2913 |
| Marcatori di sincerità | Segni involontari, come il sorriso vero, che rendono percepibile la finzione del docente | 2381-2388 |
| Placebo | Fattore non specifico di ogni comunicazione credibile; il docente lo riconosce e lo usa o lo evita, non lo usa come spiegazione | 2121-2189, 5766 |

### 7.2 Termini del metodo

| Termine | Definizione |
|---|---|
| Superapprendimento | Nome del metodo scelto dall'autore: metodo didattico fondato sulla Desuggestopedia di G. Lozanov, con integrazioni dichiarate. Non coincide con il "Superlearning" commerciale (Ostrander e Schroeder 1979), che Lozanov respinge per nome (r. 1456-1458) |
| Canone | Ciò che Lozanov afferma in Lozanov 2005, come ricostruito nel modello |
| Fonti | I documenti in `fonti/` diversi dal libro di Lozanov: Superlearning, manuale, Tango-Mind, materiali didattici, ricerca globale, articolo sul trauma |
| Strumento | Pratica o procedura del metodo con ID S-nn e scheda propria |
| Procedura di sicurezza | Regola con ID SIC-nn, descritta in 06 |
| Scheda | Descrizione di uno strumento secondo lo schema della sezione 2 |
| Etichetta | Segno colorato che dice l'origine o lo statuto di un elemento: 🟦 Fonte classica, 🟨 Tradizione, 🟩 Evidenza, 🟥 Speculativo, 🟥 Non canonico (§1.1) |
| Statuto | Tesi del fondatore, Ipotesi teorica, Dichiarato dall'autore, Proposta da confermare (§1.4) |
| Nel metodo come nelle fonti | Decisione: la pratica si descrive con la procedura delle fonti; la spiegazione corretta sta nel testo, quella delle fonti nel riquadro (D-30) |
| Variante opzionale | Forma alternativa ammessa dall'autore accanto a quella principale (D-24) |
| Modulo sperimentale | Parte separata dalla lezione, facoltativa, dichiarata non lozanoviana, con precauzioni e, se possibile, una misura prima e dopo (`DECISIONI.md` §3.4). Raccolto in 07 |
| Fuori dal metodo | Elemento documentato solo in `ricerca/` |
| Integrazione (INT) | Pratica proposta dalla ricerca attuale e approvata dall'autore (`DECISIONI.md`, blocco H) |
| Spiegazione corretta | Spiegazione coerente con le conoscenze attuali, con riferimenti dei file di verifica |
| Riquadro "Cosa dicono le fonti" | Spazio per le spiegazioni e le promesse delle fonti, con la loro etichetta (§1.5) |
| Nocciolo | Parte di una pratica che può funzionare per ragioni diverse da quelle dichiarate dalle fonti |
| Predictive coding (elaborazione predittiva) | Ipotesi teorica: il cervello genera previsioni su ciò che percepisce e le aggiorna con gli errori di predizione, pesati per la loro precisione. Fondamento centrale accanto a Lozanov (D-31) |
| Errore di predizione | Differenza tra ciò che il sistema prevede e ciò che riceve |
| Precisione | Peso, cioè affidabilità, attribuito a una previsione o a un errore di predizione |
| Aspettative di pericolo ("danger priors") | Previsioni di minaccia. Nel modello di Kotler et al. 2026 il trauma comporta un eccesso di precisione di queste aspettative (VNF H6) |
| Metastabilità | Capacità delle reti cerebrali di passare in modo flessibile da uno stato all'altro senza fissarsi in uno; ancora poco misurata nei campioni clinici (VNF H6, H9) |
| Free energy | Concetto di Friston: limite superiore della "sorpresa"; in divulgazione si approssima agli errori di predizione pesati per la precisione, ma in generale non è la stessa cosa (VNF H8) |
| Contesto sicuro e sfidante | Condizione indicata dalla fonte sul trauma e ripresa da INT-07: sicurezza senza rinuncia alla sfida |
| Sicurezza percepita | S-48: progettare lezione e sala perché nessuno si senta minacciato fisicamente, socialmente o nel contatto. Principio di progettazione, non terapia |
| Respiro come contenuto, respiro come mezzo | Distinzione del modello (§9.5): il respiro insegnato come parte della disciplina (Liu Zi Jue) è contenuto; il respiro usato per indurre uno stato in cui "passare" altro materiale è un mezzo, che il canone esclude |
| Distanziamento, richiamo attivo | S-42: riprendere il materiale a intervalli crescenti; provare a ricordare o eseguire senza modello |
| Focus attentivo esterno | S-43: indicazioni rivolte all'effetto del movimento (pavimento, partner, spazio) invece che alle parti del corpo |
| Pratica variata | S-44: variare condizioni e ordine della pratica invece di ripetere a blocchi |
| Imagery autogestita | S-45: ripasso mentale scelto dall'allievo, in aggiunta alla pratica fisica |
| Routine pre-esecuzione | S-46: breve sequenza costante scelta dall'allievo prima di un gesto impegnativo |
| Esercizi vestibolo-oculari | S-47: stabilizzare lo sguardo durante movimenti della testa; "spotting" nei giri |
| Effetto di esecuzione | S-49: eseguire l'azione indicata da una parola la fa ricordare meglio (enactment) |
| Pause brevi | S-52: pochi secondi di pausa tra blocchi di pratica motoria |
| Misure validate | S-51: test prima, dopo e a distanza; scale d'ansia validate (STAI-Y, con licenza); gruppo di confronto |
| Screening delle controindicazioni | SIC-01: questionario prima di uno strumento con gruppi a rischio |
| Consenso informato | SIC-02: adesione scritta dopo aver ricevuto i contenuti e i rischi |
| Concerto dimostrato | S-04: il docente esegue l'intero materiale nuovo su un'opera classica intera, nominando figure e immagini; gli allievi osservano |
| Concerto in movimento | S-05: il docente declama ballando, gli allievi si muovono in sincrono (forma delle fonti) |
| Conteggio a ruoli alternati | S-32: melodia e conteggio dei tempi insieme; il docente canta e gli allievi contano, o viceversa |
| Libretto | Scheda illustrata della sequenza data agli allievi nel concerto delle discipline corporee, al posto del testo con traduzione (modello §9.3) |
| Ciclo | La preparazione facoltativa e le quattro fasi canoniche (introduzione, concerti, elaborazione, performance) su più incontri (D-33) |
| Formati | Lezione settimanale, workshop intensivo, corso universitario (parametri dell'autore) |

### 7.3 Termini delle discipline

**Tango.** Grafia spagnola, senza corsivo. I termini e le orchestre sono 🟨 Tradizione della disciplina.

| Termine | Uso nel metodo |
|---|---|
| abrazo | L'abbraccio della coppia; nel testo è ammesso anche "abbraccio" |
| caminata | La camminata del tango |
| ocho (pl. ochos), adelante, atrás | Figura in cui chi segue disegna un otto con pivot sull'asse, avanti o indietro |
| giro (pl. giros), molinete | Figura circolare intorno a chi guida; molinete è la sequenza di passi avanti, laterali e indietro di chi segue |
| sacada (pl. sacadas) | Passo che entra nello spazio del partner e ne sposta la gamba |
| cadencia | Cambio di peso ritmico quasi sul posto |
| pausa | Fermata musicale della coppia, con l'abrazo mantenuto |
| musicalità | Rapporto tra movimento e musica (pulsazione, frase, melodia) |
| compás | La pulsazione del tango |
| guida, seguito | I due ruoli della coppia |
| tanda, cortina | Serie di brani della stessa orchestra in milonga; breve brano non di tango tra due tande |
| ronda | Circolazione delle coppie in pista |
| cabeceo | Invito al ballo con lo sguardo |
| milonga | Il luogo e l'evento di ballo; anche il genere musicale |
| vals | Il tango vals |
| letra | Il testo cantato di un tango |
| Orchestre | Carlos Di Sarli, Juan D'Arienzo, Aníbal Troilo, Osvaldo Pugliese, Rodolfo Biagi, Francisco Canaro, Osvaldo Fresedo |

**Qigong: Liu Zi Jue.** Sequenza della Chinese Health Qigong Association (standard del 2003; ed. inglese Foreign Languages Press 2007). Riferimento operativo: progetto QIGONG (https://andrea76b.github.io/QIGONG/), con la traccia ufficiale HQA di circa 15 minuti; i diritti d'uso dell'audio vanno verificati prima di pubblicare. Nel testo si usa il pinyin senza toni. La sequenza è 🟨 Tradizione (standard HQA).

| Termine | Caratteri e pinyin | Uso nel metodo |
|---|---|---|
| Liu Zi Jue | 六字诀 liù zì jué | "Formula dei sei caratteri": sei suoni espirati, eseguiti con movimenti |
| Preparazione | 预备势 yùbèi shì | In piedi, piedi paralleli alla larghezza delle spalle, sguardo avanti e in basso, respiro naturale |
| Apertura | 起势 qǐ shì | I palmi salgono al petto, premono verso il basso, spingono in avanti e tornano davanti all'ombelico; poi quiete |
| Xu | 嘘 xū | Primo suono; tradizione: fegato |
| He | 呵 hē | Secondo suono; tradizione: cuore |
| Hu | 呼 hū | Terzo suono; tradizione: milza |
| Si | 呬 sī | Quarto suono; tradizione: polmone |
| Chui | 吹 chuī | Quinto suono; tradizione: rene |
| Xi | 嘻 xī | Sesto suono; tradizione: triplice riscaldatore (san jiao) |
| Chiusura | 收势 shōu shì | Mani sull'ombelico, quiete, massaggio dell'addome (sei giri per senso), mani lungo i fianchi |
| Song, fangsong | 松, 放松 | Rilassamento attivo, contenuto della disciplina (nocciolo di D-08) |
| Health Qigong (HQA) | 健身气功 jiànshēn qìgōng | Il sistema di Qigong standardizzato della Chinese Health Qigong Association, di cui fa parte il Liu Zi Jue |

Ordine: preparazione, apertura, Xu, He, Hu, Si, Chui, Xi, chiusura; ogni suono si ripete sei volte. Le corrispondenze con gli organi appartengono alla teoria tradizionale: si presentano come 🟨 Tradizione, senza promesse di salute (SIC-05).
