import gspread
from google.oauth2.service_account import Credentials

SCOPES = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file"]

creds = Credentials.from_service_account_file('./data-shard-299711-2f935e547ba6.json', scopes=SCOPES)

gc = gspread.authorize(creds)

spreadsheet = gc.open_by_key("1Q-HxgkROVwWlGfGQ5a5KalL2eP056XoIx1eunRJc4_s")

worksheet = spreadsheet.sheet1

worksheet.update('A1', [['Hello, Google Sheets!']])

worksheet.append_row(['Dữ liệu 1', 'Dữ liệu 2', 'Dữ liệu 3'])
