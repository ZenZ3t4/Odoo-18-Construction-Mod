# 📄 Report Gen Data - Guida Interna

## 🚧 TO-DO
- Ripristinare la funzione di caricamento anagrafica su interfaccia script `2025-Odoo-E-Learning-Certification.py` alla funzione `[2]`

## 📝 Descrizione
Questo pacchetto genera attestati PDF di formazione professionale partendo da dati Excel (anagrafica, corsi, aziende).  
Contiene script Python per l'estrazione dati, l'integrazione con database, e la generazione automatica dei PDF, con layout personalizzato.

## ⚙️ Requisiti
- Python 3.x
- Librerie Python:
  - `fpdf`
  - `openpyxl`
  - `logging` (built-in)
- Cartelle e file necessari:
  - `db/` con Excel:
    - `stampa_pdf.xlsx`
    - `db_corsi.xlsx`
    - `aziende.xlsx`
    - `new_master.xlsx`
    - `codici_catastali_comuni.xlsx`
  - `images/` con:
    - `logo_square_autentica.png`
    - `intestazione.png`
    - `firme/firma_{nome_docente}.png`
  - `scripts/` con file `.py`
  - `logs/` per i log (viene creata automaticamente)

## 🚀 Come eseguire

```bash
python scripts/2025-Odoo-E-Learning-Certification.py
```

Segui il menu a video per:
- Generare PDF
- Effettuare confronti (funzioni in sviluppo)

📁 I PDF vengono salvati in:
```
E-Learning Odoo Reports/{ragione_sociale}/{anno}/{save_path}/
```

## 📁 Struttura Project Root

```text
report_gen_data/
├── db/
│   ├── aziende.xlsx
│   ├── codici_catastali_comuni.xlsx
│   ├── db_corsi.xlsx
│   ├── new_master.xlsx
│   └── stampa_pdf.xlsx
├── images/
│   ├── intestazione.png
│   ├── logo_square_autentica.png
│   └── firme/
│       └── firma_NomeCognome.png
├── logs/
│   └── app.log
├── scripts/
│   ├── 2025-Odoo-E-Learning-Certification.py
│   ├── freedaypdf.py
│   ├── genera_tabella_stampa_pdf.py
│   └── xlsdatafunctions.py
└── README.md
```

## 🧠 Struttura file principali

- `2025-Odoo-E-Learning-Certification.py`: script principale, gestisce flusso da Excel a PDF.
- `freedaypdf.py`: layout PDF, firme, riquadri, salvataggio.
- `genera_tabella_stampa_pdf.py`: genera `stampa_pdf.xlsx` per PDF.
- `xlsdatafunctions.py`: funzioni di supporto per Excel (caricamento, parsing).

## 🛠️ Note importanti / Changelog

- 🔁 **Font DejaVu rimosso**: ora si usa Arial/Helvetica di default.
- 📁 **Gestione dinamica cartelle**: `save_path` (in `db_corsi.xlsx`) definisce il percorso di salvataggio.
- 🖋️ **Firma docente**: caricate da `images/firme/firma_{nome_docente}.png`
- 🧾 **Log automatici**: salvati in `logs/app.log`
- ⚠️ **Controlli campi**: id_corso mancante ➜ skip con warning.

## ✅ Consigli per uso interno

- Aggiorna regolarmente i file in `db/`.
- Aggiungi nuovi corsi completando `db_corsi.xlsx` con `save_path`.
- Assicurati che ogni docente abbia la sua firma in `images/firme/`.
- Consulta i log in caso di errore.
- Modifica il layout PDF direttamente in `freedaypdf.py`.

