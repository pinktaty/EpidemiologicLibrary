from __future__ import print_function
import sys
from auth import spreadsheet_service
from auth import drive_service

def create(sheet_name):
    spreadsheet_details = {
        'properties': {
            'title': sheet_name
        }
    }
    sheet = spreadsheet_service.spreadsheets().create(body=spreadsheet_details,
                                                      fields='spreadsheetId').execute()
    sheetId = sheet.get('spreadsheetId')
    print('Spreadsheet ID: {0}'.format(sheetId))
    permission1 = {
        'type': 'user',
        'role': 'writer',
        'emailAddress': '<EMAILHERE>' # Email of the account that will be able to write in the sheet
    }
    drive_service.permissions().create(fileId=sheetId, body=permission1).execute()
    return sheetId

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python createsheet.py <SPREADSHEET_ID>")
        sys.exit(1)
    spreadsheet_name = sys.argv[1]
    create(spreadsheet_name)