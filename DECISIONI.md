# Registro delle decisioni del progetto Superapprendimento

Versione 1, 4 ottobre 2026. Redatto dall'analista sulla base dei file in `ricerca/`.

---

## 1. Scopo del registro

Il progetto Superapprendimento costruisce un metodo didattico fondato sulla Desuggestopedia di Georgi Lozanov, da applicare in quattro contesti: corsi di tango argentino, corsi di Qigong, formazione degli insegnanti, un corso universitario. L'autore del metodo è un docente certificato nella linea Lozanov.

Le fonti raccolte dal progetto mescolano tre cose diverse: il canone di Lozanov, il "Superlearning" commerciale americano e una serie di tecniche, dispositivi e integratori di origine diversa. Questo registro mette ogni elemento delle fonti in una scheda e lo affianca a tre informazioni: che cosa dice oggi la ricerca, che cosa dice Lozanov nel libro del 2005, quali rischi comporta.

**Regola fondamentale.** L'analista non toglie nulla. Ogni elemento delle fonti resta documentato in `ricerca/`, qualunque sia la decisione. Ogni scheda contiene una raccomandazione motivata; la decisione spetta solo all'autore. Tutte le schede partono con "Stato: IN ATTESA".

## 2. Come si legge una scheda

Ogni scheda del blocco A-G ha otto voci:

1. **Cosa dicono le fonti.** In quali file compare l'elemento, che cosa promette, come si esegue.
2. **Evidenza attuale.** Livello A-D, motivazione breve, da uno a tre riferimenti presi dai file di verifica.
3. **Compatibilità Lozanov.** Coerente, non trattato o rifiutato, con la citazione e la riga del libro.
4. **Rischi.** Chi è a rischio e che cosa può succedere.
5. **Nocciolo utile.** Ciò che può funzionare per ragioni diverse da quelle dichiarate.
6. **Raccomandazione dell'analista.** Una delle quattro opzioni standard e il perché.
7. **Precauzioni obbligatorie se l'autore decide di includerlo.** Solo dove ci sono rischi.
8. **Decisione dell'autore.** Stato e note.

Le schede del blocco H (integrazioni dalla scienza attuale) hanno una struttura propria, descritta all'inizio del blocco.

**Per registrare una decisione** basta sostituire "IN ATTESA" con, per esempio, "DECISO (data): opzione 3" e scrivere nelle note condizioni o modifiche. Una riga di motivazione aiuta chi lavorerà poi sui testi del manuale.

## 3. Legenda

### 3.1 Livelli di evidenza

| Livello | Significato |
|---|---|
| **A** solida | Letteratura ampia e coerente (meta-analisi, revisioni, fisiologia consolidata), oppure fatto storico o bibliografico documentato. |
| **B** plausibile-parziale | Prove reali ma limitate, eterogenee o di effetto modesto; oppure il claim è vero solo in una versione più prudente. |
| **C** debole-non verificata | Aneddoti, dati dichiarati dall'autore senza controllo, studi non rintracciabili, ipotesi non testate. |
| **D** smentita-pseudoscienza | Contraddetta dagli studi o dalle conoscenze di base, oppure senza meccanismo plausibile e con promesse sproporzionate. |

Quando la promessa e il nocciolo hanno livelli diversi, li indico entrambi (per esempio "D / B nocciolo").

### 3.2 Compatibilità con Lozanov

| Etichetta | Significato |
|---|---|
| **Coerente** | Lozanov afferma la stessa cosa o un principio compatibile. Coerente non vuol dire vero. |
| **Non trattato** | Il libro non tratta il tema. |
| **Rifiutato** | Lozanov lo nega esplicitamente come mezzo o come spiegazione dei risultati. Indico la riga del libro. |

"Lozanov 2005, r. NNNN" indica la riga del file `fonti/testo/Lozanov_2005_Suggestopaedia_Desuggestive_Teaching.txt`, come riportata in `ricerca/modello-canonico-lozanov.md` (soprattutto sezioni 7.1 e 9.4). "Modello r. NNN" indica una riga del modello canonico.

### 3.3 Rischio

| Livello | Significato |
|---|---|
| Alto | Danno fisico o psicologico serio possibile, anche in persone senza fragilità note. |
| Medio | Danno possibile in gruppi identificabili (per esempio epilessia, disturbi vestibolari, trauma). |
| Basso | Disagio lieve e reversibile, o rischio solo per pochi. |
| Nessuno rilevante | Nessun rischio fisico o psicologico oltre quelli ordinari di una lezione. Eventuali rischi reputazionali sono indicati a parte. |

### 3.4 Opzioni di decisione standard (schede D-01 - D-33)

1. **Fuori dal metodo, resta documentato in `ricerca/`.**
2. **Modulo sperimentale opzionale con avvertenze** (separato dalla lezione, facoltativo, dichiarato non lozanoviano, con precauzioni e, se possibile, una misura prima e dopo).
3. **Nel metodo, riformulato onestamente.**
4. **Nel metodo come nelle fonti.**

Per le integrazioni (INT-01 - INT-11) le opzioni sono: **Approvata / Approvata con modifiche / Respinta / Da discutere**.

### 3.5 Sigle delle fonti

| Sigla | File di estrazione in `ricerca/estrazioni/` | Righe citate |
|---|---|---|
| SL1-A, SL1-B, SL1-C | `superlearning1-A.md`, `-B.md`, `-C.md` | righe di `superlearning1.txt` (1-591, 592-1170, 1171-2587) |
| MAN | `manuale.md` | righe di `manuale-superapprendimento.txt` |
| DSS | `didattica-super-suggesto.md` | righe di `didattica_super_suggesto.txt` (L) |
| TM | `tango-musica.md` | T = `Superlearning_tango.txt` (progetto Tango-Mind), D = `didattica_superlearning.txt`, M = `musiche_relax_didattica.txt` |
| TLT | `teoria-lozanov-trauma.md` | R = `Ricerca_Globale_Suggestopedia_Lozanov.md`, T = `Trauma_Predictive_Coding_Metastabilita.md` |

I codici come "T04" o "A.3" sono quelli delle tecniche nelle estrazioni.

| Sigla | File di verifica in `ricerca/` |
|---|---|
| VNF | `verifica-neuro-fisiologia.md` (cluster A1-K1) |
| VTN | `verifica-tecnologie-nutrizione-clinica.md` (cluster A1-M4) |
| VPS | `verifica-pedagogia-storia-musica.md` (cluster P1-Q3) |

### 3.6 Nota sui riferimenti

I riferimenti vengono dai tre file di verifica. Alcuni sono segnalati lì come citati a memoria o "da ricontrollare": li indico così anche qui. Nel blocco H compaiono alcuni riferimenti noti che non sono nei file di verifica (Wulf 2013, Magill e Hall 1990, Engelkamp 1998, Schmidt e Lee): li segno con **[fuori dai file di verifica, da ricontrollare]**. Prima di pubblicare il manuale, tutti i riferimenti che si decide di citare vanno controllati sull'originale.

## 4. Una scelta a monte

Il canone di Lozanov rifiuta una parte consistente delle pratiche delle fonti: respirazione e rilassamento guidati, visualizzazioni, barocco lento, onde alfa ed entrainment, apparecchi, apprendimento nel sonno, PNL, ipnosi (Lozanov 2005, r. 5797-5815). Il modello canonico ne trae una conseguenza: un percorso che usa queste pratiche può chiamarsi "Superlearning" o "ispirato a Lozanov", non Suggestopedia o Desuggestopedia (modello r. 656-659, 781).

Le raccomandazioni di questo registro presuppongono che l'autore voglia un metodo fondato sul canone di Lozanov e integrato in modo dichiarato con la ricerca attuale. Un modulo sperimentale (opzione 2) può convivere con un corso lozanoviano solo se resta fuori dalla lezione e dichiarato come tale. Se l'autore preferisce che nel percorso non compaia nulla di ciò che il canone rifiuta, per le schede D-05, D-08 e D-11 l'opzione coerente diventa la 1. La questione è la prima delle Domande aperte.

---

## 5. Tabella riassuntiva

| ID | Elemento | Evidenza | Compatibilità Lozanov | Rischio | Raccomandazione | Stato |
|---|---|---|---|---|---|---|
| D-01 | Integratori e sostanze | D (B: carenze; tirosina in stress estremo) | Rifiutato (r. 1420-1421, 5811-5812) | Alto | 1 | IN ATTESA |
| D-02 | Luci stroboscopiche AVE | C / D (meccanismi) | Rifiutato (r. 1420-1421, 1824-1849) | Alto | 1 | IN ATTESA |
| D-03 | Elettrostimolazione cranica e microcorrenti | D (B: CES e ansia, prove deboli) | Rifiutato (r. 1420-1421, 2046-2047) | Medio-alto | 1 | IN ATTESA |
| D-04 | Dispositivi rotanti/vestibolari | D | Rifiutato (r. 1420-1421, 1453-1455) | Alto | 1 | IN ATTESA |
| D-05 | Respirazioni con apnea | D (ossigeno) / B (respiro lento senza apnee) | Rifiutato (r. 1407-1416, 5802-5803) | Medio | 1 per le apnee; 2 per il respiro lento senza apnee | IN ATTESA |
| D-06 | Memorie traumatiche e "riprogrammazione" | D (B: imagery rescripting clinico) | Rifiutato (r. 1400-1406, 2046-2047) | Alto | 1 | IN ATTESA |
| D-07 | Generatori ELF, magneti, Bio-Battery | D | Rifiutato (r. 1420-1421, 5811-5813) | Medio | 1 | IN ATTESA |
| D-08 | Rilassamento progressivo / Scan and Relax | B | Rifiutato (r. 1427-1428, 1626-1632) | Basso-medio | 2 | IN ATTESA |
| D-09 | Training autogeno | B (D: "azzera l'ansia") | Rifiutato (r. 1626-1632, 1807-1812) | Medio | 1 | IN ATTESA |
| D-10 | Visualizzazioni guidate e Image Streaming | D / B (nocciolo verbale) | Rifiutato (r. 1407-1416, 1440-1441) | Medio | 1; 3 per il nocciolo verbale | IN ATTESA |
| D-11 | Battiti binaurali (solo audio) | B-C | Rifiutato (r. 2077-2080, 5811-5813) | Basso | 2 | IN ATTESA |
| D-12 | Prova mentale / motor imagery | B (autogestita) / C (caso Drapeau) | Non trattato se autogestita; rifiutato se dettata (r. 1440-1441) | Basso | 3 autogestita; 1 dettata | IN ATTESA |
| D-13 | Subliminali e apprendimento nel sonno | D | Rifiutato (r. 1600-1624) | Medio | 1 | IN ATTESA |
| D-14 | Autoconvalida di Altorfer e affermazioni | D / B (rischio delle affermazioni) | Rifiutato (r. 1400-1406) | Basso-medio | 1 | IN ATTESA |
| D-15 | Ancoraggi emotivi | C / B (routine) | Rifiutato (r. 1400-1406, 1824-1849) | Basso | 3 (come INT-05) | IN ATTESA |
| D-16 | Raikov / Borrowed Genius | D / B (gioco di ruolo) | Rifiutato (r. 1392, 5815); coerenti le nuove identità (r. 759-762) | Medio-alto (versione ipnotica) | 3 (nelle nuove identità canoniche) | IN ATTESA |
| D-17 | Biofeedback, EEG/QEEG come training | B (EMG clinico) / D (colori QEEG) | Rifiutato (r. 1420-1421, 2417-2419) | Basso | 1 | IN ATTESA |
| D-18 | Barocco lento "a 60 BPM" nel concerto passivo | C / D | Rifiutato (r. 1446-1448, 1460, 5805) | Nessuno rilevante | 1 (vale il programma canonico) | IN ATTESA |
| D-19 | Effetto Mozart, Tomatis, alte frequenze, gregoriano, Forbrain, Turning Sound | D (A: resoconto di Rauscher 1993) | Rifiutato (r. 5805, 1420-1421) | Basso (medio per costo-opportunità) | 1 | IN ATTESA |
| D-20 | Accordature planetarie, 136,10 Hz, Schumann, diapason | D (A: dato geofisico) | Non trattato; apparecchi rifiutati (r. 1420-1421) | Nessuno rilevante | 1 | IN ATTESA |
| D-21 | Musica di tango o cinese nei concerti | Non applicabile / B (dati di tempo) | Non trattato; modifica del canone (r. 2923-2926, 4349-4352) | Nessuno rilevante | 3 | IN ATTESA |
| D-22 | Musiche commerciali "per l'apprendimento" | C (B: musica gradita in generale) | Rifiutato (r. 1433-1435, 5811-5813) | Nessuno rilevante | 1 | IN ATTESA |
| D-23 | Cicli 8 s / 12 s, unità di 7-9 parole, 13 minuti | D / B (pause motorie) | Rifiutato (r. 1830-1832, 4037-4060) | Basso | 1 (nocciolo in INT-11) | IN ATTESA |
| D-24 | Tre toni fissi contro intonazione oscillante | C / B (variazione) | Rifiutato il tono imperativo (r. 4089-4091); coerente l'oscillazione (r. 2709-2712) | Nessuno rilevante | 3 | IN ATTESA |
| D-25 | Infinity Walk | D (emisferi, test) / B (esercizio motorio) | Non trattato; tensione come test (r. 2046-2047) | Medio | 3 esercizio; 1 test | IN ATTESA |
| D-26 | Mappature diagnostiche | D (C: ciclo nasale) | Non trattato; in contrasto (r. 2046-2047, 2417-2419) | Medio | 1 | IN ATTESA |
| D-27 | Concerto attivo in movimento | C | Non trattato; adattamento (r. 4021-4099, 4073-4074) | Basso | 2 | IN ATTESA |
| D-28 | Tecnica Alexander | B / D ("energia", immunità) | Non trattato | Nessuno rilevante | 3 | IN ATTESA |
| D-29 | TPR, teatro e mimo, mappe e palazzo della memoria, odori, istruzione inversa, canzoni | A-B / B / C secondo la tecnica | In parte coerente (r. 4283, 2715-2716), in parte non trattato | Basso (odori) | 3 per quasi tutte; 2 palazzo della memoria; 1 odori | IN ATTESA |
| D-30 | Neuromiti nel linguaggio del metodo | D | Rifiutato (r. 1504-1507, 2077-2080, 5805) | Nessuno fisico; reputazionale | 3 | IN ATTESA |
| D-31 | Cornice predictive coding / trauma / metastabilità | B (riferimenti) / C (meccanismo) | Non trattato; vincolo r. 2046-2047 | Medio | 3 | IN ATTESA |
| D-32 | Presentazione storica | A (fatti) / C (risultati, Baba Vanga) | Coerente come resoconto; sintesi UNESCO più forte del verbale (r. 5793-5795) | Nessuno fisico; reputazionale | 3 | IN ATTESA |
| D-33 | Lezione modello di 2 ore delle fonti | C | Rifiutato nelle componenti; diversa dal ciclo canonico (r. 3932-3935) | Alto nella forma delle fonti | 3 (ricostruita sul ciclo, come pilota) | IN ATTESA |
| INT-01 | Pratica distribuita e richiamo attivo | A | Coerente, con tensione (r. 3971, 4007-4008) | Basso | Approvata con modifiche | IN ATTESA |
| INT-02 | Focus attentivo esterno | A-B | Non trattato; coerente con i dettagli sul secondo piano (r. 3129-3138) | Nessuno rilevante | Approvata | IN ATTESA |
| INT-03 | Pratica variata / interferenza contestuale | B | Coerente (r. 3860-3872, 4315-4369) | Nessuno rilevante | Approvata | IN ATTESA |
| INT-04 | Motor imagery autogestita | B | Non trattato; rifiutata se dettata (r. 1440-1441) | Basso | Approvata con modifiche | IN ATTESA |
| INT-05 | Routine pre-esecuzione | B | Non trattato; distinta dal "conditioning" (r. 1824-1849) | Nessuno rilevante | Approvata con modifiche | IN ATTESA |
| INT-06 | Esercizi vestibolo-oculari per i giri | A (riabilitazione) / B (danzatori) | Non trattato | Medio | Approvata con modifiche | IN ATTESA |
| INT-07 | Riduzione della minaccia percepita | A (ansia e prestazione) / C (meccanismo) | Coerente (r. 2802-2845, 3860-3915) | Basso | Approvata | IN ATTESA |
| INT-08 | Gesto ed effetto di esecuzione | A (azioni) / B (lessico) | Coerente (r. 4283) | Nessuno rilevante | Approvata | IN ATTESA |
| INT-09 | Canto e coro | B | Coerente, già canonico (r. 2715-2716, 4469-4470) | Nessuno rilevante | Approvata | IN ATTESA |
| INT-10 | Valutazione con misure validate | A (strumenti) | Coerente con i test "facili" (r. 4453-4459) | Basso | Approvata | IN ATTESA |
| INT-11 | Pause brevi nella pratica motoria | B | Non trattato; compatibile se non diventa ritmo fisso (r. 1830-1832) | Nessuno rilevante | Approvata | IN ATTESA |

---

## Blocco A. Sicurezza fisica e psicologica

### D-01 Integratori e sostanze (lecitina 70 g, DLPA/tirosina, glutammina, ginkgo, octacosanolo/alghe AFA/clorella, germanio, H2O2/ozono per bocca)

**Cosa dicono le fonti.** Solo SL1-A, cap. 6 "Neuro-nutrizione" (T33-T39, r. 336-444), con dosi testuali:
- lecitina o fosfatidilcolina, circa 70 g al giorno, 60-90 minuti prima di un quiz: memoria +25% per 4-5 ore, protezione da colesterolo e demenza (r. 397-405);
- DLPA e L-tirosina, 100-500 mg al giorno fino a 1.000 mg, "nessuna tossicità", 85-90% di successo su depressione e dolori intrattabili (r. 406-413); tirosina e soldati dell'esercito USA al freddo (r. 367-377);
- glutammina o acido glutammico, 1-4 g al giorno: QI da +10 a +17 punti, "fino alla guarigione completa" nel ritardo mentale (r. 348-351, 378-385, 414-419);
- ginkgo biloba, 120 mg al giorno per almeno 3 mesi (r. 420-425);
- octacosanolo, erba d'orzo, alghe verde-azzurre (AFA), spirulina e clorella a dosi "da 10 a centinaia di volte" quella raccomandata, per 4-6 settimane, proposti anche a bambini autistici per "ricostruire il tessuto nervoso" (r. 426-434);
- germanio organico, 30 mg al giorno, 1-1,5 g in fase acuta (r. 435-439);
- perossido di idrogeno all'1,5% e "ozono" in gocce, tre volte al giorno, per "risvegliare i cervelli letargici" (r. 439-444).

La stessa sezione cita ricerche reali (Wurtman sui precursori dei neurotrasmettitori, Schoenthaler sui multivitaminici).

**Evidenza attuale.** D per quasi tutte le promesse. B solo per due noccioli: un'integrazione di vitamine e minerali aiuta un poco i bambini con carenze, non chi è ben nutrito; la tirosina ad alte dosi attenua alcuni cali di prestazione in condizioni estreme (freddo, alta quota), non nello studio quotidiano. Cluster VTN I1-I10.
- Tao e Bolger 1997, *Regul Toxicol Pharmacol* 25:211-219 (germanio: almeno 31 casi di danno renale, decessi).
- Gilroy et al. 2000, *Environ Health Perspect* 108:435-439 (microcistine in 85 campioni su 87 di integratori AFA).
- DeKosky et al. 2008, *JAMA* 300:2253-2262 (ginkgo in 3.069 anziani: nessuna prevenzione della demenza).

**Compatibilità Lozanov.** Rifiutato. Tra le cause negate ci sono "magical pills; special diets" (Lozanov 2005, r. 1420-1421, 5811-5812; modello r. 611, 639).

**Rischi.**
- H2O2 e ozono per bocca: chiunque, soprattutto bambini e chi diluisce il prodotto al 35%. Ustioni gastrointestinali, embolia gassosa, ictus, morte (FDA 2006; Watt et al. 2004). Grave.
- Germanio: danno renale anche irreversibile, neuropatia, morte. Grave.
- Alghe AFA: bambini, gravidanza, malattie epatiche. Tossine epatiche.
- DLPA: fenilchetonuria, chi assume IMAO o selegilina, gravidanza. Crisi ipertensiva.
- Tirosina ad alte dosi: chi assume IMAO, levodopa, ormoni tiroidei; ipertiroidismo.
- Ginkgo: chi assume anticoagulanti o antiaggreganti, chi deve essere operato. Sanguinamenti.
- Lecitina a 70 g: disturbi gastrointestinali, diarrea, odore di pesce.
- In generale: un docente che consiglia integratori esce dal proprio ruolo; nell'UE le indicazioni sulla salute di alimenti e integratori sono regolate dal Reg. (CE) 1924/2006.

**Nocciolo utile.** Pasti regolari, sonno, idratazione; eventuali carenze si valutano con il medico. Nient'altro di specifico per l'apprendimento.

**Raccomandazione dell'analista.** Opzione 1. Nessuna di queste sostanze ha prove per l'apprendimento in persone ben nutrite, due sono pericolose e il canone le rifiuta per nome. Il capitolo resta in `ricerca/` come documento storico-critico.

**Precauzioni obbligatorie se l'autore decide di includerlo.** Solo in forma documentale; nessuna dose e nessuna istruzione d'uso; avvertenza esplicita di pericolo per H2O2, ozono e germanio; rinvio a medico o farmacista per qualsiasi integrazione; mai rivolto a minori.

