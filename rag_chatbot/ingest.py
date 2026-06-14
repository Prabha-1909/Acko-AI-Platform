import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings



pdf_folder = "../data/policy_data"

documents = []

print("PDF Folder:", pdf_folder)
print("Files:", os.listdir(pdf_folder))

for file in os.listdir(pdf_folder):

    if file.endswith(".pdf"):

        print(f"Loading PDF: {file}")

        pdf_path = os.path.join(pdf_folder, file)

        loader = PyPDFLoader(pdf_path)

        documents.extend(loader.load())


print(f"\nLoaded {len(documents)} pages")


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=100
)

chunks = text_splitter.split_documents(documents)

print(f"Created {len(chunks)} chunks")



embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)



db = Chroma.from_documents(
    documents=chunks,
    embedding=embedding,
    persist_directory="../vectorstore"
)

print("\nVector DB created successfully!")