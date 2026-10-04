# Tango, musica e Superlearning: estrazione completa

Fonti (tutte lette per intero, riga per riga, senza campionare):

| Sigla | File | Righe | Dimensione |
|---|---|---|---|
| **T** | `fonti/testo/Superlearning_tango.txt` | 1-278 | circa 20 KB |
| **D** | `fonti/testo/didattica_superlearning.txt` | 1-258 | circa 13 KB |
| **M** | `fonti/testo/musiche_relax_didattica.txt` | 1-273 | circa 19 KB |

Convenzione: "T:L123" vuol dire riga 123 del file T, e così per D e M. Le frasi tra virgolette sono citazioni testuali.

Stato: estrazione fedele, senza giudizio di merito. La colonna "red flag" segnala solo ciò che a prima vista sembra pseudoscientifico, esagerato o non verificabile. La verifica vera spetta a un'altra fase. Le note marcate **[nota dell'estrattore]** sono osservazioni sul testo (incoerenze interne, duplicati, refusi), non giudizi sui contenuti.

---

## 0. Natura delle fonti (da leggere prima di tutto)

Nessuno dei tre file è un libro o un articolo. Sono **output di un assistente conversazionale che lavora su "fonti" caricate** (con ogni probabilità uno strumento tipo NotebookLM). Gli indizi:

- **T** si apre dicendo che l'idea "trova solide basi nelle fonti fornite" (T:L2-3). Due blocchi si chiudono con l'offerta di generare "un Report dettagliato… oppure un Mazzo di diapositive (Slide Deck)" (T:L108-112, ripetuto in T:L117-121). L'ultimo si chiude con "Saresti interessato a espandere ulteriormente uno di questi moduli…?" (T:L270-273).
- **D** ha un punto isolato su una riga a sé dopo quasi ogni frase (per esempio D:L7, L9, L13, L15…). Sono i segni lasciati dai marcatori di citazione rimossi. Le fonti a cui rimandavano non sono più leggibili.
- **M** scrive "Le fonti indicano…" (M:L102) e "le fonti specificano…" (M:L116).
- Non c'è **nessuna bibliografia** in nessuno dei tre file. Gli studi sono evocati senza autori ("un test del 2003 su adolescenti", T:L68-69; "uno studio filippino del 2023", T:L81-82) oppure con il nome della rivista ma senza autori ("PLoS One (2023)", T:L26).
- Molti contenuti di D e M ricalcano da vicino *Superlearning 2000* di Ostrander e Schroeder (repertorio musicale, Tomatis, Hoffman, Abrezol, Cousto, Capel, Carlson, Edrington). M dichiara di riportare il "Programma Musicale Ufficiale della Suggestopedia (Capitolo 31)" (M:L1) senza dire di quale opera.

### Artefatti di conversione PDF-testo

- **Legature "fi" e "fl" perse.** Le lettere spariscono dalle parole e finiscono raccolte in righe sparse di soli "fi"/"fl" (T:L51-60, L113-116, L173-174, L229-236, L274-278; M:L53-56, L110-112, L167-168, L222, L271-273). Così "sico" sta per *fisico*, "af darsi" per *affidarsi*, "usso" per *flusso*, "de cit" per *deficit*, "In nity" per *Infinity*, "ttizia" per *fittizia*, "lippino" per *filippino*, "s de" per *sfide*, "B- at" per *B-flat*, " ute" per *flute*.
- **Passaggi duplicati** ai cambi di pagina: T:L61 = T:L50; T:L117-121 = T:L108-112; T:L237-241 = T:L224-228; M:L57-59 = M:L50-52; M:L113-115 = M:L107-109; M:L169-174 = M:L161-166. In questa estrazione sono contati una volta sola.
- **D si interrompe** a metà della sezione "DALCROZE" (D:L250-258): c'è un solo esercizio, poi il file finisce.

### Mappa dei blocchi

| Blocco | Righe | Contenuto |
|---|---|---|
| T-A | T:L1-112 | Prima proposta "Progetto Tango-Mind: Sincronizzazione Multisensoriale e Apprendimento Accelerato": 4 moduli più il disegno sperimentale |
| T-B | T:L125-168 | "Bozza accademica": premessa teorica, le tre "tecnologie mentali", metodologia di ricerca (EEG, STAI, ritenzione) |
| T-C | T:L170-246 | "Syllabus del corso Tango-Mind": 4 moduli (numerazione e contenuti diversi da T-A) |
| T-D | T:L248-273 | "Svolgimento pratico di una lezione tipo (2 ore)": 4 fasi temporizzate |
| D-1 | D:L4-82 | Musica barocca lenta (concerto passivo, 60 bpm): brani, tempo, effetti, uso, compositori contemporanei |
| D-2 | D:L83-138 | Musica classica ad alta frequenza (concerto attivo): brani, frequenze, Tomatis, effetto Mozart, uso |
| D-3 | D:L139-225 | Tecniche sonore speciali: Turning Sound, Hemi-Sync, neuroacustica, ololofonia, frequenze planetarie, frequenze "neurotrasmettitoriali", 5.000 Hz di Carlson |
| D-4 | D:L226-248 | Principi generali sull'uso della musica nel Superlearning |
| D-5 | D:L250-258 | Dalcroze: esercizi con le palle (troncato) |
| M-1 | M:L1-96 | "Programma Musicale Ufficiale della Suggestopedia (Capitolo 31)": 10 sessioni, ciascuna con un concerto attivo e uno passivo, con le durate dei movimenti |
| M-2 | M:L99-118 | Canti gregoriani (Tomatis) |
| M-3 | M:L120-174 | Musica barocca lenta 55-65 BPM: brani e registrazioni consigliate |
| M-4 | M:L176-211 | Musica per il concerto attivo (Mozart e "alta frequenza") |
| M-5 | M:L213-258 | Compositori contemporanei e selezioni "neuro-acustiche" |
| M-6 | M:L260-270 | Accordature planetarie (Hans Cousto) |

---

## 1. Sintesi

**T** è un progetto universitario ("Tango-Mind") che vuole fondere tre cose: entrainment neuro-acustico (battiti binaurali Hemi-Sync e AVE con occhiali stroboscopici), Superlearning musicale (concerto attivo su Mozart, concerto passivo su barocco a 60 bpm con cicli di 4 + 4 secondi) e tango argentino. Il tango è letto come "Total Physical Response" e come applicazione della Infinity Walk di Deborah Sunbeck: gli ochos e i pivot, cioè il movimento "a otto", "costringerebbero" i due emisferi a coordinarsi. A questo si aggiungono respirazione quadrata 4-4-4-4, assunzione di ruolo suggestopedica (identità fittizia), Image Streaming di Win Wenger e un disegno sperimentale con gruppo di controllo, EEG, questionario STAI e test di ritenzione. Il testo cita una revisione sistematica scettica sui battiti binaurali (PLoS One 2023) e uno studio filippino sulle preferenze musicali. Nel resto del documento, però, le affermazioni sono assolute ("in modo incontrovertibile", "senza alcuno sforzo cosciente", "rivoluzionare"). Il prodotto concreto più utile è la **lezione tipo di 2 ore in 4 fasi**: 15 minuti di induzione, 30 di tango, 45 di concerto attivo in movimento, 30 di concerto passivo da sdraiati.

**D** è un compendio sull'uso della musica nel Superlearning di Ostrander e Schroeder. Riporta i brani barocchi in largo (60 bpm, da 55 a 65) per il concerto passivo con i loro presunti effetti fisiologici (pressione, battito, beta −6%, alfa +6%, sincronizzazione emisferica, "supermemoria"). Riporta i brani "ad alta frequenza" (Mozart e altri) per il concerto attivo con la teoria della "ricarica corticale" di Tomatis (da 5.000 a 8.000 Hz). Poi una serie di tecniche sonore marginali: Turning Sound, Hemi-Sync, Binaural Phaser, ololofonia, frequenze planetarie di Cousto, frequenze "neurotrasmettitoriali", 5.000 Hz sulle piante. In fondo un frammento di Dalcroze.

**M** è un repertorio. Contiene un programma di 10 sessioni attribuito alla Suggestopedia ufficiale, con le durate dei movimenti, e liste commentate di canti gregoriani, barocco a 60 BPM, Mozart e classici per il concerto attivo, compositori contemporanei (Hoffman, Duncan, Gagnon, Halpern, Kobialka, Spino, Kitaro, Vangelis, Horn) e accordature planetarie.

---

## 2. Tecniche ed esercizi

### 2.1 Tecniche dal progetto Tango-Mind (file T)

