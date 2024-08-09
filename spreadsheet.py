import os
from openpyxl import Workbook, load_workbook, utils

def update_spreadsheet(path):
    if os.path.exists(path):
        # Spreadsheet exists then access it to update data
        wb = load_workbook(path)

        ws_name = "2024"
        if ws_name not in wb.sheetnames:
            raise Exception("Worksheet does not exist")
        ws = wb[ws_name]
    else:
        raise Exception("Spreadsheet does not exist")

    # Find first empty row in worksheet
    end_column = utils.column_index_from_string('K')

    for row in ws.iter_rows(min_row=1, max_col=end_column, max_row=200):
        if row[0].value is None:
                row_index = row[0].row
                ws[f'A{row_index}'] = 'SUCCESS'
                break

    # Save the spreadsheet
    wb.save(path)