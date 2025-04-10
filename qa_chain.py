"""
Crea una cadena de pregunta-respuesta usando RetrievalQA.
"""
from langchain.chains import RetrievalQA


def create_qa_chain(llm, vectordb):
    retriever = vectordb.as_retriever(search_kwargs={"k": 3})
    return RetrievalQA.from_chain_type(llm=llm, retriever=retriever, chain_type="stuff")