| ID | Tecnica | Righe | Procedura (fedele al testo) | Tempi | Musica / dispositivi | Scopo e meccanismo dichiarati | Fase |
|---|---|---|---|---|---|---|---|
| T1 | **Induzione con battiti binaurali (Hemi-Sync)** | T:L16-20, L146-148, L250-252 | In cuffia si inviano "toni con frequenze leggermente diverse a ciascun orecchio". Il cervello crea un "battito binaurale". Nella lezione tipo è la Fase 1, alternativa alle sessioni brevi con occhiali AVE. | 15 min (Fase 1) | Processo Hemi-Sync "sviluppato dall'Istituto Monroe"; cuffie | "favorisce stati focalizzati di coscienza"; abbassa l'ansia accademica, induce "allerta rilassata" (alfa e theta); "abbattere i picchi di cortisolo e portare l'aula in uno stato coeso" | preparazione |
| T2 | **Audio-Visual Entrainment (AVE)** | T:L21-24, L183-187, L250-252 | Occhiali stroboscopici più cuffie. Il cervello "viene guidato mediante la Frequency Following Response" verso stati mirati. Nella Fase 1 sono "sessioni brevi con occhiali AVE". Nel Modulo 1 del syllabus c'è una "introduzione all'uso dei dispositivi". | parte dei 15 min della Fase 1 | MindPlace Kasina, MindPlace Limina, sistemi DAVID (DAVID Delight) | "ancora più potente" dei binaurali perché accoppia suono e luce stroboscopica; "aumentando il flusso sanguigno nella corteccia prefrontale e riducendo drasticamente l'ansia da esame e i deficit di attenzione"; superare "i blocchi d'apprendimento e dell'ansia" | preparazione |
| T3 | **Respirazione ritmica "geometrica"** (quadrata) | T:L180-182 | Inspirare 4 s, apnea 4 s, espirare 4 s, pausa 4 s. Ciclo di 16 s. Numero di ripetizioni non indicato. | ciclo di 16 s; durata totale non indicata | nessuno | "sincronizzare gli emisferi e incrementare l'ossigenazione cerebrale"; obiettivo del modulo: passare da beta ad alfa e disinnescare lo stress | preparazione / autoregolazione |
| T4 | **Tango come TPR e "Infinity Walk"** | T:L32-44, L152-156, L213-216, L253-255 | Gli studenti imparano il tango "integrando i principi della Infinity Walk". Ochos ("movimenti a forma di otto"), pivot e postura obbligano a muovere gli arti in modo controlaterale. Nella Fase 2 si lavora su connessione, equilibrio e "deambulazione controlaterale". | 30 min (Fase 2) | nessun dispositivo; musica non specificata | Gli ochos "simulano a livello neurologico l'effetto" della Infinity Walk (Deborah Sunbeck). Camminare "a otto" "costringe il sistema nervoso a coordinare costantemente i due emisferi… attraverso il corpo calloso", sblocca le inibizioni e prepara a problemi complessi e nuove lingue. "integrare i lobi frontali e il cervelletto" | attivazione / input |
| T5 | **Declamazione di concetti durante il ballo** | T:L216-218; collegata a T:L256-258 | "Durante il ballo o la camminata ritmica, agli studenti verrà chiesto di declamare concetti accademici." | non indicato | nessuno | "sciogliendo l'inibizione logica dell'emisfero sinistro attraverso l'impegno fisico dell'emisfero destro" | attivazione / elaborazione |
| T6 | **Assunzione di ruolo (identità fittizia)** | T:L45-49, L219-228 | Ogni studente assume un'identità fittizia "per tutta la durata del laboratorio": "un ballerino di Buenos Aires", "un ricercatore straniero", "un matematico geniale", "un ballerino esperto di Buenos Aires", "un poliglotta". | per tutto il laboratorio | nessuno | "Ballare richiede di abbassare le inibizioni". Libera "dalla paura di fare errori accademici", crea "una disconnessione psicologica dalle ansie personali", permette di "bypassare i dogmi limitanti" e di assimilare "senza il filtro critico e pauroso dell'Ego quotidiano". Modulo intitolato "Riprogrammazione Subliminale" | preparazione / trasversale |
| T7 | **Concerto attivo (versione Tango-Mind, in movimento)** | T:L72-75, L198-200, L256-260 | Il docente "declamerà i concetti… in modo drammatico" (T-A). Testi e regole "recitati con intonazione drammatica" (T-C). Nella Fase 3 gli studenti, "mentre si muovono o eseguono passi base, ascoltano o recitano le nozioni" divise in cicli di 4 s di informazione e 4 s di pausa, "usando tre toni di voce distinti". | 45 min (Fase 3) | Mozart, Beethoven: "musica ad alta frequenza"; "base ad altissima frequenza orchestrale (Mozart)" | "ricarica le batterie cerebrali secondo il Dr. Tomatis" | input / presentazione |
| T8 | **Concerto passivo (versione Tango-Mind, da sdraiati)** | T:L75-79, L200-202, L261-265 | Gli studenti sono "rilassati dopo il ballo". Nella Fase 4 "si sdraiano e chiudono gli occhi". Ascoltano "gli stessi dati" (gli stessi della Fase 3) "formattati in cicli esatti di 8 secondi (4 di lettura, 4 di pausa)". | 30 min (Fase 4) | barocco lento "60 battiti al minuto" (Vivaldi, Bach); "misurate esattamente a 60" | "consolidare le informazioni a lungo termine". "L'attività cerebrale si allinea alla metrica del suono, consolidando la memoria a lungo termine senza alcuno sforzo cosciente, riducendo simultaneamente frequenza cardiaca e stress arterioso". "abbassare la pressione sanguigna e rallentare il cuore" | concerto / consolidamento |
| T9 | **Formattazione ritmica dei dati** | T:L63-65, L76-78, L257-259 | Materie "aride" (regole grammaticali, formule matematiche, programmazione) divise in "bocconi" da 4 s, ciascuno seguito da 4 s di pausa, con tre toni di voce (T:L259; i tre toni non sono descritti). | cicli di 8 s | vedi T7 e T8 | ancorare i dati | input / consolidamento |
| T10 | **Image Streaming / "Spettacolo Intimo" (Win Wenger)** | T:L89-94, L242-246 | Gli studenti descrivono "ad alta voce le percezioni e le immagini mentali astratte che emergono durante l'ascolto musicale o l'esecuzione dei passi di danza" (T-A). In T-C si fa "dopo il tango e l'ascolto musicale" ed è il "flusso di immagini mentali generate". | non indicato | musica non specificata | pensiero laterale e creatività. "forzando l'emisfero sinistro (logico-verbale) a collaborare massicciamente con quello destro (visivo-spaziale)". "stimolando la crescita della densità sinaptica" | elaborazione / consolidamento |
| T11 | **Lezione critica sulle evidenze dell'entrainment** | T:L25-31 | Il corso tratta "in modo critico" la revisione PLoS One 2023 sui battiti binaurali. Agli studenti si insegna che la tecnologia acustica "funziona meglio se associata a condizionamento psicologico positivo, rilassamento progressivo e respirazione controllata". | non indicato | nessuno | rigore scientifico | preparazione / teoria |
| T12 | **Teoria vestibolare e "Tomatis"** (lezione) | T:L188-197, L208-212 | Lezione teorica. Il vestibolo come "bussola" del corpo; le "cellule del Corti" che trasformano le alte frequenze "in energia elettrica pura"; il passaggio dal mondo tridimensionale a quello bidimensionale; il movimento come "nutriente". | non indicato | nessuno | capire perché il corpo serve all'apprendimento | teoria |
| T13 | **Valutazione sperimentale** | T:L96-107, L157-168 | Due gruppi (sperimentale e controllo). Misure: (1) ritenzione mnestica a breve e lungo termine; (2) stress con questionari di autovalutazione prima e dopo, STAI; (3) "performance dinamiche": coordinazione ed equilibrio "attraverso l'acquisizione delle figure del Tango"; (4) EEG per la sincronizzazione emisferica e la potenza alfa e theta. | prima e dopo; breve e lungo termine | EEG, STAI | validazione accademica | valutazione |

### 2.2 Tecniche dal compendio Superlearning (file D) e dal repertorio (file M)

