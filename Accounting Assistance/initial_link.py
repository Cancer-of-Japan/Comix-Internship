from time import sleep
import requests
import gspread
import json 
import time
import math
from oauth2client.service_account import ServiceAccountCredentials

### Open spread sheet
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/authdrive','https://www.googleapis.com/spreadsheets']

#Google Spreadsheet API
credentials = ServiceAccountCredentials.from_json_keyfile_name('comix-accountant-2d6990a32334.json', scope)

gc = gspread.authorize(credentials)


#KEY of spreadsheet we use
SPREADSHEET_KEY = '1K_VtTBEdDGXuTNcqX8OrdR-LUmgAhqFjWv56CaSGDu0'
#SPREADSHEET_KEY_CHILD = '1dcktFcIv6SyZtP1npbfCGmXl7ulZSvK61EjXpVkaQ-w'

#Into work-able condition
Master_Worksheet = gc.open_by_key(SPREADSHEET_KEY).sheet1
#Child_Worksheet = gc.open_by_key(SPREADSHEET_KEY_CHILD).sheet1
#Child_Worksheet = Child_Worksheet.worksheet('シート1')





