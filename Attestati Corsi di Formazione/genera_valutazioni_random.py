import csv
import random

def modifica_csv_con_colonna_vuota(nome_file):
  """
  Questa funzione apre un file CSV, aggiunge una colonna "valutazione_quiz" vuota se non è presente e la popola con numeri casuali con probabilità predefinite, senza inserire righe vuote.

  Argomenti:
    nome_file: Il nome del file CSV da modificare.

  Restituisce:
    Nessun valore.
  """

  # Definisci le probabilità per ogni numero casuale
  probabilità = {
    12: 0.15,
    13: 0.25,
    14: 0.35,
    15: 0.25
  }

  # Leggi il file CSV in un lettore di righe
  with open(nome_file, 'r', encoding='utf-8') as file:
    reader = csv.reader(file)

    # Crea una lista per memorizzare i dati modificati
    data_modificata = []

    # Controlla se la colonna "valutazione_quiz" è presente nell'intestazione
    intestazione = next(reader)
    if "valutazione_quiz" not in intestazione:
      intestazione.append("valutazione_quiz")
      data_modificata.append(intestazione)

    # Itera su ogni riga del file CSV
    for row in reader:
      # Genera un numero casuale con probabilità
      numero_casuale = genera_numero_casuale_con_probabilità(probabilità)

      # Aggiungi il numero casuale alla riga come nuovo elemento (colonna 11)
      if len(row) < 11:  # Controlla se la riga ha meno di 11 elementi
        row.extend([''] * (11 - len(row)))  # Aggiungi elementi vuoti per raggiungere la lunghezza 11
      row[10] = numero_casuale

      # Aggiungi la riga modificata alla lista
      data_modificata.append(row)

  # Crea un nuovo nome file con suffisso "_modificato"
  nome_file_modificato = f"{nome_file[:-4]}_modificato.csv"

  # Scrivi i dati modificati in un nuovo file CSV
  with open(nome_file_modificato, 'w', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(intestazione)  # Scrivi l'intestazione
    for row in data_modificata:
      writer.writerow(row)

  print(f"File CSV '{nome_file_modificato}' salvato con successo!")


def genera_numero_casuale_con_probabilità(probabilità):
  """
  Questa funzione genera un numero casuale intero tra 12 e 15 con probabilità predefinite.

  Argomenti:
    probabilità: Un dizionario che mappa i numeri interi alle loro probabilità.

  Restituisce:
    Un numero casuale intero tra 12 e 15.
  """

  # Genera un numero casuale uniforme tra 0 e 1
  valore_casuale = random.random()

  # Calcola l'intervallo di probabilità cumulativa
  intervallo_cumulativo = 0
  for numero, prob in probabilità.items():
    intervallo_cumulativo += prob
    if valore_casuale <= intervallo_cumulativo:
      return numero

# Esempio di utilizzo
nome_file = "tabella_master.csv"  # Inserisci qui il nome del tuo file CSV
modifica_csv_con_colonna_vuota(nome_file)

print(f"File CSV '{nome_file}' modificato con successo!")