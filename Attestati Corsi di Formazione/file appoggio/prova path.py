import os

import random

x = os.path.abspath(path="reports")
print(x)


def genera_numero_casuale():
  """
  Questa funzione genera un numero casuale intero tra 12 e 15 con probabilità 
  predefinite per ciascun valore.

  Restituisce:
    Un numero intero casuale tra 12 e 15.
  """

  # Definisco le probabilità per ogni numero
  probabilità = {
    12: 0.15,
    13: 0.25,
    14: 0.35,
    15: 0.25
  }

  # Genero un numero casuale uniforme tra 0 e 1
  valore_casuale = random.random()

  # Calcolo l'intervallo di probabilità cumulativa
  intervallo_cumulativo = 0
  for numero, prob in probabilità.items():
    intervallo_cumulativo += prob
    if valore_casuale <= intervallo_cumulativo:
      return numero

# Esempio di utilizzo
numero_casuale = genera_numero_casuale()
print(f"Numero casuale generato: {numero_casuale}")