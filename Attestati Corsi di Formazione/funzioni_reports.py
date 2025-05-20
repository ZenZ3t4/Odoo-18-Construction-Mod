
# FUNZIONE CHE TRASFORMA UN CSV IN INPUT IN UN DICT PY
def csv_to_dict(file):
    d = {}
    f = open(file, mode = 'r')
    testo = f.read()
    righe = testo.split('\n')  
    colnames = righe[0].split(',')
    for colname in colnames:
        d[colname] = []
        
    # itero dal secondo elemento fino alla fine
    for riga in righe[1:]: 
        valori = riga.split((','))
        for colname, valore in zip(colnames, valori):
            d[colname].append(valore)
            
    return d

def csv_to_list(csv_filename, id_corso):
    import csv
    import chardet

    with open(csv_filename, 'rb') as f:
        rawdata = f.read()
        result = chardet.detect(rawdata)

    with open(csv_filename, 'r', -1, result['encoding']) as file:
        csv_reader = csv.reader(file)
        data_list = list(csv_reader)

    for row in data_list:
        try:
            if str(row[0]).strip() == str(id_corso).strip():
                return row
        except IndexError:
            continue

    return None



# OLD
# def csv_to_list(csv_filename, result_string):
#     import csv
#     import chardet

#     with open(csv_filename, 'rb') as f:
#         rawdata = f.read()
#         result = chardet.detect(rawdata)
#     # Apri il file CSV
#     # with open(csv_filename, 'r', -1, 'utf-8') as file:
#     with open(csv_filename, 'r', -1, result['encoding']) as file:
#         # Crea un oggetto reader del CSV
#         csv_reader = csv.reader(file)
        
#         # Converti i dati del CSV in una lista
#         data_list = list(csv_reader)

#     # Itera attraverso la lista e stampa i risultati correlati
#     for row in data_list:
#         if row[0] == result_string:
#             return(row)