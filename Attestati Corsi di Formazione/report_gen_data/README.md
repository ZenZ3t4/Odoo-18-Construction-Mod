# Generatore PDF Attestati Formazione - Uso Interno

## Descrizione
Script Python per generare attestati PDF per corsi di formazione da dati Excel anagrafici, aziendali e corsi.

## Requisiti
- Python 3.7+
- Librerie: `fpdf`, `openpyxl`
- Cartelle dati: `./db` con Excel (`new_master.xlsx`, `aziende.xlsx`, `db_corsi.xlsx`, `stampa_pdf.xlsx`)
- Cartelle risorse: `./images` (intestazione, firme, logo), `./font` (DejaVuSansCondensed.ttf)

## Setup librerie
```bash
pip install fpdf openpyxl
```

## Come usare

1. Prepara/aggiorna i file Excel in `./db` con dati anagrafici, aziende, corsi e tabella per stampa (`stampa_pdf.xlsx`).

2. Esegui lo script principale:
```bash
python 2025-Odoo-E-Learning-Certification.py
```

3. Segui il prompt:
- Digita `1` per generare PDF.
- PDF generati in:  
`E-Learning Odoo Reports/{ragione_sociale}/{anno}/{save_path}/{codice_fiscale}_{anno}_{save_path}.pdf`

## Note importanti
- Assicurati che il campo `save_path` sia valorizzato in `db_corsi.xlsx` e correttamente caricato.
- Controlla la presenza delle immagini firme in `./images/firme/`.
- Verifica permessi scrittura cartelle output.

## Debug
- Errori su path NoneType -> verifica `save_path`
- Mancanza file font o immagini -> controlla cartelle relative

---

## Struttura cartelle

```
./db/               # File Excel dati
./images/           # Immagini header, firme, logo
./font/             # Font DejaVuSansCondensed.ttf
./report_gen_data/  # Script Python
```

---

## Contatti
Per supporto interno, contatta il team dev.

---
