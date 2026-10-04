# Superapprendimento

Superapprendimento è un metodo didattico fondato sulla Desuggestopedia di Georgi Lozanov e integrato, in modo dichiarato, con la ricerca attuale sull'apprendimento. Nasce dai corsi di tango argentino dell'autore e si applica al Qigong (Liu Zi Jue), alla formazione degli insegnanti e a un corso universitario. L'autore è docente certificato nella linea di Lozanov.

## Fondamenti

- **Il canone di Lozanov.** La base è l'ultima sintesi del fondatore: G. Lozanov, *Suggestopaedia – Desuggestive Teaching*, Vienna 2005, ricostruita in `ricerca/modello-canonico-lozanov.md`. Ne vengono il ciclo in quattro fasi (introduzione, concerti, elaborazione, performance), la suggestione intesa come "to offer, to propose", il gioco, il canto, l'arte, le percezioni periferiche e la correzione indiretta.
- **Predictive coding e metastabilità.** È il secondo fondamento, presentato come ipotesi teorica (Kotler, Mannino, Fox, Friston 2026, articolo d'opinione). Un contesto sicuro e insieme sfidante fornisce al sistema nervoso dati coerenti con l'assenza di minaccia. Nel metodo diventa un principio di progettazione della lezione (sicurezza percepita). Non è una terapia e non promette effetti sul trauma.
- **Ricerca attuale.** Undici integrazioni approvate dall'autore: distanziamento e richiamo attivo, focus attentivo esterno, pratica variata, imagery autogestita, routine pre-esecuzione, esercizi vestibolo-oculari, sicurezza percepita, gesto ed effetto di esecuzione, canto e coro, misure validate, pause brevi nella pratica motoria.

## Un metodo, due etichette

Il metodo è unico. Ogni strumento porta il livello di evidenza (A-D) e la compatibilità con il canone di Lozanov (coerente, non trattato, non compatibile), sempre nello stesso formato:

**Evidenza: B · Canone: coerente**

Accanto agli strumenti del canone il metodo tiene, per scelta dell'autore, alcune pratiche delle altre fonti, comprese pratiche che Lozanov esclude: l'etichetta lo dichiara ("Canone: non compatibile"). Le spiegazioni date dalle fonti compaiono in riquadri separati, "Cosa dicono le fonti", con il loro livello di evidenza. Le pratiche più incerte stanno in un modulo sperimentale, separato dalla lezione e facoltativo. Regole, elenco degli strumenti (S-01–S-76) e glossario sono in `metodo/00-convenzioni.md`.

## Dove si applica

| Contesto | Note |
|---|---|
| Tango argentino | corsi dell'autore; fino a 10 coppie |
| Qigong | Liu Zi Jue, sequenza Health Qigong (sei suoni: Xu, He, Hu, Si, Chui, Xi); fino a 20 persone |
| Formazione insegnanti | docenti che vogliono usare il metodo |
| Corso universitario | con valutazione basata su misure validate |

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
│   ├── 00-convenzioni.md        etichette, ID degli strumenti, mappa dei file, glossario
│   ├── 01-fondamenti-e-principi.md
│   ├── 02-ciclo-didattico.md
│   ├── 03a-catalogo-stato-suggestione-voce.md
│   ├── 03b-catalogo-corpo-memoria-integrazioni.md
│   ├── 04-musica.md
│   ├── 05-il-docente.md
│   ├── 06-sicurezza-ed-etica.md
│   └── 07-modulo-sperimentale.md
└── applicazioni/
    ├── tango.md
    ├── qigong-liu-zi-jue.md
    ├── formazione-insegnanti.md
    └── corso-universitario.md
```

## Come leggere il repository

1. **Per usare il metodo:** `metodo/00-convenzioni.md` (etichette e indice degli strumenti), poi `01` e `02`, poi il catalogo (`03a`, `03b`, `04`, `05`), infine il file di `applicazioni/` che interessa. Prima di proporre qualsiasi strumento si legge `06-sicurezza-ed-etica.md`.
2. **Per capire le scelte:** `DECISIONI.md`, a partire dalla tabella riassuntiva (sezione 5). Ogni scheda riporta che cosa dicono le fonti, l'evidenza attuale, la compatibilità con Lozanov, i rischi e la decisione dell'autore.
3. **Per controllare una fonte:** `ricerca/estrazioni/` per le procedure, `ricerca/verifica-*.md` per l'evidenza e i riferimenti, `ricerca/modello-canonico-lozanov.md` per il canone. Le righe citate si ritrovano in `fonti/testo/`.

Tutto ciò che le fonti contengono resta documentato in `ricerca/`, anche ciò che il metodo non usa.

## Stato del lavoro (4 ottobre 2026)

| Parte | Stato |
|---|---|
| `fonti/` | completo |
| `ricerca/` | completo: estrazioni, modello canonico, tre verifiche delle evidenze |
| `DECISIONI.md` | 44 schede decise dall'autore |
| `metodo/00-convenzioni.md` | pronto |
| `metodo/01`-`07`, `applicazioni/` | in stesura |

Da fare:
- rispondere alle domande ancora aperte (calendari, corsi adattivi, confine tra contenuto e induzione nel Qigong e altre): elenco in `metodo/00-convenzioni.md` §6;
- ricontrollare sull'originale ogni riferimento prima della pubblicazione (`DECISIONI.md` §3.6).

## Avvertenze

- Il metodo non è una terapia. Il docente non fa diagnosi, non fa trattamenti e non promette effetti sulla salute.
- Alcune pratiche richiedono uno screening delle controindicazioni o un consenso informato: sono indicate nelle schede e in `metodo/06-sicurezza-ed-etica.md`.
- I risultati riportati da Lozanov sono dichiarati dall'autore e riguardano i corsi descritti nel suo libro.
