from fpdf import FPDF
from datetime import datetime
import os
import logging

def stampa_dati_azienda(pdf, dettagli_azienda, id_corso):
    pdf.set_font("Helvetica", "I", size=11)

    if id_corso == 'FORMAZIONE 231':
        azienda_row_1 = f"collaboratore/dipendente dell'azienda {dettagli_azienda['ragione_sociale']} - P.IVA: {dettagli_azienda['partita_iva']}"
    else:
        azienda_row_1 = f"collaboratore dell'azienda {dettagli_azienda['ragione_sociale']} - P.IVA: {dettagli_azienda['partita_iva']}"
    pdf.cell(200, 5, txt=azienda_row_1, align='C', ln=True)

def blocco_dati_utente(pdf, data_nascita, luogo_nascita, nominativo, codice_fiscale):
    pdf.set_font("Helvetica", "BI", size=14)
    pdf.set_margins(10, 10, 10)
    testo_rilasciato_a = "il presente attestato viene conferito a"
    pdf.cell(200, 10, txt=testo_rilasciato_a, align='C', ln=True)
    pdf.ln(7)
    dati_utente = f"nato/a a {luogo_nascita} il {data_nascita} - Codice Fiscale: {codice_fiscale}"
    pdf.set_font("Helvetica", 'B', size=32)
    pdf.set_text_color(235, 9, 16)
    pdf.set_margins(10, 10, 10)
    for riga in nominativo.splitlines():
        pdf.multi_cell(0, 10, riga, align='C')
    pdf.ln(5)
    pdf.set_margins(10, 10, 10)
    pdf.set_font("Helvetica", "I", size=12)
    pdf.set_text_color(36, 35, 35)
    pdf.cell(200, 5, txt=dati_utente, align='C', ln=True)
    pdf.ln(5)

def disegna_linea(pdf):
    y_pos = pdf.get_y()
    w = pdf.w
    line_length = (3/4) * w
    line_thickness = 0.5
    x_start = (w - line_length) / 2
    pdf.set_draw_color(200, 200, 200)
    pdf.set_line_width(line_thickness)
    pdf.line(x_start, y_pos + 2, x_start + line_length, y_pos + 2)
    pdf.ln(7)

def stampa_intestazione_pdf(pdf, image_path, header_text):
    pdf.set_margins(10, 10, 10)
    pdf.ln(5)
    pdf.image(image_path, x=10, y=8, w=190)
    pdf.ln(20)
    disegna_linea(pdf)
    pdf.ln(5)
    pdf.set_text_color(235, 9, 16)
    pdf.set_font("Helvetica", "B", size=36)
    pdf.cell(193, 7, txt=header_text, align='C', ln=True)
    pdf.ln(5)
    pdf.set_text_color(36, 35, 35)
    disegna_linea(pdf)
    pdf.ln(3)

def stampa_denominazione_percorso_sviluppo(pdf, nome_corso_da_stampare):
    pdf.set_text_color(235, 9, 16)
    pdf.set_font("Arial", "B", size=24)
    pdf.set_margins(10, 10, 10)
    pdf.cell(200, 7, txt=nome_corso_da_stampare, align='C', ln=True)
    pdf.set_text_color(36, 35, 35)
    pdf.ln(6)

def stampa_contenuti_percorso(pdf, contenuti_corso):
    pdf.set_font("Arial", "", 12)
    pdf.set_margins(10, 10, 10)
    if contenuti_corso:
        for riga in contenuti_corso.splitlines():
            pdf.multi_cell(0, 5, riga)
        pdf.ln(5)

def stampa_multicell(pdf, testo):
    pdf.set_font('Arial', '', 8)
    pdf.set_margins(10, 10, 10)
    for riga in testo.splitlines():
        pdf.multi_cell(0, 5, riga)

def stampa_multicell_grande(pdf, testo):
    pdf.set_font("Arial", "I", size=10)
    pdf.set_margins(10, 10, 10)
    for riga in testo.splitlines():
        pdf.multi_cell(0, 5, riga, align='C')
    pdf.set_margins(10, 10, 10)

def stampa_multicell_nome_corso(pdf, testo):
    pdf.set_text_color(235, 9, 16)
    pdf.set_font("Arial", "B", size=24)
    pdf.set_margins(10, 10, 10)
    for riga in testo.splitlines():
        pdf.multi_cell(0, 10, riga, align='C')
    pdf.set_margins(10, 10, 10)
    pdf.set_text_color(36, 35, 35)

