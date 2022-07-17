import gspread

from credentials import credentials, table, sheet

connect_json = gspread.service_account_from_dict(credentials)

sheet_google = connect_json.open_by_url(table)
sheet_products = sheet_google.worksheet(sheet)