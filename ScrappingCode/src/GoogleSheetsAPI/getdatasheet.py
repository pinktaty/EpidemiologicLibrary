from __future__ import print_function
import sys
from auth import spreadsheet_service

# TO CHECK
def get_data_sheet(range_name, spreadsheet_id):
    result = spreadsheet_service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id, range=range_name).execute()
    rows = result.get('values', [])
    print('{0} rows retrieved.'.format(len(rows)))
    print('{0} rows retrieved.'.format(rows))
    return rows

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python getdata.py <SPREADSHEET_RANGE, SPREADSHEET_ID>")
        sys.exit(1)
    get_data_sheet(sys.argv[1], sys.argv[2])