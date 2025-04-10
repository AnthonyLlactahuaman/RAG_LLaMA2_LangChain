# llm.py
"""
Carga un modelo LLaMA 2 local usando GPT4All (sin parámetros adicionales).
"""
from langchain_community.llms import GPT4All


def load_llm(model_path):
    return GPT4All(
        model=model_path,
        verbose=True
    )