**Decisione dell'autore**

Stato: IN ATTESA

Note dell'autore:

---

### D-02 Luci stroboscopiche AVE (Kasina, Limina, DAVID, occhiali Ganzfeld)

**Cosa dicono le fonti.** SL1-B T2 (r. 600-603, 717-720); TM T2 (T:L21-24, L183-187, L250-252); MAN schede dei dispositivi 1-4 (r. 93-95), A.1, A.4 e fase 1 della lezione modello (r. 114); SL1-C sez. 3 (r. 2225-2266); DSS T11 (L384-389).
- Promesse: l'AVE è "ancora più potente" dei battiti binaurali; aumenta flusso sanguigno e produzione di ATP nella corteccia prefrontale; riduce "drasticamente" ansia da esame e deficit di attenzione; il DAVID Delight aumenta serotonina, noradrenalina ed endorfine; il cervello allinea la propria frequenza a quella dello stimolo ("Frequency Following Response").
- Procedura: occhiali a luce pulsata e cuffie, programmi "Alpha/Theta 8-10 Hz", sessioni brevi nei primi 15 minuti della lezione. Occhiali Ganzfeld (GanzFrame, DeepVision) con LED che sfumano fino al "blu ultravioletto", per la discesa cromatica e l'Image Streaming (MAN A.4, r. 36-40, 93).

**Evidenza attuale.** C per gli effetti su ansia e attenzione (studi piccoli, spesso senza controllo, in parte del produttore); D per ATP prefrontale, neurotrasmettitori e "sincronizzazione perfetta". La risposta EEG alla luce intermittente è reale, ma locale (corteccia visiva) e dura quanto lo stimolo; il flusso aumenta nella corteccia visiva, non in quella prefrontale. 8-10 Hz è alfa bassa, non "alfa/theta". Cluster VTN A5-A8, A12, A13, B1-B4; VNF A5, A6.
- Herrmann 2001, *Exp Brain Res* 137:346-353.
- Huang e Charyton 2008, *Altern Ther Health Med* 14:38-50.
- Fisher et al. 2005, *Epilepsia* 46:1426-1441 (crisi fotosensibili; aggiornamento 2022).

**Compatibilità Lozanov.** Rifiutato. Gli apparecchi sono la caricatura del "mysterious equipment" (Lozanov 2005, r. 1420-1421, 5811-5813). "Monotonous rhythmic stimuli" e "fixation of attention" sono tecniche d'induzione ipnotica (r. 1824-1849; modello r. 611, 615).

**Rischi.**
- Persone con epilessia, crisi pregresse anche isolate o familiari stretti epilettici; persone fotosensibili (circa 1 su 10.000, 1 su 4.000 tra i 5 e i 24 anni): crisi, soprattutto con frequenze intorno a 15-25 Hz. Gli occhi chiusi non proteggono del tutto.
- Persone con emicrania: attacchi.
- Persone con disturbi psicotici o dissociativi: allucinazioni geometriche ed esperienze percettive sgradevoli, anche con il Ganzfeld.
- Minori; chi guida subito dopo la sessione.

**Nocciolo utile.** Chiudere gli occhi e stare tranquilli qualche minuto aumenta già l'alfa occipitale e abbassa un poco l'attivazione, senza dispositivi.

**Raccomandazione dell'analista.** Opzione 1. Rischio fisico concreto, prove deboli, rifiuto esplicito del canone. Una pausa tranquilla dà lo stesso nocciolo senza costi né screening.

**Precauzioni obbligatorie se l'autore decide di includerlo.** Questionario scritto e consenso informato; non proporlo a chi ha storia di crisi, fotosensibilità, emicrania, disturbi psicotici o dissociativi; mai in gruppo senza screening individuale; evitare le frequenze tra 15 e 25 Hz; intensità bassa, sessioni brevi, interruzione al primo malessere; niente minori senza autorizzazione dei genitori e parere medico; non guidare subito dopo; se il produttore dichiara un'emissione ultravioletta, chiedere la classificazione di sicurezza fotobiologica IEC 62471.

**Decisione dell'autore**

Stato: IN ATTESA

Note dell'autore:

---

### D-03 Elettrostimolazione cranica e microcorrenti (CES/Alpha-Stim, Brain Tuner, NeuroElectric Therapy)

**Cosa dicono le fonti.** SL1-A T40-T41 (r. 448-457, 473-480, 504-521); MAN schede 8-10 (r. 101-102), A.6 (111 Hz ai lobi per 20 minuti) e fase 4 della lezione modello; SL1-C sez. 3 (r. 2321-2341); TM D11 (D:L207-219).
- Promesse: QI da +12 a +25 o da +20 a +30 punti; "normalizza l'attività elettrica cerebrale"; insonnia cronica risolta in poche sedute; 111 Hz liberano dopamina e beta-endorfine, 4 Hz catecolamine; 4 Hz ripristinano in 5 giorni la memoria degli alcolisti; Margaret Patterson e H. L. Wen ottennero "guarigioni clamorose"; Pete Townshend disintossicato dall'eroina in 10 sedute "senza astinenza".
- Procedura: elettrodi ai lobi o dietro le orecchie (meridiano "Triplice Riscaldatore"), pila da 9 V, 20 minuti al giorno.

**Evidenza attuale.** D per le promesse. B, con prove di bassa qualità, solo per un piccolo effetto della CES sull'ansia in pazienti; negli USA i dispositivi CES per ansia e insonnia sono in classe II dal 2019. La mappa "frequenza → neurotrasmettitore" non è confermata, e il dato più solido (elettroagopuntura) dice il contrario; Alpha-Stim lavora di norma a 0,5 Hz. Sul Brain Tuner non risultano studi controllati; NET e Wen sono serie di casi; esiste un RCT del NET contro sham (Gariti et al. 1992) il cui esito va ricontrollato. Cluster VTN C1-C6; VNF A6.
- Shekelle et al. 2018, *Ann Intern Med* 168:414-421.
- Brunyé et al. 2021, *Front Hum Neurosci* 15:625321 (gravi limiti metodologici negli studi sulla CES).
- Han 2003, *Trends Neurosci* 26:17-22 (2 Hz encefaline e beta-endorfine, 100 Hz dinorfina).

**Compatibilità Lozanov.** Rifiutato: apparecchi (Lozanov 2005, r. 1420-1421, 5811-5813). Inoltre "The teacher is not a physician" e nessuna attività di trattamento (r. 2046-2047, 3334-3336).

**Rischi.** Portatori di pacemaker o defibrillatore (interferenza); persone con epilessia; gravidanza (sicurezza non stabilita); minori; lesioni cutanee nella zona degli elettrodi. Effetti comuni: vertigini, cefalea, irritazioni o ustioni cutanee, sonnolenza. Per le dipendenze, l'astinenza da oppiacei e soprattutto da alcol richiede supervisione medica: l'astinenza alcolica può dare convulsioni e delirium tremens. Sono dispositivi medici (Reg. UE 2017/745).

**Nocciolo utile.** Nessuno trasferibile alla didattica.

**Raccomandazione dell'analista.** Opzione 1. È un trattamento medico, non uno strumento didattico, e il canone lo rifiuta.

**Precauzioni obbligatorie se l'autore decide di includerlo.** Uso solo su indicazione e sotto controllo sanitario, fuori dal corso; il docente non lo somministra; nessuna promessa su QI, sonno o dipendenze; non guidare durante o subito dopo; nei testi storici correggere il dato su Townshend (chitarrista e autore principale degli Who, non cantante).

**Decisione dell'autore**

Stato: IN ATTESA

Note dell'autore:

---

### D-04 Dispositivi rotanti/vestibolari (Graham Potentializer, IMS, SAMS, IQ Symmetron)

**Cosa dicono le fonti.** SL1-A T42 (r. 458-462, 522-537); SL1-B T13 (r. 983-988); DSS T1 (L34-41); MAN schede 11-13 (r. 104-105), A.9 e fase 2 della lezione modello; SL1-C (r. 2353-2378).
- Promesse: +25% in matematica dopo circa 40 sedute; i dispositivi "rigenerano percorsi sinaptici" e alzano il QI di bambini cerebrolesi; riorganizzano le connessioni in dislessia, autismo, lesioni e "ansia gravitazionale"; bilanciano la "pressione idrostatica" dell'orecchio interno; servono al recupero dei ritardi prima dell'esercizio dinamico. Il caso di Bruce, 5 anni, autismo e iperattività, "guarito" dopo 40 giri e senza più farmaci.
- Procedura: lettino che oscilla e ruota a 10,5 giri al minuto in senso antiorario, con un campo elettromagnetico a 125 Hz alla testa; poltrona SAMS a 3 giri al minuto; poltrona orbitale IQ Symmetron; sedute di 30-45 minuti prima dei giri del tango.

**Evidenza attuale.** D per gli effetti clinici e cognitivi. C per la storia: esiste un brevetto Graham-Lloyd per un letto rotante (1982-1984) e la stampa canadese dell'epoca ne contestava i risultati; su SAMS, Symmetron e IMS non ci sono fonti indipendenti. Fisiologia di base: i canali semicircolari rispondono ai cambi di velocità e a rotazione costante la risposta si spegne in pochi secondi. Cluster VTN D1, D2.
- American Academy of Pediatrics 2012, *Pediatrics* 129:1186-1189 (terapie sensoriali: prove limitate e inconcludenti).
- Chee, Kreutzberg, Clark 1978, *Phys Ther* 58:1071-1075 (stimolazione vestibolare in bambini con paralisi cerebrale: riflessi e motricità, non QI).

**Compatibilità Lozanov.** Rifiutato. Le poltrone come spiegazione sono "ridiculously primitive" (Lozanov 2005, r. 1453-1455, 5810); gli apparecchi rientrano nel "mysterious equipment" (r. 1420-1421).

**Rischi.** Persone con disturbi vestibolari (vertigine posizionale, Ménière, emicrania vestibolare), problemi cervicali, gravidanza, trauma cranico recente; bambini autistici (sovraccarico sensoriale, angoscia). Effetti: nausea, vomito, vertigini, cadute, più probabili se la rotazione precede subito i giri. Il rischio più serio è indiretto: il caso di Bruce presenta come successo la sospensione dei farmaci.

**Nocciolo utile.** La stimolazione vestibolare naturale, cioè giri, pivot e cambi di direzione praticati con gradualità, produce un adattamento documentato nei danzatori (Nigmatullina et al. 2015, *Cereb Cortex* 25:554-562). È il contenuto di INT-06.

**Raccomandazione dell'analista.** Opzione 1. Nessuna prova, rischi fisici, promesse cliniche su bambini. Il nocciolo è già nella pratica del tango e del Qigong.

**Precauzioni obbligatorie se l'autore decide di includerlo.** Nessun farmaco prescritto va sospeso senza il medico curante; nessun uso su bambini con diagnosi; nessuna seduta subito prima dei giri; chi ha disturbi vestibolari o cervicali non partecipa; supervisione sanitaria.

**Decisione dell'autore**

Stato: IN ATTESA

Note dell'autore:

---

### D-05 Respirazioni con apnea (4-4-4-4, 8-4-8-4, 4-2-6-2, 2/4/2, Respiro dell'Aquila)

**Cosa dicono le fonti.**
- 8-4-8-4 in piedi, dai "Seven-Minute Stress Busters" di Lisa Curtis: SL1-A T04 (r. 44-47); MAN A.3 (r. 30-34).
- Respiro dell'Aquila, 4-2-6-2, con l'attenzione che sale dai palmi alle ascelle e "l'energia" che ridiscende: SL1-A T05 (r. 48-50).
- Esercizio Sì/No: sospiro trattenuto mentre si abbassa e si scuote il collo: SL1-A T06 (r. 50-52).
- 4-4-4-4 "geometrica", poi estesa a 6 e 8: SL1-A T07 (r. 53-56); MAN A.3 e fase 1 della lezione modello; SL1-B T3 (r. 715-716); TM T3 (T:L180-182).
- Ciclo di 12 secondi con inspiro, apnea ed espiro sui tre segmenti di lettura: SL1-A T15 (r. 160-165).
- 2/4/2 con la parola da memorizzare pronunciata durante la ritenzione, presentato come fase iniziale del metodo di Lozanov poi tolta: TLT R-T1 (R:L20-21).
- Promesse: "massimizzare l'ossigeno al cervello", rallentare il battito di circa 5 bpm, "sincronizzare i due emisferi", passare dalle onde beta alle alfa.

