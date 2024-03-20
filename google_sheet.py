import time
import gspread 
from google.oauth2.service_account import Credentials
# from oauth2client.service_account import ServiceAccountCredentials
from oauth2client.service_account import ServiceAccountCredentials
import json

scopes = [
    "https://www.googleapis.com/auth/spreadsheets"
    ]

# cred = Credentials.from_service_account_file('keys.json',scopes = scopes)
scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
cred = ServiceAccountCredentials.from_json_keyfile_name('keys.json', scope)

client = gspread.authorize(cred)


sheet_id = '1uqbCj754ZmtzetUnS7jrMOELNbbiayyBSTfR3mtTFpQ' 
workBook = client.open_by_key(sheet_id)



worksheet_list = map(lambda x:x.title , workBook.worksheets())


def update_google_sheet (row,data,range_to_clear,sheetname = 'Hello World'):
    try:
        sheet = workBook.worksheet(sheetname)
        values = data.values.tolist()
      
        time.sleep(0.5)
        sheet.batch_clear([range_to_clear])
        time.sleep(0.05)
        sheet.update(row, values)
    except Exception as e:
     print(f"update_google_sheet test -------------->>>>{e}")




    
def update_cell(cell,data,sheetname):
  
    try:
        sheet = workBook.worksheet(sheetname)
        # import time
        time.sleep(1)
        sheet.update(cell,[[data]])
    except Exception as e:
     print(f"update cell  -------------->>>>{e}")



def clean_up (range_to_clear,sheetname = 'Hello World'):
    try:
        sheet = workBook.worksheet(sheetname)  
        time.sleep(1)  
        sheet.batch_clear([range_to_clear])
    except Exception as e:
     print(f"clean_up  -------------->>>>{e}")




