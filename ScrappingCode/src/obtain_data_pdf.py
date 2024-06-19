# Facade to obtain data from pdf.

from __future__ import print_function
from pdfplumberLibrary import read_pdf
from ChatGPTAPI import extract_info
from GoogleSheetsAPI import write_data_sheet

if __name__ == "__main__":
    pdf_name = input("Name of the pdf to scrap: ")
    pdf_page = input("Page to scrap from: ")
    pdf_tables = input("Do you want to scrap from tables in the page? (True or False) ")
    pdf_data = read_pdf.read_pdf('../sources/' + pdf_name, pdf_page, pdf_tables)
    print("The information extracted from the pdf is what follows:")
    print(pdf_data)

    instructions = input("Add the instructions to extract information: ")
    api_key_chatGPT = input("API key for Chat-GPT: ")
    data = extract_info.ask_chatGPT(pdf_data, api_key_chatGPT, instructions)
    print(data)

    connect_to_sheet = bool(input("Do you want to connect this information to a sheet from Google Sheets? (True or "
                                  "False) "))
    if connect_to_sheet:
        print("Make sure of adding your credentials.json document to the GoogleSheetsAPI folder.")
        help = bool(input("To add to a sheet the information must be in a format like this: [[value1, value2], "
                          "[value5, value6]]. Do you want help from ChatGPT to organize the information? (True or "
                          "False) "))
        if help:
            instructions_help = input("Add the instructions: ")
            values = extract_info.ask_chatGPT(data, api_key_chatGPT, instructions_help)
        else:
            values = input("Values (example [[value1, value2], [value5, value6]]): ")
        sheet_id = input("Sheet ID: ")
        sheet_range = input("Range (example Sheet1!A1:D4): ")
        write_data_sheet.batch_update_values(sheet_id, sheet_range, values)

    print("Goodbye!")