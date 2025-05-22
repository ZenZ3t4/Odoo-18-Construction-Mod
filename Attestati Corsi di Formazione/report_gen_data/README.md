# Report Gen Data - Guida Interna

## TO-DO
- Ripristinare la funzione di caricamento anagrafica su interfaccia script `2025-Odoo-E-Learning-Certification.py` alla funzione `[2]`

## Descrizione
Questo pacchetto genera attestati PDF di formazione professionale partendo da dati Excel (anagrafica, corsi, aziende).  
Contiene script Python per l'estrazione dati, l'integrazione con database, e la generazione automatica dei PDF, con layout personalizzato.

## Requisiti
- Python 3.x
- Librerie Python:
  - fpdf
  - openpyxl
  - logging (built-in)
- Cartelle e file necessari:
  - `db/` con Excel (`stampa_pdf.xlsx`, `db_corsi.xlsx`, `aziende.xlsx`, `new_master.xlsx`, `codici_catastali_comuni.xlsx`)
  - `images/` con logo, intestazione e firme
  - `scripts/` con file `.py` di generazione e funzioni
  - `logs/` cartella per i file di log (creata automaticamente)

## Come eseguire
1. Assicurarsi che i file Excel siano aggiornati e corretti.  
2. Eseguire lo script principale `2025-Odoo-E-Learning-Certification.py` (dalla cartella `scripts/`):  
   ```bash
   python 2025-Odoo-E-Learning-Certification.py
Seguire il menu a video per generare i PDF o altre operazioni.

I PDF vengono salvati in E-Learning Odoo Reports/{ragione_sociale}/{anno}/{save_path}/.

Struttura file principali
2025-Odoo-E-Learning-Certification.py
Script principale per caricare i dati Excel, aggiornare il master e generare i PDF. Punta al file stampa_pdf.xlsx

freedaypdf.py
Contiene funzioni per la composizione del PDF, stampa layout, firme, salvataggio e gestione percorsi.

genera_tabella_stampa_pdf.py
Script di supporto per creare e aggiornare il file stampa_pdf.xlsx contenente dati pronti per la stampa.

xlsdatafunctions.py
Funzioni di utilità per caricare e manipolare dati Excel (caricamento corsi, aziende, estrazione date).

📂 Struttura del Project Root
📁 db/
Contiene i file Excel con i dati per la generazione dei report PDF:

📄 aziende.xlsx — dati aziende

📄 db_corsi.xlsx — anagrafica corsi (incluso campo save_path)

📄 new_master.xlsx — dati anagrafici master

📄 stampa_pdf.xlsx — dati pre-elaborati per stampa PDF

📄 codici_catastali_comuni.xlsx — codici catastali per comuni/province

🖼 images/
Contiene immagini utilizzate nei PDF:

🖼 intestazione.png — header PDF

🖼 logo_square_authentica.png — logo timbro

📂 firme/ — immagini firme firmate come firma_{docente}.png

📄 logs/
Cartella per i file di log generati durante l’esecuzione:

📜 app.log — file di log eventi e errori

🛠 scripts/
Script Python principali e di supporto:

⚙️ 2025-Odoo-E-Learning-Certification.py — script principale di generazione PDF

⚙️ genera_tabella_stampa_pdf.py — aggiornamento file stampa_pdf.xlsx

⚙️ xlsdatafunctions.py — funzioni per manipolazione dati Excel

⚙️ freedaypdf.py — funzioni di composizione, layout e salvataggio PDF

📁 E-Learning Odoo Reports/
Cartella di output PDF generati, con struttura:

markdown
Mostra sempre dettagli

Copia
{ragione_sociale}/
  └── {anno}/
       └── {save_path}/
            └── file.pdf
Note importanti / Changelog
Rimozione font DejaVu: non si usa più il font DejaVu personalizzato, ora il PDF utilizza Arial/Helvetica di default.

Nuova gestione percorso salvataggio PDF:
Il campo save_path è stato aggiunto in db_corsi.xlsx e viene usato per organizzare la cartella di output PDF come:
E-Learning Odoo Reports/{ragione_sociale}/{anno}/{save_path}/nomefile.pdf

Firma e immagini:
Firme vengono caricate da images/firme/firma_{nome_docente}.png. Assicurarsi che le immagini corrispondano ai docenti specificati.

Gestione logging: tutti gli errori e le azioni vengono loggati in logs/app.log.

Controlli di presenza campi: durante la generazione PDF vengono eseguiti controlli su id_corso e altri dati, con warning e skip in caso di mancanze.

Consigli per uso interno
Mantenere sempre aggiornati i file Excel in db/.

Per aggiungere nuovi corsi, aggiornare anche db_corsi.xlsx con i campi corretti inclusi save_path.

Verificare la presenza delle immagini firme prima di generare PDF.

Log e messaggi a console aiutano a diagnosticare problemi.

Modifiche al layout PDF vanno fatte in freedaypdf.py.