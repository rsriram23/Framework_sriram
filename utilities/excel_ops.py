from openpyxl import load_workbook
from pathlib import Path


ROOT_PATH=Path(__file__).parent.parent

class ExcelOperations:

    def get_data_from_users_excel(self):
        # reading from excel
        wbook = load_workbook(fr'{ROOT_PATH}\testdata\users.xlsx')
        wsheet = wbook.active

        username = wsheet.cell(2, 1).value
        pwd = wsheet.cell(2, 2).value
        print(username, pwd)
        return username, pwd
