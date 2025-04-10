"""
Genera embeddings usando un modelo local de Hugging Face.
"""

from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


def create_vector_store(documents):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectordb = Chroma.from_documents(documents, embedding=embeddings, persist_directory="vectordb")
    return vectordb