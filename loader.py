"""
Carga todos los archivos PDF de una carpeta y los divide en fragmentos de texto.
"""

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFDirectoryLoader


def load_and_split_pdfs(folder_path):
    loader = PyPDFDirectoryLoader(folder_path)
    documents = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    return splitter.split_documents(documents)