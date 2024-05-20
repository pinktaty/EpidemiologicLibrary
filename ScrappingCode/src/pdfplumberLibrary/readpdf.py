from __future__ import print_function
import sys
import pdfplumber

def read_pdf(pdf_file_name):
    with pdfplumber.open('../../sources/' + pdf_file_name + '.pdf') as pdf:
        # To finish: extract and return text.

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python readpdf.py <PDF_FILE_NAME>")
        sys.exit(1)
    read_pdf(sys.argv[1])