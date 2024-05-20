from __future__ import print_function
import sys
from auth import drive_service
import googleapiclient.errors

def delete(sheet_id):
    try:
        drive_service.files().delete(fileId=sheet_id).execute()
        print(f'Spreadsheet with ID {sheet_id} deleted successfully.')
    except googleapiclient.errors.HttpError as error:
        print(f'An error occurred: {error}')
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python deletesheet.py <SPREADSHEET_ID>")
        sys.exit(1)
    spreadsheet_id = sys.argv[1]
    delete(spreadsheet_id)