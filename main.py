"""
Archivo principal del proyecto. Ejecuta la carga de documentos, inicializa el modelo,
y permite hacer preguntas sobre los PDFs cargados localmente, con una interfaz de consola amigable.
"""
from loader import load_and_split_pdfs
from embeddings import create_vector_store
from llm import load_llm
from qa_chain import create_qa_chain
from pyfiglet import figlet_format
from termcolor import colored
import colorama
import os
import sys
import warnings

# Ocultar errores no perjudiciales
sys.stderr = open(os.devnull, 'w')
warnings.filterwarnings("ignore", category=DeprecationWarning)

colorama.init()

# Mostrar título en consola con pyfiglet y color
print(colored(figlet_format("PDF Chatbot", font="slant"), "cyan"))
print(colored("Haz preguntas sobre tus documentos locales con LLaMA 2\n", "green"))
print(colored("Espere un momento mientras carga el programa...\n", "green"))

# Paso 1: Cargar y dividir los documentos PDF
pdf_chunks = load_and_split_pdfs("data/pdfs")

# Paso 2: Crear base de vectores local con embeddings
vectordb = create_vector_store(pdf_chunks)

# Paso 3: Cargar el modelo LLaMA 2 local en formato GGUF
llm = load_llm("models/llama-2-7b-chat.Q4_K_M.gguf")

# Paso 4: Crear el QA chain con LangChain
qa = create_qa_chain(llm, vectordb)

# Paso 5: Interfaz de preguntas
while True:
    pregunta = input(colored("\n👉 Escribe tu pregunta o escribe 'salir' para cerrar: ", "yellow"))
    if pregunta.lower() == "salir":
        print(colored("\nGracias por usar el chatbot. ¡Hasta luego!", "magenta"))
        break
    respuesta = qa.run(pregunta)
    print(colored("\n💬 Respuesta:", "cyan"))
    print(colored(respuesta, "white"))
