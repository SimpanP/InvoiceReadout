import pymongo
from pymongo import MongoClient
import dns
from gridfs import GridFS

cluster = pymongo.MongoClient("mongodb+srv://SimFil:Sommar2021@cluster0.k6mlfru.mongodb.net/?retryWrites=true&w=majority")
db = cluster["invoiceReader"]
collection = db["invoiceReader"]


# Create a GridFS object
fs = GridFS(db)

def upload_pdf(file_path, filename):
    # Open the PDF file in binary mode
    with open(file_path, 'rb') as pdf_file:
        # Store the file in GridFS
        pdf_id = fs.put(pdf_file, filename=filename)
    
    return pdf_id

def download_pdf(pdf_id, destination_path):
    try:
        # Retrieve the PDF file from GridFS
        with open(destination_path, 'wb') as pdf_file:
            fs.get(pdf_id).readinto(pdf_file)
    except NoFile:
        print(f"No file found with id: {pdf_id}")