**Evidenza attuale.** D per l'ossigenazione: in una persona sana il sangue arterioso è già saturo al 97-99%, le apnee lo riducono leggermente e l'iperventilazione riduce il flusso cerebrale. B per il respiro lento senza apnee, intorno a 6 atti al minuto: aumenta la variabilità cardiaca e riduce un poco l'attivazione. Nota tecnica: 4-4-4-4 corrisponde a 3,75 atti al minuto e 8-4-8-4 a 2,5, più lenti del necessario e con "fame d'aria". La notizia storica sul 2/4/2 non ha riscontri. Cluster VNF E1, E2, C4; VPS P5.
- Zaccaro et al. 2018, *Front Hum Neurosci* 12:353.
- Lehrer e Gevirtz 2014, *Front Psychol* 5:756.
- Balban et al. 2023, *Cell Rep Med* 4:100895 (pratiche brevi di respirazione; sospiro ciclico un po' meglio della respirazione quadrata).

**Compatibilità Lozanov.** Rifiutato. "We have never experimented with 'breathing exercise' [...] because these could principally lead to hypnosis" (Lozanov 2005, r. 1407-1416); gli esercizi di respirazione sono tra le cause negate (r. 5802-5803). Lozanov ironizza su chi credeva a "a breathing rhythm, which enhanced memory" (r. 1414-1416): questo contraddice la notizia storica del 2/4/2 (modello r. 632). Lo "sleep-like breathing" è tra le tecniche d'induzione (r. 1824-1849).

**Rischi.** Persone con disturbo di panico o ansia elevata; malattie cardiovascolari o ipertensione non controllata; asma o BPCO; gravidanza; epilessia (l'iperventilazione può provocare crisi in alcune forme). Effetti: capogiro, formicolii, fame d'aria, attacchi di panico. Con apnea a glottide chiusa e spinta del collo (esercizio Sì/No) un effetto Valsalva. Con l'apnea a vuoto eseguita in piedi e in gruppo (Aquila) possibile svenimento (SL1-A, rischio R23).

**Nocciolo utile.** Respirare lentamente per qualche minuto, senza trattenere il fiato e con l'espirazione un po' più lunga, riduce un poco battito e agitazione. Nel Qigong la regolazione del respiro è contenuto della disciplina. Il modello canonico distingue il respiro come contenuto da insegnare, che il metodo di Lozanov può governare (in forma globale, come proposta, senza dettare sensazioni, con il diritto di non seguire), dal respiro come mezzo per indurre uno stato ricettivo, che Lozanov rifiuta (modello r. 783-806).

**Raccomandazione dell'analista.** Opzione 2 per il respiro lento senza apnee, come pratica facoltativa di autoregolazione separata dalla lezione e dichiarata non lozanoviana. Per le sequenze con apnea così come sono nelle fonti (4-4-4-4, 8-4-8-4, Aquila, Sì/No, 2/4/2, ciclo di 12 secondi) raccomando l'opzione 1: il beneficio dichiarato non esiste e il rischio sì. Nel Qigong il respiro resta contenuto della disciplina; dove passa il confine tra contenuto e induzione lo decide l'autore (Domande aperte).

**Precauzioni obbligatorie se l'autore decide di includerlo.** Niente apnee forzate né conteggi rigidi; respiro lento e confortevole, da seduti o con un appoggio; interruzione al primo capogiro; esonero libero senza spiegazioni; nessuna ritenzione per chi ha le condizioni elencate; mai la parola da memorizzare durante una ritenzione; nessuna promessa su ossigeno o emisferi.

**Decisione dell'autore**

Stato: IN ATTESA

Note dell'autore:

---

### D-06 Lavoro su memorie traumatiche e "riprogrammazione" (Videos of Your Mind, riscrittura VCR, submodalità PNL)

**Cosa dicono le fonti.** SL1-A T31 "Videos of Your Mind / Inner-Weather Wizard" (r. 311-324); SL1-B T19 submodalità PNL (r. 1130-1140); MAN A.12 (r. 84-88) e fase 5 della lezione modello (r. 118); SL1-C T9 "traumi da pista" (r. 1545-1571); DSS T21 (L202-215) e T23 (L496-524).
- Procedura: rilassamento profondo, schermo immaginario con telecomando, "Play" su un ricordo anche traumatico, "Pausa" al picco dell'ansia, poi bianco e nero, personaggi rimpiccioliti, voci comiche o musica da circo, finale alternativo trionfale. In SL1-A si mettono in scena le scuse e un "abbraccio catartico" di chi ha umiliato. Nel tango: scontri in pista, rifiuti al cabeceo, blocchi in sequenza.
- Promesse: riconfigurare l'amigdala, interrompere il rilascio di cortisolo, "deconsolidare" la memoria traumatica, liberare "istantaneamente" la memoria a lungo termine.

**Evidenza attuale.** D così formulato. La PNL non ha prove sistematiche di efficacia. Esiste una tecnica clinica affine con prove, l'imagery rescripting, condotta da terapeuti (B in quel contesto). La riconsolidazione della memoria è dimostrata negli animali e discussa nell'uomo. Nessuna prova di effetti istantanei. Cluster VNF G2.
- Sturt et al. 2012, *Br J Gen Pract* 62:e757-e764 (PNL).
- Morina, Lancee, Arntz 2017, *J Behav Ther Exp Psychiatry* 55:6-15 (imagery rescripting).
- Nader, Schafe, LeDoux 2000, *Nature* 406:722-726.

**Compatibilità Lozanov.** Rifiutato. Sulla PNL: "any programming results from dictation and manipulation [...] we provoke deprogramming" (Lozanov 2005, r. 1400-1406, 5801). La guided imagery è un metodo d'induzione (r. 1440-1441). Il docente non fa terapia (r. 2046-2047, 3334-3336).

**Rischi.** Alto, psicologico. Chiunque abbia ricordi traumatici, in particolare persone con PTSD: ritraumatizzazione, inondazione emotiva, dissociazione, attacchi di panico, possibile alterazione dei ricordi. In gruppo e a fine lezione manca ogni contenimento. La riconciliazione immaginata con chi ha umiliato può invalidare vissuti di abuso.

**Nocciolo utile.** In ambito clinico l'imagery rescripting ha prove. In aula, per gli incidenti ordinari di pista (uno scontro, un rifiuto), il canale didattico è un altro: normalizzare l'errore, riprovare la situazione in condizioni sicure, lasciare che l'errore "appartenga" al personaggio di gioco (INT-07, D-16).

**Raccomandazione dell'analista.** Opzione 1. È lavoro clinico, fuori dalla competenza di un docente di tango, di Qigong o di un corso universitario, e il canone lo rifiuta. Il manuale può contenere un rinvio: se emergono contenuti traumatici, si interrompe e si indica un professionista.

**Precauzioni obbligatorie se l'autore decide di includerlo.** Solo come informazione e rinvio; conduzione riservata a psicoterapeuti abilitati, fuori dal corso; mai in gruppo; mai a fine lezione; nessuna riconciliazione immaginata con chi ha fatto del male.

**Decisione dell'autore**

Stato: IN ATTESA

Note dell'autore:

---

### D-07 Generatori ELF, bracciali magnetici, Bio-Battery di Edgar Cayce

**Cosa dicono le fonti.** SL1-A T45 (r. 569-583); MAN schede 15-16 (r. 109-110), abbinate ad A.2, A.10 e alla fase 2 della lezione modello; SL1-C (r. 2404-2418).
- Promesse: un campo a 7,83-8 Hz ("risonanza di Schumann", "pulsazione terrestre") crea uno "scudo biologico" contro Wi-Fi, radar e cavi, che "altererebbero l'acetilcolina"; stress, cancro, psicosi e jet lag sparirebbero. La Bio-Battery (pila umida bimetallica in soluzioni di sali d'oro o platino, elettrodi di rame) equalizzerebbe la carica bioelettrica lungo i meridiani e guarirebbe sindrome di Down, spasticità, lesioni del midollo e coma "tramite chi e prana".
- Procedura: generatore "sempre acceso" nell'ambiente di studio e durante il sonno; bracciali magnetici; Bio-Battery durante il riposo o il training autogeno.

**Evidenza attuale.** D. La risonanza di Schumann è un fenomeno geofisico reale (circa 7,8 Hz), ma non esiste un meccanismo per cui un campo a 8 Hz schermi le radiofrequenze. Chi si dichiara ipersensibile ai campi non li riconosce meglio del caso; i magneti statici non riducono il dolore più del placebo. La Bio-Battery viene dalle "letture" in trance di Cayce e non ha studi. Cluster VTN G1, G2; VNF A7.
- Rubin, Das Munshi, Wessely 2005, *Psychosom Med* 67:224-232.
- Pittler, Brown, Ernst 2007, *CMAJ* 177:736-742.
- Richmond et al. 2013, *PLoS ONE* 8:e71529.

**Compatibilità Lozanov.** Rifiutato: apparecchi (Lozanov 2005, r. 1420-1421, 5811-5813).

**Rischi.** Medio. Magneti forti: interferenza con pacemaker e defibrillatori. Soluzioni di sali metallici: irritanti e tossiche se ingerite. Il rischio maggiore è indiretto: promesse su cancro, psicosi, sindrome di Down, lesioni midollari e coma possono far ritardare o abbandonare le cure.

**Nocciolo utile.** Meno schermi la sera aiuta sonno e attenzione, per ragioni comportamentali.

**Raccomandazione dell'analista.** Opzione 1. Nessuna base, promesse sanitarie gravi, rifiuto del canone.

**Precauzioni obbligatorie se l'autore decide di includerlo.** Solo in forma documentale; nessuna promessa sanitaria; avvertenza per i portatori di dispositivi impiantati; nessun uso della Bio-Battery.

**Decisione dell'autore**

Stato: IN ATTESA

Note dell'autore:

---

## Blocco B. Induzione di stato

### D-08 Rilassamento progressivo / Scan and Relax

**Cosa dicono le fonti.** SL1-A T01 "Onda di rilassamento progressiva" (r. 26-30) e T02 "Scan and Relax" (r. 30-32); MAN A.1 (r. 18-22) e fase 1 della lezione modello; SL1-C sez. 2.4. Nello stesso capitolo di SL1-A compaiono la sofrologia (Caycedo, Abrezol) ed Eli Bay.
- Procedura: seduti o sdraiati, contrarre per 3-5 secondi e poi rilasciare i muscoli dai piedi al viso, con un'"onda di calore" dalla testa ai piedi; in SL1-A anche rotazioni complete del collo; nella variante Scan and Relax si esplora il corpo e si rilascia senza contrazione.
- Promesse: disattivare l'iper-tono simpatico, ridurre il cortisolo, portare all'"allerta rilassata" con predominanza di onde alfa come base dell'apprendimento. In MAN è la preparazione all'uso dell'AVE (D-02).

**Evidenza attuale.** B. Il rilassamento muscolare progressivo riduce l'ansia con effetto moderato e, in alcuni studi, il cortisolo salivare. L'aumento dell'alfa è un correlato del rilassamento, non un vantaggio per la memoria. Cluster VNF E3.
- Manzoni et al. 2008, *BMC Psychiatry* 8:41.
- Pawlow e Jones 2002, *Biol Psychol* 60:1-16.
- Heide e Borkovec 1983, *J Consult Clin Psychol* 51:171-182 (ansia paradossale indotta dal rilassamento).

**Compatibilità Lozanov.** Rifiutato come mezzo. "Guided relaxation (this is one of the methods to induce hypnosis)"; "we have never conducted guided relaxation where the teacher dictates the trainees' sensations" (Lozanov 2005, r. 1427-1428, 2043-2047). Il rilassamento muscolare per la memoria non ha provato "efficiency and harmlessness" (r. 1626-1632). "Relaxation in its own right cannot produce hypermnesia" (r. 2093). Nel canone la calma è un effetto dell'organizzazione della lezione (r. 2085-2087, 5822), non una procedura.

**Rischi.** Basso-medio. Persone con disturbi d'ansia: in una quota non trascurabile il rilassamento provoca ansia paradossale. Persone con storia di trauma: dissociazione e intrusioni, soprattutto a occhi chiusi con una voce che guida. Persone con depressione grave o disturbi psicotici. Le rotazioni complete del collo sono sconsigliabili per chi ha problemi cervicali o vertigini.

**Nocciolo utile.** Meno ansia significa più memoria di lavoro disponibile. Nel Qigong il rilassamento attivo (song, fangsong) è contenuto della disciplina e vale la stessa distinzione del respiro: contenuto sì, induzione no (modello r. 783-806). Nel tango, una breve presa di coscienza delle tensioni di spalle e mani prima dell'abbraccio è tecnica, non induzione.

**Raccomandazione dell'analista.** Opzione 2. Funziona sull'ansia, ma il canone lo rifiuta come mezzo didattico. Può stare in un modulo facoltativo, separato dalla lezione e dichiarato non lozanoviano. Nel Qigong va trattato come contenuto della disciplina (Domande aperte).

**Precauzioni obbligatorie se l'autore decide di includerlo.** Occhi aperti sempre possibili; in piedi o seduti, non sdraiati in una sala di ballo; nessuna sensazione dettata ("senti il calore"); niente rotazioni complete del collo, solo mobilizzazioni dolci; libertà di interrompere e uscire; nessuna promessa su cortisolo o onde alfa.

**Decisione dell'autore**

Stato: IN ATTESA

Note dell'autore:

---

### D-09 Training autogeno (Schultz/Fryling)

**Cosa dicono le fonti.** SL1-A T03 (r. 33-43); MAN A.2 (r. 24-28) e PR4; SL1-C sez. 2.4. Attribuito a "Schultz e Fryling".
- Procedura: seduti o supini, occhi chiusi, "maschera rilassante" sul viso, lingua appoggiata alla gengiva superiore, respiro 2:6; formule ripetute 6-8 volte ("il mio braccio destro è pesante", poi calore, cuore calmo e regolare, plesso solare caldo, fronte fresca), tre giorni per arto, 7-10 minuti due o tre volte al giorno; chiusura con "Io sono supremamente calmo" e flessione degli arti. In MAN abbinato alla Bio-Battery o al generatore ELF.
- Promesse: bilancia il sistema nervoso autonomo, aumenta la vascolarizzazione periferica, "azzera" l'ansia da prestazione.

**Evidenza attuale.** B per la riduzione dell'ansia (effetto medio in meta-analisi) e per il riscaldamento delle mani; D per "azzera". Attribuzione da correggere: il training autogeno è di J. H. Schultz (1932); Vera Fryling lo ha combinato con il Superlearning, non ne è coautrice; lingua al palato e respiro 2:6 vengono da altre tradizioni. Cluster VNF E4; VPS P8.
- Stetter e Kupper 2002, *Appl Psychophysiol Biofeedback* 27:45-98.

**Compatibilità Lozanov.** Rifiutato. Training autogeno e rilassamento muscolare non hanno provato "efficiency and harmlessness" (Lozanov 2005, r. 1626-1632). La formula "pesante e caldo" è proprio l'esempio di induzione ipnotica che Lozanov riporta: "Your legs are heavy and warm" (r. 1807-1812; modello r. 634).

**Rischi.** Medio. Persone con cardiopatie recenti (formula sul cuore); persone con disturbi d'ansia (ansia paradossale); sopravvissuti a traumi (dissociazione); persone con disturbi psicotici o depressione grave. Si apprende in settimane, con una guida qualificata.

**Nocciolo utile.** È uno strumento valido di autoregolazione dell'ansia, da imparare in un contesto adatto. La lingua al palato è anche una prescrizione classica del Qigong: lì è contenuto della disciplina.

**Raccomandazione dell'analista.** Opzione 1. È la tecnica che Lozanov cita come modello di induzione, richiede un percorso proprio con un professionista e i suoi benefici sull'ansia si ottengono anche fuori dal corso. Il manuale può indicare dove impararlo. Alternativa ragionevole, se l'autore la preferisce: opzione 2, condotta da un professionista qualificato.

**Precauzioni obbligatorie se l'autore decide di includerlo.** Conduzione affidata a un professionista qualificato; screening per cardiopatie, ansia grave, trauma, psicosi; nessuna formula sul cuore per chi ha cardiopatie; separato dalla lezione e dichiarato non lozanoviano; nessuna promessa di "azzerare" l'ansia; mai abbinato a dispositivi (D-07).

**Decisione dell'autore**

Stato: IN ATTESA

Note dell'autore:

---

### D-10 Visualizzazioni guidate (discesa cromatica, viaggio calmante) e Image Streaming

**Cosa dicono le fonti.**
- Viaggio calmante e discesa a colori: SL1-A T08 (r. 57-63); MAN A.4 "Ascensore dei colori" (r. 36-40), unita al concerto passivo nella fase 4 della lezione modello (r. 117); DSS T23-bis "escalator interiore" (L505-506). Procedura: occhi chiusi, si scende dal 7° piano rosso al piano terra blu profondo o "ultravioletto", poi spiaggia o foresta per 3-5 minuti. Promessa: spegnere i pensieri intrusivi, stimolare l'emisfero destro, "aprire il canale mnestico visivo-spaziale".
- Image Streaming di Win Wenger: SL1-A T21 (r. 180-181, 236-245); MAN A.8 (r. 60-64); SL1-B T10 (r. 645-650, 755-758); TM T10 (T:L89-94, L242-246). Procedura: fissare una lampadina, osservare i fosfeni a occhi chiusi, descrivere ad alta voce per 10-20 minuti il flusso di immagini, porre al segnale una domanda e interpretare le metafore; nel Tango-Mind, verbalizzare le immagini durante o dopo il ballo. Promesse: "pole-bridging" tra gli emisferi attraverso il corpo calloso, crescita della densità sinaptica, tempi di lettura ridotti del 60%.

**Evidenza attuale.** D per le promesse: nessuno studio su un "canale mnestico", nessuno studio indipendente sull'Image Streaming, nessuna prova del 60%. A per il fenomeno dei fosfeni. B per il nocciolo dell'Image Streaming: descrivere a voce ciò che si impara e unire parole e immagini aiuta a capire e a ricordare. Cluster VNF E5, J1, J2; VPS I3; VTN B4.
- Chi et al. 1994, *Cogn Sci* 18:439-477 (auto-spiegazione).
- Wammes, Meade, Fernandes 2016, *Q J Exp Psychol* 69:1752-1776 (disegnare per ricordare).

**Compatibilità Lozanov.** Rifiutato. "We have never experimented with [...] 'visualization exercises' or 'guided fantasy'" (Lozanov 2005, r. 1407-1416). "'Guided imagery' (which really is one of the methods to induce hypnosis)", con l'esempio "You are on top of a mountain, the sun is rising [...] Everything is happening just as I say" (r. 1440-1441, 1815-1820).

**Rischi.** Medio. Persone con storia di trauma, disturbi dissociativi, psicosi o rischio di psicosi, depressione grave: immagini intrusive, ansia, senso di irrealtà. Fissare fonti luminose intense (sole, laser, LED potenti) può danneggiare la retina. Con il Ganzfeld, esperienze percettive anomale (D-02).

**Nocciolo utile.** Verbalizzare la propria esperienza. Dopo una figura, a coppie, dire in poche frasi che cosa si è sentito nell'asse, nell'abbraccio, nei piedi; nel Qigong, descrivere la forma appena eseguita. È elaborazione attiva, non visualizzazione guidata, e si fa a occhi aperti.

**Raccomandazione dell'analista.** Opzione 1 per la discesa cromatica e il viaggio calmante: sono esattamente la guided imagery che il canone rifiuta e non hanno prove. Opzione 3 per il nocciolo dell'Image Streaming, riformulato come verbalizzazione a occhi aperti dopo la pratica, senza lampadine e senza promesse sugli emisferi.

**Precauzioni obbligatorie se l'autore decide di includerlo.** Per la versione riformulata: occhi aperti, facoltativa, nessuna fonte luminosa, nessun contenuto personale richiesto. Per un'eventuale visualizzazione guidata: consenso informato; persone con trauma, dissociazione o psicosi non partecipano; conduttore con formazione clinica; possibilità di aprire gli occhi e uscire in ogni momento; durata breve; momento finale di rientro con attivazione fisica.

**Decisione dell'autore**

Stato: IN ATTESA

Note dell'autore:

---

### D-11 Battiti binaurali / Hemi-Sync / Binaural Phaser (solo audio)

**Cosa dicono le fonti.** SL1-A T43 (r. 463-466, 538-552); SL1-B T1 (r. 597-609) e T21 (Devon Edrington, r. 925-931); MAN A.3 e A.11 (r. 34, 82); TM T1 (T:L16-20, L146-148, L250-252), T11 (T:L25-31) e D7 (D:L159-172); DSS T11 (L384-389); SL1-C.
- Procedura: cuffie chiuse, 105 Hz a destra e 100 Hz a sinistra, battimento a 5 Hz (che la fonte chiama "delta"); il Binaural Phaser sposta la frequenza secondo la materia; Edrington inserisce segnali Hemi-Sync in brani di Kitaro, Vangelis e Paul Horn; nel Tango-Mind 15 minuti all'inizio della lezione.
- Promesse: "stati focalizzati di coscienza", "allerta rilassata", abbattere i "picchi di cortisolo", sincronizzare gli emisferi "in pochi secondi".
- A merito delle fonti: TM T11 e SL1-B T1 citano la revisione scettica di PLoS ONE 2023 e ammettono che la tecnologia funziona meglio se associata a rilassamento e respirazione.

**Evidenza attuale.** B-C. Il battimento si percepisce davvero; 5 Hz è banda theta, non delta. Una meta-analisi trova un effetto medio su ansia, attenzione e memoria (g = 0,45, 22 studi piccoli ed eterogenei); l'idea che il cervello si "sintonizzi" sulla frequenza del battito non è confermata (14 studi: 5 a favore, 8 contrari, 1 misto). Gli effetti possono venire dal suono piacevole, dall'aspettativa e dalla pausa. Nessuna prova sul cortisolo in 15 minuti. Cluster VNF A3-A5; VTN A1-A3, A14.
- Ingendoh, Posny, Heine 2023, *PLoS ONE* 18:e0286023.
- Garcia-Argibay, Santed, Reales 2019, *Psychol Res* 83:357-372.

**Compatibilità Lozanov.** Rifiutato. Onde alfa come spiegazione: chi ha alfa prevalente "do not exhibit increased memory potential" (Lozanov 2005, r. 1460, 2077-2080, 5804). "Special audio cassettes on sale" (r. 1433-1435, 5811-5813).

**Rischi.** Basso. Volume alto e prolungato (danno uditivo); sonnolenza se si guida o si svolgono attività che richiedono vigilanza. Alcuni produttori lo sconsigliano a chi ha epilessia: cautela teorica ma ragionevole. In sala, senza cuffie, l'effetto binaurale non esiste.

**Nocciolo utile.** Un ascolto breve e piacevole prima di un compito può ridurre un poco l'ansia, probabilmente per aspettativa e pausa.

**Raccomandazione dell'analista.** Opzione 2. È il modulo sperimentale a rischio più basso dell'area tecnologica e le due revisioni di verifica concordano. Va tenuto separato dalla lezione, facoltativo, dichiarato non lozanoviano, con una misura prima e dopo. Se l'autore vuole un percorso del tutto privo di ciò che il canone rifiuta, l'opzione coerente è la 1 (sezione 4).

**Precauzioni obbligatorie se l'autore decide di includerlo.** Solo audio, mai con luci intermittenti; volume moderato; sessioni brevi; mai alla guida; facoltativo con esonero libero; nessuna promessa su cortisolo o emisferi; misura semplice dell'ansia prima e dopo (INT-10); mai durante il sonno (D-13).

**Decisione dell'autore**

Stato: IN ATTESA

Note dell'autore:

---

### D-12 Prova mentale / motor imagery (caso Drapeau)

**Cosa dicono le fonti.** SL1-A T09 (r. 17-19): Christian Drapeau avrebbe vinto il titolo nordamericano di Tae Kwon Do "sostituendo gli allenamenti puramente fisici con studio autogeno e prove mentali". La fonte non dà una procedura. Nelle altre fonti l'immaginazione motoria compare solo in forma guidata: lo script notturno per i giros con la visualizzazione della milonga (MAN r. 202; DSS L627-669), l'olofonia per le "prove mentali" (TM D9), il Borrowed Genius (D-16).

**Evidenza attuale.** Il caso Drapeau è un aneddoto non verificabile (C). La pratica mentale ha invece prove buone, livello B: migliora la prestazione rispetto a nessuna pratica, con effetti moderati che dipendono dal compito, ma meno della pratica fisica; le due insieme funzionano meglio. "Sostituire" l'allenamento non è sostenuto. Il cervello di norma distingue l'immaginato dal reale (D per "il cervello non distingue"). Cluster VPS B9; VNF G3; VTN H5.
- Driskell, Copper, Moran 1994, *J Appl Psychol* 79:481-492.
- Toth et al. 2020, *Psychol Sport Exerc* 48:101672 (replicazione meta-analitica).
- Dijkstra e Fleming 2023, *Nat Commun* 14:1627.

**Compatibilità Lozanov.** Due forme da distinguere.
- Imagery autogestita, cioè l'allievo che ripassa da sé un movimento: non trattata.
- Guided imagery dettata dal docente ("immagina di...", "senti che..."): rifiutata come induzione (Lozanov 2005, r. 1440-1441, 1815-1820); anche le meditazioni guidate con voce monotona sono tra i metodi ipnotici (r. 1833-1836).

**Rischi.** Basso. Il rischio concreto è usarla al posto della pratica fisica: decondizionamento, coordinazione insufficiente, infortuni al rientro (VPS 7.5). La forma guidata a occhi chiusi ha i rischi di D-10.

**Nocciolo utile.** Brevi ripassi immaginativi, scelti dall'allievo, tra le ripetizioni o nei giorni di riposo. È INT-04.

**Raccomandazione dell'analista.** Opzione 3 per l'imagery autogestita, riformulata come ripasso facoltativo in aggiunta alla pratica fisica (INT-04). Opzione 1 per l'imagery dettata dal docente come induzione e per l'idea di sostituire l'allenamento.

**Precauzioni obbligatorie se l'autore decide di includerlo.** Mai al posto della pratica fisica; mai dettata come sequenza di sensazioni; occhi aperti o chiusi a scelta dell'allievo; il caso Drapeau solo come aneddoto non verificato.

**Decisione dell'autore**

Stato: IN ATTESA

Note dell'autore:

---

## Blocco C. Suggestione e riprogrammazione

### D-13 Subliminali e apprendimento nel sonno (Mahaney, nastri notturni, Silverman/Parker "Mommy and I are one", Dial 1-800-SUB)

**Cosa dicono le fonti.**
- Nastri notturni con 100-200 suggestioni personali su musica Superlearning, per 10 notti: prima la "detersione" (perdono a genitori, docenti, autorità), poi formule di "fusione" con la materia: SL1-A T28 (r. 302-310).
- "Change Your Mind" di Teri Mahaney: audio di 20-30 minuti all'addormentamento per 10-14 notti, anche sotto la soglia udibile; un manager con -20% di tempo all'esame e +20% nei voti; versioni per il tango e script integrale per i giros con induzione di "calore e pesantezza" e comando di sonno: SL1-A T30 (r. 257-259, 275-281); SL1-B T17 (r. 1104-1115); MAN A.11 (r. 78-82) e T6.4 (r. 201-202); DSS T17-T19 (L171-186, L435-466, L627-669); SL1-C T7, T14.
- Subliminale tachistoscopico "Mommy and I are one" (Lloyd Silverman, Kenneth Parker): lampi di 4 ms, ansia ridotta e circa 10 punti in più rispetto ai controlli: SL1-A T29 (r. 264-274); SL1-B T18 (r. 1117-1128); DSS T20 (L187-201). Studi su minori attribuiti a Rose Bryant-Tucker: SL1-A r. 266-267.
- "Dial Direct 1-800-SUB": telefono di cristallo immaginato, quattro formule rivolte al "subconscio", risposte attraverso figure o sintomi fisici, ginnastica finale "per uscire dalla trance": SL1-A T32 (r. 325-334).
- Promesse: la finestra ipnagogica aggira il "filtro analitico"; la propria voce o una voce femminile è "accettata dal subconscio"; lo script integra "le verità" nei neuroni e riduce "drasticamente" la frequenza cardiaca in pista.

**Evidenza attuale.** D. Gli studi controllati non mostrano apprendimento esplicito di informazioni nuove durante il sonno. I nastri subliminali di auto-aiuto, testati in doppio cieco su 237 persone, non producono gli effetti dichiarati. Il filone di Silverman è storico e controverso, con repliche difficili. Sui dati di Mahaney e di Bryant-Tucker non esistono studi rintracciabili. Esiste un effetto reale ma diverso: riproporre nel sonno un segnale associato a materiale studiato da svegli può rafforzarne un poco il ricordo, in laboratorio. Cluster VNF F9-F12; VTN A4, L1; VPS I4-I6.
- Greenwald et al. 1991, *Psychol Sci* 2:119-122.
- Wood et al. 1992, *Psychol Sci* 3:236-239.
- Hu et al. 2020, *Psychol Bull* 146:218-244 (riattivazione mirata della memoria nel sonno).

**Compatibilità Lozanov.** Rifiutato. "During training under this method, sleep turns into hypnosis" (Lozanov 2005, r. 1600-1624); programmazione e PNL (r. 1400-1406); cassette in vendita (r. 1433-1435, 5811-5813); il "telefono" e le sue formule sono guided imagery (r. 1440-1441). Le percezioni periferiche canoniche sono stimoli sopra soglia, controllabili, che lasciano libertà di scelta (r. 2232-2264): il subliminale è il loro contrario.

**Rischi.** Medio. Persone con insonnia, ansia, depressione: sonno frammentato o peggiorato. Formule di perdono verso genitori o persone che hanno fatto del male: in persone fragili possono alimentare autocritica o riaprire ferite. Auricolari tutta la notte: irritazione del condotto uditivo. Minori: servono il consenso dei genitori e, in ricerca, un comitato etico. Il subliminale è incompatibile con il consenso informato.

**Nocciolo utile.** Il sonno regolare dopo la lezione consolida ciò che si è imparato da svegli. Un ascolto serale facoltativo della musica della lezione, senza suggestioni, è innocuo.

**Raccomandazione dell'analista.** Opzione 1. Nessuna prova, un problema etico (subliminale), un rischio sul sonno e un rifiuto esplicito del canone.

**Precauzioni obbligatorie se l'autore decide di includerlo.** Nessun messaggio subliminale; nessun audio con suggestioni durante il sonno; al più un ascolto informativo prima di dormire, facoltativo; niente con minori; nessuna formula di perdono verso persone reali.

**Decisione dell'autore**

Stato: IN ATTESA

Note dell'autore:

---

### D-14 Autoconvalida di Otto Altorfer e affermazioni

**Cosa dicono le fonti.** SL1-A T27 (r. 260-263, 290-301); SL1-B T16 (r. 1089-1102); MAN A.10 (r. 72-76), PR7 con l'esempio di "Marco e la fisica quantistica" (r. 169-193) e T6.3 per i giros (r. 199-200); DSS T14-T16 (L152-170, L408-433, L604-625); SL1-C T6, T13 e sez. 2.5 (r. 2497-2582, con lo specchio e le affermazioni dette camminando o ballando).
- Procedura: foglio in due colonne, "Convalida" e "Risposta"; affermazione al presente ruotando io, tu ed egli con il proprio nome ("Io, [Nome], ruoto nei giros con asse perfetto e assoluta fluidità"); a destra si trascrivono le obiezioni interne senza reprimerle; 10-15 minuti due volte al giorno per 4 giorni, oppure per 14-21 giorni, finché la colonna di destra resta vuota.
- Promesse: nuova configurazione sinaptica in 2-3 settimane; "desensibilizzazione sistematica" dei condizionamenti; nel tango, rilascio della tensione scapolo-omerale e stabilità posturale in due settimane.

**Evidenza attuale.** D per il protocollo e per i tempi: nessuno studio pubblicato; la formazione delle abitudini richiede in mediana 66 giorni, con grande variabilità; "desensibilizzazione sistematica" è il nome di un'altra tecnica (esposizione graduale). B per un'osservazione che le fonti fanno bene: un'affermazione positiva può suscitare obiezioni e combatterle le rafforza; le auto-affermazioni migliorano l'umore di chi ha alta autostima e lo peggiorano in chi l'ha bassa. Dati biografici su Altorfer non verificati. Cluster VNF F13, F14; VPS I7.
- Wood, Perunovic, Lee 2009, *Psychol Sci* 20:860-866.
- Lally et al. 2010, *Eur J Soc Psychol* 40:998-1009.
- Ramirez e Beilock 2011, *Science* 331:211-213 (scrivere le proprie preoccupazioni prima di una prova; da ricontrollare).

**Compatibilità Lozanov.** Rifiutato come auto-programmazione: "any programming results from dictation and manipulation [...] On the contrary, we provoke deprogramming" (Lozanov 2005, r. 1400-1406). È coerente, invece, l'idea di non reprimere le obiezioni: le barriere antisuggestive "should not be stimulated" (r. 2842-2845).

**Rischi.** Basso-medio, psicologico. Persone con bassa autostima o umore depresso: le formule "io faccio con assoluta facilità" possono peggiorare l'umore; senso di colpa se "non funziona".

**Nocciolo utile.** Due strumenti diversi e meglio studiati: scrivere brevemente le proprie preoccupazioni prima di una prova (scrittura espressiva) e l'affermazione dei propri valori. Nel tango, un diario di pratica con osservazioni concrete ("oggi il pivot a sinistra era più stabile") è più vicino alla realtà di una formula.

**Raccomandazione dell'analista.** Opzione 1. Il protocollo programma, cioè fa l'opposto della desuggestione, non ha prove e può peggiorare l'umore proprio di chi ne avrebbe bisogno. Se l'autore vuole uno strumento scritto, conviene valutarne a parte uno diverso (diario di pratica, scrittura espressiva), come proposta nuova e dichiarata.

**Precauzioni obbligatorie se l'autore decide di includerlo.** Facoltativo e fuori dalla lezione; nessuna formula "io sono"; nessuna promessa di tempi; attenzione a chi mostra umore basso; mai abbinato a rilassamento profondo o a dispositivi.

**Decisione dell'autore**

Stato: IN ATTESA

Note dell'autore:

---

### D-15 Ancoraggi emotivi (Excelebration, Triggering/Sports Flow, ancora prima del giro)

**Cosa dicono le fonti.** SL1-A T18 "Excelebration" (r. 214-220); MAN A.6 (r. 48-52) e T6.5 (r. 203-204); SL1-C T10 (r. 1575-1598) e T15 (r. 1869-1885); DSS T25-T26 (L526-553, L672-692). Triggering e "Sports Flow" sono attribuiti a Dyveke Spino e Don Schuster.
- Procedura: rievocare il momento più radioso della propria vita, amplificare brividi, calore, postura eretta; al picco unire pollice e indice della mano sinistra, quella dell'abbraccio; riattivare il gesto all'inizio del compito o, in milonga, subito prima del primo passo o del giro. In MAN abbinato a Brain Tuner o Alpha-Stim a 111 Hz e a *Eine kleine Nachtmusik*.
- Promesse: dopamina e beta-endorfine facilitano il consolidamento nell'ippocampo; i contenuti vengono "inondati" da un "neuro-fiume di endorfine"; l'ancora richiama "istantaneamente lo stato biochimico ed elettrico" di centratura ed elasticità.

**Evidenza attuale.** C per l'ancora così formulata: nessuna prova specifica e nulla si "trasferisce". B per due noccioli: emozione, novità e ricompensa modulano davvero il consolidamento; una breve routine costante prima di un gesto migliora la prestazione sportiva, per attenzione e automatismo. Cluster VNF F8, G4; VPS I8.
- Rupprecht, Tran, Gröpel 2021, *Int Rev Sport Exerc Psychol* (meta-analisi sulle routine pre-esecuzione).
- Cotterill 2010, *Int Rev Sport Exerc Psychol* 3:132-153.
- McGaugh 2004, *Annu Rev Neurosci* 27:1-28.

**Compatibilità Lozanov.** Rifiutato come ancoraggio di tipo PNL (Lozanov 2005, r. 1400-1406, 5801) e come "conditioning", che Lozanov elenca tra le tecniche d'induzione (r. 1824-1849). Coerenti invece la gioia e la risata come sistema (r. 2716-2726) e il principio della "joyful and spontaneous concentrative calmness" (r. 2931).

**Rischi.** Basso. La rievocazione intensa può far emergere ricordi dolorosi in chi ha una storia traumatica (SL1-A, rischio R6). L'ancora può diventare un rituale da cui si dipende e distogliere dal partner (MAN, rischio S19).

**Nocciolo utile.** La routine pre-esecuzione: un respiro, sentire l'appoggio, uno sguardo, una parola chiave, sempre uguali e scelti dall'allievo. È INT-05.

**Raccomandazione dell'analista.** Opzione 3, riformulato come routine pre-esecuzione (INT-05): senza induzione, senza rievocare ricordi personali, senza linguaggio "biochimico". La gioia resta dove il canone la mette: giochi, canti, risata.

**Precauzioni obbligatorie se l'autore decide di includerlo.** Nessuna rievocazione a occhi chiusi di ricordi personali; nessun abbinamento a dispositivi; routine scelta dall'allievo, non imposta dal docente.

**Decisione dell'autore**

Stato: IN ATTESA

Note dell'autore:

---

### D-16 Reincarnazione artificiale di Raikov / Borrowed Genius (da distinguere dalle nuove identità canoniche di Lozanov)

**Cosa dicono le fonti.** SL1-A T19 (r. 187-188, 221-228); SL1-B T9 (r. 620-623, 747-754) e T15 (r. 1142-1151); MAN A.7 (r. 54-58) e T6.5 con Carlos Gavito (r. 203-204); DSS T22 (L216-229) e T24 (L468-494); SL1-C T8 (r. 1519-1541) e T15; TM T6 (T:L45-49, L219-228). Autori citati: Vladimir Raikov, Win Wenger ("Borrowed Genius"), Rosella Wallace ("Putting on a New Head"), Robert Hartley.
- Procedura: breve meditazione visiva, "indossare" un maestro (Einstein, un poliglotta, Gavito), adottarne postura, respiro ed espressione, restare in ruolo; nel tango, ancora pollice-indice prima del giro.
- Promesse: "ipnosi d'identità alterata" che disconnette dalle ansie, sospende l'Ego, "azzera all'istante" la paura di sbagliare, produce una "temporanea e profonda ristrutturazione della personalità", trasferisce le abilità del modello e fa assimilare "senza il filtro critico e pauroso dell'Ego".
- Da distinguere: le nuove identità canoniche (nome, nazionalità, professione e biografia nuovi dentro un gioco-progetto dichiarato), riportate correttamente in TLT R-T2 (R:L41, L51) e DSS T40 (L1082-1085, L1147-1151).

**Evidenza attuale.** D per la versione ipnotica: gli studi di Raikov, anni '70, non sono stati replicati in modo indipendente (l'articolo del 1976 va ricontrollato; non verificato anche Hartley 1986). B per il nocciolo: assumere la prospettiva di un personaggio aumenta la perseveranza nei bambini; la pedagogia teatrale ha effetti positivi in meta-analisi, con disegni deboli. Cluster VNF G1; VPS I1, I2, C1, C2.
- White et al. 2017, *Child Dev* 88:1563-1571 ("effetto Batman").
- Banakou, Kishore, Slater 2018, *Front Psychol* 9:917.
- Lee et al. 2015, *Rev Educ Res* 85:3-49 (pedagogia teatrale).

**Compatibilità Lozanov.** Rifiutato nella forma delle fonti: è un'ipnosi d'identità, e l'ipnosi "was explicitly rejected" (Lozanov 2005, r. 1392, 5815). L'infantilizzazione canonica è "increased trust and receptivity while retaining a critical attitude and self-control" (r. 2289-2293): togliere il filtro critico è il suo contrario. Coerente la forma canonica: nuove identità per "salvare la faccia", a occhi aperti, senza induzione, con l'indicazione che "teachers should not discuss it with the students" (r. 759-762, 2704-2707, 3937-3951).

**Rischi.** Nella versione ipnotica medio-alto: persone con tendenza dissociativa, disturbi di personalità, psicosi o traumi possono avere depersonalizzazione, confusione d'identità, falsi ricordi, dipendenza dal conduttore. Nella forma canonica basso: restano la libertà di non aderire e l'attenzione a personaggi che tocchino temi personali dolorosi (TLT, rischio S11).

**Nocciolo utile.** Il personaggio riduce la paura del giudizio, non il senso critico. Nel tango: un nome e una biografia porteña dentro un "film" o una milonga d'epoca; "ballare come" un milonguero di riferimento come imitazione dichiarata di postura e camminata, a occhi aperti. Nel Qigong la forma è meno naturale: un gioco-progetto neutro può funzionare meglio (modello r. 765).

**Raccomandazione dell'analista.** Opzione 3, dentro le nuove identità canoniche: gioco dichiarato, occhi aperti, nessuna induzione, possibilità di restare se stessi. La versione di Raikov come ipnosi d'identità resta documentata in `ricerca/`.

**Precauzioni obbligatorie se l'autore decide di includerlo.** Nessuna induzione né "meditazione visiva" iniziale; occhi aperti; adesione volontaria; il docente non interpreta psicologicamente le scelte dei personaggi; nessun personaggio legato a vissuti dolorosi; nessuna ancora associata.

**Decisione dell'autore**

Stato: IN ATTESA

Note dell'autore:

---

### D-17 Biofeedback (Mindscope, EEG/QEEG come training)

**Cosa dicono le fonti.**
- Mindscope di Barry Bittman: SL1-A T44 (r. 467-470, 553-568); MAN scheda 14 (r. 107), abbinato ad A.8, A.12 e alla fase 5 della lezione modello; SL1-C (r. 2384-2393). Procedura: sensori EMG collegati a un computer e a un lettore laserdisc; l'immagine (cascata, cigno) si sfoca se la tensione sale e torna nitida se scende. Promessa: chi rievoca il cigno è più veloce del 135% nei quiz contro il 48% dei non allenati; il controllo involontario si "riprogramma".
- EEG e QEEG: SL1-C T5 (r. 1290-1306) e DSS T10-T11 (L371-389), QEEG a 24 canali in 3D prima e dopo AVE o Hemi-Sync, con il blu e il viola come aree "inefficienti" o in "ipo-efficienza energetica"; TM T13 e SL1-B T23 (EEG come misura di "sincronizzazione emisferica" nel disegno sperimentale Tango-Mind).

**Evidenza attuale.** B per il dispositivo, che è esistito, e per il biofeedback EMG in ambito clinico (cefalea tensiva). C per il 135%: nessuna pubblicazione. A per l'EEG come strumento di misura, ma un cambiamento nell'EEG non prova un beneficio didattico. D per la lettura dei colori QEEG come "inefficienza": sono una scala convenzionale del software, e la QEEG ha un ruolo clinico riconosciuto solo in ambiti limitati. Cluster VTN F1, F2, A9, A11.
- Nestoriuc, Rief, Martin 2008, *J Consult Clin Psychol* 76:379-396 (da ricontrollare).
- Nuwer 1997, *Neurology* 49:277-292.
- Kane et al. 2017, *Clin Neurophysiol Pract* 2:170-185 (glossario EEG).

**Compatibilità Lozanov.** Rifiutato: apparecchi (Lozanov 2005, r. 1420-1421, 5811-5813). Sull'EEG: chi ha alfa prevalente "do not exhibit increased memory potential" e l'EEG non è legato "with the content of the mind" (r. 2077-2080, 2417-2419).

**Rischi.** Basso. Nessun rischio fisico rilevante per il biofeedback EMG. Per la QEEG letta in aula: etichette pseudo-diagnostiche, ansia, effetto nocebo, costi.

**Nocciolo utile.** Un feedback esterno semplice sulla tensione (specchio, video, il partner che segnala le spalle alzate) è didattica ordinaria. Conviene darlo con moderazione e orientarlo sull'effetto del movimento più che sul muscolo (INT-02).

**Raccomandazione dell'analista.** Opzione 1. Dispositivi datati o clinici, nessun beneficio didattico dimostrato; per il corso universitario l'EEG non è una buona misura di risultato (INT-10).

**Precauzioni obbligatorie se l'autore decide di includerlo.** Biofeedback strumentale solo in contesto clinico; nessuna mappa QEEG mostrata o interpretata in aula; nessuna diagnosi.

**Decisione dell'autore**

Stato: IN ATTESA

Note dell'autore:

---

## Blocco D. Musica

### D-18 Barocco lento "a 60 BPM" come base del concerto passivo

**Cosa dicono le fonti.** SL1-A T10 (r. 97-105); SL1-B T8 e sez. 5.2 (r. 636-638, 772-776, 817-856); MAN P9, A.1, A.3 e fase 4 della lezione modello (r. 21, 33, 116-117); TM D1-D3 (D:L28-68), M-3 (M:L120-174) e T8 (T:L75-79, L261-265); TLT R-T7 (R:L50, L89-90); DSS L630-631.
- Promesse: largo o andante barocco a 55-65 BPM, ideale 60, ad archi; "ogni tipo di musica è stato testato" e quella a 60 battiti ha dato i risultati migliori; il cuore si allinea e scende di 5 bpm, beta -6% e alfa +6%, "supermemoria", "comunica con il subconscio", consolidamento "senza alcuno sforzo cosciente".
- Procedura: 12-15 minuti sdraiati (SL1-A); nel Tango-Mind 30 minuti sdraiati a occhi chiusi con lettura a cicli di 8 secondi; in TLT allievi adagiati sulle poltrone a occhi chiusi. Brani tipici: Largo dell'Inverno, Aria BWV 1068, Canone di Pachelbel, "Adagio di Albinoni".

**Confronto con il Programma musicale ufficiale.** TM M:L1-96 (`musiche_relax_didattica.txt`) riporta un programma in 10 sessioni che coincide con il cap. 31 di Lozanov 2005 (r. 4118-4246), refusi compresi. Le differenze con il barocco a 60 BPM sono sostanziali:

| Punto | Fonti Superlearning | Programma canonico (Lozanov 2005) |
|---|---|---|
| Che cosa si ascolta | Movimenti lenti isolati (largo, andante) | Opere pre-classiche intere, movimenti veloci compresi: fantasie e fughe per organo di Bach, Concerti grossi op. 6 di Corelli, *Wassermusik* di Händel, concerti per flauto e *Le quattro stagioni* complete di Vivaldi, Couperin, Rameau |
| Tempo | 55-65 BPM, "esattamente 60" | Nessuna indicazione di BPM; la lettura segue il tempo della musica |
| Volume | Basso, di sottofondo | "Mainly as a background, but is as loud as a normal concert" (r. 4100-4115) |
| Allievi | Sdraiati o adagiati, occhi chiusi, rilassati | Seduti tranquilli, senza istruzioni; nessuna istruzione di rilassarsi o chiudere gli occhi (modello r. 398-408) |
| Lettura | Cicli fissi di 4 + 4 secondi | Lettura colloquiale, "like everyday speech" |
| Funzione | Rallentare cuore e onde cerebrali | Arte: opere "austere" per forma e profondità |

Le fonti mettono le due tradizioni fianco a fianco senza distinguerle (nota dell'estrattore in TM, sezione P8). Due tonalità del programma canonico sono refusi del libro: la Sinfonia n. 101 di Haydn è in re maggiore, il Concerto op. 73 di Beethoven in mi bemolle maggiore.

**Evidenza attuale.** C/D così formulato. Il cuore non si "aggancia" ai 60 bpm; la musica lenta abbassa un poco respiro e battito rispetto a quella veloce, e una pausa di silenzio li abbassa di più. Come sottofondo durante lo studio la musica ha in media un effetto nullo o lievemente negativo. L'unico studio controllato in classe sul protocollo Superlearning non ha trovato vantaggi né aumento dell'alfa. Lo "studio del 2003" citato dalle fonti non è identificabile. Cluster VNF B1, B2, B8; VPS S5, S6, M6, C8.
- Kämpfe, Sedlmeier, Renkewitz 2011, *Psychol Music* 39:424-448.
- Bernardi, Porta, Sleight 2006, *Heart* 92:445-452.
- Wagner e Tilney 1983, *TESOL Quarterly* 17:5-17 (dettagli da ricontrollare).

**Compatibilità Lozanov.** Rifiutato. "Isolated 'slow baroque' music" e "slow baroque music" sono tra le cause negate (Lozanov 2005, r. 1446-1448, 1460, 5805). Il concerto passivo canonico usa opere pre-classiche intere (r. 487-488, 4100-4115); le poltrone reclinabili come spiegazione sono "ridiculously primitive" (r. 1453-1455).

**Rischi.** Nessun rischio fisico rilevante. Sul volume vedi le Domande aperte.

**Nocciolo utile.** Una musica calma e gradita può ridurre l'ansia di alcune persone, prima o dopo la lezione, come scelta d'atmosfera dichiarata. Se si usano i brani delle fonti: l'"Adagio di Albinoni" è di Remo Giazotto (1958).

**Raccomandazione dell'analista.** Opzione 1 per il barocco lento a 60 BPM come base del concerto passivo. L'alternativa esiste già ed è canonica: il programma del cap. 31, con opere intere. I brani lenti possono restare come musica d'atmosfera fuori dai concerti, dichiarata come tale.

**Precauzioni obbligatorie se l'autore decide di includerlo.** Non necessarie: rischio non rilevante.

**Decisione dell'autore**

Stato: IN ATTESA

Note dell'autore:

---

### D-19 Effetto Mozart, Tomatis, alte frequenze, gregoriano "brain food", Forbrain/Sonic Brain Activator, Turning Sound

**Cosa dicono le fonti.**
- Effetto Mozart e Sonata K. 448 "per memorizzare dati": SL1-B (r. 876-880); MAN r. 136-139 e fase 3 della lezione modello; TM D:L122-123, M:L192-198.
- Tomatis e l'Orecchio Elettronico: filtrare le basse frequenze, "ginnastica" di "staffa e martello", ascolto spostato sull'orecchio destro, 30-60 minuti al giorno per circa 100 ore, contro dislessia, balbuzie, deficit di attenzione; Sound Therapy di Patricia Joudry: SL1-A T12 (r. 70-74, 113-121); MAN scheda 5 (r. 97); SL1-C T4; DSS T9.
- "Ricarica" della corteccia con le alte frequenze (5.000-8.000 Hz) di Mozart, Beethoven e Brahms nel concerto attivo: SL1-A T11 (r. 106-112); TM D-2 (D:L83-138), T7, T12.
- Gregoriano come "sublime cibo per il cervello", da ascoltare come "terapia di ricarica isolata": SL1-B T11 (r. 798-813); TM M1 (M:L99-118).
- Forbrain e Sonic Brain Activator: la propria voce per conduzione ossea, "10 volte più veloce", per attenzione e memoria di lavoro e per "ricaricare la neocorteccia": MAN schede 6-7 (r. 98-99), A.5, A.7.
- Turning Sound di Raymond Abrezol: barocco alterato elettronicamente che passa da un orecchio all'altro, stato in cui il dolore "non ferisce", memorizzazione con 7-8 secondi di osservazione: TM D6 (D:L141-157).

**Evidenza attuale.** A solo come resoconto dello studio di Rauscher, Shaw e Ky 1993 (36 studenti, compito spaziale, effetto di 10-15 minuti, non memoria). Per il resto D: le meta-analisi non trovano un effetto specifico di Mozart; le cellule ciliate consumano energia, non "ricaricano" la corteccia; staffa e martello sono ossicini, non muscoli; gli studi controllati indipendenti sul Tomatis sono negativi e la revisione Cochrane non trova prove per le terapie sonore affini; per Forbrain c'è un solo studio esplorativo sulla qualità della voce; Turning Sound non è identificabile. Cluster VNF B3-B7; VTN E1-E4; VPS M1-M3.
- Pietschnig, Voracek, Formann 2010, *Intelligence* 38:314-323.
- Sinha et al. 2011, *Cochrane* CD003681.
- Escera, López-Caballero, Gorina-Careta 2018, *J Speech Lang Hear Res* 61:801-810.

**Compatibilità Lozanov.** Rifiutato come meccanismo: "the secret lies only in the music programs, which activate the right cerebral hemisphere" è un'interpretazione sbagliata (Lozanov 2005, r. 5805); apparecchi (r. 1420-1421, 5811-5813). Nota: le Sinfonie n. 29, n. 40, "Haffner" e "Praga" di Mozart sono nel programma canonico come opere del concerto attivo (r. 4118-4246); la Sonata K. 448 no.

**Rischi.** Fisico basso (volume). Rischio principale: costi e false aspettative per le famiglie di bambini con dislessia o autismo, con possibile ritardo di interventi documentati come la logopedia e il trattamento fonologico.

**Nocciolo utile.** Musica brillante e gradita ascoltata prima di un compito migliora per poco umore e attivazione (Thompson, Schellenberg, Husain 2001, *Psychol Sci* 12:248-251). Dire o leggere ad alta voce aiuta a ricordare più della lettura silenziosa, con o senza cuffia (effetto di produzione, MacLeod et al. 2010, da ricontrollare). Il gregoriano resta arte di grande valore.

**Raccomandazione dell'analista.** Opzione 1 per tutte le spiegazioni e per i dispositivi. Le opere di Mozart restano nel metodo per la via canonica: come arte nei concerti.

**Precauzioni obbligatorie se l'autore decide di includerlo.** Mai presentare Tomatis, Forbrain o simili come trattamento; nessuna indicazione a famiglie di bambini con diagnosi; rinvio ai servizi sanitari.

**Decisione dell'autore**

Stato: IN ATTESA

Note dell'autore:

---

### D-20 Accordature planetarie (Hans Cousto), 136,10 Hz, risonanza di Schumann, diapason sui punti di agopuntura

**Cosa dicono le fonti.** SL1-B T12 (r. 935-944) e r. 948-950 ("i 136,10 Hz dell'OM e i 60 bpm di Bach rallentano il battito e allineano i due emisferi"); TM D10 (D:L190-205) e M-6 (M:L260-270); MAN r. 69, 115, 155 (tango "accordato sulla frequenza della Terra di 136,10 Hz") e r. 94, 109 (Schumann a 7,83 Hz nel Limina e nel generatore ELF); SL1-C r. 2105.
- Procedura: diapason tarati su 136,10 Hz (do diesis, "anno terrestre", calmante, "OM"), 194,71 Hz (sol, "giorno terrestre", energizzante), 172,06 Hz (fa, "anno platonico", gioioso), applicati sui punti di agopuntura prima dello studio; i punti non sono indicati.

**Evidenza attuale.** D. 136,10 Hz si ottiene raddoppiando più volte la frequenza di un periodo orbitale finché diventa udibile: è aritmetica, non una proprietà fisica della Terra o del corpo. La risonanza di Schumann (circa 7,8 Hz) è un dato geofisico reale (A), senza significato biologico dimostrato. Nessuno studio sull'apprendimento. Cluster VNF A7, A8; VTN G3; VPS M5.
- Nessun riferimento a sostegno.
- Per il nocciolo: Bernardi et al. 2001, *BMJ* 323:1446-1449 (recitare un mantra o il rosario rallenta il respiro a circa 6 atti al minuto).

**Compatibilità Lozanov.** Non trattato (Cousto, diapason). Il generatore a 8 Hz rientra negli apparecchi rifiutati (Lozanov 2005, r. 1420-1421, 5811-5813). Il criterio canonico di scelta della musica è artistico: "specially selected art of the classical type" (r. 2923-2926).

**Rischi.** Nessun rischio fisico rilevante.

**Nocciolo utile.** Un breve rito d'inizio (un suono, un gesto, un silenzio) aiuta a raccogliere l'attenzione, con un diapason qualsiasi o senza. Cantare o recitare lentamente rallenta il respiro: è un effetto del respiro, non della frequenza.

**Raccomandazione dell'analista.** Opzione 1. Numeri senza effetti dimostrati. Nel Qigong rischia di mescolare alla tradizione calcoli senza fondamento e di urtare la barriera critico-logica degli allievi (Lozanov 2005, r. 2802-2845).

**Precauzioni obbligatorie se l'autore decide di includerlo.** Non necessarie: rischio non rilevante.

**Decisione dell'autore**

Stato: IN ATTESA

Note dell'autore:

---

### D-21 Musica di tango (o cinese per il Qigong) dentro i concerti

**Cosa dicono le fonti.** Le fonti usano la musica di tango per il movimento, non per i concerti: MAN A.9 (r. 66-70) e fase 2 della lezione modello (r. 115) con tango "a 60-120 BPM" (Di Sarli, D'Arienzo, Piazzolla); SL1-C (r. 2104-2105, 2445). Nel Tango-Mind i concerti restano su Mozart e sul barocco (TM T7, T8). Un concerto passivo su "tango lento strumentale a pulsazione intorno a 60" compare solo come ipotesi dell'estrattore (SL1-A, nota a T10), non nella fonte. Per il Qigong nessuna fonte propone musica cinese nei concerti; le uniche musiche di ispirazione cinese citate sono Vangelis (*China*) e Kitaro (*Silk Road*), usate come sottofondo per il role-play, l'Image Streaming o le materie scolastiche (MAN A.7, A.8; SL1-B T21). La questione nasce dall'adattamento del canone (modello r. 762).

**Evidenza attuale.** Non c'è una domanda di efficacia da verificare: nessuno studio confronta concerti su tango o musica cinese con concerti sul repertorio canonico. Sui dati di tempo, B: il pulsare dei tanghi da ballo è intorno a 60-70 al minuto, le milonghe vanno da circa 76 a oltre 120, Piazzolla è per lo più musica da ascolto; "60-120 BPM" mescola cose diverse (VPS M9). Le canzoni con testo aiutano il ricordo verbale, mentre una musica cantata come sottofondo disturba l'elaborazione di materiale verbale (VPS C10).
- Ludke, Ferreira, Overy 2014, *Mem Cognit* 42:41-52.
- Kämpfe et al. 2011.

**Compatibilità Lozanov.** Non trattato, ma l'uso nei concerti modifica il canone. Il quinto fattore indispensabile parla di "a classical type of arts" (Lozanov 2005, r. 5853); le associazioni più efficaci nascono da "specially selected art of the classical type" (r. 2923-2926); il programma è quello del cap. 31. La musica e i canti del paese entrano nelle elaborazioni come cultura ("culture of the respective country", r. 4349-4352).

**Rischi.** Nessun rischio fisico rilevante.

**Nocciolo utile.** Nel tango la musica è contenuto: musicalità, orchestre, letras. Nel Qigong la musica tradizionale cinese può dare contesto culturale. In entrambi i casi il posto canonico è nelle canzoni d'apertura e chiusura, nei giochi e nella pratica.

**Raccomandazione dell'analista.** Opzione 3. Tango e musica cinese entrano nel metodo come contenuto e come cultura (pratica, canti, giochi, apertura e chiusura), mentre i concerti restano sul repertorio classico canonico. Se l'autore decide di usarli anche nei concerti, è un adattamento da dichiarare e, nel corso universitario, da valutare. È una scelta in cui pesa l'esperienza dell'autore (Domande aperte).

**Precauzioni obbligatorie se l'autore decide di includerlo.** Non necessarie: rischio non rilevante. Conviene misurare il tempo reale dei brani scelti.

**Decisione dell'autore**

Stato: IN ATTESA

Note dell'autore:

---

### D-22 Musiche commerciali "per l'apprendimento" (Hoffman, Halpern, Kobialka, Brain/Mind Resonance, olofonia Zuccarelli)

**Cosa dicono le fonti.** Janalea Hoffman (*Rhythmic Medicine*, *Deep Daydreams* a 60 e poi 50 BPM, *Mind Body Tempo*): SL1-A r. 75-77; MAN A.2, A.4, A.8; TM M2 (M:L217-230) e D:L71-81; SL1-B T22. Steven Halpern (*Anti-Frantic Alternative*): MAN A.2, A.12 e fase 5. Daniel Kobialka: TM M-5 (M:L213-258). Nastri "Brain/Mind Resonance" di Terry Patten e Julian Isaacs: TM D8 (D:L174-182). Olofonia di Hugo Zuccarelli: TM D9 (D:L184-188). Altri: William Duncan (*Exultate*), André Gagnon, Paul Horn, Dyveke Spino, Kitaro, Vangelis (MAN sez. 7.1; TM M-5).
- Promesse: effetti su pressione, aritmie, insonnia e ansia da esame (Hoffman); "rilassamento senza sforzo" e "stati di gioia, unità e beatitudine" (Patten e Isaacs); sinestesia e immaginazione potenziata per memoria, apprendimento e prove mentali (olofonia).

**Evidenza attuale.** C per i prodotti: nessuno studio controllato rintracciabile su prodotti specifici. B per la musica gradita in generale: riduce stress e ansia e, nell'insonnia, aiuta un poco ad addormentarsi. Nessuna prova su aritmie o allergie. Cluster VTN H1-H5; VPS M8.
- Jespersen et al. 2022, *Cochrane* CD010459.pub3 (musica e insonnia: piccolo beneficio, qualità moderata).
- de Witte et al. 2020, *Health Psychol Rev* 14:294-324 (da ricontrollare).

**Compatibilità Lozanov.** Rifiutato: "special audio cassettes on sale", "selling tapes" (Lozanov 2005, r. 1433-1435, 5811-5813). Nel canone la musica è arte di tipo classico (r. 2923-2926), non sottofondo funzionale.

**Rischi.** Nessun rischio fisico rilevante.

**Nocciolo utile.** Musica gradita, scelta dagli allievi, nelle pause o a casa.

**Raccomandazione dell'analista.** Opzione 1. Prodotti commerciali senza prove specifiche, estranei al criterio artistico del canone.

**Precauzioni obbligatorie se l'autore decide di includerlo.** Non necessarie: rischio non rilevante.

**Decisione dell'autore**

Stato: IN ATTESA

Note dell'autore:

---

## Blocco E. Formattazione "Superlearning"

### D-23 Cicli ritmici 8 s / 12 s, unità di 7-9 parole, sessioni di 13 minuti

**Cosa dicono le fonti.** SL1-A T13-T15 (r. 149-165); MAN A.5 "Protocollo Lozanov/Bancroft" (r. 42-46), PR2 e fase 3 della lezione modello; SL1-B T6 (r. 625-638, 768-771); TM T9 (T:L63-65, L76-78, L257-259) e D1 (D:L57-61); SL1-C P5 (r. 2008-2017).
- Procedura: unità di non più di 7-9 parole; ciclo di 8 secondi, 4 di lettura e 4 di silenzio, con metronomo, per circa 13 minuti; ciclo di 12 secondi (parola, sillabazione, frase di contesto) coordinato con inspiro, apnea ed espiro. Nel Tango-Mind i cicli stanno sui passi base del concerto attivo oppure nel concerto passivo da sdraiati: il file si contraddice.
- Promesse: nella pausa le "reti chimiche" del cervello "solidificano" l'informazione; consolidamento a lungo termine; il protocollo è attribuito a Lozanov e Bancroft.

**Evidenza attuale.** D per il protocollo e il meccanismo: viene dal Superlearning (Ostrander e Schroeder 1979), non da Lozanov 2005; l'unico studio controllato in classe non ha trovato vantaggi; in un esperimento moderno parlare in ritmo non ha aiutato, cantare sì; per i 13 minuti non c'è fonte. B per due noccioli: frasi brevi e di senso compiuto dentro un testo intero; nell'apprendimento motorio, brevi pause tra le ripetizioni producono guadagni rapidi. Cluster VPS S1-S3, P10; VNF B9.
- Wagner e Tilney 1983 (da ricontrollare).
- Ludke, Ferreira, Overy 2014, *Mem Cognit* 42:41-52.
- Bönstrup et al. 2019, *Curr Biol* 29:1346-1351.

**Compatibilità Lozanov.** Rifiutato. Un ritmo fisso e ripetuto è un "monotonous rhythmic stimulus", meccanismo d'induzione (Lozanov 2005, r. 1394-1397, 1830-1832). La lettura canonica segue la frase musicale (r. 4037-4060). L'insegnamento "of small, isolated portions [...] contradicts certain psycho-physiological laws" (r. 2885-2889). Il concerto attivo dura fino a 45-50 minuti con opere intere (r. 4049-4050). Il libro "Super Learning" è respinto per nome (r. 1456-1458).

**Rischi.** Basso. Il ciclo di 12 secondi con apnea ha i rischi di D-05.

**Nocciolo utile.** Frasi brevi dentro una storia intera (VPS R-S2). Nella pratica motoria, alternare esecuzione e brevi pause, senza metronomo verbale: è INT-11.

**Raccomandazione dell'analista.** Opzione 1. La procedura è attribuita a Lozanov in modo sbagliato, contraddice il canone e non ha prove. Il nocciolo motorio passa in INT-11.

**Precauzioni obbligatorie se l'autore decide di includerlo.** Nessuna apnea associata al ciclo di 12 secondi.

**Decisione dell'autore**

Stato: IN ATTESA

Note dell'autore:

---

### D-24 Tre toni fissi (normale/sussurrato/imperativo) contro intonazione oscillante canonica

**Cosa dicono le fonti.** SL1-A T16 (r. 166-172): foglio a tre colonne; voce normale, voce sussurrata "cospiratoria", voce alta e "perentoria", solo per le parole straniere, con la traduzione detta in tono neutro. MAN A.5 (r. 42-46); TM T7 e T9 (T:L259); SL1-B T6. TLT R-T4 (R:L43) dà un'altra terna: autorevole ed esortativo, solenne, sussurrato e confidenziale.
- Promesse: i tre toni aggirano "saturazione e noia della corteccia", mantengono l'attenzione selettiva, ancorano l'informazione alla memoria episodica ed emotiva.

**Evidenza attuale.** C per i tre toni fissi: nessuno studio. B per il principio: una voce variata tiene l'attenzione meglio di una monotona e un elemento distintivo si ricorda meglio. Cluster VNF B10; VPS S4, T12.
- Hunt 1995, *Psychon Bull Rev* 2:105-112 (distintività).

**Compatibilità Lozanov.** Rifiutati il tono imperativo e lo schema fisso. Il docente evita di esagerare gli elementi "sentimentali e imperativi" (Lozanov 2005, r. 4089-4091); "order", "guidance", "monotonous intonation", "monotonous rhythm" "might cause hypnosis" (r. 1394-1397). Coerente l'intonazione oscillante, morbida, mai monotona (r. 2709-2712, 2740-2741), che nel concerto segue modo, tempo e frase musicale e cambia l'intonazione dell'ultima parola di ogni frase (r. 4021-4099). Lozanov avverte: "the intonation cannot be described – it must be heard and corrected" (r. 4447-4452).

**Rischi.** Nessun rischio fisico rilevante.

**Nocciolo utile.** Voce espressiva e variata, che segue il senso e la musica. Nel tango e nel Qigong vale per le indicazioni verbali: variare voce e ritmo, evitare il conteggio meccanico continuo e la cantilena uniforme delle conduzioni guidate.

**Raccomandazione dell'analista.** Opzione 3: intonazione oscillante canonica al posto dei tre toni fissi. Su questo punto la formazione pratica dell'autore vale più di qualsiasi testo.

**Precauzioni obbligatorie se l'autore decide di includerlo.** Non necessarie: rischio non rilevante.

**Decisione dell'autore**

Stato: IN ATTESA

Note dell'autore:

---

## Blocco F. Corpo, vestibolo, mappature

### D-25 Infinity Walk (Sunbeck): come esercizio di camminata/ochos contro "integrazione emisferica" e test diagnostico

**Cosa dicono le fonti.** SL1-A T22 (r. 185-186, 246-252); SL1-B T4 (r. 611-619, 692-695, 734-745) e T5 (r. 997-1010); MAN A.9 (r. 66-70) e fase 2 della lezione modello (30 minuti); DSS T2 (L50-66) e T3 come test (L313-332); SL1-C T3 come test (r. 1234-1249) e T10 con l'ancoraggio; TM T4 e T5 (T:L32-44, L152-156, L213-218).
- Procedura: camminare su un grande otto tracciato a terra, braccia in oscillazione controlaterale, appoggi di tallone decisi, sguardo fisso su un bersaglio; poi compiti cognitivi camminando (recitare vocaboli, risolvere equazioni). Nel tango, ochos, pivot e giri al posto della camminata, "declamando concetti accademici". Come test: simmetria dei loop, ancoraggio visivo, coordinazione crociata.
- Promesse: armonizzare emisferi "disallineati" attraverso il corpo calloso; risolvere la "cecità di lettura" e la dipendenza dalla TV; cancellare la "nebbia mentale"; abbattere ansia e fobia dello studio; preparare a nuove lingue; gli ochos "simulano neurologicamente" l'Infinity Walk. Come test indicherebbe disallineamento emisferico e disfunzione vestibolo-cerebellare. Il percorso è chiamato "nastro di Möbius".

**Evidenza attuale.** D per l'integrazione emisferica e per l'uso come test: nessuno studio controllato; programmi simili di "integrazione cerebrale" (Brain Gym) non hanno prove; mancano standardizzazione e valori di riferimento. B per il nocciolo: una breve attività motoria migliora un poco umore e funzioni esecutive, camminare favorisce le idee, esercitare equilibrio e coordinazione migliora equilibrio e coordinazione. Attribuzione corretta a Deborah Sunbeck. Correzione: il percorso è una lemniscata, non un nastro di Möbius. Cluster VNF D7, D8, C2; VPS B2, B3.
- Spaulding, Mostert, Beam 2010, *Exceptionality* 18:18-30.
- Oppezzo e Schwartz 2014, *J Exp Psychol Learn Mem Cogn* 40:1142-1152.
- Khan, Naseer, Mirtaheri 2024, *IBRO Neurosci Rep* (fNIRS su 6 persone, studio di fattibilità sulla pronazione del piede).

**Compatibilità Lozanov.** Non trattato. Il movimento come veicolo è nel canone ("easy dances", Lozanov 2005, r. 4283; allievi in piedi, r. 4073-4074). L'uso come test diagnostico è in tensione con "The teacher is not a physician" (r. 2046-2047).

**Rischi.** Medio. Anziani; persone con disturbi vestibolari o vertigini, postumi di commozione cerebrale, neuropatie, gravidanza avanzata, farmaci sedativi: capogiro, perdita d'equilibrio, cadute. In gruppo: collisioni. Il doppio compito (ballare e recitare) in coppia e in sala affollata aumenta il rischio. Come test: etichette, ansia, effetto nocebo, ritardo di una valutazione vera se i sintomi sono reali.

**Nocciolo utile.** La camminata a otto è un buon riscaldamento per il tango (cambi di direzione, asse, sguardo, preparazione agli ochos) e per le camminate del Qigong.

**Raccomandazione dell'analista.** Opzione 3 come esercizio di equilibrio, orientamento e coordinazione, senza promesse cognitive e senza il linguaggio degli emisferi. Opzione 1 per l'uso come test diagnostico.

**Precauzioni obbligatorie se l'autore decide di includerlo.** Spazio libero e pavimento non scivoloso; percorsi distanziati; velocità lenta; occhi aperti; rotazioni della testa introdotte gradualmente; fermarsi al primo capogiro; versione ridotta o con appoggio; chi ha disturbi vestibolari noti chiede prima al medico; doppio compito solo da soli e in spazio ampio; appoggi di tallone morbidi.

**Decisione dell'autore**

Stato: IN ATTESA

Note dell'autore:

---

### D-26 Mappature diagnostiche (lateralità Sunbeck, orecchio dominante Tomatis, ciclo nasale, EEG 24 canali/QEEG)

**Cosa dicono le fonti.** SL1-C T1-T5 e P8 (r. 1173-1306, ripetuto a r. 1312-1450); DSS T7-T10 e PR6 (L252-389); MAN scheda 5 (Tomatis, r. 97). Collegata la tesi attribuita a Harold Levinson: oltre il 90% dei disturbi d'apprendimento nascerebbe da una disfunzione vestibolare e cerebellare (SL1-B r. 989-992; DSS L42-46).
Sequenza proposta:
1. test del ciclo nasale: la dominanza emisferica cambierebbe ogni 90 minuti, "strettamente sincronizzata" con la narice aperta, e "sdraiarsi sul fianco destro attiva l'emisfero sinistro";
2. tre canali di Sunbeck (occhio, orecchio, mano) con 8 combinazioni; la dominanza "divisa" crea latenze e "statico";
3. test dinamico Infinity Walk (D-25);
4. audiometria Tomatis tra 2.000 e 12.000 Hz: l'orecchio sinistro dominante sarebbe all'origine di dislessia, balbuzie e deficit d'attenzione, con un ritardo di 0,1-0,2 secondi;
5. QEEG a 24 canali in 3D prima e dopo AVE o Hemi-Sync, con il blu e il viola come aree "inefficienti".

**Evidenza attuale.** D per lateralità crociata, orecchio dominante, regola del fianco (che contraddice la mappa dello stesso testo), colori QEEG, tesi di Levinson. C per il legame tra ciclo nasale ed emisferi (piccoli studi degli anni '80; il ciclo in veglia dura in media circa 2 ore). Una meta-analisi su 26 studi e 3.578 bambini non trova associazioni affidabili tra lateralità crociata e rendimento; il trasferimento tra emisferi richiede pochi millisecondi; la dislessia è soprattutto un disturbo fonologico. Insegnare secondo il canale "preferito" non ha prove. Cluster VNF C3-C7, D4, D8; VTN A9, A11; VPS B4.
- Ferrero, West, Vadillo 2017, *PLoS ONE* 12:e0183618.
- Pashler et al. 2008, *Psychol Sci Public Interest* 9:105-119 (stili di apprendimento).
- Nuwer 1997, *Neurology* 49:277-292 (QEEG).

**Compatibilità Lozanov.** Non trattato come tale, ma in contrasto con due punti del canone: "The teacher is not a physician" (Lozanov 2005, r. 2046-2047) e l'EEG non legato "with the content of the mind" (r. 2417-2419).

**Rischi.** Medio. Bambini con dislessia, autismo o ADHD e le loro famiglie: costo-opportunità (tempo e denaro sottratti a interventi con prove), etichette che generano ansia, effetto nocebo. Adulti: etichette stabili senza base ("sono a cervello destro"). Ritardo di una valutazione vera se i sintomi (vertigini, difficoltà di lettura) sono reali.

**Nocciolo utile.** Presentare il materiale in più modalità aiuta tutti, non un "tipo". Il ciclo nasale esiste ed è una curiosità fisiologica.

**Raccomandazione dell'analista.** Opzione 1. Pseudo-diagnosi senza validità, fuori dal ruolo del docente, con rischi concreti proprio per i più fragili.

**Precauzioni obbligatorie se l'autore decide di includerlo.** Nessuna diagnosi né profilo in aula; in presenza di difficoltà reali, rinvio a neuropsichiatria infantile, logopedia, otorinolaringoiatria; nessuna mappa QEEG interpretata da personale non sanitario.

**Decisione dell'autore**

Stato: IN ATTESA

Note dell'autore:

---

### D-27 Concerto attivo in movimento (adattamento non canonico per tango e Qigong)

**Cosa dicono le fonti.**
- SL1-A T11 (r. 106-112): nel concerto attivo il discente "non è prima in rilassamento fisico": "si cammina e ci si muove" mentre il testo è letto in modo molto drammatico, con la voce che asseconda o contrasta i picchi degli archi.
- TM T7 (T:L72-75, L256-260) e SL1-B T7 (r. 768-771): fase 3 del Tango-Mind, 45 minuti, gli studenti "mentre si muovono o eseguono passi base, ascoltano o recitano le nozioni" in cicli di 4 + 4 secondi e con tre toni, su Mozart "ad altissima frequenza".
- TM T5 (T:L216-218): declamare concetti accademici durante il ballo.
- TLT, ipotesi dell'estrattore: concerto attivo come dimostrazione del maestro sulla musica, con commento vocale modulato.

**Evidenza attuale.** C: nessuno studio sul formato. Indirettamente, brevi pause di attività fisica in classe migliorano un poco il comportamento in compito, con effetti incerti sul rendimento (B). Le componenti aggiunte nel Tango-Mind (cicli di 8 secondi, tre toni) hanno le valutazioni di D-23 e D-24. Cluster VPS C9.
- Watson et al. 2017, *Int J Behav Nutr Phys Act* 14:114 (da ricontrollare).

**Compatibilità Lozanov.** Non trattato: Lozanov non tratta l'apprendimento motorio (modello r. 718). Nel concerto attivo canonico gli allievi hanno testo e traduzione, guardano il testo "and only listen to the music – not to try to memorise", e si alzano ogni tanto per leggere con il docente, 1-3 volte per 1-3 minuti (Lozanov 2005, r. 4021-4099, 4073-4074); attivo e passivo "must never be separated". Il modello canonico propone un adattamento più vicino al canone: il docente esegue o racconta l'intera "storia" della sequenza su un'opera classica intera, gli allievi guardano e ascoltano a occhi aperti con una scheda illustrata come "libretto"; e mette in guardia dal movimento sincronizzato guidato dalla voce su musica lenta (modello r. 761, interpretazione).

**Rischi.** Basso. Collisioni e cadute se tutto il gruppo si muove in sala affollata; doppio compito in coppia. Se combinato con apnee o cicli fissi, i rischi di D-05 e D-23.

**Nocciolo utile.** Nel tango e nel Qigong il movimento è il contenuto, non un sottofondo del concerto. Un concerto con il corpo fermo può sembrare lontano dalla disciplina; uno in cui il corpo esegue mentre la voce guida rischia di diventare un'induzione. Lo spazio di progettazione sta in mezzo.

**Raccomandazione dell'analista.** Opzione 2. È un adattamento strutturale senza prove e senza indicazioni nel canone: conviene provarlo come pilota dichiarato, confrontando almeno due versioni (allievi che guardano e ascoltano, con brevi momenti in piedi; allievi che segnano i passi in modo leggero e libero, senza comandi), con una valutazione semplice (INT-10). Il formato Tango-Mind con cicli di 8 secondi e tre toni resta documentato. È una delle decisioni in cui l'esperienza dell'autore pesa di più (Domande aperte).

**Precauzioni obbligatorie se l'autore decide di includerlo.** Spazio libero; movimento libero e leggero, non sincronizzato da comandi vocali; niente occhi chiusi in movimento; possibilità di restare seduti; niente cicli fissi né apnee.

**Decisione dell'autore**

Stato: IN ATTESA

Note dell'autore:

---

### D-28 Tecnica Alexander (inibizione e facilitazione)

**Cosa dicono le fonti.** SL1-B T14 (r. 1012-1022); DSS T4 (L67-80).
- Procedura: inibizione, cioè sopprimere le risposte motorie casuali o involontarie portando un focus intenzionale su ogni singola contrazione e riducendo le tensioni parassite; facilitazione, cioè la corteccia dirige in modo fluido le azioni necessarie, con una corretta biomeccanica spinale.
- Promesse: non sovraccaricare il sistema nervoso; togliere le tensioni che "bloccano il flusso energetico"; una corretta biomeccanica spinale è essenziale per la salute del sistema nervoso e immunitario.

**Evidenza attuale.** B per la Tecnica Alexander nel mal di schiena cronico e nel dolore cervicale (studi randomizzati); D per "flusso energetico" e sistema immunitario. Cluster VNF D15.
- Little et al. 2008, *BMJ* 337:a884.
- MacPherson et al. 2015, *Ann Intern Med* 163:653-662.

**Compatibilità Lozanov.** Non trattato.

**Rischi.** Nessun rischio fisico rilevante.

**Nocciolo utile.** La pausa prima del movimento (inibizione) e il riconoscimento delle tensioni inutili servono nel tango (abbraccio, spalle, collo) e sono affini al song del Qigong. Una tensione da segnalare: la procedura delle fonti chiede attenzione "su ogni singola contrazione", cioè un focus interno, mentre nell'apprendimento motorio il focus esterno dà in media risultati migliori (INT-02). Le due cose si conciliano con una pausa di inibizione prima del gesto, seguita da un'indicazione rivolta all'effetto del movimento.

**Raccomandazione dell'analista.** Opzione 3, riformulato come principio di pausa prima del movimento e di riduzione delle tensioni inutili: senza "energia" né sistema immunitario, e senza presentarlo come insegnamento della Tecnica Alexander, che ha una propria formazione di insegnanti.

**Precauzioni obbligatorie se l'autore decide di includerlo.** Non necessarie: rischio non rilevante.

**Decisione dell'autore**

Stato: IN ATTESA

Note dell'autore:

---

### D-29 Altre tecniche delle fonti: TPR (Asher), teatro e mimo, mappe mentali / palazzo della memoria, contesto olfattivo, istruzione inversa (Guthridge), filastrocche e canzoni mnemoniche

**Cosa dicono le fonti.** Tutte in SL1-A, cap. 3-4.
- **TPR** (James Asher): T23 (r. 182-184), apprendimento che "imprime le memorie muscolarmente", nei programmi di Tam Gisler e Ann Arruda. TM T4 e SL1-B T4 leggono il tango come TPR.
- **Teatro e mimo**: T26 (r. 202-211). Peter Ginn fa mimare la sintassi degli algoritmi con giocolieri finti e ruoli da show televisivo; A. Galceran prepara un'attrice in 2 ore di "esperienze teatrali barocche sensoriali".
- **Mappe mentali e palazzo della memoria**: T20 (r. 229-235). Grandi fogli con le nozioni che si diramano da un fusto, colori, pastelli profumati (mela, pino), immagini enormi o ridicole; nozioni fissate in luoghi familiari con "statue mentali disarmoniche".
- **Contesto olfattivo**: T25 (r. 197-201). Studio "di Yale" con lo stesso odore di cioccolato allo studio e al test, attribuito a "Frank Staub", con prestazioni "molto superiori".
- **Istruzione inversa** (George Guthridge): T24 (r. 191-196). Problem solving a ritroso e immedesimazione; i ragazzi yupik di Gambell che avrebbero battuto circa 16.000 scuole.
- **Filastrocche e canzoni**: T17 (r. 136-138, 177-179). Leo Wood mette la chimica su melodie natalizie; Rosella Wallace usa rime, ritmo muscolare e filastrocche con il salto della corda.

**Evidenza attuale.**

| Tecnica | Livello | Motivazione | Riferimenti |
|---|---|---|---|
| TPR | A (memoria di azioni) / B (lessico) | Eseguire l'azione indicata da una frase la fa ricordare meglio; i gesti aiutano il lessico straniero; come metodo completo il TPR è adatto soprattutto ai livelli iniziali e al lessico concreto. Gisler e Arruda non verificati (VPS B1) | Roberts, MacLeod, Fernandes 2022, *Psychol Bull* 148:397-434; Macedonia e Knösche 2011, *Mind Brain Educ* 5:196-211 |
| Teatro e mimo | B (aneddoti: C) | La pedagogia teatrale ha effetti positivi in meta-analisi, con disegni deboli; gli aneddoti delle fonti non sono verificati (VPS C1, N1) | Lee et al. 2015, *Rev Educ Res* 85:3-49 |
| Mappe mentali e palazzo della memoria | B per il metodo dei loci; C per l'uso proposto | Nei file di verifica non c'è un cluster dedicato. Il metodo dei loci è usato da mnemonisti allenati (citato in VNF I5). Le varianti delle fonti (pastelli profumati, statue disarmoniche) non sono verificate | Dresler et al. 2017, *Neuron* 93:1227-1235 |
| Contesto olfattivo | B | Lo studio è di Frank Schab (1990), non "Staub": l'odore presente allo studio e al test migliora il ricordo. Effetto di contesto reale ma modesto e variabile; "molto superiori" è eccessivo (VNF F6) | Schab 1990, *J Exp Psychol Learn Mem Cogn* 16:648-655; Smith e Vela 2001, *Psychon Bull Rev* 8:203-220 |
| Istruzione inversa | B come fatto storico; C come tecnica | I ragazzi di Gambell vinsero due volte il Future Problem Solving (1983-1984); il numero di scuole va verificato; il successo non si può attribuire al Superlearning (VPS N2) | Fonti di contesto citate in VPS N2 (risoluzione del Senato dell'Alaska, 1984) |
| Filastrocche e canzoni | B | Le melodie semplici aiutano il ricordo parola per parola; cantare frasi straniere aiuta più che dirle. È il nocciolo vero degli aneddoti Superlearning (VPS N1) | Wallace 1994, *J Exp Psychol Learn Mem Cogn* 20:1471-1485; Ludke, Ferreira, Overy 2014 |

**Compatibilità Lozanov.**
- Coerenti: il sistema delle canzoni (Lozanov 2005, r. 2715-2716, 4321); i dettagli "acted out through games and songs (and even through easy dances)" (r. 4283); il gioco-progetto del film e le voci da attori (r. 755-759, 3943-3949, 4265-4313); mostrare prima il tutto e poi le parti, che è il senso dell'istruzione inversa, corrisponde al principio globale-parziale (r. 2932-2933).
- Non trattati: TPR (compatibile con i giochi), contesto olfattivo, mappe mentali e palazzo della memoria. Le mappe appese alle pareti diventano percezioni periferiche, che il canone vuole "done artistically and in good taste" e senza sovraccarico (r. 3104-3110).

**Rischi.** Basso. Odori in aula: persone con asma, allergie, sensibilità ai profumi (crisi d'asma, cefalea, irritazione). Per le altre tecniche nessun rischio fisico rilevante.

**Nocciolo utile.** Fare, mimare e cantare aiutano a ricordare. Nel tango la lezione è già in gran parte TPR (consegna verbale, risposta del corpo), anche per i termini spagnoli; nel corso universitario e nella formazione insegnanti il gesto e il teatro servono ai concetti.

**Raccomandazione dell'analista.**
- TPR: opzione 3, come integrazione dichiarata (vedi INT-08).
- Teatro e mimo: opzione 3, dentro il gioco-progetto canonico.
- Mappe mentali: opzione 3 come mappa delle figure o dei concetti appesa alla parete, curata come percezione periferica.
- Palazzo della memoria: opzione 2, strumento facoltativo di studio individuale (corso universitario, formazione insegnanti).
- Contesto olfattivo: opzione 1. Lo stesso effetto di contesto si ottiene senza rischio allergico con un segnale sonoro costante, per esempio la canzone d'apertura e chiusura canonica.
- Istruzione inversa: opzione 3, come "mostrare prima la figura intera, poi le parti".
- Filastrocche e canzoni: opzione 3, dentro il sistema delle canzoni (INT-09); conte ritmiche per il compás e la milonga.

**Precauzioni obbligatorie se l'autore decide di includerlo.** Per gli odori: solo con il consenso di tutto il gruppo, niente diffusori o oli essenziali in ambienti chiusi. Per le altre tecniche non necessarie.

**Decisione dell'autore**

Stato: IN ATTESA

Note dell'autore:

---

## Blocco G. Linguaggio e teoria

### D-30 Neuromiti nel linguaggio del metodo (onde alfa, emisferi, 4% del potenziale, "supermemoria"): come trattarli nei testi

**Cosa dicono le fonti.** Il linguaggio ricorre in quasi tutte le fonti:
- onde alfa e "allerta rilassata" come stato d'apprendimento: MAN P4-P6 (r. 20-22, 94); SL1-A T10 (beta -6%, alfa +6%); TLT R:L89-90; TM D:L41-44;
- scuola "dell'emisfero sinistro" e integrazione emisferica: MAN P2 (r. 10); SL1-B P5 (r. 615-619, 681-685); TLT R:L83 (attribuita a Edelmann); TM T:L139-144; SL1-C r. 1904-1907;
- "il 4% del potenziale", con il 96% inibito dalle norme sociali: TLT R:L6;
- "supermemoria", "memoria immensa", consolidamento "senza sforzo cosciente": TM D:L49-55, T:L263-265; SL1-A r. 104-105;
- altre immagini: il movimento "nutriente" del cervello e la transizione 3D-2D (SL1-B r. 725-740, 967-983), il "cervello rettiliano" (MAN r. 196), le "tossine dello stress" (DSS L239-241), il paradigma dei "tre blocchi da scardinare" (SL1-B T20).

**Evidenza attuale.** D. Chi ha più alfa non ricorda di più, e la buona codifica si accompagna anzi a una riduzione dell'alfa nelle aree impegnate; non esistono persone "a cervello sinistro o destro"; la cifra del 4% è una variante del mito del "10% del cervello"; "supermemoria" non è un costrutto scientifico. Questi neuromiti sono molto diffusi tra gli insegnanti. Cluster VNF A1, A2, C1, C2, D9, D11, E6, F2; VPS B5, T2; VTN A12.
- Klimesch 2012, *Trends Cogn Sci* 16:606-617.
- Nielsen et al. 2013, *PLoS ONE* 8:e71275.
- Dekker et al. 2012, *Front Psychol* 3:429.

**Compatibilità Lozanov.** Rifiutato. Onde alfa (Lozanov 2005, r. 1460, 2077-2080, 5804). "The 'super' reminds us of 'Superman' and, as in anything that smacks of pure advertising, provokes distrust": il termine giusto è "hypermnesia, not supermemory" (r. 1504-1507). "The secret lies only in the music programs, which activate the right cerebral hemisphere" è un'interpretazione sbagliata (r. 5805). La cifra del 4% non è nel libro. Le barriere non si "scardinano": "should not be stimulated" (r. 2842-2845). Sono canonici, invece, "ipermnesia", "riserve" e "norma sociale suggestiva" (r. 529-582, 2752-2800): tesi del fondatore, livello C, non verificate in modo indipendente.

**Rischi.** Nessun rischio fisico rilevante. Rischio reputazionale alto: davanti a un pubblico universitario è il punto più esposto del progetto. Promesse che deludono e colpevolizzano; etichette ("sei a cervello destro").

**Nocciolo utile.** Ciò che queste immagini cercano di dire ha formulazioni oneste: ridurre l'ansia libera memoria di lavoro; il movimento fa bene a umore e funzioni esecutive; la paura di cadere irrigidisce il corpo. I testi pronti sono in VNF sez. 4.1 e VPS sez. 6.

**Raccomandazione dell'analista.** Opzione 3. Riformulare tutti i testi con le formulazioni oneste dei file di verifica; usare i termini canonici (ipermnesia, riserve) presentandoli come tesi del fondatore; segnare le affermazioni scientifiche con la scala A-D, come suggerito in VNF sez. 7.8.

**Precauzioni obbligatorie se l'autore decide di includerlo.** Regole redazionali: nessuna percentuale sul "potenziale"; nessun "emisfero" come stile cognitivo; nessun "super"; ogni dato numerico con la sua fonte.

**Decisione dell'autore**

Stato: IN ATTESA

Note dell'autore:

---

### D-31 Cornice teorica predictive coding / trauma / metastabilità (Kotler et al. 2026 e altri)

**Cosa dicono le fonti.** TLT, file T (`Trauma_Predictive_Coding_Metastabilita.md`): bibliografia ragionata costruita intorno a Kotler, Mannino, Fox, Friston 2026.
- Tesi: il trauma non è "conservato nei tessuti", è un disturbo di inferenza predittiva, con un eccesso di precisione dei "danger priors" e una perdita di metastabilità, cioè di flessibilità tra stati di rete (T:L88-101). Il corpo è messaggero, non archivio (T:L99-103).
- Implicazioni: movimento in ambienti realmente sicuri, flow, gioco, danza e arti marziali come "dati di sicurezza" e "training di metastabilità e neuro-percezione" (T:L111-124, L143); bellezza e incertezza vissute in sicurezza come fattori trasformativi (T:L60-63).
- La fonte stessa avverte che il modello è teorico e non validato (T:L133-136).
- Problemi: premessa "muscoli e fascia non innervati" (T:L88); riferimenti di bassa qualità (Instagram, LinkedIn, Substack, un blog in cinese); "tutte le terapie efficaci" condividerebbero l'obiettivo di ripristinare la metastabilità (T:L109); l'EMDR è elencato tra le terapie corporee (T:L112).

**Evidenza attuale.** B per i riferimenti principali, che esistono e sono attribuiti correttamente, e per il nucleo cognitivo (interpretazioni catastrofiche dei segnali del corpo, minaccia percepita come attuale), che è un modello clinico consolidato. C per la traduzione in "metastabilità", poco misurata nei campioni clinici, e per il movimento come training di metastabilità. D per la premessa anatomica: muscoli e fasce sono riccamente innervati. Sono soprattutto modelli teorici e articoli d'opinione. Cluster VNF H1-H11; VTN M2-M4.
- Kotler, Mannino, Fox, Friston 2026, *Front Syst Neurosci* 20:1812957 (articolo d'opinione).
- Ehlers e Clark 2000, *Behav Res Ther* 38:319-345.
- Rosenbaum et al. 2015, *Psychiatry Res* 230:130-136 (attività fisica e sintomi di PTSD).

**Compatibilità Lozanov.** Non trattato: Lozanov non parla di trauma. Due vincoli: il docente non fa terapia (Lozanov 2005, r. 2046-2047, 3334-3336); le barriere antisuggestive non si forzano (r. 2802-2845). Un punto di contatto: l'estetica come "teaching, healing and personality harmonising method" (r. 3924-3928) e l'obiettivo di togliere la paura dell'apprendimento.

**Rischi.** Medio. Promettere una "terapia del trauma" a persone traumatizzate in un corso di tango o di Qigong; il contatto dell'abbraccio come possibile innesco; la narrativa del "trauma nella fascia", che la stessa fonte critica, può essere iatrogena; propagare dati errati da fonti deboli.

**Nocciolo utile.** Un linguaggio comune per spiegare perché la sicurezza conta in aula: in un contesto sicuro e insieme sfidante il sistema riceve dati coerenti con l'assenza di minaccia. La traduzione operativa è INT-07.

**Raccomandazione dell'analista.** Opzione 3: cornice teorica dichiarata come ipotesi, con le fonti primarie al posto di blog e social, la premessa anatomica corretta, la frase "tutte le terapie" ridimensionata, l'EMDR descritto come psicoterapia, e nessuna promessa terapeutica. È utile soprattutto nella formazione insegnanti e nel corso universitario.

**Precauzioni obbligatorie se l'autore decide di includerlo.** Dichiarazione esplicita "questo corso non è una terapia"; consenso al contatto e libertà di scelta del partner; canali di invio a professionisti; correggere T:L88; completare o sostituire il riferimento non identificato sulla C-PTSD (VNF H2).

**Decisione dell'autore**

Stato: IN ATTESA

Note dell'autore:

---

### D-32 Presentazione storica (UNESCO 1978, esperimento delle 1000 parole, Baba Vanga, risultati dichiarati da Lozanov)

**Cosa dicono le fonti.**
- TLT, file R (`Ricerca_Globale_Suggestopedia_Lozanov.md`): istituto di Sofia del 1966; studio della veggente Baba Vanga con "oltre 7.000 consultanti" e "70% di accuratezza" (R:L12); 1000 vocaboli in una giornata con ritenzione tra 92,9% e 98,08% (R:L56); UNESCO 1978 come "approvazione formale" e "validazione istituzionale senza precedenti", con la Suggestopedia "nettamente superiore" (R:L7, L57-62); 4% del potenziale (R:L6); critiche di Scovel, Wagner e Tilney, Lukesch (R:L102-105); bibliografia che attribuisce "Superlearning" a Timothy Leary (R:L125).
- DSS L816-829: esperimento sul prestigio della fonte (versi attribuiti al poeta Javorov) raccontato in prima persona, come se la voce fosse il gruppo di Lozanov.
- SL1-A r. 68-69 e TM D:L5-7: scoperte "neuro-acustiche" del blocco sovietico "validate" in cliniche bulgare con Aleko Novakov.
- Aneddoti di successo del Superlearning: SL1-A r. 14-16, 80-83, 130-146, 202-211.

**Evidenza attuale.**
- A per i fatti storici: Lozanov, il centro statale di Suggestologia dall'ottobre 1966, la riunione di Sofia di dicembre 1978, le raccomandazioni del gruppo di esperti, le critiche (Scovel 1979, Lukesch 2000).
- B per il giudizio UNESCO: il verbale esiste e dice "a generally superior teaching method [...] compared with traditional methods". Gli esperti erano invitati a titolo personale, dichiaravano incomplete le informazioni, e le raccomandazioni non furono attuate. Non è una validazione ufficiale dell'UNESCO.
- C per l'esperimento delle 1000 parole e per i risultati dichiarati: dati dell'autore, mai replicati. Il canone stesso segnala incongruenze: 14 allievi; parole scelte dagli allievi stessi; media reale dei valori elencati 97,9%; "± 7,39" non è una deviazione standard; il 92,9% e il "lungo termine" non sono nel libro. Le valutazioni esterne degli anni '80-'90 non trovano effetti di quell'ordine, ma non bastano a dimostrare che il ciclo completo sia inefficace.
- C per Baba Vanga: nessun rapporto con metodo verificabile; non compare in Lozanov 2005.
- Errore bibliografico: "Superlearning" (1979) è di Sheila Ostrander e Lynn Schroeder con Nancy Ostrander, non di Leary.
Cluster VPS P1-P13, R1-R8, K1-K8; modello sez. 8.
- Felix 1991, *Unterrichtswissenschaft* 19:23-47.
- Dipamo e Job 1991, *Aust J Educ Technol* 7:127-143.
- Scovel 1979, *TESOL Quarterly* 13:255-266.

**Compatibilità Lozanov.** Coerente come resoconto: Lozanov riporta l'esperimento del 1964 (Lozanov 2005, r. 1261-1322) e il verbale UNESCO (r. 5651-5745). Ma la sua sintesi ("the best methodology and should be immediately implemented all over the world", r. 5793-5795) è più forte del verbale che lui stesso riporta (r. 5678-5687; "incomplete", r. 5686; esperti "invited in their private capacity", r. 5672). Lozanov stesso chiama il 1964 "merely a memorisation experiment" (r. 447-448). Placebo, Hawthorne e Pygmalion come spiegazione sono per lui "far from the truth" (r. 2188-2189).

**Rischi.** Nessun rischio fisico rilevante. Rischio reputazionale alto davanti a un pubblico critico; promesse che generano delusione o pubblicità ingannevole; Baba Vanga e la parapsicologia accanto ai dati didattici abbassano la credibilità.

**Nocciolo utile.** La storia vera è interessante di per sé ed è più solida della sua versione gonfiata. Testi pronti: VPS R-R1, R-R5, R-R7, R-K3, R-K5, R-P12.

**Raccomandazione dell'analista.** Opzione 3. Raccontare la storia con i testi riformulati: UNESCO come raccomandazione di un gruppo di esperti; le 1000 parole come esperimento riferito dall'autore; i risultati come dati non verificati; le critiche citate correttamente (Wagner e Tilney hanno testato il Superlearning, non il ciclo canonico). Baba Vanga, se l'autore vuole tenerla, come notizia storica non verificata, senza la cifra del 70%.

**Precauzioni obbligatorie se l'autore decide di includerlo.** Nessuna cifra di accelerazione promessa per tango, Qigong o corso universitario; nessuna narrazione in prima persona al posto di Lozanov.

**Decisione dell'autore**

Stato: IN ATTESA

Note dell'autore:

---

### D-33 Lezione modello di 2 ore in 5 fasi delle fonti (manuale / Tango-Mind) contro ciclo canonico di Lozanov

**Cosa dicono le fonti.** MAN PR1 (r. 113-118), ripresa in SL1-C P1 (r. 2424-2458), proposta "come modulo didattico universitario o seminario pratico":

| Tempo | Fase | Tecniche | Dispositivo | Musica |
|---|---|---|---|---|
| 0-15' | 1. Preparazione e centratura | respirazione geometrica e rilassamento progressivo | Kasina o DAVID Delight (alfa 10 Hz) | Aria BWV 1068 |
| 15-45' | 2. Integrazione vestibolare e movimento | Infinity Walk o tango | Graham Potentializer o generatore ELF | tango, "136,10 Hz" |
| 45-75' | 3. Assimilazione attiva | lettura a tre toni e cicli | Forbrain o Sonic Brain Activator | Mozart K. 448 o Sinfonia 35 |
| 75-105' | 4. Assimilazione passiva | concerto passivo con visualizzazione cromatica | Brain Tuner ai lobi | Vivaldi e Pachelbel a 60 BPM |
| 105-120' | 5. "Riprogrammazione subliminale" e chiusura | autoconvalida o riscrittura del VCR | Mindscope | Hoffman o Halpern |

Lezione "Tango-Mind" in 4 fasi (TM P1, T:L248-265; SL1-B PR1, r. 762-776): 15' battiti binaurali o AVE; 30' tango e propriocezione; 45' concerto attivo in movimento con cicli di 4 + 4 secondi e tre toni; 30' concerto passivo sdraiati a occhi chiusi su barocco a 60 BPM. Nessuna fase di verifica né di attivazione finale.

**Evidenza attuale.** C: è una proposta progettuale, non un risultato. Quasi tutte le componenti hanno le valutazioni delle schede D-02, D-03, D-04, D-05, D-06, D-07, D-08, D-10, D-11, D-14, D-17, D-18, D-19, D-23, D-24. Cluster VPS Q3.
- Nessuno studio sul formato; per un pilota vedi INT-10.

**Compatibilità Lozanov.** Rifiutato nelle componenti (vedi le schede citate). La struttura si allontana dal ciclo canonico in quattro fasi: introduzione, concerti (attivo e passivo, che "must never be separated"), elaborazione, performance degli allievi (Lozanov 2005, r. 3932-3935, 4021-4099). L'elaborazione avviene nei giorni successivi al concerto (r. 4248-4369); il corso base è di 24 giorni con 4 ore accademiche al giorno (r. 4541-4544). Una singola lezione di 2 ore non può contenere il ciclo: va pensata come parte di un ciclo su più incontri.

**Rischi.** Alto nella forma delle fonti: le due lezioni ereditano i rischi delle pratiche incluse, cioè crisi fotosensibili (AVE), cadute e nausea (Potentializer prima dei giri), apnee, lavoro su ricordi traumatici in gruppo a fine lezione, dispositivi elettromedicali.

**Nocciolo utile.** L'alternanza di movimento, ascolto e riposo in una lezione di 2 ore; l'idea di un modulo pilota con misure prima e dopo (TM T13).

**Raccomandazione dell'analista.** Opzione 3: ricostruire la lezione, o meglio una sequenza di lezioni, sul ciclo canonico, con le integrazioni del blocco H dichiarate come tali, e proporla come pilota con valutazione (INT-10). Le lezioni delle fonti, così come sono, restano documentate in `ricerca/`.

**Precauzioni obbligatorie se l'autore decide di includerlo.** Nessuna componente delle schede con rischio alto; tempi di transizione e attivazione finale; valutazione dichiarata agli allievi.

**Decisione dell'autore**

Stato: IN ATTESA

Note dell'autore:

---

## Blocco H. Integrazioni dalla scienza attuale (proposte INT, da approvare)

Queste schede non riportano elementi delle fonti: sono proposte dell'analista, ricavate dalla ricerca attuale e in parte dai noccioli utili delle schede precedenti. Ogni scheda indica che cosa è, l'evidenza, la compatibilità con il canone (con le tensioni, dove ci sono), l'applicazione concreta nel tango e nel Qigong, i rischi e una raccomandazione.

Opzioni: **Approvata / Approvata con modifiche / Respinta / Da discutere**.

### INT-01 Pratica distribuita (spacing) e richiamo attivo (retrieval practice)

**Che cos'è.** Distribuire la ripresa del materiale nel tempo, a intervalli crescenti, invece di concentrarla in una volta. Provare a ricordare o a eseguire senza modello, invece di rivedere o rifare guardando.

**Evidenza.** A. Il distanziamento migliora il ricordo a lungo termine, e l'intervallo ottimale cresce con il tempo per cui si vuole ricordare; il richiamo consolida più della rilettura; vale anche per il lessico straniero. Nel motorio il principio è affine (pratica distribuita), con prove meno uniformi.
- Cepeda et al. 2006, *Psychol Bull* 132:354-380.
- Roediger e Karpicke 2006, *Psychol Sci* 17:249-255 (da ricontrollare).
- Adesope, Trevisan, Sundararajan 2017, *Rev Educ Res* 87:659-701.

**Compatibilità con il canone.** In parte coerente: il ciclo canonico distribuisce già il materiale, con l'elaborazione primaria e secondaria nei giorni successivi e le canzoni che ritornano (Lozanov 2005, r. 4248-4369); Lozanov descrive una "legge del ricordo spontaneo ritardato" (r. 3209-3213); la performance degli allievi è richiamo (r. 4463-4468); i test sono "facili e stimolanti" (r. 4453-4459).
Tensione reale: il richiamo come interrogazione va contro "not asked individual questions" (r. 3971, 4007-4008), contro il divieto di chiedere di memorizzare (r. 746-749) e contro l'assenza di compiti obbligatori (r. 4479-4481). La forma compatibile è il richiamo in gioco collettivo, senza esposizione individuale forzata.

**Applicazione nel tango.** Riprendere le figure di una lezione dopo 2-3 giorni, poi dopo una settimana, poi dopo un mese. All'inizio della lezione, in coppia e in musica: "ricostruite la sequenza della volta scorsa", prima che il docente la mostri. Giochi di musicalità in cui la coppia sceglie da sé quali figure richiamare.

**Applicazione nel Qigong.** Eseguire un tratto della forma in gruppo senza guardare il docente, poi il docente la mostra; riprendere le forme delle settimane precedenti a intervalli crescenti.

**Nel corso universitario e nella formazione insegnanti.** Brevi autotest facoltativi e non valutati, a distanza di giorni; il giorno della performance come richiamo.

**Rischi.** Basso: ansia da verifica se il richiamo diventa interrogazione.

**Raccomandazione dell'analista.** Approvata con modifiche: richiamo sempre in forma di gioco o di lavoro di gruppo, mai come domanda individuale obbligata; distanziamento esplicito nel calendario del corso.

**Decisione dell'autore**

Stato: IN ATTESA

Note dell'autore:

---

### INT-02 Focus attentivo esterno (Wulf)

**Che cos'è.** Indicazioni che orientano l'attenzione sull'effetto del movimento (il pavimento, il partner, lo spazio) invece che sulle parti del corpo.

**Evidenza.** A-B. Le meta-analisi trovano un vantaggio del focus esterno su prestazione e apprendimento motorio; gli effetti variano con il compito e il livello.
- Chua et al. 2021, *Psychol Bull* 147:618-645 (da ricontrollare).
- Wulf e Lewthwaite 2016, *Psychon Bull Rev* 23:1382-1414.
- Wulf 2013, *Int Rev Sport Exerc Psychol* 6:77-104 [fuori dai file di verifica, da ricontrollare].

**Compatibilità con il canone.** Non trattato. Coerente con il principio dei dettagli "on a second plane": il docente richiama un dettaglio "only for a short time and then goes back quickly to the sense" (Lozanov 2005, r. 3129-3138). Tensione con le fonti: la procedura Alexander (D-28) e molte indicazioni tradizionali di tango e Qigong sono a focus interno.

**Applicazione nel tango.** "Spingi il pavimento", "porta il partner verso la finestra", "disegna un cerchio a terra con il piede", invece di "piega il ginocchio", "ruota l'anca".

**Applicazione nel Qigong.** "Spingi l'aria come se fosse acqua", "allunga verso il punto lontano", "la sfera tra le mani si allarga". Avvertenza: nel Qigong l'attenzione al corpo e al respiro è in parte contenuto della disciplina. Il focus esterno serve alla forma e alla coordinazione; non sostituisce il lavoro interiore che la tradizione prevede. Il confine lo fissa l'autore.

**Rischi.** Nessuno rilevante.

**Raccomandazione dell'analista.** Approvata, con la nota sul Qigong.

**Decisione dell'autore**

Stato: IN ATTESA

Note dell'autore:

---

### INT-03 Pratica variata / interferenza contestuale

**Che cos'è.** Variare le condizioni e l'ordine della pratica (musica, partner, spazio, combinazioni) e alternare elementi simili invece di ripeterli a blocchi.

**Evidenza.** B. La pratica variata peggiora un po' la prestazione immediata ma migliora ritenzione e trasferimento; l'alternanza aiuta a distinguere elementi simili, con effetti che dipendono dal materiale e dal livello. Con i principianti assoluti un primo blocco ripetuto può servire.
- Shea e Morgan 1979, *J Exp Psychol Hum Learn Mem* 5:179-187 (da ricontrollare).
- Magill e Hall 1990, *Hum Mov Sci* 9:241-289 [fuori dai file di verifica, da ricontrollare].
- Schmidt e Lee, *Motor Control and Learning*, Human Kinetics, varie edizioni [fuori dai file di verifica, da ricontrollare l'edizione].
- Per l'alternanza: Brunmair e Richter 2019, *Psychol Bull* 145:1029-1052 (da ricontrollare).

**Compatibilità con il canone.** Coerente. Lozanov rifiuta la "gerarchia delle abitudini", cioè costruire abitudini elementari da smontare a ogni livello (Lozanov 2005, r. 3124-3127, 3860-3872), e chiede un'elaborazione "very dynamic and very often changing the tasks" (r. 4315-4369).

**Applicazione nel tango.** Cambiare orchestra e tempo (Di Sarli, D'Arienzo, vals, milonga), partner, ruolo, direzione nella ronda; alternare ocho avanti e ocho indietro invece di dieci ripetizioni dell'uno e poi dieci dell'altro; evitare la "base a 8 tempi" come stereotipo rigido (modello r. 741).

**Applicazione nel Qigong.** La stessa forma in direzioni diverse, a velocità diverse, da fermi e in cammino, in spazi diversi.

**Rischi.** Nessuno rilevante; con i principianti dosare la variazione per non scoraggiare.

**Raccomandazione dell'analista.** Approvata.

**Decisione dell'autore**

Stato: IN ATTESA

Note dell'autore:

---

### INT-04 Motor imagery autogestita (collegata a D-12)

**Che cos'è.** L'allievo ripassa mentalmente un movimento quando e come vuole, in aggiunta alla pratica fisica.

**Evidenza.** B. Utile rispetto a nessuna pratica, meno della pratica fisica, meglio in combinazione.
- Driskell, Copper, Moran 1994, *J Appl Psychol* 79:481-492.
- Toth et al. 2020, *Psychol Sport Exerc* 48:101672.

**Compatibilità con il canone.** Non trattata come pratica autogestita. Diventa rifiutata se si trasforma in guided imagery dettata dal docente (Lozanov 2005, r. 1440-1441, 1815-1820) o in meditazione guidata con voce monotona (r. 1833-1836). Il confine: il docente può proporre ("chi vuole può ripassare mentalmente la sequenza"), non dettare il contenuto delle immagini né le sensazioni.

**Applicazione nel tango.** Un minuto tra due tande per ripassare la sequenza, a occhi aperti o chiusi a scelta; a casa, mentre si ascolta la musica della lezione; nei periodi di infortunio come complemento alla riabilitazione.

**Applicazione nel Qigong.** Ripasso mentale della forma nei giorni senza pratica e prima di eseguirla da soli.

**Rischi.** Basso: usarla al posto della pratica (decondizionamento).

**Raccomandazione dell'analista.** Approvata con modifiche: mai dettata, mai sostitutiva, sempre facoltativa.

**Decisione dell'autore**

Stato: IN ATTESA

Note dell'autore:

---

### INT-05 Routine pre-esecuzione

**Che cos'è.** Una breve sequenza costante, scelta dall'allievo, prima di un gesto impegnativo: un respiro, sentire l'appoggio, uno sguardo, una parola chiave.

**Evidenza.** B. Migliora la prestazione sportiva: effetto piccolo nei confronti prima-dopo, da moderato a grande negli esperimenti; agisce su attenzione e automatismo.
- Rupprecht, Tran, Gröpel 2021, *Int Rev Sport Exerc Psychol* (meta-analisi).
- Cotterill 2010, *Int Rev Sport Exerc Psychol* 3:132-153.

**Compatibilità con il canone.** Non trattata. Va tenuta distinta dall'ancoraggio di tipo PNL (Lozanov 2005, r. 1400-1406) e dal "conditioning" che Lozanov elenca tra le tecniche d'induzione (r. 1824-1849): la routine non richiama ricordi né stati indotti, la sceglie l'allievo e serve a concentrarsi.

**Applicazione nel tango.** Prima della tanda: abbraccio, un respiro insieme, sentire il peso sui piedi, ascoltare le prime battute prima del primo passo, che è già un'abitudine diffusa in milonga. Prima di un giro: sguardo, asse, appoggio.

**Applicazione nel Qigong.** La postura d'apertura e il raccoglimento iniziale delle forme svolgono già questa funzione: si tratta di renderla esplicita e personale.

**Rischi.** Nessuno rilevante; evitare che diventi un rituale da cui si dipende.

**Raccomandazione dell'analista.** Approvata con modifiche: chiamarla "routine", non "ancora"; scelta dall'allievo; nessun richiamo di ricordi personali. Raccoglie il nocciolo di D-15.

**Decisione dell'autore**

Stato: IN ATTESA

Note dell'autore:

---

### INT-06 Esercizi vestibolo-oculari (VOR) per i giri

**Che cos'è.** Esercizi di stabilizzazione dello sguardo (ruotare e inclinare lentamente la testa mantenendo lo sguardo su un bersaglio fermo) e pratica graduale dei giri con lo "spotting". Le fonti contengono già l'esercizio come "Danza dei canali semicircolari" (MAN T6.2, r. 198; SL1-C T12, r. 1789-1798; DSS T6, L591-602), ma con la promessa di una "calibrazione perfetta" del vestibolo.

**Evidenza.** A nella riabilitazione vestibolare (pazienti con ipofunzione); B nei danzatori sani, dove l'adattamento ai giri è documentato, con correlati nel cervelletto e nella corteccia.
- Hall et al. 2022, *J Neurol Phys Ther* 46:118-177 (linea guida).
- Nigmatullina et al. 2015, *Cereb Cortex* 25:554-562.

**Compatibilità con il canone.** Non trattato.

**Applicazione nel tango.** Riscaldamento prima dei giri: 10 rotazioni lente della testa a destra e a sinistra con lo sguardo fisso, poi 10 in alto e in basso; giri progressivi con spotting; pivot lenti prima di quelli veloci.

**Applicazione nel Qigong.** Le forme con rotazioni del busto e della testa, e con lo sguardo che segue le mani, lavorano già sulla stabilità dello sguardo; si possono proporre con la stessa gradualità.

**Rischi.** Medio. Persone con vertigine parossistica posizionale, Ménière, neurite vestibolare, problemi cervicali, anziani o a rischio di caduta: vertigine, nausea, cadute, dolore cervicale.

**Raccomandazione dell'analista.** Approvata con modifiche: progressione graduale, movimenti lenti, spazio libero, possibilità di appoggio (parete, partner), interruzione ai primi sintomi; chi ha disturbi vestibolari noti chiede prima al medico; nessuna promessa di "calibrazione".

**Decisione dell'autore**

Stato: IN ATTESA

Note dell'autore:

---

### INT-07 Riduzione della minaccia percepita / sicurezza come condizione (predictive processing; collegata a D-31)

**Che cos'è.** Progettare lezione e sala perché nessuno si senta minacciato: fisicamente (pavimento, spazio, cadute), socialmente (giudizio, esposizione), nel contatto (abbraccio, partner). È la traduzione operativa della cornice di D-31, senza pretese terapeutiche.

**Evidenza.** A per l'effetto dell'ansia e dello stress su prestazione e memoria; B per la minaccia posturale che irrigidisce il corpo; C per la spiegazione in termini di "precisione dei priors" e metastabilità.
- Shields et al. 2017, *Psychol Bull* 143:636-675.
- Teimouri, Goetze, Plonsky 2019, *Stud Second Lang Acquis* 41:363-387 (ansia e rendimento nelle lingue, r ≈ -0,36).
- Adkin e Carpenter 2018, *Front Neurol* 9:789 (minaccia posturale e controllo dell'equilibrio).

**Compatibilità con il canone.** Coerente: è uno dei punti di maggiore accordo tra canone e ricerca. "Freedom accompanied by fear of learning is equal to giving up" (Lozanov 2005, r. 3860-3915); "to suggest = to offer, to propose" (r. 1774-1775); nessuna pressione (r. 3087-3088); le barriere antisuggestive non si forzano (r. 2802-2845); niente domande individuali obbligate (r. 3971, 4007-4008); correzione indiretta (r. 4275-4276, 4358-4360). Vincolo: il docente non fa terapia (r. 2046-2047).

**Applicazione nel tango.** Libertà di scegliere partner, ruolo e distanza dell'abbraccio; consenso al contatto e un modo semplice per dire di no; nessuna correzione in pubblico; nessun cambio di coppia imposto; pavimento e calzature adatti; personaggi di gioco che "prendono" l'errore (D-16). Eccezione: gli errori pericolosi (ginocchia, schiena, cadute, collisioni) si correggono subito e in modo diretto.

**Applicazione nel Qigong.** Occhi aperti sempre possibili; nessuna sensazione dettata; libertà di fermarsi; la ragione di ogni esercizio spiegata; nessuna insistenza su affermazioni "energetiche" che urtano la barriera critico-logica.

**Rischi.** Basso. Il rischio è l'opposto: confondere la sicurezza con l'assenza di sfida. La fonte T parla di contesti "sicuri e sfidanti".

**Raccomandazione dell'analista.** Approvata, come principio di progettazione e non come terapia.

**Decisione dell'autore**

Stato: IN ATTESA

Note dell'autore:

---

### INT-08 Gesto ed effetto di esecuzione (enactment) nella codifica

**Che cos'è.** Eseguire l'azione indicata da una parola o da una frase, o accompagnarla con un gesto, per ricordarla meglio.

**Evidenza.** A per la memoria di azioni (meta-analisi, g ≈ 1,23 negli studi comportamentali); B per il lessico straniero con gesti. Alcuni effetti più astratti di "cognizione incarnata" non si sono replicati.
- Roberts, MacLeod, Fernandes 2022, *Psychol Bull* 148:397-434.
- Macedonia e Knösche 2011, *Mind Brain Educ* 5:196-211.
- Engelkamp 1998, *Memory for Actions*, Psychology Press [fuori dai file di verifica, da ricontrollare].

**Compatibilità con il canone.** Coerente: i dettagli lessicali e grammaticali sono "acted out through games and songs (and even through easy dances)" (Lozanov 2005, r. 4283); gioco-progetto e voci da attori (r. 4265-4313).

**Applicazione nel tango.** Dire il nome della figura (adelante, atrás, ocho, sacada) mentre la si esegue. Nel corso universitario e nella formazione insegnanti, associare un gesto ai concetti chiave del metodo.

**Applicazione nel Qigong.** Dire o pensare il nome della forma, anche nella lingua d'origine, all'inizio del movimento; apprendere le sequenze per immagini d'azione.

**Rischi.** Nessuno rilevante.

**Raccomandazione dell'analista.** Approvata.

**Decisione dell'autore**

Stato: IN ATTESA

Note dell'autore:

---

### INT-09 Canto e coro come strumento (già presente nel canone Lozanov: specifica come)

**Che cos'è.** Cantare insieme a inizio e fine lezione e nei giochi; leggere o recitare in coro.

**Evidenza.** B. Le melodie aiutano il ricordo parola per parola; cantare frasi in lingua straniera le fa ricordare meglio che dirle, anche in ritmo; parlare da soli davanti agli altri è una delle fonti principali d'ansia nelle lingue, e il coro riduce l'esposizione; il canto di gruppo favorisce un legame sociale rapido.
- Ludke, Ferreira, Overy 2014, *Mem Cognit* 42:41-52.
- Wallace 1994, *J Exp Psychol Learn Mem Cogn* 20:1471-1485.
- Pearce, Launay, Dunbar 2015, *R Soc Open Sci* 2:150221 (da ricontrollare).

**Compatibilità con il canone.** Coerente, è già canonico. La lezione finisce con una canzone e la successiva comincia con la stessa; ogni elaborazione si apre e si chiude con una canzone; il corso si apre e si chiude con "one of the best songs in the language of study" (Lozanov 2005, r. 2715-2716, 4321, 4469-4470). Il primo dialogo si legge per lo più in coro (r. 4265-4313). Il docente scalda la voce cantando prima della lezione (r. 3114-3115). Canti e giochi fanno parte del quinto fattore indispensabile (r. 5853).

**Come specificarlo.**
- **Tango.** Un tango cantato, con letra semplice, apre e chiude ogni lezione e l'intero corso. Le letras come materiale linguistico e musicale. Cantare il compás e la sincope prima di camminarli. Una canzone nuova per ciclo, ripresa nei giorni seguenti (distanziamento, INT-01).
- **Qigong.** Un canto breve d'apertura e di chiusura, anche nella lingua della tradizione; i nomi delle forme recitati in coro. Evitare la cantilena lenta e uniforme come mezzo d'induzione (r. 1394-1397).
- **Corso universitario e formazione insegnanti.** Canzone d'apertura e di chiusura del modulo; letture corali di brevi testi.
- **Per tutti.** Nessuno è obbligato a cantare da solo.

**Rischi.** Nessuno rilevante; volume moderato, nessuno sforzo vocale.

**Raccomandazione dell'analista.** Approvata.

**Decisione dell'autore**

Stato: IN ATTESA

Note dell'autore:

---

### INT-10 Valutazione con misure validate (STAI, test pre/post, gruppo di controllo) per il corso universitario

**Che cos'è.** Misurare gli effetti del corso invece di presumerli: test di conoscenze e abilità prima, dopo e a distanza; misure d'ansia validate; un gruppo di confronto.

**Evidenza.** A per gli strumenti. Lo STAI (forma Y) è uno strumento standard con versione italiana, protetto da diritti: serve una licenza d'uso. Senza un confronto, i risultati restano esposti ad aspettative, novità, selezione dei partecipanti e valutazioni non cieche. Le fonti contengono già un disegno a due gruppi (TM T13; SL1-B T23) con l'EEG tra le misure; ma l'EEG misura cambiamenti, non un beneficio didattico, e non è una buona misura di risultato (VTN A9).
- Spielberger 1983, *Manual for the State-Trait Anxiety Inventory (Form Y)* (da ricontrollare).
- McCambridge, Witton, Elbourne 2014, *J Clin Epidemiol* 67:267-277 (effetto Hawthorne).
- Felix 1991 (per le valutazioni storiche della Suggestopedia).

**Compatibilità con il canone.** Coerente con i test "facili e stimolanti" (Lozanov 2005, r. 4453-4459) e con un criterio canonico che si può misurare: "If pupils get tired in lessons, we cannot speak of Suggestopaedia" (r. 561-562). Il canone non prevede gruppi di controllo e presenta dati dell'autore non verificati (modello sez. 8.4); Lozanov respinge placebo e Hawthorne come spiegazione (r. 2188-2189), e un confronto controllato è il modo per discuterne. Tensione da gestire: la valutazione non deve diventare un esame che crea ansia.

**Applicazione nel corso universitario.** Test di conoscenze prima, alla fine e dopo 4-8 settimane; STAI-Y di stato (con licenza) o una scala breve d'ansia; questionario anonimo su fatica e gradimento; confronto con un'altra edizione o un altro gruppo; consenso informato e, se i dati si pubblicano, parere di un comitato etico e trattamento dei dati conforme al GDPR.

**Applicazione nel tango e nel Qigong.** Video delle stesse sequenze all'inizio e alla fine, valutati da docenti che non sanno quale video è quale; brevi scale di ansia e fatica; ritenzione dopo qualche settimana.

**Rischi.** Basso: ansia da valutazione; protezione dei dati.

**Raccomandazione dell'analista.** Approvata, con misure anonime e a basso peso per gli allievi.

**Decisione dell'autore**

Stato: IN ATTESA

Note dell'autore:

---

### INT-11 Pause brevi nella pratica motoria (micro-offline gains, consolidamento)

**Che cos'è.** Alternare brevi blocchi di pratica e pause di pochi secondi, e chiudere con una pausa tranquilla invece che con un'attività che interferisce.

**Evidenza.** B. Nell'apprendimento di sequenze motorie, brevi pause (circa 10 secondi) tra i blocchi producono rapidi guadagni "offline", con riattivazione neurale durante la pausa; una breve pausa tranquilla dopo lo studio migliora il ricordo rispetto a un compito che interferisce; il sonno consolida. È il nocciolo sensato dei cicli di 4 + 4 secondi (D-23).
- Bönstrup et al. 2019, *Curr Biol* 29:1346-1351.
- Buch et al. 2021, *Cell Rep* 35:109193.
- Dewar et al. 2012, *Psychol Sci* 23:955-960.

**Compatibilità con il canone.** Non trattato. Compatibile se le pause seguono la musica e il lavoro e non diventano un ritmo fisso e monotono, che il canone considera induzione (Lozanov 2005, r. 1830-1832). La giornata canonica senza concerto alterna i ritmi e prevede una pausa (r. 4422-4435).

**Applicazione nel tango.** Ripetere una figura due o tre volte, fermarsi qualche secondo nell'abbraccio, riprendere; alla fine della lezione qualche minuto di ascolto senza nuove consegne.

**Applicazione nel Qigong.** Breve quiete in piedi tra le ripetizioni di una forma; la chiusura tradizionale delle forme ha già questa funzione.

**Rischi.** Nessuno rilevante.

**Raccomandazione dell'analista.** Approvata.

**Decisione dell'autore**

Stato: IN ATTESA

Note dell'autore:

---

## 6. Elementi delle fonti senza scheda propria

Per rispettare la regola fondamentale, questa tabella elenca gli elementi delle fonti che non hanno una scheda dedicata e indica la scheda più vicina. Restano tutti documentati in `ricerca/`. Se l'autore vuole decidere uno di questi elementi a parte, si può aprire una nuova scheda.

| Elemento | Dove compare | Scheda o nota |
|---|---|---|
| Centratura sul Tanden ("metodo della Terra", formula "Sono radicato, stabile e sicuro") | MAN T6.1 (r. 198); SL1-C T11 (r. 1782-1788); DSS T5 (L583-590) | Il tanden è un riferimento delle arti marziali, vicino solo in modo approssimativo al centro di massa (VPS B6). Utile come immagine didattica per l'asse; la formula rientra in D-14; il punto riguarda il Qigong (Domande aperte) |
| Esercizio Sì/No di Lisa Curtis | SL1-A T06 (r. 50-52) | D-05 (apnea e Valsalva) |
| Sofrologia (Caycedo, Abrezol), Eli Bay, "Seven-Minute Stress Busters" | SL1-A cap. 1 | D-08; Caycedo era colombiano, non spagnolo (VPS P7) |
| Esercizi con la palla di Dalcroze | TM D13 (D:L255-258, file troncato) | Affine a INT-03 e INT-08; non verificato |
| Allestimento periferico: luci soffuse, sedute da salotto, poster non spiegati | TLT R-T3 (R:L42); DSS T34, T43 | Canone delle percezioni periferiche (Lozanov 2005, r. 2232-2264, 3104-3110); pareti sovraccariche distraggono (VNF F3); luci soffuse e rischio d'inciampo (TLT, rischio S9) |
| Correzione indiretta, test facili, regola del 70-75%, Performance Day, ripasso "come sfogliando un giornale" | DSS T38, T42, T44-T47 | Canone; VPS C3-C5 (da tenere); eccezioni di sicurezza in INT-07 |
| Tre blocchi logico, emotivo, etico "da scardinare" | SL1-B T20 (r. 1026-1079) | D-30 e INT-07; nel canone le barriere non si forzano (VPS T2) |
| Körperlernen (Schiffler) e metodo di attivazione (Kitaigorodskaya) | TLT R-T16, R-T17 | D-32; ponti storici verso INT-08 |
| Declamare concetti durante il ballo | TM T5 (T:L216-218) | D-25, D-27 |
| Teoria della transizione 3D-2D, movimento come "nutriente", tesi di Levinson | SL1-B r. 725-740, 967-995; DSS L14-49 | D-26, D-30 |
| Sound Therapy di Patricia Joudry; suono a 5.000 Hz di Dan Carlson | SL1-A r. 73-74, 355-357; TM D12 | D-19 (VTN E1, H6) |
| Clarence Cone e le onde che "rigenerano" | SL1-A r. 481-485 | D-03 (VTN C6) |
| Inner-Weather Wizard | MAN r. 84 | D-06; fonte non trovata (VPS I9) |
| Anestesia suggestiva del 1965 | TLT R-T18; Lozanov 2005, r. 1203-1213 | D-32 (VTN M1) |
| Raja Yoga di Lozanov e lo yogi "Sha" | TLT R-T19 (R:L18-21) | D-32 (VPS P4; VNF I5) |
| Aneddoti (Caruso, monaci benedettini, Georgiana Stehli, 170 dipendenti di Toronto, Brian Hamilton, Leo Wood, Charles Croucher, Rosa di Sabadell) | SL1-A r. 14-23, 80-94, 130-146, 202-211 | D-32 (VNF I1-I4; VPS N1, N3) |
| Musica per materia con segnali Hemi-Sync (Edrington) | SL1-B T21 (r. 925-931) | D-11 |
| Specchio e affermazioni dette camminando o ballando | SL1-C sez. 2.5 (r. 2576-2582) | D-14 |
| Unità metodiche ampliate, iceberg linguistico, sezione aurea dei tempi | DSS T30, T31, T35; DSS B8 | Canone; VPS T8, T11 (sezione aurea come criterio estetico); Domande aperte |
| Persone e organizzazioni citate (Eli Bay, Lisa Curtis, Vera Fryling, Stephan Cooter, Superlearning Inc., Charles Schmid) | SL1-A r. 4-11, 129-133 | D-32; indice dei nomi con "non verificato" dove serve (VPS X1) |

---

## 7. Domande aperte per l'autore

Il libro di Lozanov del 2005 è un riassunto di lezioni: le istruzioni operative complete stanno nel *Trainer's Manual* (1988) e nella *Guide for Work* (1992), riservate ai docenti formati (modello r. 21-24), e Lozanov scrive che molte cose "cannot be described on paper". Su questi punti l'esperienza dell'autore certificato è la fonte migliore.

1. **Etichetta e certificazione.** Il percorso si chiamerà Desuggestopedia, "ispirato a Lozanov" o in altro modo? Lozanov chiede una formazione certificata (Lozanov 2005, r. 77-83, 3771-3776, 4449-4450) e introdusse la certificazione contro chi diceva di possedere il "segreto" (r. 1469-1472). Lozanov è morto nel 2012: chi oggi abbia titolo a certificare va verificato (modello r. 576). Dalla risposta dipendono D-05, D-08, D-09, D-11, D-21, D-27 e D-33 (sezione 4).

2. **Numero di allievi.** Il libro non dà un numero standard (modello r. 216, 326, 497). Gli esperimenti citati hanno 14 allievi (r. 1266), 75 in sei gruppi (r. 1341), 12 a Kharkov (r. 5272); il "massimo 12" viene dalla letteratura secondaria (TLT R:L110; VPS K6). Nel tango contano anche il numero pari e l'equilibrio dei ruoli; nel corso universitario i numeri sono di solito più alti. Qual è il numero praticabile in ciascun contesto, e che cosa cambia sopra quella soglia?

3. **Calendario giorno per giorno.** Il corso base è di 24 giorni con 4 ore accademiche al giorno (r. 4541-4544) e il primo livello ha 10 sessioni di concerto (cap. 31), ma il libro non dà il calendario giorno per giorno né dice come si incastrano introduzione, concerti ed elaborazioni (modello r. 339, 499). In media c'è un concerto ogni due giorni e mezzo. Come si traduce in un corso di tango settimanale, in un ciclo di Qigong, in un corso universitario semestrale, in una formazione intensiva per insegnanti? Concerto ed elaborazione primaria devono stare a un giorno di distanza anche quando le lezioni sono settimanali?

4. **Corsi adattivi.** Lozanov li chiama "one of the cornerstones in our methodology", introdotti contro la "dissociazione negativa" tra il rendimento in corso e quello fuori (r. 2460-2469), e li mette tra le competenze del docente, ma non dice in che cosa consistano. Che cosa ha ricevuto l'autore nella formazione su questo punto? Nel tango il problema è concreto: chi balla bene a lezione e si blocca in milonga.

5. **Quarta fase.** La performance degli allievi è nominata come fase a sé, "because it assumes an increasing importance for the independence and self-confidence of the students" (r. 3932-3935, 3958-3965), ma è descritta solo come giorno finale (r. 4463-4468). Esiste una quarta fase dentro ogni ciclo, non solo alla fine del corso? Che forma ha nel tango (milonga, piccola esibizione), nel Qigong (pratica condivisa), all'università e nella formazione insegnanti?

6. **Secondo livello.** Il contenuto del corso di secondo livello non è descritto (r. 4440-4441).

7. **Il concerto nelle discipline corporee.** Qual è il "testo" del concerto in un corso di tango o di Qigong: terminologia, storia della sequenza, letras, teoria? Gli allievi stanno seduti, in piedi, segnano i passi? Musica del programma canonico o musica della disciplina? (D-21, D-27; modello r. 761-762).

8. **Qigong: respiro, rilassamento, intenzione, immagine.** Sono contenuto della disciplina e insieme le procedure che Lozanov considera induzione quando servono a "passare" altro materiale (modello r. 783-806). Dove l'autore mette il confine, per esempio per la quiete in piedi a occhi chiusi, le immagini tradizionali ("la sfera tra le mani"), i conteggi del respiro, la lingua al palato? Quali segnali d'allarme della lista canonica (occhi chiusi a lungo, voce lenta e uniforme, musica monotona, istruzioni su che cosa l'allievo "sta sentendo", conteggio costante; r. 1845-1849) l'autore considera inevitabili nel Qigong e come li gestisce?

9. **Volume di materiale nel movimento.** Il primo fattore indispensabile è "covering a huge bulk of learning material" (r. 5845); per il movimento non ci sono dati e il volume motorio ha limiti fisici (modello r. 763). Che cosa è un "volume enorme" in una lezione di tango o di Qigong: vedere e vivere una tanda intera, una forma completa, un repertorio ampio in forma passiva?

10. **Correzione indiretta e sicurezza.** Il canone vuole correzioni impercettibili, "as if by chance" (r. 4275-4276, 4358-4360). Nel lavoro corporeo alcuni errori (ginocchia, schiena, cadute, collisioni) chiedono una correzione diretta e immediata (TLT, rischio S10). Quali eccezioni ammette l'autore?

11. **Valutazione e domande individuali.** Nessuna domanda individuale obbligata (r. 3971, 4007-4008), test facili, parte del livello d'uscita proposta "cautiously" (r. 4453-4459). Il corso universitario richiede però un esame e un voto. Come conciliare le due cose (INT-01, INT-10)?

12. **Compiti e pratica a casa.** Niente compiti obbligatori, solo una lettura informativa "the way one skims through a newspaper" (r. 4479-4481). Nella pratica motoria la ripetizione a casa è comunemente ritenuta utile (modello r. 764). Che cosa propone l'autore, e in che forma?

13. **Contatto, ruoli, cambi di coppia.** Il canone non parla di contatto fisico; la regola trasferibile è quella delle barriere antisuggestive (r. 2802-2845). Quali regole fissare per l'abbraccio, il cambio di coppia e lo scambio dei ruoli, che il modello legge come varianti della "personalità multipla" (r. 2409-2432)?

14. **Sezione aurea e tempi.** La regola dei tre tempi (veloce, moderato, lento) con durate vicine alla sezione aurea (r. 885-908, 4422-4435) va adattata a lezioni di 60, 90 o 120 minuti e alla fatica fisica. Quali proporzioni usa l'autore nella pratica?

15. **Gioco-progetto e introduzione.** Il film come gioco-progetto (r. 3943-3949) funziona bene nel tango (una milonga d'epoca, un film porteño). Nel Qigong rischia il folklore (modello r. 765); nel corso universitario e nella formazione insegnanti la cornice è diversa. Quale gioco-progetto per ciascun contesto?

16. **Lingua madre e traduzione.** Nei corsi di lingua la traduzione si dà all'inizio e si ritira presto (r. 4482-4495, 4460-4462). Esiste un analogo nei corsi corporei (spiegazioni analitiche, schede illustrate) e quando si ritira?

17. **Formazione degli insegnanti.** Lozanov scrive che l'intonazione e le 14 competenze del docente si imparano solo "in a practical course" (r. 4447-4452, 5753-5773). Che cosa può stare in un manuale scritto e che cosa resta riservato alla formazione pratica condotta dall'autore?

18. **Aula, luci, volume.** Disposizione dell'aula e sedute non sono stabilite (modello r. 498). Le luci soffuse aumentano il rischio d'inciampo in una sala di ballo; il concerto passivo è "as loud as a normal concert" (r. 4100-4115), che in un'aula può essere fastidioso per chi ha acufeni o ipersensibilità (VPS 7.7). Quali standard di sala adotta l'autore?

19. **Procedura di invio.** Se in aula emergono contenuti traumatici, crisi d'ansia o sintomi fisici (vertigini, cadute), qual è la procedura e a chi si indirizza la persona? Il canone dice solo che il docente non fa terapia (r. 2046-2047, 3334-3336).
