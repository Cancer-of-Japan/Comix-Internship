from time import sleep
import requests
import gspread
import json 
import time
import math
from oauth2client.service_account import ServiceAccountCredentials

### Open spread sheet
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/spreadsheets']

#Google Spreadsheet API
credentials = ServiceAccountCredentials.from_json_keyfile_name('hybrid-chess-327705-9b1124e8db38.json', scope)

gc = gspread.authorize(credentials)


#KEY of spreadsheet we use
SPREADSHEET_KEY_MASTER = '1K_VtTBEdDGXuTNcqX8OrdR-LUmgAhqFjWv56CaSGDu0'
SPREADSHEET_KEY_CHILD = '1dcktFcIv6SyZtP1npbfCGmXl7ulZSvK61EjXpVkaQ-w'

#Into work-able condition
Master_Worksheet = gc.open_by_key(SPREADSHEET_KEY_MASTER).sheet1
Child_Worksheet = gc.open_by_key(SPREADSHEET_KEY_CHILD).sheet1
#Child_Worksheet = Child_Worksheet.worksheet('シート1')

val = Master_Worksheet.row_values(745)
print(val)
Child_Worksheet.update_cell(96,1, val[2])

i = 1
check = False
while check == False:
    i += 1
    import_val = str(Master_Worksheet.cell(i,2).value)
    if import_val == '':
        check = True
print(i)