| ID | Tecnica | Righe | Procedura (fedele al testo) | Tempi | Musica / dispositivi | Scopo e meccanismo dichiarati | Fase |
|---|---|---|---|---|---|---|---|
| D1 | **Fase di "assorbimento dei dati"** (concerto passivo alla Superlearning) | D:L57-61 | Musica barocca lenta "a basso volume" mentre il materiale viene presentato "in 'bocconi sonori' di quattro secondi, seguiti da una pausa di quattro secondi". | cicli di 8 s | largo barocco a 60 bpm | "Questo ritmo aiuta le cellule cerebrali ad assorbire e registrare meglio i dati" | input / concerto |
| D2 | **"Sessione di concentrazione interiore"** (rinforzo della memoria) | D:L63-65 | Gli studenti chiudono gli occhi e ascoltano "lo stesso materiale letto nuovamente sulla musica". | non indicato | barocco lento | rinforzo della memoria | concerto / consolidamento |
| D3 | **Ascolto prolungato di musica a 60 bpm** | D:L66-68 | Ascoltare "per almeno 20 minuti". | almeno 20 min | barocco a 60 bpm | "comunicare con il subconscio e… stabilizzare gli atteggiamenti" | autoregolazione / consolidamento |
| D4 | **Concerto attivo alla Superlearning** | D:L125-137 | Musica di sottofondo per una "lettura drammatica del materiale". Si usa per "l'intera durata della sinfonia o del concerto". "Sequenza della musica, melodie e dinamiche si legano ai dati". Consiglio: "inviare più suono all'orecchio destro che al sinistro". | intera sinfonia o concerto | Mozart, Beethoven, Brahms, Čajkovskij, Chopin, Haydn | ancorare il materiale; "ricarica" corticale; orecchio destro con "percorso più diretto… al centro del linguaggio" | input / presentazione |
| D5 | **Ascolto "attivo" nella vita quotidiana** | D:L128-129 | Musica ad alta frequenza durante "spostamenti, faccende domestiche o mentre si revisiona il testo". | non indicato | come D4 | energizzare | autoregolazione fuori aula |
| D6 | **Turning Sound (musica sofrologica, Raymond Abrezol)** | D:L141-157 | Musica barocca con frequenze "alterate elettronicamente". Il suono si sposta ritmicamente da un orecchio all'altro. C'è un "tono di respirazione", cioè un segnale periodico che mantiene il respiro lento e ritmico. Per memorizzare: "si osserva il materiale per 7-8 secondi e poi ci si rilassa con la musica". | 7-8 s di osservazione, poi rilassamento (durata non indicata) | registrazioni Turning Sound in cuffia; Abrezol sperimenta anche con musica contemporanea | stimolare alternativamente gli emisferi; stato "in cui il dolore non ferisce" (atleti, parto naturale); memorizzazione accelerata | input / autoregolazione |
| D7 | **Battiti binaurali e Binaural Phaser (Monroe, Edrington)** | D:L159-172; M:L249-258 | Due segnali leggermente diversi, uno per orecchio (esempio: 100 Hz a sinistra, 105 Hz a destra, il cervello "risuona a 5 Hz"). Il Binaural Phaser di Devon Edrington mescola sei schemi di frequenza alla musica: prima onde delta "per il relax", poi battiti specifici "per l'inglese o la biologia". Nelle scuole elementari di Tacoma Edrington ha inserito segnali Hemi-Sync in brani noti abbinati a una materia (Kitaro per la matematica, Vangelis per l'ortografia, Paul Horn per la scrittura creativa). | "in pochi secondi" | cuffie; Binaural Phaser | "selezionare lo stato cerebrale più adatto"; concentrazione | preparazione / input |
| D8 | **Neuroacustica "Brain/Mind Resonance"** (Terry Patten, Julian Isaacs) | D:L174-182 | Suono 3D, battiti binaurali e "frequenze finestra" combinati. Quattro obiettivi: (a) energizzare la produttività, (b) approfondire il rilassamento, (c) centrare la consapevolezza, (d) espandere la coscienza. | non indicato | nastri | "rilassamento senza sforzo", "stati di gioia, unità, beatitudine" | preparazione |
| D9 | **Ololofonia (Hugo Zucarelli)** | D:L184-188 | Registrazione audio 3D con "raggi sonori auricolari". | non indicato | registrazioni olofoniche in cuffia | "Induce sinestesia" e potenzia "l'imaging completo per memoria, apprendimento e prove mentali" | elaborazione / prova mentale |
| D10 | **Diapason "planetari" sui punti di agopuntura (Hans Cousto)** | D:L190-205; M:L260-270 | Diapason tarati sulle tre chiavi (Do diesis 136,10 Hz; Sol 194,71 Hz; Fa 172,06 Hz) "posizionati sui punti di agopuntura" (D), "applicati sui punti di agopuntura prima dello studio" (M). | prima dello studio | diapason calibrati | Do diesis calma e centra (OM); Sol stimola ed energizza; Fa porta gioia e spiritualità | preparazione |
| D11 | **Frequenze "neurotrasmettitoriali" e Brain Tuner (Ifor Capel, Bob Beck)** | D:L207-219 | "Impulsi elettrici a bassa frequenza o toni musicali a ottave più alte". 10 Hz per la serotonina; da 90 a 111 Hz per le beta-endorfine; circa 4 Hz per le catecolamine. Il "Brain Tuner" raggruppa 256 frequenze "come un accordo musicale risonante". | non indicato | dispositivo elettrico Brain Tuner | modulare i neurotrasmettitori, "migliorare le funzioni cerebrali" | preparazione |
| D12 | **Suono pulsato a 5.000 Hz (Dan Carlson)** | D:L221-224 | Suono pulsato a 5.000 Hz "simile a canti di grilli giganti" inserito nella musica barocca. Testato sulle piante; per l'uomo è solo un'ipotesi. | non indicato | registrazione | assorbimento dei nutrienti nelle piante "700% maggiore"; ipotesi sull'assorbimento "di nutrienti e dati negli esseri umani" | (ipotesi) |
| D13 | **Esercizi con le palle (Dalcroze)** | D:L255-258 | "Utilizzando una piccola palla (es. da tennis), gli studenti la fanno rimbalzare e la riprendono a tempo con la musica, adattando l'azione a diversi metri musicali." Il file si interrompe qui. | non indicato | palla da tennis; musica con metri diversi | sincronizzare l'azione al metro | attivazione |
| M1 | **Canti gregoriani come "terapia di ricarica" isolata** | M:L99-118 | Ascolto di canto gregoriano (Solesmes; monache di Santa Cecilia, Isola di Wight). **Non** va usato come sottofondo del concerto attivo: la voce dell'insegnante deve sovrapporsi alla musica. Va "ascoltato come terapia di ricarica isolata". | non indicato | registrazioni corali | "sublime cibo per il cervello" (Tomatis); ricarica le cellule cerebrali grazie alle armoniche superiori e alla metrica vocale | autoregolazione / ricarica |
| M2 | **Tempo discendente 60 → 50 BPM per la visualizzazione (Hoffman)** | M:L217-230; D:L71-76 | *Deep Daydreams*: lato A a 60 BPM "per sincronizzare il corpo", lato B a 50 BPM "per la visualizzazione profonda". *Rhythmic Medicine*: video a 60 e 50 BPM con immagini sincronizzate "per il biofeedback". | due lati di un album | brani di Janalea Hoffman | sincronizzare il corpo, poi visualizzare in profondità; effetti su pressione, aritmie, insonnia, ansia da test | preparazione / visualizzazione |
| M3 | **Scelta delle esecuzioni su strumenti d'epoca** | M:L157-174 | Preferire le registrazioni su strumenti d'epoca (Tafelmusik, consigliata da David Fallis) e la Suite per violoncello BWV 1007 di Yo-Yo Ma. | n/a | dischi | "armoniche superiori naturali e non alterate" | preparazione dei materiali |

---

## 3. Protocolli e sequenze

### P1. Lezione tipo "Tango-Mind" (2 ore), T:L248-265

| Fase | Durata | Contenuto | Musica / dispositivi | Posizione del corpo |
|---|---|---|---|---|
| 1 | 15 min | Induzione del rilassamento con battiti binaurali (Hemi-Sync) **o** sessioni brevi con occhiali AVE; "abbattere i picchi di cortisolo", "stato coeso" dell'aula | cuffie, occhiali stroboscopici | non indicata (presumibilmente seduti) |
| 2 | 30 min | Laboratorio di tango e propriocezione vestibolare: connessione, equilibrio, deambulazione controlaterale ("integrare i lobi frontali e il cervelletto") | non indicata | in piedi, in coppia |
| 3 | 45 min | Concerto attivo: in movimento o durante i passi base, ascolto o recitazione delle nozioni in cicli di 4 s di informazione e 4 s di pausa, con tre toni di voce | "base ad altissima frequenza orchestrale (Mozart)" | in movimento |
| 4 | 30 min | Concerto passivo: sdraiati, occhi chiusi, stesse informazioni della Fase 3 | barocco a 60 bpm (Bach, Vivaldi) | sdraiati |

Totale: 15 + 30 + 45 + 30 = **120 minuti**. Non sono previsti tempi di transizione, una fase di attivazione finale (ritorno alla veglia) né momenti di verifica dentro la lezione.

### P2. Sequenza dei due concerti nella prima proposta (T-A), T:L72-79

1. Concerto attivo: il docente declama in modo drammatico su Mozart o Beethoven.
2. Concerto passivo: gli studenti, "rilassati dopo il ballo", ascoltano gli stessi dati in cicli esatti di 8 s (4 di lettura, 4 di pausa) su barocco lento a 60 bpm.

**[nota dell'estrattore]** Il ciclo 4 + 4 sta nel **concerto passivo** in T:L76-78, ma nel **concerto attivo** in T:L256-260 (lezione tipo). È un'incoerenza interna del file. In D:L58-60 il ciclo 4 + 4 appartiene alla fase di assorbimento su barocco lento, cioè al concerto passivo.

### P3. Struttura del corso (due versioni non coincidenti)

- **T-A (L11-94):** Modulo 1, induzione dello stato ottimale (Hemi-Sync, AVE, contesto scientifico) → Modulo 2, tango come TPR e Infinity Walk più assunzione di ruolo → Modulo 3, ritmo e memoria (musica classica, i due concerti, preferenze personali) → Modulo 4, immaginazione e problem solving (Image Streaming).
- **T-C (L170-246):** Modulo 1, induzione e bio-regolazione (respirazione 4-4-4-4, AVE) → Modulo 2, sistema vestibolare, suono e corpo (teoria Tomatis, concerto attivo e passivo) → Modulo 3, tango come laboratorio cinestesico (teoria 3D/2D, movimento come nutriente, ochos, declamazione) → Modulo 4, "Riprogrammazione Subliminale" e assunzione di ruolo più consolidamento con Image Streaming.

### P4. Disegno sperimentale, T:L96-107 e L157-168

Gruppo sperimentale (tecniche Tango-Mind) contro gruppo di controllo. Variabili: ritenzione a breve e lungo termine, stress (questionari prima e dopo, STAI), coordinazione ed equilibrio (acquisizione delle figure di tango), EEG (sincronizzazione emisferica, potenza alfa e theta). Riferimenti di confronto dichiarati: "studio sulla memoria musicale" e "studio sul Sudoku".

### P5. Sessione Superlearning standard (D), D:L57-68

Fase di assorbimento dati (barocco a basso volume, cicli 4 + 4) → "sessione di concentrazione interiore" (occhi chiusi, stesso materiale riletto sulla musica). Ascolto di almeno 20 minuti.

### P6. Ciclo Turning Sound, D:L154-155

Osservare il materiale per 7-8 s → rilassarsi con la musica (durata non indicata) → ripetere (implicito). Il "tono di respirazione" regola il respiro durante tutto il ciclo.

### P7. Binaural Phaser, D:L170-172

Prima schemi delta "per il relax", poi battiti specifici per la materia (esempi: inglese, biologia).

### P8. Programma musicale "ufficiale" della Suggestopedia in 10 sessioni, M:L1-96

Ogni sessione ha un concerto attivo (classici e romantici, opere intere con tutti i movimenti) seguito da un concerto passivo (barocco, spesso per organo o clavicembalo). La colonna "durata" è la somma dei movimenti cronometrati nel testo. È la durata totale dei brani elencati: il testo non dice se vadano eseguiti tutti nella stessa sessione.

| Sessione | Concerto attivo (durate dei movimenti dichiarate) | Durata attivo | Concerto passivo | Righe |
|---|---|---|---|---|
| 1 | Mozart, Concerto per violino n. 5 in la magg. (9:35, 11:05, 9:50); Sinfonia KV 201 n. 29 in la magg. (8:40, 7:25, 3:50, 5:40); Sinfonia KV 550 n. 40 in sol min. (8:10, 7:35, 4:47, 4:50) | 30:30 + 25:35 + 25:22 = **81:27** | Bach, Fantasia per organo in sol magg. BWV 572; Fantasia in do min. BWV 562 | M:L2-12 |
| 2 | Haydn, Concerto per violino n. 1 in do magg. (9:30, 4:10, 4:10); Concerto per violino n. 2 "in G Major" (8:35, 7:05, 3:45) | 17:50 + 19:25 = **37:15** | Bach, Preludio e fuga in sol magg. BWV 541; "Dogmatic Chorales" | M:L13-21 |
| 3 | Mozart, Sinfonia "Haffner" KV 385 (4:55, 4:30, 3:30, 3:55); Sinfonia "Praga" KV 504 (11:55, 8:50, 6:00) | 16:50 + 26:45 = **43:35** | Händel, Concerto per organo e orchestra in si bem. magg. op. 7 n. 6 | M:L22-30 |
| 4 | Haydn, Sinfonia n. 101 "L'Horloge", indicata "in C Major" (8:00, 8:00, 4:00, 4:00); Sinfonia n. 94 in sol magg. (12:00, 7:00, 4:00, 4:00) | 24:00 + 27:00 = **51:00** | Corelli, Concerti grossi op. 6 nn. 4, 10, 11, 12 | M:L31-39 |
| 5 | Beethoven, Concerto per pianoforte n. 5 op. 73, indicato "in B-flat" (19:30, 8:00, 10:40). Il testo stesso annota che l'op. 73 è storicamente in mi bemolle | **38:10** | Vivaldi, cinque concerti per flauto e orchestra da camera | M:L40-47 |
| 6 | Beethoven, Concerto per violino in re magg. op. 61 (24:30, 11:20, 9:30) | **45:20** | Corelli, Concerti grossi op. 6 nn. 2, 8, 5, 9 | M:L48-61 |
| 7 | Čajkovskij, Concerto per pianoforte n. 1 in si bem. min. (I mov. 21:50; II-III 15:15) | **37:05** | Händel, "Wassermusik" | M:L62-68 |
| 8 | Brahms, Concerto per violino in re magg. op. 77 (22:05, 9:25, 8:05) | **39:35** | Couperin, sonate per clavicembalo "Le Parnasse" (Apoteosi di Corelli), "L'Astrée"; Rameau, "Pièces de clavecin" n. 1 e n. 5 | M:L69-78 |
| 9 | Čajkovskij, Concerto per violino in re magg. op. 35 (22:00, 7:00, 10:00) | **39:00** | Bach, Corali dogmatici per organo BWV 680-689; Fuga in mi bem. magg. BWV 552 | M:L79-86 |
| 10 | Mozart, Concerto per pianoforte n. 18 in si bem. magg. KV 456 (11:55, 10:10, 7:35); n. 23 in la magg. KV 488 (11:00, 7:05, 8:05) | 29:40 + 26:10 = **55:50** | Vivaldi, Le Quattro Stagioni op. 8 | M:L87-96 |

**[nota dell'estrattore]** Il concerto passivo di questo programma usa opere barocche **intere**: fantasie e corali per organo, concerti grossi, Wassermusik, pezzi per clavicembalo, le Quattro Stagioni complete. Questo è in tensione con l'idea, presente in D e M-3, che il concerto passivo usi solo i **movimenti lenti** (largo o andante) a 60 bpm. Le due tradizioni (Lozanov da una parte, Ostrander e Schroeder dall'altra) convivono nei file senza essere distinte.

---

## 4. Principi teorici

| # | Principio | Righe | Descrizione fedele |
|---|---|---|---|
| 1 | **Allerta rilassata** | T:L13-14, L147-148; D:L46-47 | Stato "essenziale per l'apprendimento", da raggiungere prima di ogni attività fisica o accademica: "corpo rilassato, mente allerta" (onde alfa e theta) |
| 2 | **Superare la passività accademica** | T:L3-5, L139-141 | L'insegnamento tradizionale è passivo e "si rivolge quasi esclusivamente all'emisfero sinistro", ignorando la sintesi spaziale, emotiva e motoria del destro e del corpo |
| 3 | **Integrazione emisferica** | T:L11, L38-44, L141-144, L152-156, L216-218, L244-246; D:L44, L145-146 | Si impara meglio quando i due emisferi collaborano. Si ottiene con movimento incrociato, battiti binaurali, musica, verbalizzazione delle immagini |
| 4 | **Apprendimento come integrazione totale** | T:L129-130 | L'apprendimento ottimale richiede "l'integrazione simultanea di mente conscia, subconscio, corpo, sensi ed emozioni" |
| 5 | **Ancoraggio corporeo** | T:L35-36, L142-144, L205-206 | Il tango è il "veicolo cinestesico per radicare l'apprendimento". Le informazioni vengono "ancorate" nella "memoria posturale e muscolare" |
| 6 | **Tango come meta-linguaggio** | T:L34-35 | Il tango argentino "non è solo un ballo, ma un meta-linguaggio" fatto di connessione non verbale, postura, ritmo e consapevolezza spaziale |
| 7 | **Filtro affettivo e inibizione** | T:L45-46 | "Ballare richiede di abbassare le inibizioni". Il nome di Krashen non compare |
| 8 | **Assunzione di ruolo e disconnessione dall'ansia** | T:L46-49, L221-228 | Il ruolo fittizio sospende l'incredulità e scollega dalle ansie abituali. "Bypassare i dogmi limitanti" e "il filtro critico… dell'Ego" |
| 9 | **Il vestibolo come bussola e il movimento come nutriente** | T:L190-197, L208-212 | L'orecchio interno coordina "tutti i movimenti muscolari e l'orientamento spaziale contro la gravità". Il movimento ritmico è "letteralmente" un "nutriente" per il cervello |
| 10 | **Disconnessione 3D → 2D** | T:L208-210 | Il passaggio dal mondo tridimensionale dell'infanzia a quello bidimensionale dei libri "crea spesso disconnessioni neurologiche" |
| 11 | **Ricarica corticale con l'alta frequenza (Tomatis)** | T:L74-75, L195-197; D:L90-91, L104-120; M:L100-102, L178-179 | Il suono, soprattutto da 5.000 a 8.000 Hz, è un "nutriente" che ricarica le "batterie" del cervello. I suoni a bassa frequenza invece "drenano" (D:L242-244) |
| 12 | **Tempo cardiaco e sincronizzazione (60 bpm)** | T:L149-151; D:L28-30; M:L122-124, L217-219 | La musica a circa 60 bpm (da 55 a 65), in 4/4 e con archi, sincronizza il battito, rallenta il cuore, abbassa la pressione. Il metronomo è tarato "sul ritmo cardiaco umano a riposo" |
| 13 | **Formattazione ritmica (4 + 4 s)** | T:L63-65, L76-78; D:L58-61 | Presentare i dati in "bocconi sonori" da 4 s con 4 s di pausa aiuta le cellule cerebrali a "registrare" |
| 14 | **La musica si lega ai dati** | D:L133-134 | Sequenza, melodie e dinamiche della musica "si legano ai dati per ancorare il materiale nella memoria" |
| 15 | **La musica non è intrattenimento** | D:L227-230, L246-248 | La musica si sceglie per le sue "precise proprietà neuroacustiche e fisiologiche", non per il valore estetico o per il piacere |
| 16 | **Sinergia olistica** | D:L231-233 | La musica funziona insieme a rilassamento, visualizzazione e suggestione per coinvolgere cervello, sensi, emozioni e immaginazione |
| 17 | **Canale verso il subconscio** | D:L66, L235-236 | La musica apre un canale di comunicazione con il subconscio e "stabilizza gli atteggiamenti" |
| 18 | **Preferenze individuali** | T:L80-85 | La musica classica non migliora la prestazione in tutti. Aiuta chi la ama e può distrarre chi non la tollera. Le risposte individuali vanno valutate |
| 19 | **La tecnologia va integrata con il lavoro psicologico** | T:L25-31 | L'entrainment acustico funziona meglio se associato a condizionamento positivo, rilassamento progressivo e respirazione controllata. Le evidenze sui soli binaurali sono "ancora incerte" |
| 20 | **La voce del docente sopra la musica** | M:L116-118 | Nel concerto attivo la voce dell'insegnante deve "sovrapporsi alla musica", quindi niente musica corale o cantata |
| 21 | **Armoniche naturali** | D:L31-33; M:L123-124, L161-166 | Archi e strumenti d'epoca producono armoniche naturali ad alta frequenza "non alterate" |
| 22 | **Orecchio destro privilegiato** | D:L136-137 | L'orecchio destro avrebbe un percorso più diretto verso il centro del linguaggio, quindi va mandato più suono a destra |
| 23 | **Validazione sperimentale** | T:L96-107, L157-168 | Il metodo va validato con gruppo di controllo e misure oggettive (EEG) e soggettive (STAI) |
| 24 | **Sincronizzazione movimento-metro (Dalcroze)** | D:L255-258 | L'azione corporea si adatta ai diversi metri musicali |
| 25 | **Struttura matematica di Mozart** | M:L181-182 | Le strutture "matematiche" di Mozart "stimolano la comunicazione tra le diverse aree del cervello" |

---

## 5. Musica citata

### 5.1 Concerto passivo e barocco lento (circa 60 BPM, da 55 a 65, in 4/4, largo o andante)

| Compositore | Brano | BPM dichiarato | Uso | Righe |
|---|---|---|---|---|
| Vivaldi | Largo da "L'Inverno" (Le Quattro Stagioni) | circa 60 | concerto passivo | D:L11; M:L127 |
| Vivaldi | Largo dal Concerto in re magg. per chitarra (liuto) e archi | circa 60 | concerto passivo | D:L11-12; M:L128 |
| Vivaldi | Largo dal Concerto in do magg. per mandolino, archi e clavicembalo | circa 60 | concerto passivo | D:L12; M:L129-130 |
| Vivaldi | Andante molto dal Concerto "Con molti stromenti" in do magg. RV 558 | da 55 a 65 | concerto passivo | M:L131-132 |
| Vivaldi | Andante dal Concerto per due mandolini in sol magg. RV 532 | da 55 a 65 | concerto passivo | M:L133-134 |
| Vivaldi | Le Quattro Stagioni op. 8 (complete) | n.d. | concerto passivo, sessione 10 | M:L95-96 |
| Vivaldi | Cinque concerti per flauto e orchestra da camera | n.d. | concerto passivo, sessione 5 | M:L46-47 |
| Telemann | Largo dalla Doppia Fantasia in sol magg. per clavicembalo | circa 60 | concerto passivo | D:L14; M:L143-144 |
| J. S. Bach | Largo dal Concerto per clavicembalo in fa min. BWV 1056 | circa 60 | concerto passivo | D:L16; M:L138 |
| J. S. Bach | Aria sulla quarta corda (Air), Suite n. 3 BWV 1068 | circa 60 | concerto passivo | D:L17; M:L136-137 |
| J. S. Bach | Largo dal Concerto per clavicembalo in do magg. BWV 975 | circa 60 | concerto passivo | D:L17; M:L139-140 |
| J. S. Bach | Concerto per oboe in re min., secondo movimento | da 55 a 65 | concerto passivo | M:L141 |
| J. S. Bach | Suite per violoncello n. 1 BWV 1007, Preludio (Yo-Yo Ma) | n.d. | registrazione consigliata | M:L158-160 |
| J. S. Bach | Concerti Brandeburghesi (Tafelmusik) | n.d. | registrazione consigliata da David Fallis | M:L161-166 |
| J. S. Bach | Fantasia per organo in sol magg. BWV 572; Fantasia in do min. BWV 562 | n.d. | concerto passivo, sessione 1 | M:L11-12 |
| J. S. Bach | Preludio e fuga in sol magg. BWV 541; "Dogmatic Chorales" | n.d. | concerto passivo, sessione 2 | M:L20-21 |
| J. S. Bach | Corali dogmatici per organo BWV 680-689; Fuga in mi bem. magg. BWV 552 | n.d. | concerto passivo, sessione 9 | M:L85-86 |
| Corelli | Largo dal Concerto n. 10 in fa magg., "Dodici Concerti Grossi, Op. 5" | circa 60 | concerto passivo | D:L19; M:L146-147 |
| Corelli | Concerti grossi op. 6 nn. 4, 10, 11, 12 | n.d. | concerto passivo, sessione 4 | M:L39 |
| Corelli | Concerti grossi op. 6 nn. 2, 8, 5, 9 | n.d. | concerto passivo, sessione 6 | M:L61 |
| Albinoni | Adagio in sol min. "per Archi" (D) / "per archi e organo" (M) | circa 60 | concerto passivo | D:L21; M:L149 |
| Caudioso (in M "Giovanni Battista Caudioso") | Largo dal Concerto per mandolino e archi | circa 60 | concerto passivo | D:L23; M:L150-151 |
| Pachelbel | Canone in re | circa 60 | concerto passivo | D:L25; M:L153 |
| Händel | "A tempo giusto" dal Concerto grosso in sol magg. op. 6 n. 1 | da 55 a 65 | concerto passivo | M:L155-156 |
| Händel | Concerti grossi (Tafelmusik) | n.d. | registrazione consigliata | M:L163-164 |
| Händel | Concerto per organo e orchestra in si bem. magg. op. 7 n. 6 | n.d. | concerto passivo, sessione 3 | M:L29-30 |
| Händel | "Wassermusik" | n.d. | concerto passivo, sessione 7 | M:L68 |
| F. Couperin | "Le Parnasse" (Apoteosi di Corelli), "L'Astrée" | n.d. | concerto passivo, sessione 8 | M:L75-76 |
| J.-Ph. Rameau | "Pièces de clavecin" n. 1 e n. 5 | n.d. | concerto passivo, sessione 8 | M:L77-78 |
| Vivaldi, Bach (generico) | barocco lento | "esattamente" 60 | concerto passivo Tango-Mind, Fase 4 | T:L77-78, L200-202, L263 |

### 5.2 Concerto attivo ("alta frequenza", da 5.000 a 8.000 Hz secondo M e T; da 7.000 a 8.000 Hz secondo D:L105)

| Compositore | Brano | Uso | Righe |
|---|---|---|---|
| Mozart | Sinfonia "Haffner" n. 35 KV 385 | concerto attivo (sessione 3) | D:L87; M:L24-25, L183 |
| Mozart | Sinfonia "Praga" n. 38 KV 504 | concerto attivo (sessione 3) | D:L87; M:L26-27, L184 |
| Mozart | Sinfonie nn. 29 (KV 201), 32, 39, 40 (KV 550) | concerto attivo (sessione 1); "Sound Therapy per la ricarica cerebrale" | D:L87; M:L6-9, L197-198 |
| Mozart | Concerti per violino nn. 1, 2, 3, 4 (KV 218), 5 (KV 219) | concerto attivo (il n. 5 nella sessione 1) | D:L87-88; M:L4-5, L185-186 |
| Mozart | Concerti per pianoforte n. 18 KV 456 e n. 23 KV 488 | concerto attivo (sessione 10) | D:L88-89; M:L89-93, L187-189 |
| Mozart | Quartetti per archi, Sinfonia Concertante, Controdanze | concerto attivo | D:L89; M:L199 |
| Mozart | Eine kleine Nachtmusik KV 525, in particolare la Romance (Andante) | concerto attivo | M:L190-191 |
| Mozart | Sonata per due pianoforti in re magg. KV 448 | "Effetto Mozart" (Rauscher e Shaw) | M:L192-196 |
| Mozart, Beethoven (generico) | "musica ad alta frequenza" | concerto attivo Tango-Mind | T:L74, L199, L259-260 |
| Beethoven | Concerto per violino in re magg. op. 61 | concerto attivo (sessione 6) | D:L93; M:L50-52, L201-202 |
| Beethoven | Concerto per pianoforte n. 5 op. 73 | concerto attivo (sessione 5) | M:L42-45 |
| Brahms | Concerto per violino in re magg. op. 77 | concerto attivo (sessione 8) | D:L95; M:L71-73, L203-204 |
| Čajkovskij | Concerto per pianoforte n. 1 in si bem. min. op. 23 | concerto attivo (sessione 7) | D:L97; M:L64-66, L206-207 |
| Čajkovskij | Concerto per violino in re magg. op. 35 | concerto attivo (sessione 9) | D:L97-98; M:L81-83, L208 |
| Chopin | Valzer | concerto attivo | D:L100; M:L209 |
| Haydn | Sinfonie n. 67 in fa magg. e n. 68 in si bem. magg. | concerto attivo | D:L102; M:L210-211 |
| Haydn | Concerti per violino n. 1 in do magg. e n. 2 "in G Major" | concerto attivo (sessione 2) | M:L15-18 |
| Haydn | Sinfonie n. 101 "L'Horloge" e n. 94 | concerto attivo (sessione 4) | M:L33-37 |

### 5.3 Canto e "ricarica"

| Esecutori | Uso | Righe |
|---|---|---|
| Canto gregoriano, monaci dell'Abbazia di Solesmes (Francia) | "terapia di ricarica isolata", mai come sottofondo del concerto attivo | M:L104-106 |
| Canto gregoriano, monache benedettine dell'Abbazia di Santa Cecilia (Isola di Wight) | idem; "stimolazione corticale" | M:L107-109 |

### 5.4 Compositori contemporanei e brani neuro-acustici

| Autore | Brano | BPM | Uso dichiarato | Righe |
|---|---|---|---|---|
| Janalea Hoffman | Mind Body Tempo (pianoforte e orchestra) | 60 | ridurre l'ansia da esame negli studenti di infermieristica | D:L71; M:L220-221 |
| Janalea Hoffman | Deep Daydreams | lato A 60, lato B 50 | prima sincronizzare il corpo, poi la visualizzazione profonda | D:L71-72; M:L223-225 |
| Janalea Hoffman | Music for Mellow Minds; Music to Facilitate Imagery (pianoforte e archi) | 60 (implicito) | rilassamento, immaginazione | D:L72-73; M:L226 |
| Janalea Hoffman | Children's Meditation Tape ("The Dolphin Song") | n.d. | meditazione per bambini | D:L73; M:L227-228 |
| Janalea Hoffman | Rhythmic Medicine (video) | 60 e 50 | immagini sincronizzate, biofeedback | D:L73-74; M:L229-230 |
| William Duncan | Exultate – Music to Expand Learning (chitarra) | 60 | apprendimento | D:L78; M:L231-233 |
| André Gagnon | Lullaby for My Mother (album *The St. Lawrence*, Columbia) | n.d. ("stile barocco" lento) | concerto passivo | D:L80-81; M:L234-237 |
| Steven Halpern | Anti-Frantic Alternative | n.d. | stato profondo di quiete | M:L238-240 |
| Daniel Kobialka e Steven Halpern | brani orchestrali | n.d. | usati da Charles Schmid nei laboratori Languages in New Dimensions per lo "sblocco emotivo" e i "viaggi nella mente" | M:L241-244 |
| Dyveke Spino | musiche ad "altissima frequenza" | n.d. | seminari sportivi e didattici "Education for the New Millennium" | M:L245-248 |
| Kitaro | Silk Road, con segnali Hemi-Sync (Edrington) | n.d. | matematica, Tacoma | M:L249-254 |
| Vangelis | China, con segnali Hemi-Sync | n.d. | ortografia | M:L255-256 |
| Paul Horn | "musica melodica per auto" | n.d. | scrittura creativa | M:L257-258 |
| Musica classica "50-60 bpm" (studio filippino 2023) | n.d. | 50-60 | risoluzione di Sudoku | T:L81-85 |
| Turning Sound (Abrezol) | barocco alterato elettronicamente | n.d. | memorizzazione, controllo del dolore | D:L141-157 |

### 5.5 Frequenze e toni (non brani)

| Fonte | Frequenza | Effetto dichiarato | Righe |
|---|---|---|---|
| Hemi-Sync, esempio | 100 Hz a sinistra + 105 Hz a destra = 5 Hz | il cervello "risuona a 5 Hz" | D:L160-162 |
| Cousto, Do diesis | 136,10 Hz (anno terrestre; OM) | calmante, meditativo, centrante; turchese-verde | D:L197-199; M:L264-266 |
| Cousto, Sol | 194,71 Hz (giorno terrestre) | dinamico, energizzante; rosso-arancio | D:L194-195; M:L267-268 |
| Cousto, Fa | 172,06 Hz (anno platonico, circa 26.000 anni) | gioioso, spirituale; viola-violetto | D:L201-203; M:L269-270 |
| Capel e Beck | 10 Hz | serotonina | D:L211-212 |
| Capel e Beck | da 90 a 111 Hz | beta-endorfine | D:L214 |
| Capel e Beck | circa 4 Hz | catecolamine | D:L216 |
| Brain Tuner | 256 frequenze | "migliorare le funzioni cerebrali" | D:L218-219 |
| Carlson | 5.000 Hz pulsati | piante (+700%) | D:L221-224 |
| Tomatis | da 5.000 a 8.000 Hz (massimo a 8.000) | "ricarica" più rapida | D:L119-120; T:L196 |

---

## 6. Affermazioni verificabili (claim)

### 6.1 File T (Tango-Mind)

| # | Affermazione | Righe | Red flag |
|---|---|---|---|
| T-c1 | Hemi-Sync è stato sviluppato dall'Istituto Monroe. Toni leggermente diversi per orecchio producono un "battito binaurale" che "favorisce stati focalizzati di coscienza" | T:L17-20 | no (attribuzione); sì per l'effetto |
| T-c2 | L'AVE è "ancora più potente" dei binaurali: aumenta il flusso sanguigno nella corteccia prefrontale e riduce "drasticamente" l'ansia da esame e i deficit di attenzione | T:L21-24 | **sì** |
| T-c3 | Kasina e Limina (MindPlace) e DAVID / DAVID Delight sono dispositivi AVE | T:L21, L184-185 | no |
| T-c4 | Una revisione sistematica su PLoS One (2023) trova incerta l'efficacia dei soli binaurali sull'attività oscillatoria: 5 studi a favore, 8 contrari, 1 misto | T:L25-28 | no |
| T-c5 | La tecnologia acustica funziona meglio associata a condizionamento positivo, rilassamento progressivo e respirazione | T:L29-31 | no (plausibile, senza fonte) |
| T-c6 | Gli ochos e i pivot del tango "simulano a livello neurologico" l'effetto della Infinity Walk | T:L38-40 | **sì** |
| T-c7 | La Infinity Walk è della psicologa (dott.ssa) Deborah Sunbeck | T:L40, L154 | no |
| T-c8 | Camminare "a otto" costringe a coordinare gli emisferi attraverso il corpo calloso, sblocca le inibizioni e prepara a problemi complessi e nuove lingue | T:L41-44 | **sì** |
| T-c9 | L'"Assunzione di Ruolo" è un concetto suggestopedico | T:L46-47 | no |
| T-c10 | "La ricerca empirica ha dimostrato in modo incontrovertibile che la musica classica migliora la memoria" | T:L67-68 | **sì** |
| T-c11 | Test del 2003 su adolescenti: 84,2% con musica classica contro 74,2% in silenzio (oggetti, parole, numeri) | T:L68-71, L166-168 | **sì** (studio non identificato) |
| T-c12 | Mozart e Beethoven sono "musica ad alta frequenza che ricarica le batterie cerebrali secondo il Dr. Tomatis" | T:L74-75 | **sì** |
| T-c13 | I due "concerti" sono di Lozanov. Il passivo usa cicli esatti di 8 s (4 + 4) a 60 bpm e consolida a lungo termine | T:L72-79 | **sì** (attribuzione dei cicli a Lozanov ed effetto) |
| T-c14 | Studio filippino del 2023: la musica classica a 50-60 bpm non migliora automaticamente il Sudoku; aiuta chi ama il genere e distrae chi non lo tollera | T:L80-85 | no |
| T-c15 | Image Streaming / "Spettacolo Intimo" teorizzato da Win Wenger | T:L90-91, L242-243 | no (attribuzione) |
| T-c16 | L'Image Streaming "forza" l'emisfero sinistro a collaborare "massicciamente" con il destro | T:L93-94, L244-245 | **sì** |
| T-c17 | Il calo della tensione è "uno dei maggiori benefici documentati" di Superlearning e Hemi-Sync | T:L103-105 | **sì** |
| T-c18 | Il progetto "si basa sull'evidenza" che l'apprendimento ottimale richiede l'integrazione simultanea di conscio, subconscio, corpo, sensi ed emozioni | T:L128-130 | **sì** |
| T-c19 | Il paradigma accademico si rivolge "quasi esclusivamente all'emisfero sinistro" | T:L139-141 | **sì** |
| T-c20 | L'apprendimento è "radicalmente accelerato" con integrazione emisferica, entrainment e coinvolgimento vestibolare (presentata come ipotesi da testare) | T:L141-144 | **sì** |
| T-c21 | AVE e binaurali abbassano l'ansia e inducono alfa e theta | T:L146-148 | **sì** |
| T-c22 | Barocco a 60 bpm e Mozart "sincronizzano il battito cardiaco, espandono la memoria e ricaricano l'energia corticale" | T:L149-151 | **sì** |
| T-c23 | Il tango costringe i due emisferi a "comunicare continuamente" per equilibrio e coordinazione | T:L152-156 | **sì** |
| T-c24 | L'EEG può monitorare la "sincronizzazione degli emisferi" e l'aumento della potenza alfa e theta durante l'entrainment | T:L161-162 | no |
| T-c25 | Lo STAI è un questionario clinico standard usato negli studi neuro-acustici | T:L163-165 | no |
| T-c26 | La respirazione 4-4-4-4 sincronizza gli emisferi e aumenta l'ossigenazione cerebrale | T:L180-182 | **sì** |
| T-c27 | Con l'AVE il cervello è guidato "mediante la Frequency Following Response" verso stati che superano blocchi e ansia | T:L185-187 | **sì** |
| T-c28 | Il vestibolo è la "bussola" del corpo e coordina "tutti i movimenti muscolari" e l'orientamento contro la gravità | T:L193-195 | sì (generalizzazione) |
| T-c29 | Le "cellule del Corti" trasformano i suoni da 5.000 a 8.000 Hz "in energia elettrica pura per ricaricare la neocorteccia" | T:L195-197 | **sì** |
| T-c30 | Il barocco "esattamente a 60" bpm abbassa la pressione e rallenta il cuore | T:L200-202 | **sì** |
| T-c31 | Il passaggio dal mondo 3D a quello 2D "crea spesso disconnessioni neurologiche" | T:L208-210 | **sì** |
| T-c32 | Il movimento ritmico è "letteralmente" un nutriente: i fluidi dei canali semicircolari inviano segnali che creano nuove connessioni | T:L210-212 | **sì** |
| T-c33 | Declamare ballando scioglie "l'inibizione logica dell'emisfero sinistro" grazie all'impegno del destro | T:L216-218 | **sì** |
| T-c34 | Con l'identità fittizia la mente assimila "senza il filtro critico… dell'Ego" | T:L226-228 | **sì** |
| T-c35 | L'Image Streaming stimola "la crescita della densità sinaptica" | T:L245-246 | **sì** |
| T-c36 | 15 minuti di binaurali o AVE "abbattono i picchi di cortisolo" | T:L250-252 | **sì** |
| T-c37 | La deambulazione controlaterale integra "i lobi frontali e il cervelletto" | T:L254-255 | **sì** |
| T-c38 | Nel concerto passivo l'attività cerebrale "si allinea alla metrica del suono", consolida la memoria "senza alcuno sforzo cosciente" e riduce frequenza cardiaca e "stress arterioso" | T:L263-265 | **sì** |
| T-c39 | Il syllabus potrà "rivoluzionare i tempi e la qualità dell'educazione superiore" | T:L266-268 | **sì** |

### 6.2 File D (compendio Superlearning)

| # | Affermazione | Righe | Red flag |
|---|---|---|---|
| D-c1 | La "scoperta rivoluzionaria" della musica per l'apprendimento rapido viene da scienziati del blocco sovietico | D:L5-7 | sì (enfasi) |
| D-c2 | La musica barocca del XVII e XVIII secolo ha "effetti potenti sulla mente e sulla memoria" | D:L7-8 | **sì** |
| D-c3 | La sezione chiave è il largo o andante a circa 60 bpm (da 55 a 65) | D:L28-30 | no |
| D-c4 | Gli strumenti a corda producono suoni ricchi di armoniche naturali ad alta frequenza | D:L31-33 | no |
| D-c5 | Durante i larghi la pressione si abbassa e il battito rallenta | D:L36-37 | **sì** |
| D-c6 | Calano i "fattori di stress nel sangue", "probabilmente migliorando il sistema immunitario" | D:L39 | **sì** |
| D-c7 | EEG: beta −6% e alfa +6% in media | D:L41-42 | **sì** (senza fonte) |
| D-c8 | Gli emisferi destro e sinistro si sincronizzano | D:L44 | **sì** |
| D-c9 | La musica induce il "rilassamento allerta" | D:L46-47 | sì |
| D-c10 | Il barocco lento promuove la "supermemoria" | D:L49-50 | **sì** |
| D-c11 | Provoca una sensazione di "espansione del tempo" | D:L52 | sì |
| D-c12 | Gli effetti corrispondono a quelli della meditazione con mantra "senza… alcuno sforzo" | D:L54-55 | **sì** |
| D-c13 | Il ritmo 4 + 4 s "aiuta le cellule cerebrali ad assorbire e registrare meglio i dati" | D:L58-61 | **sì** |
| D-c14 | La musica aiuta a comunicare con il subconscio e a stabilizzare gli atteggiamenti | D:L66 | **sì** |
| D-c15 | Si consiglia di ascoltare almeno 20 minuti | D:L68 | no |
| D-c16 | La musica di Hoffman ha effetti positivi su pressione, aritmie, insonnia e ansia da test (il soggetto di "Ha notato" è ambiguo) | D:L75-76 | **sì** |
| D-c17 | Mozart è ricco di suoni "a ultra-alta frequenza (fino a 8.000 Hz)" e ricarica più rapidamente le "batterie del cervello" | D:L90-91 | **sì** |
| D-c18 | Il concerto attivo usa 7.000-8.000 Hz, le più efficaci; la musica a 60 bpm arriva a circa 5.000 Hz | D:L105-107 | **sì** |
| D-c19 | La musica dà una "potente spinta energetica alla corteccia" | D:L109-110 | **sì** |
| D-c20 | "La ricerca mostra" che la musica ad alta frequenza armonizza ed energizza il cervello, sostituendo il malessere con il benessere | D:L112-113 | **sì** |
| D-c21 | Tomatis: il suono è un "nutriente" che ricarica le cellule dei "nuclei grigi centrali", che agiscono come "piccole batterie elettriche" | D:L115-117 | **sì** |
| D-c22 | Tomatis: da 5.000 a 8.000 Hz la ricarica è più rapida, al massimo a 8.000 Hz | D:L119-120 | **sì** |
| D-c23 | 10 minuti di Mozart alzano di 8-9 punti il QI spaziale, effetto che svanisce rapidamente | D:L122-123 | no (studio identificabile) |
| D-c24 | Musica, melodie e dinamiche si legano ai dati e li ancorano | D:L133-134 | sì |
| D-c25 | L'orecchio destro ha un percorso più diretto ed efficiente verso il centro del linguaggio, quindi va inviato più suono a destra | D:L136-137 | **sì** |
| D-c26 | Il Turning Sound è stato sviluppato dal sofrologo svizzero Raymond Abrezol | D:L141-143 | no |
| D-c27 | Lo spostamento del suono tra le orecchie stimola alternativamente gli emisferi | D:L145-146 | **sì** |
| D-c28 | Il Turning Sound induce uno stato "in cui il dolore non ferisce" (atleti, parto) | D:L151-152 | **sì** |
| D-c29 | Il Turning Sound crea uno stato ideale per la memorizzazione accelerata (7-8 s di osservazione) | D:L154-155 | **sì** |
| D-c30 | Esempio binaurale: 100 Hz e 105 Hz producono una risonanza a 5 Hz | D:L160-162 | no (meccanismo percettivo) |
| D-c31 | L'entrainment porta il cervello in schemi sincronizzati "in pochi secondi" | D:L164-165 | **sì** |
| D-c32 | Binaural Phaser di Devon Edrington con sei schemi di frequenza | D:L170-172 | no |
| D-c33 | Patten e Isaacs: i nastri "Brain/Mind Resonance" evocano "stati di gioia, unità, beatitudine" | D:L175-182 | **sì** |
| D-c34 | Ololofonia di Hugo Zucarelli: induce sinestesia e potenzia l'imaging | D:L184-188 | **sì** |
| D-c35 | Frequenze planetarie di Cousto: Sol 194,71 Hz, Do diesis 136,10 Hz, Fa 172,06 Hz, con colori ed effetti emotivi | D:L190-203 | **sì** |
| D-c36 | 136,10 Hz è la frequenza del tono fondamentale "OM" della musica indiana | D:L199 | sì |
| D-c37 | Diapason tarati applicati ai punti di agopuntura | D:L204-205 | **sì** |
| D-c38 | Capel e Beck: impulsi elettrici o toni a 10 Hz aumentano la serotonina; da 90 a 111 Hz le beta-endorfine; circa 4 Hz le catecolamine | D:L207-216 | **sì** |
| D-c39 | Il Brain Tuner raggruppa 256 frequenze e migliora le funzioni cerebrali | D:L218-219 | **sì** |
| D-c40 | Dan Carlson: 5.000 Hz pulsati nel barocco aumentano del 700% l'assorbimento di nutrienti nelle piante (ipotesi estesa all'uomo) | D:L221-224 | **sì** |
| D-c41 | "Ogni tipo di musica è stato testato" e quella a 60 battiti ha dato i migliori risultati | D:L229-230 | **sì** |
| D-c42 | La musica riduce stress, ansia e tensione, con meno mal di testa e "miglioramento delle allergie" | D:L238-240 | **sì** |
| D-c43 | Le basse frequenze (traffico, aeroporti, cantieri, rock martellante) "drenano" il cervello | D:L242-244 | **sì** |

### 6.3 File M (repertorio)

| # | Affermazione | Righe | Red flag |
|---|---|---|---|
| M-c1 | Esiste un "Programma Musicale Ufficiale della Suggestopedia (Capitolo 31)" con 10 sessioni (fonte non dichiarata) | M:L1 | sì (fonte non dichiarata) |
| M-c2 | Il Concerto per pianoforte op. 73 di Beethoven è indicato "in B-flat"; il testo stesso nota che è in mi bemolle | M:L42-45 | no (refuso dichiarato) |
| M-c3 | La Sinfonia n. 101 "L'Horloge" di Haydn è indicata "in C Major" | M:L33 | da verificare |
| M-c4 | Il Concerto per violino n. 2 di Haydn è indicato "in G Major" | M:L17-18 | da verificare |
| M-c5 | Tomatis definisce il canto gregoriano "sublime cibo per il cervello", capace di ricaricare le cellule cerebrali grazie alle armoniche superiori | M:L100-103 | **sì** |
| M-c6 | Le registrazioni di Solesmes e di Santa Cecilia (Isola di Wight) sono raccomandate per la "stimolazione corticale" | M:L104-109 | sì |
| M-c7 | Il largo barocco è "rigorosamente" tra 55 e 65 BPM, in 4/4 | M:L122-124 | sì ("rigorosamente") |
| M-c8 | Corelli: il Concerto n. 10 in fa maggiore è indicato come tratto dai "Dodici Concerti Grossi, Op. 5" | M:L146-147; D:L19 | da verificare |
| M-c9 | Il compositore del concerto per mandolino è "Giovanni Battista Caudioso" | M:L150 | da verificare |
| M-c10 | David Fallis raccomanda Tafelmusik, orchestra canadese su strumenti d'epoca con armoniche "naturali e non alterate" | M:L161-166 | sì (sulle armoniche) |
| M-c11 | La musica del concerto attivo (da 5.000 a 8.000 Hz) "ricarica elettricamente le cellule cerebrali" | M:L177-179 | **sì** |
| M-c12 | Le strutture matematiche di Mozart stimolano la comunicazione tra aree cerebrali | M:L181-182 | **sì** |
| M-c13 | La Sonata K. 448 è stata usata da Rauscher e Shaw (UC Irvine) per mostrare +8-9 punti di QI spaziale dopo 10 minuti | M:L192-196 | no (studio identificabile) |
| M-c14 | Le Sinfonie 29, 32, 39 e 40 sono usate in "Sound Therapy" per la ricarica cerebrale | M:L197-198 | sì |
| M-c15 | Janalea Hoffman, musicoterapeuta della Kansas University, tara il metronomo sul ritmo cardiaco a riposo | M:L217-219 | no |
| M-c16 | Mind Body Tempo è stata usata per ridurre l'ansia da esame negli studenti di infermieristica | M:L220-221 | no (verificabile) |
| M-c17 | Deep Daydreams: lato A a 60 BPM, lato B a 50 BPM | M:L223-225 | no |
| M-c18 | Rhythmic Medicine: video a 60 e 50 BPM con immagini "per il biofeedback" | M:L229-230 | sì |
| M-c19 | Exultate di William Duncan è un album di brani per chitarra interamente a 60 BPM | M:L232-233 | no |
| M-c20 | André Gagnon, franco-canadese: Lullaby for My Mother dall'album *The St. Lawrence* (Columbia Records) | M:L234-237 | no (verificabile) |
| M-c21 | Steven Halpern, "pioniere della New Age": Anti-Frantic Alternative | M:L238-240 | no |
| M-c22 | Charles Schmid usava Kobialka e Halpern nei laboratori Languages in New Dimensions | M:L241-244 | no |
| M-c23 | Dyveke Spino, pianista "danese-americana": musica ad "altissima frequenza" nei seminari "Education for the New Millennium" | M:L245-248 | sì |
| M-c24 | Devon Edrington, nelle elementari di Tacoma, ha integrato Hemi-Sync in Kitaro (matematica), Vangelis (ortografia) e Paul Horn (scrittura) | M:L249-258 | no (verificabile) |
| M-c25 | Hans Cousto, *The Cosmic Octave*: frequenze calcolate sui movimenti planetari; Do diesis 136,10 Hz è la "frequenza di oscillazione dell'India" (OM); Fa 172,06 Hz è l'anno platonico di circa 26.000 anni | M:L261-270 | **sì** (effetti) |

---

## 7. Rischi per i partecipanti (safety)

| # | Rischio | Righe | Perché |
|---|---|---|---|
| S1 | **Occhiali stroboscopici (AVE)** | T:L21-24, L183-187, L250-252 | La luce intermittente può scatenare crisi in chi ha epilessia fotosensibile, anche non diagnosticata, ed emicrania. Il testo non prevede screening, controindicazioni o consenso informato e propone l'uso a un'aula intera |
| S2 | **Apnea di 4 s nella respirazione quadrata** | T:L180-182 | È una tecnica in genere lieve. Ripetuta a lungo può però dare capogiri. La promessa di "aumentare l'ossigenazione cerebrale" è un'aspettativa errata. Serve cautela con disturbi cardio-respiratori, attacchi di panico e gravidanza, e prima di passare subito al ballo |
| S3 | **Passaggio rapido da stati di rilassamento profondo al movimento** | T:L250-255 | Dopo 15 minuti di AVE o binaurali si passa al tango, con pivot e ochos. Sonnolenza o disorientamento dopo l'entrainment possono favorire perdite di equilibrio e cadute. Il protocollo non prevede una fase di riattivazione |
| S4 | **Lavoro vestibolare intenso** (pivot, ochos, camminata a otto) | T:L38-44, L193-195, L253-255 | Possibili vertigini in chi ha disturbi vestibolari, labirintite, ipotensione ortostatica o in età avanzata |
| S5 | **Doppio compito: ballare mentre si declamano concetti** | T:L216-218, L256-258 | L'attenzione divisa in coppia aumenta il rischio di collisioni in pista e di errori di guida e marca |
| S6 | **Sdraiarsi a occhi chiusi dopo il ballo e rialzarsi** | T:L261-265; D:L36-37 | Il testo dichiara che la musica abbassa la pressione. Se così fosse, rialzarsi in fretta può dare capogiri a chi è ipoteso. Manca una fase di uscita graduale |
| S7 | **Assunzione di ruolo "per tutta la durata del laboratorio" e "Riprogrammazione Subliminale"** | T:L219-228 | Lo scopo dichiarato è aggirare "il filtro critico… dell'Ego". In persone vulnerabili (dissociazione, disturbi dell'identità, trauma) può destabilizzare. Pone anche una questione etica di consenso: si agisce sotto la soglia critica |
| S8 | **Stati a occhi chiusi, immaginazione guidata, "sblocco emotivo", "viaggi nella mente"** | T:L242-246; M:L241-244; D:L66 | Possono riaffiorare ricordi traumatici o emozioni intense. Serve una conduzione informata sul trauma, con diritto di uscita e contenimento |
| S9 | **Dispositivi elettrici di stimolazione** (impulsi a bassa frequenza, Brain Tuner) | D:L207-219 | La stimolazione elettrica cranica è controindicata con pacemaker o dispositivi impiantati, epilessia e gravidanza. Non è un uso da aula didattica. Le promesse sui neurotrasmettitori sono di tipo medico |
| S10 | **Volume asimmetrico e cuffie** | D:L136-137; T:L16-20 | "Più suono all'orecchio destro" e l'ascolto in cuffia prolungato rischiano esposizioni eccessive. Ballare in cuffia aumenta anche il rischio di collisioni |
| S11 | **Ascolto durante gli spostamenti** | D:L128-129 | Audio di rilassamento, binaurale o Turning Sound non va mai usato alla guida o in situazioni che richiedono vigilanza. Il testo parla di "spostamenti" senza distinguere |
| S12 | **Promesse sanitarie** | D:L36-44, L75-76, L151-152, L238-240; T:L200-202, L263-265 | Pressione, aritmie, insonnia, sistema immunitario, allergie, mal di testa, dolore del parto: queste promesse possono spingere a ritardare o sostituire cure mediche e vanno trattate come pubblicità sanitaria |
| S13 | **Diapason su punti di agopuntura** | D:L204-205; M:L262-263 | Il rischio fisico è minimo. Il problema è il confine di competenza (atti para-sanitari) e l'efficacia attribuita |
| S14 | **Promesse di risultato irrealistiche** | T:L67-68, L141-144, L264, L266-268; D:L5-8, L49-50 | "Incontrovertibile", "radicalmente", "senza alcuno sforzo cosciente", "rivoluzionare", "supermemoria": aspettative irrealistiche, rischio di delusione e di pubblicità ingannevole verso gli allievi |
| S15 | **Sperimentazione su studenti** (EEG, STAI, gruppo di controllo) | T:L96-107, L157-168 | Serve l'approvazione di un comitato etico, il consenso informato, la tutela dei dati personali e sanitari (GDPR) e la possibilità di ritirarsi senza conseguenze sul voto |
| S16 | **Etichettare alcuni suoni come "drenanti"** | D:L242-244 | Il rischio fisico è basso, ma si può creare un effetto nocebo e un'ansia inutile verso suoni comuni |

---

## 8. Idee originali o riusabili per il metodo (senza giudizio di validità)

1. **Lezione in 4 fasi che alterna corpo e concerti.** Induzione → tango → concerto attivo *in movimento* → concerto passivo *da sdraiati* (T:L248-265). È un formato già pensato per una lezione di 2 ore.
2. **Concerto attivo fatto camminando o durante i passi base** (T:L256-258) invece che da seduti, come in Lozanov e in Ostrander.
3. **Concerto passivo "dopo il ballo"**: si usa la stanchezza fisica come porta d'ingresso al rilassamento (T:L76).
4. **Ochos e pivot come "Infinity Walk"** (T:L38-44, L213-216): il vocabolario del tango (giri, ochos, pivot, camminata incrociata) letto come lavoro sul movimento a otto e controlaterale.
5. **Identità fittizia da "ballerino di Buenos Aires"** (T:L47-48, L225): l'assunzione di ruolo suggestopedica applicata a un'identità di danza.
6. **Image Streaming durante i passi o subito dopo** (T:L91-94, L242-244): verbalizzare le immagini che nascono dal movimento e dalla musica.
7. **Un modulo critico sulle evidenze dentro il corso** (T:L25-31): insegnare agli allievi i limiti dell'entrainment.
8. **Misurare anche la performance motoria** (acquisizione delle figure, coordinazione, equilibrio) accanto a memoria e ansia (T:L106-107).
9. **Personalizzare la musica** in base alle preferenze individuali (T:L80-85).
10. **Tempo discendente 60 → 50 BPM** per approfondire il rilassamento (Hoffman, M:L223-225).
11. **Un brano associato a ogni materia** (Edrington: Kitaro per la matematica, Vangelis per l'ortografia, Horn per la scrittura, M:L253-258). Trasposizione al tango: una musica di riferimento per ogni elemento (camminata, ochos, giro).
12. **"Tono di respirazione" dentro la musica** per guidare il respiro (Turning Sound, D:L148-149).
13. **Ciclo "osserva 7-8 s, poi rilassati"** (D:L154-155) come alternativa al 4 + 4.
14. **Gregoriano come "ricarica" separata**, mai come sottofondo della voce (M:L116-118).
15. **Strumenti d'epoca** per il materiale del concerto passivo (M:L161-166).
16. **Rimbalzi di palla sui diversi metri (Dalcroze)** (D:L255-258): trasferibile alla musicalità del tango (2/4, 4/4, 3/4 del vals; tiempo, contratiempo, doble tiempo) e al ritmo del Qigong.
17. **Programma in 10 sessioni con repertorio diverso ogni volta** (M:L1-96): il repertorio ruota e il concerto attivo usa opere intere (da 37 a 81 minuti di musica elencata per sessione).
18. **Ascolto quotidiano di almeno 20 minuti** come compito tra una lezione e l'altra (D:L68).

---

## 9. Incoerenze interne e refusi rilevati **[nota dell'estrattore]**

- I cicli 4 + 4 s sono nel concerto passivo in T:L76-78 e nel concerto attivo in T:L256-260.
- I moduli di T-A (L11-94) e di T-C (L170-246) hanno numerazione e contenuti diversi. Per esempio il "Modulo 3" è "Ritmo e Memoria" in T-A e "Tango come Laboratorio Cinestesico" in T-C.
- La banda di frequenza del concerto attivo è da 7.000 a 8.000 Hz in D:L105 e da 5.000 a 8.000 Hz in M:L178-179 e T:L196.
- L'Adagio di Albinoni è "per Archi" in D:L21 e "per archi e organo" in M:L149.
- "Caudioso" in D:L23 diventa "Giovanni Battista Caudioso" in M:L150.
- I "tre toni di voce distinti" sono citati (T:L259) ma non descritti.
- Refusi nel programma M: "maestoto" (L65) per *maestoso*, "Vivace assasi" (L36) per *assai*. "Op. 73" in si bemolle è annotato dal testo stesso (L44-45).
- T:L2 contiene "movimento sico" (fisico), e simili per via delle legature perse (vedi sezione 0).
- Il file D si interrompe dopo il primo esercizio Dalcroze (D:L258).
