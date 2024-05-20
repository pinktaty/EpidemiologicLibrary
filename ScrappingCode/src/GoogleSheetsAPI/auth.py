from __future__ import print_function
from googleapiclient.discovery import build
from google.oauth2 import service_account


SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

# credentials.json document missing in Github for safety reasons,
# these are credentials of a service account to connect with Google's APIs
credentials = service_account.Credentials.from_service_account_file('credentials.json', scopes=SCOPES)

spreadsheet_service = build('sheets', 'v4', credentials=credentials)
drive_service = build('drive', 'v3', credentials=credentials)