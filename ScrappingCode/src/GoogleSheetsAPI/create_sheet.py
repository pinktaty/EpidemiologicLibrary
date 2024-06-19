from __future__ import print_function
import sys
import json
from auth import spreadsheet_service
from auth import drive_service

def create_sheet(sheet_name):
    spreadsheet_details = {
        'properties': {
            'title': sheet_name
        }
    }
    sheet = spreadsheet_service.spreadsheets().create(body=spreadsheet_details,
                                                      fields='spreadsheetId').execute()
    sheet_id = sheet.get('spreadsheetId')
    print('Spreadsheet ID: {0}'.format(sheet_id))
    permission1 = {
        'type': 'user',
        'role': 'writer',
        'emailAddress': '<EMAILHERE>' # Email of the account that will be able to write in the sheet
    }
    drive_service.permissions().create(fileId=sheet_id, body=permission1).execute()
    return sheet_id

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python create_sheet.py <SPREADSHEET_NAME>")
        sys.exit(1)
    create_sheet(sys.argv[1])