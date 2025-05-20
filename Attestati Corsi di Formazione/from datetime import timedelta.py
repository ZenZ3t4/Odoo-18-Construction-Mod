from datetime import timedelta

# Cerca tutti i dipendenti con la "data scadenza visita" valorizzata
employees = env['hr.employee'].search([('visa_expire', '!=', False)])

for employee in employees:
    # Recupera la data di scadenza
    scadenza_data = employee.visa_expire
    
    # Calcola la data 10 giorni prima della scadenza
    promemoria_data = scadenza_data - timedelta(days=10)
    
    # Imposta un'ora di inizio predefinita alle 9:00 (aggiunge l'ora alla data)
    ora_inizio = datetime.combine(promemoria_data, datetime.min.time()).replace(hour=9, minute=0)
    
    # Durata evento in ore (15 minuti = 0.25 ore)
    durata_evento = 0.25
    
    # Cerca eventuali eventi nel giorno del promemoria
    eventi = env['calendar.event'].search([
        ('start', '>=', ora_inizio.replace(hour=0, minute=0, second=0)),
        ('start', '<', ora_inizio.replace(hour=23, minute=59, second=59))
    ], order='start asc')
    
    # Se ci sono eventi, trova la prima ora libera
    if eventi:
        ultimo_evento = eventi[-1]
        ora_inizio = ultimo_evento.stop  # Imposta l'inizio dopo l'ultimo evento
    
    # Crea un appuntamento sul calendario
    env['calendar.event'].create({
        'name': f'Promemoria scadenza visita per {employee.name}',
        'start': ora_inizio,
        'stop': ora_inizio + timedelta(minutes=15),  # Durata di 15 minuti
        'duration': durata_evento,  # Imposta la durata in ore
        'allday': False,
        'partner_ids': [(4, employee.user_id.partner_id.id)] if employee.user_id else False,
        'description': f'Visita medica in scadenza per {employee.name} il {scadenza_data}',
    })
