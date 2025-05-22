# Report Gen Data - Guida Interna

## TO-DO
- Ripristinare la funzione di caricamento anagrafica su interfaccia script 2025-Odoo-E-Learning-Certification.py alla funzione [2]'

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
  - db/ con Excel (stampa_pdf.xlsx, db_corsi.xlsx, aziende.xlsx, new_master.xlsx, codici_catastali_comuni.xlsx)
  - images/ con logo, intestazione e firme
  - scripts/ con file .py di generazione e funzioni
  - logs/ cartella per i file di log (creata automaticamente)

## Come eseguire
1. Assicurarsi che i file Excel siano aggiornati e corretti.
2. Eseguire lo script principale 2025-Odoo-E-Learning-Certification.py (dalla cartella scripts/):
   
python 2025-Odoo-E-Learning-Certification.py

3. Seguire il menu a video per generare i PDF o altre operazioni.
4. I PDF vengono salvati in E-Learning Odoo Reports/{ragione_sociale}/{anno}/{save_path}/.

## Struttura file principali
- **2025-Odoo-E-Learning-Certification.py**  
  Script principale per caricare i dati Excel, aggiornare il master e generare i PDF. Punta al file stampa_pdf.xlsx

- **freedaypdf.py**  
  Contiene funzioni per la composizione del PDF, stampa layout, firme, salvataggio e gestione percorsi.

- **genera_tabella_stampa_pdf.py**  
  Script di supporto per creare e aggiornare il file stampa_pdf.xlsx contenente dati pronti per la stampa.

- **xlsdatafunctions.py**  
  Funzioni di utilità per caricare e manipolare dati Excel (caricamento corsi, aziende, estrazione date).

## Note importanti / Changelog
- **Rimozione font DejaVu:** non si usa più il font DejaVu personalizzato, ora il PDF utilizza Arial/Helvetica di default.
- **Nuova gestione percorso salvataggio PDF:**  
  Il campo save_path è stato aggiunto in db_corsi.xlsx e viene usato per organizzare la cartella di output PDF come:  
  E-Learning Odoo Reports/{ragione_sociale}/{anno}/{save_path}/nomefile.pdf
- **Firma e immagini:**  
  Firme vengono caricate da images/firme/firma_{nome_docente}.png. Assicurarsi che le immagini corrispondano ai docenti specificati.
- **Gestione logging:** tutti gli errori e le azioni vengono loggati in logs/app.log.
- **Controlli di presenza campi:** durante la generazione PDF vengono eseguiti controlli su id_corso e altri dati, con warning e skip in caso di mancanze.

## Consigli per uso interno
- Mantenere sempre aggiornati i file Excel in db/.
- Per aggiungere nuovi corsi, aggiornare anche db_corsi.xlsx con i campi corretti inclusi save_path.
- Verificare la presenza delle immagini firme prima di generare PDF.
- Log e messaggi a console aiutano a diagnosticare problemi.
- Modifiche al layout PDF vanno fatte in freedaypdf.py.

---