def stampa_paragrafo(pdf, header_str, text_string):
    pdf.set_font("Helvetica", "BI", size=12)
    pdf.set_margins(10, 10, 10)
    pdf.cell(200, 7, txt=header_str, align='C', ln=True)
    pdf.ln(3)
    stampa_multicell(pdf, text_string)

def stampa_grassetto(pdf, text_to_print):
    pdf.set_font("Helvetica", "BI", size=12)
    pdf.set_margins(10, 10, 10)
    pdf.cell(200, 7, txt=text_to_print, align='C', ln=True)
    pdf.ln(1)

def stampa_firme_accettazione(pdf, data_emissione, docente, id_corso):
    pdf.ln(2)
    disegna_linea(pdf)
    stampa_timbro(pdf)
    pdf.set_margins(10, 10, 10)
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(60, 10, 'Luogo e Data', 0, 0, 'C')
    pdf.set_font('Arial', 'I', 11)
    txt_date = 'Terni, lì ' + data_emissione
    pdf.text(25, pdf.get_y() + 12, txt=txt_date)
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(60, 10, ' ', 0, 0, 'C')

    if id_corso == 'FORMAZIONE 231':
        pdf.cell(60, 10, 'Il direttore del corso', 0, 1, 'C')
        
    elif id_corso == 'Nozioni di sicurezza alimentare e applicazione HACCP':
        pdf.cell(60, 10, 'Il direttore del corso', 0, 1, 'C')
         
    elif id_corso is not None:
        pdf.cell(60, 10, 'Il Docente', 0, 1, 'C')
    
    y_firma = pdf.get_y()
    larghezza_pagina = pdf.w
    margine_dx = pdf.r_margin
    nome_formatore = docente
    if id_corso == 'Nozioni di sicurezza alimentare e applicazione HACCP':
        img_w = 43.2
    else:
        img_w = 39
    x_firma = larghezza_pagina - margine_dx - img_w - 15
    stampa_firma(pdf, id_corso, nome_formatore, x_firma, y_firma)
    pdf.ln(15)
    pdf.cell(60, 10, ' ', 0, 0, 'C')
    pdf.cell(60, 10, ' ', 0, 0, 'C')

def stampa_firma(pdf, id_corso, nome_formatore="", x=None, y=None):
    if not nome_formatore:
        return
    sign_path = "./images/firme/firma_" + nome_formatore + ".png"
    if id_corso == 'Nozioni di sicurezza alimentare e applicazione HACCP':
        img_w = 25.56
        img_h = 34.44
    else:
        img_w = 39
        img_h = 14
    if x is None:
        x = (pdf.w - img_w) / 2
    if y is None:
        y = pdf.get_y()
    pdf.image(sign_path, x=x, y=y, w=img_w, h=img_h)

def salvapdf(pdf, codice_fiscale, ragione_sociale, report_save_path):
    # Ottieni solo l'anno corrente come stringa
    year = datetime.now().strftime("%Y")

    # Costruisci il nome del file con l'anno prima di corso_id
    saved_file_name = f"{codice_fiscale}_{year}_{report_save_path}.pdf"
    
    output_path = os.path.join("E-Learning Odoo Reports", year, ragione_sociale, report_save_path, saved_file_name)
    output_dir = os.path.dirname(output_path)
    os.makedirs(output_dir, exist_ok=True)

    pdf.output(output_path, "F")

    print(f"Il file PDF è stato salvato in: {output_path}")
    logging.info(f"Il file PDF è stato salvato in: {output_path}")

def stampa_riquadri(pdf):
    pdf.set_draw_color(200, 200, 200)
    w, h = pdf.w, pdf.h
    margin = 5
    thin_border = 0.5
    pdf.set_line_width(thin_border)
    pdf.rect(margin, margin, w - 2*margin, h - 2*margin)
    thick_line = 4
    length = 30
    pdf.set_draw_color(36, 35, 35)
    pdf.set_line_width(thick_line)
    pdf.line(margin, h - margin, margin + length, h - margin)
    pdf.line(margin, h - margin, margin, h - margin - length)
    gap = 3
    thick_line = 3
    pdf.set_line_width(thick_line)
    pdf.set_draw_color(235, 9, 16)
    pdf.line(margin + 2*gap, h - margin - 2*gap, margin + length - 2*gap, h - margin - 2*gap)
    pdf.line(margin + 2*gap, h - margin - 2*gap, margin + 2*gap, h - margin - length + 2*gap)
    pdf.set_draw_color(36, 35, 35)
    thick_line = 4
    pdf.set_line_width(thick_line)
    pdf.line(w - margin, margin, w - margin - length, margin)
    pdf.line(w - margin, margin, w - margin, margin + length)
    gap = 3
    thick_line = 3
    pdf.set_line_width(thick_line)
    pdf.set_draw_color(235, 9, 16)
    x_start = w - margin - 2*gap
    y_start = margin + 2*gap
    reduced_length = length - 4*gap
    pdf.line(x_start, y_start, x_start - reduced_length, y_start)
    pdf.line(x_start, y_start, x_start, y_start + reduced_length)
    pdf.set_draw_color(235, 9, 16)
    pdf.set_fill_color(235, 9, 16)
    pdf.set_line_width(1)
    margin = 3
    triangle_size = 20
    w, h = pdf.w, pdf.h
    points_br = [w - margin, h - margin, w - margin - triangle_size, h - margin, w - margin, h - margin - triangle_size]
    polygon(pdf, points_br, style='F')
    points_tl = [margin, margin, margin + triangle_size, margin, margin, margin + triangle_size]
    polygon(pdf, points_tl, style='F')

