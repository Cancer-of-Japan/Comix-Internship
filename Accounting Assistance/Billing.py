#Code that based on initial_cav.py, creates billing csv
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
SPREADSHEET_KEY_SERVICE_AND_COMPANY = '1EZRQIo7hboKegdt9kEPJhNzgbGecYvftdCb3q2Yf0ao'

#Into work-able condition
Master_Worksheet = gc.open_by_key(SPREADSHEET_KEY_MASTER).sheet1
Child_Worksheet = gc.open_by_key(SPREADSHEET_KEY_CHILD_1).sheet1
Kid_Worksheet = gc.open_by_key(SPREADSHEET_KEY_CHILD_2).sheet1
Ref_Worksheet = gc.open_by_key(SPREADSHEET_KEY_SERVICE_AND_COMPANY).sheet1

file = open('Master.csv')
type(file)
csvreader = csv.reader(file)

for i in range(2,Ref_Worksheet.row_count):
    print(str(Ref_Worksheet.row_values(i)))
    company = (Ref_Worksheet.cell(i,1).value)
    service = (Ref_Worksheet.cell(i,2).value)
    print(company)
    print(service)
    service = " '" + str(service) + "'"
    for row in csvreader:
        print(str(row[1]) + ' ' + service)
        if str(row[1]) == str(service):
            print(True)
        else: print(False)
