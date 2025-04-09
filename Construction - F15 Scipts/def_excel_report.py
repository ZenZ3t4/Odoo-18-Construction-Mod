    def action_print_budget_excel_report(self):
        """Print Budget excel report"""
        workbook = xlwt.Workbook(encoding='utf-8')
        sheet1 = workbook.add_sheet('Riepilogo', cell_overwrite_ok=True)
        sheet1.show_grid = False
        sheet1.col(0).width = 400
        sheet1.col(3).width = 600
        sheet1.col(9).width = 600
        sheet1.row(4).height = 400
        sheet1.row(5).height = 200
        sheet1.row(6).height = 400
        sheet1.row(7).height = 200
        sheet1.row(8).height = 400
        sheet1.row(9).height = 200
        sheet1.row(10).height = 400
        sheet1.row(11).height = 200
        sheet1.row(12).height = 400
        sheet1.row(17).height = 400
        sheet1.col(12).width = 5000
        sheet1.col(13).width = 4000
        sheet1.col(14).width = 5000
        sheet1.col(15).width = 5000
        sheet1.col(16).width = 8000
        sheet1.col(17).width = 7000
        sheet1.col(18).width = 7000
        sheet1.col(19).width = 7000
        sheet1.col(20).width = 7000
        sheet1.col(21).width = 7000
        sheet1.col(22).width = 5000
        sheet1.row(14).height = 600
        border_squre = xlwt.Borders()
        border_squre.bottom = xlwt.Borders.HAIR
        border_squre.bottom_colour = xlwt.Style.colour_map["sea_green"]
        al = xlwt.Alignment()
        al.horz = xlwt.Alignment.HORZ_LEFT
        al.vert = xlwt.Alignment.VERT_CENTER
        date_format = xlwt.XFStyle()
        date_format.num_format_str = 'mm/dd/yyyy'
        date_format.font.name = "Century Gothic"
        date_format.borders = border_squre
        date_format.alignment = al
        date_format.font.colour_index = 0x36
        date_format.font.bold = 1
        sheet1.set_panes_frozen(True)
        sheet1.set_horz_split_pos(18)
        sheet1.remove_splits = True
        #
        # 0.0 Data formats
        #
        title = xlwt.easyxf(
            "font: height 350, name Century Gothic, bold on, color_index blue_gray;"
            " align: vert center, horz center;"
            "border: bottom thick, bottom_color sea_green;")
        values = xlwt.easyxf(
            "font:name Century Gothic, bold on, color_index blue_gray;"
            " align: vert center, horz left;"
            "border: bottom hair, bottom_color sea_green;")
        line_percentage_value = xlwt.easyxf(
            "font:name Century Gothic, bold on, color_index blue_gray;"
            " align: vert center, horz center;"
            "border: bottom hair, bottom_color blue_gray, right hair,right_color blue_gray;")
        line_values = xlwt.easyxf(
            "font:name Century Gothic;"
            " align: vert center, horz center;"
            "border: bottom hair, bottom_color blue_gray, right hair,right_color blue_gray,left hair,left_color blue_gray;")
        line_amount_values = xlwt.easyxf(
            "font:name Century Gothic;"
            " align: vert center, horz right;"
            "border: bottom hair, bottom_color blue_gray, right hair,right_color blue_gray,left hair,left_color blue_gray;")
        line_amount_sub_title = xlwt.easyxf(
            "font: height 185, name Century Gothic, bold on, color_index gray80; "
            "align: vert center, horz right; "
            "border: top hair, bottom hair, left hair, right hair, "
            "top_color gray50, bottom_color gray50, left_color gray50, right_color gray50")
        sub_title = xlwt.easyxf(
            "font: height 185, name Century Gothic, bold on, color_index gray80; "
            "align: vert center, horz center; "
            "border: top hair, bottom hair, left hair, right hair, "
            "top_color gray50, bottom_color gray50, left_color gray50, right_color gray50")
        #
        # 20250401 f15_euro_value style
        #
        f15_euro_value = xlwt.easyxf(
            "font: height 185, name Century Gothic, bold on, color_index gray80; "
            "align: vert center, horz right; "
            "border: top hair, bottom hair, left hair, right hair, "
            "top_color gray50, bottom_color gray50, left_color gray50, right_color gray50"
            ,num_format_str = "€_#,##0.00")
        #
        # 1.0 Budget details
        #
        # Notes:
        # 20250401 - vecchia stampa
        # budget_amount = str(self.budget_id.currency_id.symbol) + \
        #                 " " + str(self.budget_id.total_budget_amount)
        # per stampare correttamente i numeri e sfruttare le funzioni di somma di Excel:
        # bisogna levare la funzione str da ogni variabile numerica in stampa sulle celle

        budget_amount = self.budget_id.total_budget_amount
        # utilization_amount = str(self.budget_id.currency_id.symbol) + " " + str(
        #     self.budget_id.utilization_amount)
        utilization_amount = self.budget_id.utilization_amount
        utilization_percentage = str(self.budget_id.progress) + " %"
        sheet1.write_merge(0, 2, 1, 11, "Dettaglio del Budget", title)
        sheet1.write_merge(4, 4, 1, 2, "Commessa", sub_title)
        sheet1.write_merge(4, 4, 4, 5, self.construction_site_id.name, values)
        sheet1.write_merge(6, 6, 1, 2, "Sub Commessa", sub_title)
        sheet1.write_merge(6, 6, 4, 5, self.name, values)
        sheet1.write_merge(4, 4, 7, 8, "Data Inizio", sub_title)
        sheet1.write_merge(
            4, 4, 10, 11, self.budget_id.start_date, date_format)
        sheet1.write_merge(6, 6, 7, 8, "Data Fine", sub_title)
        sheet1.write_merge(6, 6, 10, 11, self.budget_id.end_date, date_format)
        sheet1.write_merge(8, 8, 1, 2, "Totale Budget", sub_title)
        sheet1.write_merge(8, 8, 4, 5, budget_amount, values)
        sheet1.write_merge(10, 10, 1, 2, "Utilizzo del Budget", sub_title)
        sheet1.write_merge(10, 10, 4, 5, utilization_amount, f15_euro_value)
        sheet1.write_merge(12, 12, 1, 2, "Utilizzo (%)", sub_title)
        sheet1.write_merge(12, 12, 4, 5, utilization_percentage, values)
        # Budget Lines
        sheet1.write_merge(14, 15, 1, 22, "Linee di Budget", title)
        sheet1.write_merge(17, 17, 1, 3, "Tipologia Lavorazione", sub_title)
        sheet1.write_merge(17, 17, 4, 6, "Sottotipo lavorazione", sub_title)
        sheet1.write(17, 7, "BOQ Qta", line_amount_sub_title)
        sheet1.write_merge(17, 17, 8, 10, "Qta da aggiungere",
                           line_amount_sub_title)
        sheet1.write(17, 11, "Qta Totale", line_amount_sub_title)
        sheet1.write(17, 12, "Analisi dei costi", sub_title)
        sheet1.write(17, 13, "Prezzo cad", line_amount_sub_title)
        sheet1.write(17, 14, "Budget Netto", line_amount_sub_title)
        sheet1.write(17, 15, "Imposte (I.V.A.)", line_amount_sub_title)
        sheet1.write(17, 16, "Budget Totale", line_amount_sub_title)
        sheet1.write(17, 17, "Materiale utilizzato", line_amount_sub_title)
        sheet1.write(17, 18, "Attrezzatura utilizzata", line_amount_sub_title)
        sheet1.write(17, 19, "Manodopera utilizzata", line_amount_sub_title)
        sheet1.write(17, 20, "Spese generali utilizzate", line_amount_sub_title)
        sheet1.write(17, 21, "Budget rimanente", line_amount_sub_title)
        sheet1.write(17, 22, "Utilizzo (%)", sub_title)
        col = 18
        for data in self.budget_id.budget_line_ids:
            sheet1.row(col).height = 400
            sheet1.write_merge(
                col, col, 1, 3, data.job_type_id.name, line_values)
            sheet1.write_merge(
                col, col, 4, 6, data.sub_category_id.name, line_values)
            sheet1.write(col, 7, data.boq_qty, line_amount_values)
            sheet1.write_merge(
                col, col, 8, 10, data.additional_qty, line_amount_values)
            sheet1.write(col, 11, (data.boq_qty +
                                   data.additional_qty), line_amount_values)
            sheet1.write(col, 12, ((data.rate_analysis_id.name)
                                   if data.rate_analysis_id else ""), line_values)
            # -------------------------------------------------------------------------------------
            # 20250401 fix after newly created f15_euro_value style - see changelog
            #
            # sheet1.write(col, 13, (str(self.budget_id.currency_id.symbol) +
            #                        " " + str(data.price_per_qty)), line_amount_values)
            # sheet1.write(col, 14, (str(self.budget_id.currency_id.symbol) +
            #                        " " + str(data.untaxed_amount)), line_amount_values)
            # sheet1.write(col, 15, (str(self.budget_id.currency_id.symbol) +
            #                        " " + str(data.tax_amount)), line_amount_values)
            # sheet1.write(col, 16, (str(self.budget_id.currency_id.symbol) +
            #                        " " + str(data.budget)), line_amount_values)
            # sheet1.write(col, 17, (str(self.budget_id.currency_id.symbol) +
            #                        " " + str(data.material_spent)), line_amount_values)
            # sheet1.write(col, 18, (str(self.budget_id.currency_id.symbol) +
            #                        " " + str(data.equipment_spent)), line_amount_values)
            # sheet1.write(col, 19, (str(self.budget_id.currency_id.symbol) +
            #                        " " + str(data.labour_spent)), line_amount_values)
            # sheet1.write(col, 20, (str(self.budget_id.currency_id.symbol) +
            #                        " " + str(data.overhead_spent)), line_amount_values)
            # sheet1.write(col, 21, (str(self.budget_id.currency_id.symbol) +
            #                        " " + str(data.remaining_budget)), line_amount_values)
            # -------------------------------------------------------------------------------------
            sheet1.write(col, 13, (data.price_per_qty), f15_euro_value)
            sheet1.write(col, 14, (data.untaxed_amount), f15_euro_value)
            sheet1.write(col, 15, (data.tax_amount), f15_euro_value)
            sheet1.write(col, 16, (data.budget), f15_euro_value)
            sheet1.write(col, 17, (data.material_spent), f15_euro_value)
            sheet1.write(col, 18, (data.equipment_spent), f15_euro_value)
            sheet1.write(col, 19, (data.labour_spent), f15_euro_value)
            sheet1.write(col, 20, (data.overhead_spent), f15_euro_value)
            sheet1.write(col, 21, (data.remaining_budget), f15_euro_value)
            sheet1.write(
                col, 22, (str(data.total_spent) + " " + "%"), line_percentage_value)
            col = col + 1

        # Budget Spent
        self.get_budget_spent(workbook=workbook)

        # Print Report
        stream = BytesIO()
        workbook.save(stream)
        out = base64.encodebytes(stream.getvalue())
        attachment = self.env['ir.attachment'].sudo()
        filename = self.construction_site_id.name + ' - Budget Report' + ".xls"
        attachment_id = attachment.create(
            {'name': filename,
             'type': 'binary',
             'public': False,
             'datas': out})
        if attachment_id:
            report = {
                'type': 'ir.actions.act_url',
                'url': '/web/content/%s?download=true' % (attachment_id.id),
                'target': 'self',
            }
            return report
        return True

    def get_budget_spent(self, workbook):
        """Budget Spent Excel Report"""
        title = xlwt.easyxf(
            "font: height 300, name Century Gothic, bold on, color_index blue_gray;"
            " align: vert center, horz center;"
            "border: bottom thick, bottom_color sea_green;")
        title2 = xlwt.easyxf(
            "font: height 250, name Century Gothic, bold on, color_index blue_gray;"
            " align: vert center, horz left;"
            "border: bottom thin, bottom_color sea_green;")
        title3 = xlwt.easyxf(
            "font: height 250, name Century Gothic, bold on;"
            " align: vert center, horz right;"
            "border: bottom thin, bottom_color sea_green;")
        line_amount_sub_title = xlwt.easyxf(
            "font: height 185, name Century Gothic, bold on, color_index gray80; "
            "align: vert center, horz right; "
            "border: top hair, bottom hair, left hair, right hair, "
            "top_color gray50, bottom_color gray50, left_color gray50, right_color gray50")
        line_values = xlwt.easyxf(
            "font:name Century Gothic;"
            " align: vert center, horz center;"
            "border: bottom hair, bottom_color blue_gray, right hair,right_color blue_gray,left hair,left_color blue_gray;")
        sub_title = xlwt.easyxf(
            "font: height 185, name Century Gothic, bold on, color_index gray80; "
            "align: vert center, horz center; "
            "border: top hair, bottom hair, left hair, right hair, "
            "top_color gray50, bottom_color gray50, left_color gray50, right_color gray50")
        sub_title2 = xlwt.easyxf(
            "font: height 200, name Century Gothic, bold on, color_index gray80; "
            "align: vert center, horz left; "
            "border: bottom hair,"
            "bottom_color sea_green;")
        sub_title_amount = xlwt.easyxf(
            "font: height 200, name Century Gothic, bold on, color_index gray80; "
            "align: vert center, horz right; "
            "border: bottom hair,"
            "bottom_color sea_green;")
        horiz_double_line = xlwt.easyxf("border: top double, top_color gray50")
        #
        # 20250401 f15_euro_value style
        #
        f15_euro_value = xlwt.easyxf(
            "font: height 185, name Century Gothic, bold on, color_index gray80; "
            "align: vert center, horz right; "
            "border: top hair, bottom hair, left hair, right hair, "
            "top_color gray50, bottom_color gray50, left_color gray50, right_color gray50",
            num_format_str = "€_#,##0.00")
        
        for data in self.budget_id.budget_line_ids:
            budget_phase_ids = self.env['job.costing'].search(
                [('project_id', '=', self.id), ('activity_id', '=', data.job_type_id.id)]).mapped(
                'id')
            domain = [('project_id', '=', self.id), ('work_type_id', '=', data.job_type_id.id),
                      ('sub_category_id', '=',
                       data.sub_category_id.id), ('state', '=', 'complete'),
                      ('job_sheet_id', 'in', budget_phase_ids)]
            material_spent_rec = self.env['order.material.line'].search(domain)
            equip_spent_rec = self.env['order.equipment.line'].search(domain)
            labour_spent_rec = self.env['order.labour.line'].search(domain)
            overhead_spent_rec = self.env['order.overhead.line'].search(domain)
            sheet_name = data.sub_category_id.name
            sheet = workbook.add_sheet(sheet_name, cell_overwrite_ok=True)
            sheet.show_grid = False
            row = 0
            sheet.row(4).height = 400
            sheet.row(6).height = 400
            sheet.write_merge(0, 2, 0, 6, sheet_name, title)
            sheet.write(4, 0, "Budget totale", sub_title2)
            # sheet.write(4, 1, (str(self.budget_id.currency_id.symbol) +
            #                    " " + str(data.budget)), sub_title_amount)
            sheet.write(4, 1, (data.budget), f15_euro_value)
            sheet.write_merge(4, 4, 3, 4, "Ammontare Budget utilizzato", sub_title2)
            # sheet.write_merge(4, 4, 5, 6, (str(self.budget_id.currency_id.symbol) +
            #                                " " + str((data.budget - data.remaining_budget))),
            #                   sub_title_amount)
            sheet.write_merge(4, 4, 5, 6, (data.budget - data.remaining_budget), f15_euro_value)
            sheet.write_merge(6, 6, 3, 4, "Budget rimanente", sub_title2)
            # sheet.write_merge(6, 6, 5, 6, (str(self.budget_id.currency_id.symbol) +
            #                                " " + str(data.remaining_budget)), sub_title_amount)
            sheet.write_merge(6, 6, 5, 6, (data.remaining_budget), f15_euro_value)
            row = 5
            # Material Rec
            sheet.write_merge(row + 4, row + 5, 0, 4, "Materiale speso", title2)
            # sheet.write_merge(row + 4, row + 5, 5, 6, (str(self.budget_id.currency_id.symbol) +
            #                                            " " + str(data.material_spent)), title3)
            sheet.write_merge(row + 4, row + 5, 5, 6, (data.material_spent), f15_euro_value)
            
            sheet.col(0).width = 8000
            sheet.col(1).width = 8000
            sheet.col(2).width = 6500
            sheet.col(3).width = 5000
            sheet.col(4).width = 5000
            sheet.col(5).width = 5000
            sheet.col(6).width = 5000
            sheet.row(row + 6).height = 600
            sheet.write(row + 6, 0, "Fase del Progetto (WBS)", sub_title)
            sheet.write(row + 6, 1, "Ordine di Lavoro", sub_title)
            sheet.write(row + 6, 2, "Materiali", sub_title)
            sheet.write(row + 6, 3, "Qta.", line_amount_sub_title)
            sheet.write(row + 6, 4, "Unita", sub_title)
            sheet.write(row + 6, 5, "Prezzo cad.", line_amount_sub_title)
            sheet.write(row + 6, 6, "Importo Totale", line_amount_sub_title)
            row = row + 7
            for rec in material_spent_rec:
                sheet.row(row).height = 400
                sheet.write(row, 0, rec.job_sheet_id.name, line_values)
                sheet.write(row, 1, rec.job_order_id.name, line_values)
                sheet.write(row, 2, rec.name, line_values)
                sheet.write(row, 3, rec.qty, line_amount_sub_title)
                sheet.write(row, 4, rec.uom_id.name, line_values)
                # sheet.write(row, 5, (str(self.budget_id.currency_id.symbol) +
                #                      " " + str(rec.price)), line_amount_sub_title)
                sheet.write(row, 5, (rec.price), f15_euro_value)
                # sheet.write(row, 6, (str(self.budget_id.currency_id.symbol) +
                #                      " " + str(rec.total_price)), line_amount_sub_title)
                sheet.write(row, 6, (rec.total_price), f15_euro_value)
                row = row + 1
            sheet.write_merge(row, row, 0, 6, " ", horiz_double_line)
            row = row + 1

            # Equipment Rec
            sheet.write_merge(row + 1, row + 2, 0, 4,
                              "Attrezzatura spesa", title2)
            # sheet.write_merge(row + 1, row + 2, 5, 6, (str(self.budget_id.currency_id.symbol) +
            #                                            " " + str(data.equipment_spent)), title3)
            sheet.write_merge(row + 1, row + 2, 5, 6, (data.equipment_spent), f15_euro_value)
            row = row + 3
            sheet.row(row).height = 600
            sheet.write(row, 0, "Fase del progetto(WBS)", sub_title)
            sheet.write(row, 1, "Ordine di Lavoro", sub_title)
            sheet.write(row, 2, "Fornitore", sub_title)
            sheet.write(row, 3, "Attrezzatura", sub_title)
            sheet.write(row, 4, "Qta.", line_amount_sub_title)
            sheet.write(row, 5, "Prezzo cad", line_amount_sub_title)
            sheet.write(row, 6, "Sub Totale", line_amount_sub_title)
            row = row + 1
            for rec in equip_spent_rec:
                sheet.row(row).height = 400
                # sheet.write(row, 0, (rec.job_sheet_id.name +
                #                      " - " + rec.job_order_id.name), line_values)
                sheet.write(row, 0, (rec.job_order_id.name), line_values)
                # sheet.write(row, 1, (rec.job_order_id.name +
                #                      " - " + rec.job_order_id.name), line_values)
                sheet.write(row, 1, (rec.job_order_id.name), line_values)
                sheet.write(row, 2, rec.vendor_id.name, line_values)
                sheet.write(row, 3, rec.desc, line_values)
                sheet.write(row, 4, rec.qty, line_amount_sub_title)
                # sheet.write(row, 5, (str(self.budget_id.currency_id.symbol) +
                #                      " " + str(rec.cost)), line_amount_sub_title)
                # sheet.write(row, 6, (str(self.budget_id.currency_id.symbol) +
                #                      " " + str(rec.total_cost)), line_amount_sub_title)
                sheet.write(row, 5, (rec.cost), f15_euro_value)
                sheet.write(row, 6, (rec.total_cost), f15_euro_value)
                row = row + 1
            sheet.write_merge(row, row, 0, 6, " ", horiz_double_line)
            row = row + 1

            # Labour Rec
            sheet.write_merge(row + 1, row + 2, 0, 4, "Manodopera spesa", title2)
            # sheet.write_merge(row + 1, row + 2, 5, 6, (str(self.budget_id.currency_id.symbol) +
            #                                            " " + str(data.labour_spent)), title3)
            sheet.write_merge(row + 1, row + 2, 5, 6, (data.labour_spent), f15_euro_value)
            row = row + 3
            sheet.row(row).height = 600
            sheet.write(row, 0, "Fase del progetto(WBS)", sub_title)
            sheet.write(row, 1, "Ordine di Lavoro", sub_title)
            sheet.write(row, 2, "Fornitore", sub_title)
            sheet.write(row, 3, "Prodotto", sub_title)
            sheet.write(row, 4, "Ore", line_amount_sub_title)
            sheet.write(row, 5, "Costo Orario", line_amount_sub_title)
            sheet.write(row, 6, "Sub Totale", line_amount_sub_title)
            row = row + 1
            for rec in labour_spent_rec:
                sheet.row(row).height = 400
                sheet.write(row, 0, rec.job_sheet_id.name, line_values)
                sheet.write(row, 1, rec.job_order_id.name, line_values)
                sheet.write(row, 2, rec.vendor_id.name, line_values)
                sheet.write(row, 3, rec.name, line_values)
                sheet.write(row, 4, rec.hours, line_amount_sub_title)
                # sheet.write(row, 5, (str(self.budget_id.currency_id.symbol) +
                #                      " " + str(rec.cost)), line_amount_sub_title)
                # sheet.write(row, 6, (str(self.budget_id.currency_id.symbol) +
                #                      " " + str(rec.sub_total)), line_amount_sub_title)
                sheet.write(row, 5, (rec.cost),f15_euro_value)
                sheet.write(row, 6, (rec.sub_total), f15_euro_value)
                row = row + 1
            sheet.write_merge(row, row, 0, 6, " ", horiz_double_line)
            row = row + 1

            # Overhead Rec
            sheet.write_merge(row + 1, row + 2, 0, 4, "Spese generali ", title2)
            # sheet.write_merge(row + 1, row + 2, 5, 6, (str(self.budget_id.currency_id.symbol) +
            #                                            " " + str(data.overhead_spent)), title3)
            sheet.write_merge(row + 1, row + 2, 5, 6, (data.overhead_spent), f15_euro_value)
            row = row + 3
            sheet.row(row).height = 600
            sheet.write(row, 0, "Fase del progetto(WBS)", sub_title)
            sheet.write(row, 1, "Ordine di Lavoro", sub_title)
            sheet.write(row, 2, "Fornitore", sub_title)
            sheet.write(row, 3, "Prodotto", sub_title)
            sheet.write(row, 4, "Qta", line_amount_sub_title)
            sheet.write(row, 5, "Prezzo cad.", line_amount_sub_title)
            sheet.write(row, 6, "Sub Totale", line_amount_sub_title)
            row = row + 1
            for rec in overhead_spent_rec:
                sheet.row(row).height = 400
                # sheet.write(row, 0, (rec.job_sheet_id.name +
                #                      " - " + rec.job_order_id.name), line_values)
                # sheet.write(row, 1, (rec.job_order_id.name +
                #                      " - " + rec.job_order_id.name), line_values)
                sheet.write(row, 0, rec.job_order_id.name, line_values)
                sheet.write(row, 1, rec.job_order_id.name, line_values)
                sheet.write(row, 2, rec.vendor_id.name, line_values)
                sheet.write(row, 3, rec.name, line_values)
                sheet.write(row, 4, rec.qty, line_amount_sub_title)
                # sheet.write(row, 5, (str(self.budget_id.currency_id.symbol) +
                #                      " " + str(rec.cost)), line_amount_sub_title)
                # sheet.write(row, 6, (str(self.budget_id.currency_id.symbol) +
                #                      " " + str(rec.sub_total)), line_amount_sub_title)
                sheet.write(row, 5, (rec.cost), f15_euro_value)
                sheet.write(row, 6, (rec.sub_total), f15_euro_value)
                row = row + 1
            sheet.write_merge(row, row, 0, 6, " ", horiz_double_line)
            row = row + 1