def polygon(pdf, points, style='D'):
    h = pdf.h
    k = pdf.k
    op = {'F': 'f', 'FD': 'b', 'DF': 'b'}.get(style, 's')
    points_str = ''
    for i in range(0, len(points), 2):
        x = points[i] * k
        y = (h - points[i+1]) * k
        if i == 0:
            points_str += f'{x:.2f} {y:.2f} m '
        else:
            points_str += f'{x:.2f} {y:.2f} l '
    pdf._out(points_str + op)

def stampa_timbro(pdf):
    page_w = pdf.w
    img_w = 30
    img_h = 30
    x = ((page_w - img_w) / 2)
    y = pdf.get_y()
    pdf.image("./images/logo_square_autentica.png", x=x, y=y, w=img_w, h=img_h)

def crea_pdf(codice_fiscale, info):
    for corso in info['corsi']:
        pdf = FPDF()
        pdf.add_page()

        image_path = "./images/intestazione.png"
        header_text = "ATTESTATO DI FORMAZIONE"
        stampa_intestazione_pdf(pdf, image_path, header_text)

        blocco_dati_utente(pdf,
                           info.get('data_nascita', ''),
                           info.get('comune', ''),
                           info.get('nominativo', ''),
                           codice_fiscale)

        dettagli_azienda = info.get('dettagli_azienda', {})
        if not dettagli_azienda:
            dettagli_azienda = {
                'ragione_sociale': 'Dati aziendali non disponibili',
                'partita_iva': 'N/A',
                'codice_ateco': 'N/A'
            }
        
        id_corso = corso.get('id_corso')

        stampa_dati_azienda(pdf, dettagli_azienda, id_corso)
        pdf.ln()

        if not id_corso:
            print(f"CF:{codice_fiscale}; id_corso non trovato")
            logging.error(f"CF:{codice_fiscale}; id_corso non trovato")
            continue

        nome_corso = corso.get('nome_corso', 'Corso non trovato')
        contenuti_corso = corso.get('contenuti_corso', '')
        durata_corso = corso.get('durata_corso', '')
        odoo_report_save_path = corso.get('save_path', '')
        
        pdf.ln(4)
        pdf.set_font("Helvetica", "BI", size=14)

        if id_corso == "Nozioni di sicurezza alimentare e applicazione HACCP":
            testo_header = "ha frequentato il corso di formazione"
            
        if id_corso == "FORMAZIONE 231":
            testo_header = "per la partecipazione al Corso di Formazione:"
            
        if id_corso == "CORSO SICUREZZA SUL LAVORO 2025":
            testo_header = "per la partecipazione al corso di formazione generale e specifica"
            
        pdf.cell(200, 7, txt=testo_header, align='C', ln=True)
        pdf.ln(8)

        stampa_multicell_nome_corso(pdf, nome_corso)

        #print(f"Id corso: {id_corso} della durata di {durata_corso}")
        #print(f"contenuti: {contenuti_corso}")
        if id_corso == 'Nozioni di sicurezza alimentare e applicazione HACCP':
            
            header_str = 'CORSO EROGATO AI SENSI DEL REG.CE 852/2004, REG.CE 178/2002, REG.CE 1169/2011'
            stampa_grassetto(pdf, header_str)

            header_str_2 = f"della durata complessiva di {durata_corso} ore, tenutosi in modalità e-learning, con i seguenti contenuti:"
            stampa_paragrafo(pdf, header_str_2, contenuti_corso)

            pdf.ln(2)

        elif id_corso == 'FORMAZIONE 231':

            grassetto_1 = f"della durata complessiva di {durata_corso} ore, tenutosi in modalità FAD"
            stampa_grassetto(pdf, grassetto_1)
            
            pdf.ln(2)

            grassetto_2 = ("nel periodo 02/2025 - 03/2025 con i seguenti contenuti:")
            stampa_grassetto(pdf, grassetto_2)

            pdf.ln(7)
            
            pdf.set_margins(10, 10, 10)
            # Testo da stampare, coppie di righe
            coppie = [
                ("La normativa del D.Lgs 231/2001 principi generali", "a cura del Presidente OdV Prof. Paolo Fratini"),
                ("Il sistema sanzionatorio ed elenco dei reati presupposto", "a cura del Membro OdV Avv. Fabio Calaciura"),
                ("I reati fiscali e societari nella normativa 231", "a cura del Membro OdV Dott. Marco Rosatelli")
            ]
            for titolo, autore in coppie:
                # Calcola larghezza testo con font appropriati
                pdf.set_font('Arial', 'B', 11)
                w_titolo = pdf.get_string_width(titolo)
                
                pdf.set_font('Arial', 'B', 11)
                w_trattino = pdf.get_string_width(' - ')
                
                pdf.set_font('Arial', 'I', 10)
                w_autore = pdf.get_string_width(autore)
                
                total_width = w_titolo + w_trattino + w_autore
                
                # Calcola larghezza area scrivibile (escludendo margini)
                page_width = pdf.w - pdf.l_margin - pdf.r_margin
                
                # Calcola posizione X centrata nell'area scrivibile
                x = pdf.l_margin + (page_width - total_width) / 2
                
                # Imposta cursore in posizione (x, y corrente)
                y = pdf.get_y()
                pdf.set_xy(x, y)
                
                # Stampa titolo
                pdf.set_font('Arial', 'B', 11)
                pdf.cell(w_titolo, 10, titolo, border=0, ln=0)
                
                # Stampa trattino
                pdf.set_font('Arial', 'B', 11)
                pdf.cell(w_trattino, 10, ' - ', border=0, ln=0)
                
                # Stampa autore
                pdf.set_font('Arial', 'I', 10)
                pdf.cell(w_autore, 10, autore, border=0, ln=1)


        else:
            paragrafo_ai_sensi = ("ai sensi dell'Art.37 del D. Lgs. n° 81/08 e s.m.i. e secondo l'Accordo Stato Regioni e "
                                 "Provincie Autonome di Trento e Bolzano del 21.12.2011")
            stampa_multicell_grande(pdf, paragrafo_ai_sensi)

            header_str = f"della durata complessiva di {durata_corso} ore, tenutosi in modalità FAD, con i seguenti contenuti:"
            stampa_paragrafo(pdf, header_str, contenuti_corso)
            pdf.ln(2)
            
            

        pdf.ln(12)

        data_certificazione = datetime.now().strftime("%d-%m-%Y")
        stampa_firme_accettazione(pdf, data_certificazione, corso.get('docente', ''), id_corso)

        stampa_riquadri(pdf)

        ragione_sociale = dettagli_azienda.get('ragione_sociale', 'default')
        salvapdf(pdf, codice_fiscale, ragione_sociale, odoo_report_save_path)


