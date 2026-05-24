from langchain_community.document_loaders import PyPDFLoader

from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain_community.embeddings import HuggingFaceEmbeddings

from langchain_community.vectorstores import Chroma

import os

# -----------------------------------
# PDF PATH
# -----------------------------------

PDF_PATH = "documents/medical_book.pdf"

# -----------------------------------
# LOAD PDF
# -----------------------------------

loader = PyPDFLoader(PDF_PATH)

documents = loader.load()

print(f"Loaded {len(documents)} pages")

# -----------------------------------
# SPLIT DOCUMENTS
# -----------------------------------

text_splitter = RecursiveCharacterTextSplitter(

    chunk_size=500,
    chunk_overlap=50

)

docs = text_splitter.split_documents(documents)

print(f"Created {len(docs)} chunks")

# -----------------------------------
# EMBEDDING MODEL
# -----------------------------------

embedding_model = HuggingFaceEmbeddings(

    model_name="sentence-transformers/all-MiniLM-L6-v2"

)

# -----------------------------------
# CREATE VECTOR DATABASE
# -----------------------------------

vector_db = Chroma.from_documents(

    docs,
    embedding_model,
    persist_directory="vector_store"

)

print("Vector Database Created Successfully")