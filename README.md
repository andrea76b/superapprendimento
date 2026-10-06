# Superapprendimento

**In breve.** Superapprendimento è un metodo didattico fondato sulla Desuggestopedia di Georgi Lozanov e integrato, in modo dichiarato, con la ricerca attuale sull'apprendimento. Gli esempi applicativi pratici sono stati tarati su tango argentino e Qigong, sulla formazione degli insegnanti e su un corso universitario. Il metodo può essere applicato a qualsiasi campo didattico e di apprendimento.

## Da dove cominciare

| Che cosa | Dove | Forma |
|---|---|---|
| Il manuale | `manuale/` (17 capitoli in ordine di lettura) | Markdown; PDF in `pdf/Superapprendimento_manuale.pdf` (circa 95 pagine A4) |
| La guida operativa del docente di tango | `guide/guida-operativa-docente-tango.md` | Markdown; PDF in `pdf/Guida_operativa_docente_tango.pdf` (circa 17 pagine A4) |

Il manuale racconta il metodo dall'inizio: chi era Lozanov e che cosa scrive, l'idea del cervello che prevede, il ciclo della lezione e i formati, gli strumenti del docente, le pratiche di stato, la musica, il ruolo del docente, la sicurezza, il modulo sperimentale e le applicazioni a tango, Liu Zi Jue, formazione degli insegnanti e corso universitario. La guida è lo strumento da consultare prima di ogni lezione di tango.

## Fondamenti

- **Il canone di Lozanov.** La base è l'ultima sintesi del fondatore: G. Lozanov, *Suggestopaedia - Desuggestive Teaching*, Vienna 2005, ricostruita in `ricerca/modello-canonico-lozanov.md`.
- **Il cervello che prevede.** Predictive coding e metastabilità (Kotler, Mannino, Fox, Friston 2026) sono il secondo fondamento, presentato come ipotesi teorica. Non è una terapia e non promette effetti sul trauma.
- **La ricerca attuale sull'apprendimento.** Undici integrazioni approvate dall'autore, dal distanziamento della pratica al focus attentivo esterno.

## Struttura del repository

```
superapprendimento/
├── README.md
├── manuale/          il manuale, 17 capitoli
├── guide/            la guida operativa del docente di tango
├── pdf/              i PDF del manuale e della guida
├── DECISIONI.md      le 44 decisioni dell'autore, scheda per scheda
├── ricerca/          canone di Lozanov, verifiche delle evidenze, estrazioni delle fonti, log delle decisioni, resoconti delle revisioni
├── fonti/            documenti di partenza e testo estratto, con le righe citate
├── archivio/         la versione tecnica precedente (5 ottobre 2026), con le schede S-xx e le etichette, e la prima guida
└── strumenti/        script per rigenerare i PDF
```

Per rigenerare i PDF dopo una modifica: `python3 strumenti/genera_pdf.py` (servono il pacchetto Python `markdown` e Node.js con Playwright).

## Stato del lavoro (6 ottobre 2026)

Il manuale e la guida sono stati riscritti il 6 ottobre 2026 in forma discorsiva, senza etichette e senza elementi teatrali, su decisione dell'autore. Il resoconto della revisione è in `ricerca/revisione-manuale-2026-10-06.md`; le decisioni sono registrate in `ricerca/decisioni-log.md`.

Restano aperti:
- la struttura della formazione insegnanti (ore, moduli, tirocinio, valutazione);
- le sessioni musicali dalla quinta alla nona, con opere troppo lunghe per i 43 minuti di concerto della lezione settimanale;
- alcune proposte da confermare, elencate nel capitolo 17 del manuale.

## Avvertenze

- Il metodo non è una terapia. Il docente non fa diagnosi, non fa trattamenti e non promette effetti sulla salute.
- Alcune pratiche richiedono lo screening per autoesclusione, con un questionario anonimo, o un consenso informato. Chiunque può non fare un'attività, senza spiegare.
- I risultati riportati da Lozanov sono dichiarati dall'autore e riguardano i corsi descritti nel libro.