def genera_PDF(data, azienda_da_gen):
    n_errori = 0
    n_stampe = 0
    n_non_generati = 0
    for codice_fiscale, info in data.items():
        for corso in info.get('corsi', []):
            id_corso = corso.get('id_corso')
            if not id_corso:
                n_non_generati += 1
                logging.warning(f"ID corso mancante per azienda '{azienda_da_gen}', codice fiscale '{codice_fiscale}'. PDF non generato.")
                print(f"Attenzione: ID corso mancante per azienda '{azienda_da_gen}', codice fiscale '{codice_fiscale}'. PDF non generato.")
                continue
            try:
                # Unisci info del corso con info anagrafica per creare pdf
                info_corrente = info.copy()
                info_corrente.update(corso)
                crea_pdf(codice_fiscale, info_corrente)
                n_stampe += 1
            except Exception as e:
                n_errori += 1
                print(f"Errore nel creare PDF per {codice_fiscale}: {e}")
                logging.error(f"Errore nel creare PDF per {codice_fiscale}: {e}")

    print(f"N. totale stampe: {n_stampe}")
    print(f"N. PDF non generati per mancanza id_corso: {n_non_generati}")
    print(f"N. ERRORI CRITICI: {n_errori}")
    logging.info(f"N. totale stampe: {n_stampe}")
    logging.info(f"N. PDF non generati per mancanza id_corso: {n_non_generati}")
    logging.info(f"N. ERRORI CRITICI: {n_errori}")
