#Code that extracts Master data to local csv
from time import sleep
import requests
import gspread
import json 
import time
import math
import csv
from oauth2client.service_account import ServiceAccountCredentials

### Open spread sheet
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/spreadsheets']

# Google Spreadsheet API
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

filename = 'Master.csv'
f = open(filename, 'w')
headers = 'No.,	紹介サービス,	紹介者,	被紹介者,	従業員数,	担当,	ベンダー打診日,	判断,	商談日,	リマインド,	成果確定日,	成功報酬対象金額, 備考'
f.write(headers)

master_data = Master_Worksheet.get('A3:I752')
# print(master_data)
# f.write(master_data)

print(master_data[1])



for i in range(len(master_data)):
    val = str(master_data[i])
    f.write(val + '\n')
    print(val)

