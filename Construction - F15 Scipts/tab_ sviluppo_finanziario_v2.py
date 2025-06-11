for record in self:
    try:
        # Variabili di base
        durata_contratto = record.x_durata_contratto or 1  # Durata del contratto (in anni)
        durata_finanziamento = record.x_durata_finanziamento or 0  # Durata del finanziamento (in anni)
        importo_banca = record.x_importo_banca or 0.0  # Importo del finanziamento
        percentuale_interessi = record.x_percentuale_interessi or 0.0  # Percentuale di interesse
        percentuale_ires = record.x_percentuale_ires or 0.0  # Percentuale IRES
        costi_totali = record.x_computed_costi_totali or 0.0  # Costi totali della commessa
        costi_generali = record.x_costi_gestione or 0.0  # Costi generali della commessa
        ricavi_previsti = record.expected_revenue or 0.0  # Ricavi previsti
        ricavi_recorrenti = record.recurring_revenue or 0.0  # Ricavi ricorrenti
        oneri_finanziari_totali = record.x_oneri_finanziari_totali or 0.0  # Oneri finanziari totali
        contributo_pubblico = record.x_importo_contributo_extra or 0.0  # Contributo pubblico
        equity = record.x_importo_equity or 0.0  # Equity
        investimento = record.x_importo_untaxed_investimento or 0.0  # Investimento
        costi_investimento = investimento  # Investimento iniziale
        costi_operativi_anno_0 = record.x_importo_gestione_anno_0 or 0.0  # Costi operativi anno 0
        costi_operativi_successivo = record.x_importo_untaxed_gestione or 0.0  # Costi operativi anni successivi
        percenutale_costi_generali = record.x_percentuale_costi_gestione or 0.0
        tabella_sviluppo = ""  # Stringa per generare la tabella HTML
        project_equity = record.x_importo_equity
        
        # Calcolo aliquota costi generali applicati alla Gestione
        if percenutale_costi_generali > 0:
            aliquota_costi_generali = (percenutale_costi_generali / 100)
        else:
            aliquota_costi_generali = 0

        # Variabili per ammortamento materiale
        am_mat_importo_1 = record.x_ammortamento_materiale_importo_1 or 0.0
        am_mat_durata_1 = record.x_ammortamento_materiale_durata_1 or 0.0
        
        am_mat_importo_2 = record.x_ammortamento_materiale_importo_2 or 0.0
        am_mat_durata_2 = record.x_ammortamento_materiale_durata_2 or 0.0
        
        am_mat_importo_3 = record.x_ammortamento_materiale_importo_3 or 0.0
        am_mat_durata_3 = record.x_ammortamento_materiale_durata_3 or 0.0
        
        # Variabili per ammortamento immateriale
        am_imm_importo_1 = record.x_ammortamento_immateriale_importo_1 or 0.0
        am_imm_durata_1 = record.x_ammortamento_immateriale_durata_1 or 0.0
        
        am_imm_importo_2 = record.x_ammortamento_immateriale_importo_2 or 0.0
        am_imm_durata_2 = record.x_ammortamento_immateriale_durata_2 or 0.0
        
        am_imm_importo_3 = record.x_ammortamento_immateriale_importo_3 or 0.0
        am_imm_durata_3 = record.x_ammortamento_immateriale_durata_3 or 0.0
        
        # Calcolo ammortamenti con controllo divisione per zero
        ammortamento_materiale_1 = (am_mat_importo_1 / am_mat_durata_1) if am_mat_durata_1 else 0.0
        ammortamento_materiale_2 = (am_mat_importo_2 / am_mat_durata_2) if am_mat_durata_2 else 0.0
        ammortamento_materiale_3 = (am_mat_importo_3 / am_mat_durata_3) if am_mat_durata_3 else 0.0
        
        ammortamento_immateriale_1 = (am_imm_importo_1 / am_imm_durata_1) if am_imm_durata_1 else 0.0
        ammortamento_immateriale_2 = (am_imm_importo_2 / am_imm_durata_2) if am_imm_durata_2 else 0.0
        ammortamento_immateriale_3 = (am_imm_importo_3 / am_imm_durata_3) if am_imm_durata_3 else 0.0
            
        if durata_finanziamento > 1:
            # Calcolare il tasso d'interesse annuale
            tasso_interesse_annuo = percentuale_interessi / 100
            # Calcolare la rata fissa annuale (metodo alla francese)
            rata_fissa = importo_banca * (tasso_interesse_annuo / (1 - (1 + tasso_interesse_annuo)**-durata_finanziamento))
        
            # Calcolo della quota di interessi e rata per ogni anno
            capitale_residuo = importo_banca
        else:
            rata_fissa = 0
            capitale_residuo = 0
            tasso_interesse_annuo = 0
        
        # Calcolo interessi finanziari normalizzati a durata contratto
        interessi_normalizzati = oneri_finanziari_totali / durata_contratto

        # Calcolare i valori aggregati di LLCR DSCR e ROE
        fco_totale = 0
        debito_totale = 0
        utile_netto_totale = 0
        fco_attualizzato_totale = 0
        dscr_cumulato = 0
        payback_year = 0
        fco_cumulato = 0.0
        payback_trovato = False
        tasso_attualizzazione = 0.0465  # Puoi anche renderlo personalizzabile da un campo
        van_totale = 0.0
        
        for anno in range(1, durata_contratto + 1):
             # Ammortamento materiale annuale
            if anno <= am_mat_durata_1:
                ammortamento_materiale_1_anno = am_mat_importo_1 / am_mat_durata_1
            else:
                ammortamento_materiale_1_anno = 0

            if anno <= am_mat_durata_2:
                ammortamento_materiale_2_anno = am_mat_importo_2 / am_mat_durata_2
            else:
                ammortamento_materiale_2_anno = 0

            if anno <= am_mat_durata_3:
                ammortamento_materiale_3_anno = am_mat_importo_3 / am_mat_durata_3
            else:
                ammortamento_materiale_3_anno = 0

            ammortamento_materiale_totale = ammortamento_materiale_1_anno + ammortamento_materiale_2_anno + ammortamento_materiale_3_anno

            # Ammortamento immateriale annuale
            if anno <= am_imm_durata_1:
                ammortamento_immateriale_1_anno = am_imm_importo_1 / am_imm_durata_1
            else:
                ammortamento_immateriale_1_anno = 0

            if anno <= am_imm_durata_2:
                ammortamento_immateriale_2_anno = am_imm_importo_2 / am_imm_durata_2
            else:
                ammortamento_immateriale_2_anno = 0

            if anno <= am_imm_durata_3:
                ammortamento_immateriale_3_anno = am_imm_importo_3 / am_imm_durata_3
            else:
                ammortamento_immateriale_3_anno = 0

            ammortamento_immateriale_totale = ammortamento_immateriale_1_anno + ammortamento_immateriale_2_anno + ammortamento_immateriale_3_anno
            
            # Determina i valori per anno 1 e per gli anni successivi
            if anno == 1:
                finanziamento = importo_banca  # Finanziamento valido solo per l'anno 1
                contributo_pubblico = contributo_pubblico  # Contributo pubblico valido solo per l'anno 1
                equity = equity  # Equity valido solo per l'anno 1
                investimento = investimento  # Investimento valido solo per l'anno 1
                costi_generali_investimento = investimento * (aliquota_costi_generali / 100) # Costi generali dell'investimento
            else:
                finanziamento = 0
                contributo_pubblico = 0
                equity = 0
                investimento = 0  # Investimento uguale a 0 per gli anni successivi
                costi_generali_investimento = 0

            # Calcolare la quota di interesse (inizia alta e diminuisce nel tempo)
            if anno <= durata_finanziamento + 1 and anno != 1:
                quota_interessi = capitale_residuo * tasso_interesse_annuo
                rata_annuale = rata_fissa
            else:
                quota_interessi = 0  # Gli interessi non vengono più applicati dopo la durata del finanziamento
                rata_annuale = 0  # Dopo la fine del finanziamento la rata diventa 0
                
            # Calcolare i ricavi annuali (ricavi previsti distribuiti + ricavi ricorrenti ogni anno)
            ricavi_anno = ricavi_previsti + ricavi_recorrenti + contributo_pubblico

            # Costi operativi: Anno 1 prende costi operativi specifici, anni successivi usano x_importo_untaxed_gestione
            

            if anno == 1 and costi_operativi_anno_0 > 0:
                costi_generali = (costi_operativi_anno_0 * aliquota_costi_generali) + costi_generali_investimento
                costi_operativi = costi_operativi_anno_0 + costi_generali
            else:
                costi_generali = (costi_operativi_successivo * aliquota_costi_generali) + costi_generali_investimento
                costi_operativi = costi_operativi_successivo + costi_generali

            

            # Calcolare EBITDA, EBT e Utile Netto per ogni anno, tenendo conto della quota interessi

            ebitda = ricavi_anno - costi_operativi - costi_generali
            ebt = ebitda - quota_interessi - ammortamento_materiale_totale - ammortamento_immateriale_totale# EBT diminuisce con la quota interessi
            irap = ricavi_anno * (record.x_percentuale_irap / 100)  # IRAP calcolato sui ricavi
            ires = (ebt - irap) * (record.x_percentuale_ires / 100)
            
            # Calcolo DSCR
            dscr_cumulato += (ebitda/rata_annuale) if anno <= durata_finanziamento + 1 and anno!= 1 else 0
            
            
            if ires < 0:
                ires = 0  # Se il valore è negativo, IRES è 0

            utile_netto = ebt - irap - ires  # Calcolare l'imposta IRES
            
            if durata_finanziamento > 1:
                # Calcolare la quota capitale (rata - quota interessi)
                quota_capitale = rata_annuale - quota_interessi
                 # Ridurre il capitale residuo ogni anno (dopo aver pagato la rata)
                capitale_residuo -= (rata_fissa - quota_interessi) if anno != 1 and anno <= durata_finanziamento else 0
            else:
                quota_capitale = 0
                capitale_residuo = 0
                
            # Flusso di cassa operativo
            fco = utile_netto + ammortamento_materiale_totale + ammortamento_immateriale_totale
            
            # Somma del flusso di cassa operativo per il calcolo di DSCR
            fco_totale += fco
            
            # Somma della quota capitale e degli interessi per il calcolo di DSCR
            if anno != 1 and anno <= durata_finanziamento:
                debito_totale += (quota_capitale + quota_interessi)
            
            # Somma dell'utile netto per il calcolo di ROE
            utile_netto_totale += utile_netto
            
            # Somma dei flussi di cassa operativi attualizzati per il calcolo di LLCR
            if anno <= durata_finanziamento + 1:
                fco_attualizzato_totale += fco / (1 + tasso_interesse_annuo)**anno
            
             # Calcolo PAYBACK Year
            if not payback_trovato:
                fco_cumulato += fco
                if fco_cumulato >= project_equity:
                    payback_year = anno
                    payback_trovato = True
            
            # Calcolo VAN
            van_totale += fco / ((1 + tasso_attualizzazione) ** anno)

            # Applicare colore rosso se il valore è negativo
            def color_negative(value):
                return f'<span style="color:red; text-align:right;">{value:,.2f} €</span>' if value < 0 else f'{value:,.2f} €'

            # Creare la riga della tabella HTML per ogni anno
            tabella_sviluppo += f"""
                <tr>
                    <td>{anno}</td>
                    <td>{(ricavi_previsti + ricavi_recorrenti):,.2f} €</td>
                    <td>{finanziamento:,.2f} €</td>
                    <td>{contributo_pubblico:,.2f} €</td>
                    <td>{equity:,.2f} €</td>
                    <td>{investimento:,.2f} €</td>
                    <td>{costi_operativi:,.2f} €</td>
                    <td>{costi_generali:,.2f} €</td>
                    <td>{ammortamento_materiale_totale:,.2f} €</td>
                    <td>{ammortamento_immateriale_totale:,.2f} €</td>
                    <td style="color:grey;">{color_negative(interessi_normalizzati)}</td>
                    <td>{color_negative(quota_interessi)}</td>
                    <td>{color_negative(quota_capitale)}</td>
                    <td>{color_negative(rata_annuale)}</td>
                    <td>{color_negative(ebitda)}</td>
                    <td>{color_negative(ebt)}</td>
                    <td>{color_negative(irap)}</td>
                    <td>{color_negative(ires)}</td>
                    <td>{color_negative(utile_netto)}</td>
                    <td>{color_negative(fco)}</td>
                </tr>
            """

        # Aggiungere la tabella HTML
        record['x_t_sviluppo_economico'] = f"""
            <table style="width:100%; table-layout: fixed; white-space: normal; border: 1px solid #ddd; border-collapse: collapse;">
                <thead>
                    <tr>
                        <th style="width: 50px; padding: 5px; text-align: center; word-wrap: break-word;">Anno</th>
                        <th style="width: 100px; padding: 5px; text-align: center; word-wrap: break-word;">Canone Annuo</th>
                        <th style="width: 110px; padding: 5px; text-align: center; word-wrap: break-word;">Finanziamento</th>
                        <th style="width: 100px; padding: 5px; text-align: center; word-wrap: break-word;">Contributo Extra</th>
                        <th style="width: 100px; padding: 5px; text-align: center; word-wrap: break-word;">Equity</th>
                        <th style="width: 110px; padding: 5px; text-align: center; word-wrap: break-word;">Investimento</th>
                        <th style="width: 90px; padding: 5px; text-align: center; word-wrap: break-word;">Costi Operativi</th>
                        <th style="width: 90px; padding: 5px; text-align: center; word-wrap: break-word;">Costi Generali</th>
                        <th style="width: 90px; padding: 5px; text-align: center; word-wrap: break-word;">Ammortamento Materiale</th>
                        <th style="width: 90px; padding: 5px; text-align: center; word-wrap: break-word;">Ammortamento Immateriale</th>
                        <th style="width: 90px; padding: 5px; text-align: center; word-wrap: break-word;">Q.Int. Distribuita</th>
                        <th style="width: 90px; padding: 5px; text-align: center; word-wrap: break-word;">Q. Interessi</th>
                        <th style="width: 90px; padding: 5px; text-align: center; word-wrap: break-word;">Q. Capitale</th>
                        <th style="width: 90px; padding: 5px; text-align: center; word-wrap: break-word;">Rata Annuale</th>
                        <th style="width: 100px; padding: 5px; text-align: center; word-wrap: break-word;">EBITDA</th>
                        <th style="width: 100px; padding: 5px; text-align: center; word-wrap: break-word;">EBT</th>
                        <th style="width: 100px; padding: 5px; text-align: center; word-wrap: break-word;">IRAP</th>
                        <th style="width: 100px; padding: 5px; text-align: center; word-wrap: break-word;">IRES</th>
                        <th style="width: 100px; padding: 5px; text-align: center; word-wrap: break-word;">Utile Netto</th>
                        <th style="width: 100px; padding: 5px; text-align: center; word-wrap: break-word;">FCO</th>
                    </tr>
                </thead>
                <tbody>
                    {tabella_sviluppo}
                </tbody>
            </table>
        """
        
        # Calcolo del DSCR come valore unico
        dscr_unico = dscr_cumulato / durata_finanziamento if durata_finanziamento > 1 else 0

        # Calcolo del LLCR come valore unico
        llcr_unico = fco_attualizzato_totale / importo_banca if importo_banca > 0 else 0

        # Calcolo del ROE come valore unico
        roe_unico = utile_netto_totale / project_equity if project_equity != 0 else 0
        
        # Calcolo del VAN
        project_investimento = record.x_importo_untaxed_investimento
        van_finale = van_totale - project_equity  # oppure -investimento se vuoi il VAN globale
        
        record['x_dscr'] = dscr_unico
        record['x_llcr'] = llcr_unico
        record['x_roe'] = roe_unico
        record['x_payback_year'] = payback_year
        record['x_indicatore_van'] = van_finale
        
    except Exception:
        record['x_t_sviluppo_economico'] = "<p>...</p>"
