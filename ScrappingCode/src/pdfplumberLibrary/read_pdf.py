from __future__ import print_function
import sys
import pdfplumber

def transform_table(table):
    return ' '.join(' '.join(map(str, row)) for row in table)

def read_pdf(pdf_file_name, page, extract_tables):
    try:
        page = int(page)
    except ValueError:
        print("The second argument must be an integer representing the page number.")
        sys.exit(1)
    try:
        extract_tables = bool(extract_tables)
    except ValueError:
        print("Third argument must be a boolean.")
        sys.exit(1)
    with pdfplumber.open(pdf_file_name + '.pdf') as pdf:
        if page < 0:
            print("Page must be positive or 0.")
            sys.exit(1)
        elif page > len(pdf.pages):
            print("Page must be less or equal to the number of pages in the pdf.")
            sys.exit(1)
        if extract_tables == True:
            table = pdf.pages[page].extract_tables()
            return transform_table(table)
        elif extract_tables == False:
            text = pdf.pages[page].extract_text_simple()
            if text:
                return text
            else:
                print("No text found on the page.")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python readpdf.py <PDF_FILE_NAME, PAGE, EXTRACT_TABLES (True or False)>")
        sys.exit(1)
    print(read_pdf('../../sources/' + sys.argv[1], sys.argv[2], sys.argv[3]))