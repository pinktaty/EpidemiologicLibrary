from __future__ import print_function
import sys
from auth import spreadsheet_service
from googleapiclient.errors import HttpError

# To add information in specific ranges of the sheet
def batch_update_values(spreadsheet_id, range_name, _values):
    try:

        values = _values
        data = [
            {"range": range_name, "values": values},
            # Additional ranges to update ...
        ]
        body = {"valueInputOption": "USER_ENTERED", "data": data}
        result = (
            spreadsheet_service.spreadsheets()
            .values()
            .batchUpdate(spreadsheetId=spreadsheet_id, body=body)
            .execute()
        )
        print(f"{(result.get('totalUpdatedCells'))} cells updated.")
        print(result)
        return result
    except HttpError as error:
        print(f"An error occurred: {error}")
        return error

# To add information at the end of a range or of the sheet
def append_values(spreadsheet_id, range_name, _values):
    try:
        values = _values
        body = {"values": values}
        result = (
            spreadsheet_service.spreadsheets()
            .values()
            .append(
                spreadsheetId=spreadsheet_id,
                range=range_name,
                valueInputOption="USER_ENTERED",
                body=body,
            )
            .execute()
        )
        print(f"{(result.get('updates').get('updatedCells'))} cells appended.")
        return result
    except HttpError as error:
        print(f"An error occurred: {error}")
    return error

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python write_data_sheet.py <SPREADSHEET_ID, SPREADSHEET_RANGE, VALUES>\n" +
              "SPREADSHEET_RANGE example: Sheet1!A1:D4 \n" +
              "VALUES example: [[value1, value2], [value3, value4], [value5, value6]]")
        sys.exit(1)
    batch_update_values(sys.argv[1], sys.argv[2], sys.argv[3:])