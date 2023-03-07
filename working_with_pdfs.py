'''
Several functions for working with PDFs in python
1. Read Metadata
2. Extract data from pdf
3. Split pdfs into individual pages
4. Split PDFs at a particular page
5. Get the last page of a PDF
6. Merge several PDFs
7. Rotate PDF at a particular page for particular angle
8. Rotate first page
9. Encrypt pdf
'''
**********************************************************************************************************

from PyPDF2 import PdfReader, PdfWriter
import os
**********************************************************************************************************
#Reading metadata w/out a function
file = open('fraility.pdf', 'rb')
reader = PdfReader(file)  
info = reader.metadata
print(len(reader.pages))

print(reader.pages[0].extract_text())
**********************************************************************************************************
#function to get pdf metadata and number of pages
def get_pdf_metadata(pdf_path):
    with open(pdf_path, 'rb') as f:
        reader = PdfReader(f)
        info = reader.metadata
        no_of_pages = len(reader.pages)
    return info, no_of_pages

meta, pages = get_pdf_metadata("pdf_path")
*******************************************************************************************************
#function to read extaract text from pages
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as f:
        reader = PdfReader(f)
        results = []
        for i in range(0, len(reader.pages)):
           selected_page = reader.pages[i]
           text = selected_page.extract_text()
           results.append(text)
        return ' '.join(results) #converts list to string

print(extract_text_from_pdf(pdf_path))
***********************************************************************************************************************


#function to split pdf to individual pages

def split_pdf(pdf_path):
    with open(pdf_path, 'rb') as f:
        reader = PdfReader(f)
        #loop tthrough all pages
        for page_num in range(0, len(reader.pages)):
            selected_page = reader.pages[page_num]
            #writer to write
            writer = PdfWriter()
            writer.add_page(selected_page)
            filename = os.path.splitext(pdf_path)[0]
            output_filename = f"{filename}{page_num + 1}.pdf"
            
            #save and compile to pdf
            with open(output_filename, "wb") as out:
                writer.write(out)
                
            print('created a pdf:{}' .format(output_filename))

split_pdf(pdf_path)
*****************************************************************************************************************************
#To split upto a particular page
def get_pdf_upto(pdf_path, start_page: int=0,stop_page: int = 0, output_path="output"):
    with open(pdf_path, "rb") as f:
        reader = PdfReader(f)
        writer = PdfWriter()
        for page_num in range(start_page, stop_page):
            selected_page = reader.pages[page_num]
            writer.add_page(selected_page)
            filename = os.path.splitext(pdf_path)[0]
            output_filename = f"{filename} from {start_page} to {stop_page}.pdf"
        with open(output_filename, 'wb') as out:
            writer.write(out)


get_pdf_upto(pdf_path, 0,4)
******************************************************************************************************************************
#to get the last page of pdf
def get_last_page(pdf_path):
    with open(pdf_path, "rb") as f:
        reader = PdfReader(f)
        writer = PdfWriter()
        last_page = len(reader.pages) - 1
        selected_page = reader.pages[last_page]
        writer.add_page(selected_page)
        filename = os.path.splitext(pdf_path)[0]
        output_filename = f"{filename}_last_page.pdf"
        with open(output_filename, "wb") as out:
            writer.write(out)



get_last_page(pdf_path)
*****************************************************************************************************************************
#how to merge pdfs
#get list of pdfs you want to work on
#Use pdf file merger

#to fetch all pdfs:
def fetch_all_pdf_files(parent_folder):
    target_files = []
    for path, subdirs, files in os.walk(parent_folder):
        for name in files:
            if name.endswith(".pdf"):
                target_files.append(os.path.join(path, name))
    return target_files

print(fetch_all_pdf_files(pdf_path))
**********************************************************************************************************************************
#to merge
#merges in the order the pdfs appear on lists
from PyPDF2 import PdfMerger
def merge_pdf(list_of_pdfs, output_filename="merger.pdf"):
    merger = PdfMerger()
    with open(output_filename, "wb") as f:
        for file in list_of_pdfs:
            merger.append(file)
            
        merger.write(f)
pdf_list = fetch_all_pdf_files(pdf_path)
merge_pdf(pdf_1, pdf_2)
*************************************************************************************************************************************

#to rotate pdfs
def rotate_pdf(pdf_path, page_num: int, rotation: int = 90):
    with open(pdf_path, "rb") as f:
        reader = PdfReader(f)
        num_pages = len(reader.pages)
        if page_num < 0 or page_num >= num_pages:
            print(f"Error: page number {page_num} is out of range (0 - {num_pages-1})")
            return
        writer = PdfWriter()
        writer.add_page(reader.pages[page_num])
        #rotate
        writer.pages[0].rotate = rotation
        filename = os.path.splitext(pdf_path)[0]
        output_filename = f"{filename}_{page_num}_{rotation}_rotated.pdf"
        with open(output_filename, "wb") as out:
            writer.write(out)
        print(f"Rotated page {page_num}!")


rotate_pdf(pdf_path, page,angle)

file_to_rotate = open("doc_to_rotate.pdf", "rb")
reader = PdfReader(file_to_rotate)
**************************************************************************************************************************************
#assume we wish to rotate the first page
page = reader.pages[0]
#rotate 90 
page.rotate(90)

writer = PdfWriter()
writer.add_page(page)
#the resulting pdf has one page which we save it
result = open('rotatedpage.pdf', 'wb')
writer.write(result)

result.close()
file_to_rotate.close()

************************************************************************************************************************8
#to add an encryption
secret = open('pdf_to_encrypt.pdf', 'rb')
reader = PdfReader(secret)
writer = PdfWriter()

for page_num in range(len(reader.pages)):
    page = reader.pages[page_num]
    writer.add_page(page)
    
#first arg[user password: viewing]
#second arg[owner password]: print, comment, extaract text
#If only one string argument is passed to encrypt(), 
#it will be used for both passwords. 
#password is swordfish

writer.encrypt('swordfish')
encryptedDoc = open('encrypteddoc.pdf', 'wb')
writer.write(encryptedDoc)

secret.close()
encryptedDoc.close()
******************************************************************************************************************************
#Combining two pdfs into one
#open both files in read binary
march_pdf = open("minutes1.pdf", 'rb')
jan_pdf = open('minutes2.pdf', 'rb')



#PDF reader object for both pdfs
reader_march = PdfReader(march_pdf)
reader_jan = PdfReader(jan_pdf)

#pdf writer object for blank pdf
new_pdf = PdfWriter()

#copy all pages from the two pdfs to a write object
#Loop through the pages march and jan pdf

for page_num in range(len(reader_jan.pages)):
    #get the page object for the current page
    
    page = reader_jan.pages[page_num]
    
    #add the page object to the PDF writer object
    new_pdf.add_page(page)
    
for page_num in range(len(reader_march.pages)):
    #get the page object for the current page
    
    page = reader_march.pages[page_num]
    
    #add the page object to the PDF writer object
    new_pdf.add_page(page)
    
output_file = open("combined_minutes.pdf", "wb")
new_pdf.write(output_file)
output_file.close()

march_pdf.close()
jan_pdf.close()



