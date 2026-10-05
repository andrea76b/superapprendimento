# Superapprendimento

**In breve.** Superapprendimento è un metodo didattico fondato sulla Desuggestopedia di Georgi Lozanov e integrato, in modo dichiarato, con la ricerca attuale sull'apprendimento. Nasce dai corsi di tango argentino dell'autore e si applica al Qigong (Liu Zi Jue), alla formazione degli insegnanti e a un corso universitario. L'autore è docente certificato nella linea di Lozanov. Questo repository contiene le fonti, la ricerca che le ha verificate, le 44 decisioni dell'autore, il metodo in nove file e le quattro applicazioni. Ogni strumento porta un'etichetta a colori che dice da dove viene e che cosa ne sappiamo.

## Fondamenti

- **Il canone di Lozanov.** La base è l'ultima sintesi del fondatore: G. Lozanov, *Suggestopaedia – Desuggestive Teaching*, Vienna 2005, ricostruita in `ricerca/modello-canonico-lozanov.md`. Ne vengono il ciclo in quattro fasi (introduzione, concerti, elaborazione, performance), la suggestione intesa come "to offer, to propose", il gioco, il canto, l'arte, le percezioni periferiche e la correzione indiretta.
- **Predictive coding e metastabilità.** È il secondo fondamento, presentato come ipotesi teorica (Kotler, Mannino, Fox, Friston 2026, articolo d'opinione). Un contesto sicuro e insieme sfidante fornisce al sistema nervoso dati coerenti con l'assenza di minaccia. Nel metodo diventa un principio di progettazione della lezione (sicurezza percepita). Non è una terapia e non promette effetti sul trauma.
- **Ricerca attuale.** Undici integrazioni approvate dall'autore: distanziamento e richiamo attivo, focus attentivo esterno, pratica variata, imagery autogestita, routine pre-esecuzione, esercizi vestibolo-oculari, sicurezza percepita, gesto ed effetto di esecuzione, canto e coro, misure validate, pause brevi nella pratica motoria.

I due fondamenti e come si incontrano sono in `metodo/01-fondamenti-e-principi.md`.

## Un metodo, etichette a colori

Il metodo è unico. Ogni strumento, pratica o affermazione porta una o più etichette, combinate quando aspetti diversi hanno statuti diversi. Il sistema è lo stesso del progetto QIGONG dell'autore (https://andrea76b.github.io/QIGONG/).

| Etichetta | Che cosa indica | Accanto si scrive |
|---|---|---|
| 🟦 **Fonte classica** | attestato nel libro di Lozanov del 2005 | la riga del libro (r. NNNN) |
| 🟨 **Tradizione** | tramandato dalla tradizione suggestopedica e Superlearning (Ostrander e Schroeder, Bancroft, manuali) o dallo standard di una disciplina (Health Qigong, tango); non testato scientificamente come tale | la sigla della fonte |
| 🟩 **Evidenza** | sostenuto da studi, **solida** o **parziale** | il riferimento o il cluster dei file di verifica |
| 🟥 **Speculativo** | **non verificato** oppure **contraddetto** dagli studi | il cluster dei file di verifica |
| 🟥 **Non canonico** | pratica che Lozanov rifiuta esplicitamente | la riga del libro |

Esempio: S-22 Respirazioni con apnea porta 🟨 Tradizione per la procedura, 🟩 Evidenza parziale per il respiro lento senza apnee, 🟥 Speculativo (contraddetto) per la promessa di "più ossigeno al cervello", 🟥 Non canonico (r. 1407-1416).

**Corrispondenza con le lettere di `DECISIONI.md` e di `ricerca/`.** A = Evidenza solida; B = Evidenza parziale; C = Speculativo (non verificato); D = Speculativo (contraddetto); "Rifiutato" = Non canonico; "Non trattato" = dicitura "Non trattato da Lozanov". Le regole complete, la forma breve per le tabelle e le etichette di ogni strumento sono in `metodo/00-convenzioni.md` §1 e §3.

**Una differenza con il sito QIGONG.** Sul sito "Fonte classica" indica i testi classici cinesi; in questo metodo il blu è riservato a Lozanov 2005, e i testi classici cinesi e la sequenza HQA portano 🟨 Tradizione (`applicazioni/qigong-liu-zi-jue.md` §1).

**Come convivono le pratiche.**
- **Canone** (🟦): il ciclo della lezione e gli strumenti di Lozanov.
- **Integrazioni dalla ricerca** (🟩): le undici pratiche approvate, con il principio canonico affine quando c'è.
- **Pratiche delle fonti "come nelle fonti"** (🟨, spesso 🟥 Non canonico): l'autore le ha volute nel metodo con la procedura originale. La spiegazione corretta sta nel testo; quella delle fonti in un riquadro "Cosa dicono le fonti" con la sua etichetta. Le pratiche di stato (respiro con apnea, rilassamento, visualizzazioni, ancoraggi) stanno in una fase di preparazione facoltativa, all'inizio della lezione (`metodo/02-ciclo-didattico.md` §1.1).
- **Modulo sperimentale**: separato dalla lezione, facoltativo, dichiarato non lozanoviano, con precauzioni (`metodo/07-modulo-sperimentale.md`).
- **Fuori dal metodo**: luci stroboscopiche, dispositivi rotanti, generatori ELF e magneti; restano documentati in `ricerca/`.

## Dove si applica

| Contesto | File | Note |
|---|---|---|
| Tango argentino | `applicazioni/tango.md` | corsi dell'autore; fino a 10 coppie |
| Qigong | `applicazioni/qigong-liu-zi-jue.md` | Liu Zi Jue, sequenza Health Qigong (sei suoni: Xu, He, Hu, Si, Chui, Xi); fino a 20 persone; collegato al progetto QIGONG |
| Formazione insegnanti | `applicazioni/formazione-insegnanti.md` | docenti di tango, Qigong e altre discipline |
| Corso universitario | `applicazioni/corso-universitario.md` | 12 settimane, laboratori di tango e Liu Zi Jue, sperimentazione con misure validate |

Formati: lezione settimanale, workshop intensivo, corso universitario. Gruppi fino a 20 persone.

## Struttura del repository

```
superapprendimento/
├── README.md
├── DECISIONI.md                 le 44 decisioni dell'autore, scheda per scheda
├── fonti/
│   ├── originali/               documenti di partenza (libro di Lozanov, manuali, ricerche)
│   └── testo/                   testo estratto, con le righe citate nei file di ricerca
├── ricerca/
│   ├── modello-canonico-lozanov.md      il canone del fondatore, con le righe del libro
│   ├── verifica-neuro-fisiologia.md     livelli di evidenza e riferimenti, per area
│   ├── verifica-pedagogia-storia-musica.md
│   ├── verifica-tecnologie-nutrizione-clinica.md
│   ├── decisioni-log.md                 sintesi delle decisioni e parametri del progetto
│   └── estrazioni/                      procedure e affermazioni delle fonti, file per file
├── metodo/
│   ├── 00-convenzioni.md                            etichette, ID degli strumenti, mappa, regole, glossario
│   ├── 01-fondamenti-e-principi.md                  canone, predictive coding, che cosa esclude il canone, storia
│   ├── 02-ciclo-didattico.md                        ciclo, fase di preparazione, formati, scalette, lezione modello (S-01–S-14)
│   ├── 03a-catalogo-strumenti-stato-suggestione-voce.md     gioco, stato, sonno, voce, comunicazione (S-15–S-34, S-57–S-60)
│   ├── 03b-catalogo-strumenti-corpo-memoria-integrazioni.md corpo, memoria, integrazioni (S-35–S-52)
│   ├── 04-musica.md                                 programma dei concerti, musica delle discipline (S-53–S-56)
│   ├── 05-il-docente.md                             condizioni, voce e corpo, 14 competenze, formazione
│   ├── 06-sicurezza-ed-etica.md                     procedure SIC-01–SIC-07, invio, privacy e ricerca
│   ├── 07-modulo-sperimentale.md                    S-61–S-76
│   └── REVISIONE.md                                 esito della revisione: controlli, correzioni, punti aperti, rischi
└── applicazioni/
    ├── tango.md                     obiettivi per livello, film e identità porteñe, testo del concerto, 8 settimane, workshop, milonga
    ├── qigong-liu-zi-jue.md         sequenza HQA, respiro come contenuto e come tecnica, sei suoni come canto, 8 settimane, workshop
    ├── formazione-insegnanti.md     competenze, moduli e ore, intensivo, tirocinio, valutazione, certificazione
    └── corso-universitario.md       syllabus, correzione del Tango-Mind, sperimentazione, etica, voto, bibliografia
```

## Come leggere il repository

1. **Per conoscere il metodo.** `metodo/00-convenzioni.md` (etichette e indice degli strumenti), poi `01` (fondamenti) e `02` (ciclo e formati). Il catalogo (`03a`, `03b`, `04`) contiene le schede: ogni strumento ha un ID (S-01–S-76), le etichette, la procedura con i tempi, un esempio di tango e uno di Liu Zi Jue, la spiegazione, il riquadro delle fonti quando serve, le precauzioni. `05` riguarda il docente; `06` la sicurezza, da leggere prima di proporre qualsiasi strumento; `07` il modulo sperimentale.
2. **Per insegnare.** I file di `applicazioni/` non aggiungono strumenti: prendono le schede con il loro ID e le loro etichette e le mettono in sequenza. Contengono scalette minuto per minuto, cicli di 8 settimane, workshop, esempi concreti per ogni tecnica e, alla fine, un indice degli strumenti con le etichette e l'elenco dei punti da confermare con l'autore.
   - tango: `applicazioni/tango.md`;
   - Liu Zi Jue: `applicazioni/qigong-liu-zi-jue.md`, insieme al player del progetto QIGONG;
   - formazione dei docenti: `applicazioni/formazione-insegnanti.md`;
   - università: `applicazioni/corso-universitario.md`.
3. **Per capire le scelte.** `DECISIONI.md`, a partire dalla tabella riassuntiva (sezione 5). Ogni scheda riporta che cosa dicono le fonti, l'evidenza attuale, la compatibilità con Lozanov, i rischi e la decisione dell'autore. `metodo/REVISIONE.md` dice che cosa è stato controllato e corretto nei testi e che cosa resta da decidere.
4. **Per controllare una fonte.** `ricerca/estrazioni/` per le procedure, `ricerca/verifica-*.md` per l'evidenza e i riferimenti, `ricerca/modello-canonico-lozanov.md` per il canone. Le righe citate si ritrovano in `fonti/testo/`.

**Diciture da conoscere.** "Proposta, da confermare con l'autore" segna i punti che l'autore non ha ancora deciso; "[da chiarire con l'autore]" una precauzione di `DECISIONI.md` in tensione con una procedura voluta "come nelle fonti"; "[da verificare]" un riferimento o un dato da controllare sull'originale.

