# stampa tabella riepilogativa corsi

# Aggiungi l'intestazione della tabella
    pdf.set_font("Arial", size=10)
    pdf.cell(60, 10, "Corso", 1)
    pdf.cell(40, 10, "Votazione", 1)
    pdf.cell(40, 10, "Superato", 1)
    pdf.ln()
    
    def convert_minutes_to_hours_minutes(minutes):
        hours = int(minutes // 60)
        remaining_minutes = int(minutes % 60)
        return f"{hours:02d}:{remaining_minutes:02d}"
    
    valutazione = "14/15"
    esito_corso = corso['stato_corso']
    durata_ore = convert_minutes_to_hours_minutes(corso['durata_min'])
    testo_intro_corsi = f"Percorso: {corso['titolo_azione_con_id']}"
    testo_corsi_2 = f" - Durata del percorso di {corso['Totaleorecorso']} ore di cui 20 ore di FAD asincrona. Ore svolte effettive 20 ore."
    testo_corsi_3 = f"Corso {esito_corso} Valutazione finale: valutazione {valutazione}, valutazione tramite quiz."
    
    # Aggiungi i dati dei corsi nella tabella
    for corso in info['corsi']:
        pdf.cell(60, 10, corso['titolo_azione_con_id'] if corso['titolo_azione_con_id'] else '', 1)
        pdf.cell(40, 10, str(corso['titolo_sessione_formativa']) if corso['titolo_sessione_formativa'] else '', 1)
        pdf.cell(40, 10, str(corso['Totaleorecorso']) if str(corso['Totaleorecorso']) else '', 1)
        durata_ore = (float(corso['durata_min'])/60)
        pdf.cell(20, 10, f"{durata_ore:.0f}" if durata_ore else '', 1)
        pdf.ln()