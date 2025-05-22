# DEPRECATO
# ANDARE SU report_gen_data per nuovo generatore
# ------------------------------------------
# PDF Generator - Attestati FAD

I dati utilizzati per generare i file sono contenuti all'interno della tabella master
Per generare tutti i PDF eseguire lo script 1-course-compiler.py
Per generare i PDF di un singolo utente si può utilizzare lo script 2-course by codice_fiscale.py
Se si utilizza lo script singolo (2), la console chiederà in input il codice fiscale della persona di cui si vogliono estrarre i dati. Il metodo di salvataggio dei documenti è lo stesso dello script (1).

N.B. Per eseguire lo script 1-course_compiler.py bisogna aprire la directory "generazione pdf" su VSCode. Aprendo solo lo script, non viene generato l'ambiente virtuale in cui sono presenti le librerie e quindi lo script incappa in degli errori. Invece, aprendo tramite VSCode la directory, sarà possibile installare le varie librerie necessarie (tipo FPDF), se richiesto, e mantenerle per l'esecuzione del programma.

***
# Informazioni sulla base dati

## Tabella Master - Campi
  - moodle_institution
  - cognome
  - nome
  - codice_fiscale
  - data_di_nascita
  - comune_di_nascita
  - titolo_azione_con_id
  - titolo_sessione_formativa
  - Totale ore corso
  - durata_min
  - stato_corso
  - valutazione_quiz
  - partita_iva
  - codice_ateco
  - ente_formatore
  - ente_certificatore

Per matchare i dati tra la tabella Master ed il DB di Euromedia possiamo sfruttare i match di moodle_institution e codice_fiscale, dati ugualmente presenti in entrambe le basi dati.

## Estrapolazione dei dati e composizione del front-end
Per l'estrazione dei dati proporrei una maschera con, all'interno, la possibilità di selezionare i dati come nel seguente Tree:

Ricerca per:

moodle_institution

├── codice_fiscale {Cognome} {Nome}

└── titolo_sessione_formativa

Per quanto concerne la maschera, procederei ad una configurazione come la seguente:
![maschera_dati_euromedia](https://github.com/user-attachments/assets/b0f57848-19a9-4609-92fe-a4ea5f98161a)

Inoltre, in ogni riga, aggiungerei un tasto PDF export per effettuare il download dell'attestato dalla risorsa FTP in cui verrano salvati

# Note sul funzionamento del generatore

## Salvataggio degli attestati

Una volta partito lo script di generazione degli attestati, i file verranno salvati come segue:

- __Nome del file__: i file saranno sempre composti dal codice fiscale e dalla sigla del corso di cui stiamo emettendo l'attestato. Aggiungiamo alla fine del nome il suffisso "inc" se il corso non è stato completato.

```python
if corso['stato_corso'] == 'incompleto':
    saved_file_name = f"{codice_fiscale}_{sigla_corso}_inc.pdf"
else:
    saved_file_name = f"{codice_fiscale}_{sigla_corso}.pdf"
```

- __Percorso del file__: /reports/{azienda}/{saved_file_name}

```python
# Directory di salvataggio del file
output_path = os.path.join("reports", azienda, saved_file_name)

# Crea la cartella se non esiste
output_dir = os.path.dirname(output_path)
os.makedirs(output_dir, exist_ok=True)
```

## Path dei file necessari al funzionamento

I file necessari al generatore come la tabella master ed i file di emissione del pdf (intestazioni, firme, ecc) risiedono tutti nella cartella in cui è posizionata la sorgente con path *"./nomefile.estensione"*

## Librerie utilizzate
- __openpyxl__: Estrapolazione dei dati tramite Excel - File type: .xlsx
- __fpdf__: Per la composizione visuale dei PDF
