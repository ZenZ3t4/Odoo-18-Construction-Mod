from freedaypdf import *
from xlsdatafunctions import *
import os
import logging

log_dir = './logs'
os.makedirs(log_dir, exist_ok=True)
log_file_path = os.path.join(log_dir, 'app.log')
logging.basicConfig(
    filename=log_file_path,
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO
)

# Funzione che estrae data di nascita da codice fiscale e restituisce gg/mm/aaaa
def estrai_data_nascita_da_codice_fiscale(codice_fiscale):
    mesi_codice = 'ABCDEHLMPRST'  # Mesi: A=Gen, B=Feb, ..., T=Dic
    anno = int(codice_fiscale[6:8])
    mese = mesi_codice.index(codice_fiscale[8]) + 1
    giorno = int(codice_fiscale[9:11])
    # Correzione giorno per donne
    if giorno > 40:
        giorno -= 40
    # Determina il secolo
    if anno < 40:
        anno += 2000
    else:
        anno += 1900
    data_ita = f"{giorno}/{mese}/{anno}"
    return data_ita

# Percorsi e costanti
path_db_master = "./db/test_db_anagrafica.xlsx"
path_aziende = "./db/aziende.xlsx"
path_stampa_pdf = "./db/test_stampa_pdf.xlsx"
print(os.getcwd())
if not os.path.exists(path_stampa_pdf):
    print(f"Errore: il file {path_stampa_pdf} non esiste. Prima devi generarlo")
    exit(1)
    
print("\n[1] Genera PDF attestati")
print("[0] Esci")
scelta = input("Scegli un'opzione: ")

if scelta == '1':
    corsi_db = carica_db_corsi('./db/db_corsi.xlsx')
    aziende_db = carica_aziende('./db/aziende.xlsx')
    data = carica_stampa_pdf(path_stampa_pdf)  # Carica i dati da stampa_pdf.xlsx

    logging.info("------------------------------- INIZIO GENERAZIONE PDF ------------------------------------ ")
    print("Caricamento dati da:", path_stampa_pdf)

    try:
        for cf, info in data.items():
            id_azienda = info.get('id_azienda', 'default_azienda')
            info['dettagli_azienda'] = aziende_db.get(str(id_azienda), {
                'ragione_sociale': 'Dati aziendali non disponibili',
                'partita_iva': 'N/A',
                'codice_ateco': 'N/A'
            })
            for corso in info['corsi']:
                id_corso = corso.get('id_corso')
                if id_corso and id_corso in corsi_db:
                    corso.update(corsi_db[id_corso])
                else:
                    corso.update({
                        "nome_corso": "Corso non trovato",
                        "contenuti_corso": "",
                        "durata_corso": "",
                        "save_path": "default_path"
                    })
                    
        azienda_da_gen = "default_azienda"
        genera_PDF(data, azienda_da_gen)

    except Exception as e:
        print(f"Errore durante la generazione PDF: {e}")
        logging.error(f"Errore durante la generazione PDF: {e}")


elif scelta == '0':
    print(f"Aggiornamento dati master con dati da azienda '{azienda_da_gen}'...")
    aggiorna_master_da_azienda(azienda_da_gen)
    print("Aggiornamento completato. Uscita dal programma.")
    logging.info("------------------------------- EXITING SESSION LOG --------------------------------------- ")
    logging.info("------------------------------------------------------------------------------------------- ")
    print("SCELTA: FUNZIONE IMPORT DATI ANAGRAFICA...")

else:
    print("Opzione non valida.")