Tutto ciò che le fonti contengono resta documentato in `ricerca/`, anche ciò che il metodo non usa.

## Stato del lavoro (4 ottobre 2026)

| Parte | Stato |
|---|---|
| `fonti/` | completo |
| `ricerca/` | completo: estrazioni, modello canonico, tre verifiche delle evidenze |
| `DECISIONI.md` | 44 schede decise dall'autore |
| `metodo/00`-`07` | prima stesura completa, rivista il 5 ottobre 2026 (`metodo/REVISIONE.md`): decisioni, sicurezza, etichette, citazioni e riferimenti controllati; testo riscritto per la lettura in classe |
| `applicazioni/` | prima stesura completa dei quattro file, rivista con il metodo |

Da fare (l'elenco completo, con i rischi residui, è in `metodo/REVISIONE.md`):
- rispondere alle domande ancora aperte (calendari, corsi adattivi, testo del concerto nelle discipline corporee, confine tra contenuto e induzione nel Qigong, voto universitario e altre): elenco in `metodo/00-convenzioni.md` §6.1 e alla fine di ogni file di `applicazioni/`;
- chiarire le precauzioni in tensione con le pratiche "come nelle fonti" (`metodo/00-convenzioni.md` §6.2);
- decidere la regola per l'ordine delle sessioni musicali dei concerti: in ordine di programma (ciclo 1 = sessione 1, come nel tango) oppure per durata (sessioni 3 e 4 nel Liu Zi Jue); attivo e passivo usano ora sempre la stessa sessione (`metodo/04-musica.md` §2.2);
- verificare i titoli e le registrazioni del repertorio di tango e i diritti d'uso della traccia HQA;
- ricontrollare sull'originale ogni riferimento prima della pubblicazione (`DECISIONI.md` §3.6), compresi quelli che vengono dal sito QIGONG.

## Avvertenze

- Il metodo non è una terapia. Il docente non fa diagnosi, non fa trattamenti e non promette effetti sulla salute.
- Alcune pratiche richiedono uno screening delle controindicazioni o un consenso informato: sono indicate nelle schede e in `metodo/06-sicurezza-ed-etica.md`.
- I risultati riportati da Lozanov sono dichiarati dall'autore e riguardano i corsi descritti nel suo libro.
