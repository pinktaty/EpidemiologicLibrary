from __future__ import print_function
import sys
from auth import spreadsheet_service

# TO CHECK
def write_data_sheet(spreadsheet_id, range_name, values):
    value_input_option = 'USER_ENTERED'
    body = {
        'values': values
    }
    result = spreadsheet_service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id, range=range_name,
        valueInputOption=value_input_option, body=body).execute()
    print('{0} cells updated.'.format(result.get('updatedCells')))


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python writedata.py <SPREADSHEET_ID, SPREADSHEET_RANGE, VALUES>\n" +
              "SPREADSHEET_RANGE example: Sheet1!A1:D4 \n" +
              "VALUES example: [[value1, value2], [value3, value4], [value5, value6]]")
        sys.exit(1)
    write_data_sheet(sys.argv[1], sys.argv[2], sys.argv[3])