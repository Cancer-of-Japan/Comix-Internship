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
SPREADSHEET_KEY_CHILD_1 = '1dcktFcIv6SyZtP1npbfCGmXl7ulZSvK61EjXpVkaQ-w'
SPREADSHEET_KEY_CHILD_2 = '1VqVgJoRiXVn7mq8gh02F1BFPClnQ61wOJWGcfiLoSrE'

#Into work-able condition
Master_Worksheet = gc.open_by_key(SPREADSHEET_KEY_MASTER).sheet1
Child_Worksheet = gc.open_by_key(SPREADSHEET_KEY_CHILD_1).sheet1
Kid_Worksheet = gc.open_by_key(SPREADSHEET_KEY_CHILD_2).sheet1
#Child_Worksheet = Child_Worksheet.worksheet('シート1')

val = Master_Worksheet.get_all_values()
print(val)
Child_Worksheet.update_cell(96,1, val[2])

i = 748
check = False
chk_list = ["Child", "Kid"]
key_list = [Child_Worksheet, Kid_Worksheet]



# while check == False:
#     i += 1
#     import_val = str(Master_Worksheet.cell(i,4).value)
#     print(import_val)
    
# #Loop to check each company
#     inner_check = False
#     while inner_check == False:
#         import_val = str(Master_Worksheet.cell(i,4).value)
#         x = 0
#         if import_val == chk_list[x]:
#             print('found')
#             child_chk = 3
#             sample = str(key_list[x].cell(3,3).value)
#             print(sample)
#             while str(key_list[x].cell(child_chk,3).value) != 'None':
#                 child_chk += 1
#             sleep(1)
#             upd_customer = Master_Worksheet.cell(i,4).value
#             sleep(1)
#             upd_intr_day = Master_Worksheet.cell(i,7).value 
#             sleep(1) 
#             upd_mtg_day = Master_Worksheet.cell(i,9).value

#             key_list[x].update_cell(child_chk,3,upd_customer)
#             key_list[x].update_cell(child_chk,4,upd_intr_day)
#             key_list[x].update_cell(child_chk,5,upd_mtg_day)


#             if import_val == 'None':
#                 inner_check == True
#                 x += 1
#         if import_val == 'None':
#             check = True

#     if import_val == 'None':
#         check = True
# print(i)
