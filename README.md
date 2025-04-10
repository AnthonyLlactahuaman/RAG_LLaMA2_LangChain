# RAG_LLaMA2_LangChain

# 🤖 PDF Chatbot con LLaMA 2 y LangChain

<img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python">
<img src="https://img.shields.io/badge/LangChain-0.2+-orange?logo=python">
<img src="https://img.shields.io/badge/Offline-100%25-green">

## 📚 ¿Qué hace este proyecto?

Este proyecto te permite **hacer preguntas en lenguaje natural sobre documentos PDF** locales usando un **modelo de lenguaje LLaMA 2** en formato **GGUF**, ejecutado totalmente **offline** mediante **LangChain** y **GPT4All**.

### ⚙️ ¿Cómo funciona?

1. 📂 Carga automáticamente todos los archivos PDF en `data/pdfs`.
2. ✂️ Divide el contenido en fragmentos manejables.
3. 🧠 Genera embeddings locales con un modelo de HuggingFace (`MiniLM`).
4. 🧠 Carga un modelo LLaMA 2 (`.gguf`) para generar respuestas.
5. 🤖 Puedes hacer preguntas desde consola ¡y obtener respuestas contextuales!

---

## 🛠️ Requisitos

- Python `>=3.10`
- Windows, Linux o macOS
- ~8 GB RAM (mínimo recomendado)
- Modelo `.gguf` descargado localmente

---

## 🚀 Cómo usar este proyecto

### 1. 🔽 Clona el repositorio

```bash
git clone https://github.com/tu-usuario/pdf-chatbot-llama2.git
cd pdf-chatbot-llama2
```

### 2. 🐍 Crea un entorno virtual

```bash
python -m venv venv
venv\\Scripts\\activate  # en Windows
# o
source venv/bin/activate  # en Linux/macOS
```

### 3. 📦 Instala las dependencias
```bash
pip install -r requirements.txt
```

### 4. 📁 Descarga un modelo LLaMA 2 (.gguf)
Ve a 👉 [TheBloke LLaMA 2 Chat GGUF](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/tree/main)

Descarga el archivo:
llama-2-7b-chat.Q4_K_M.gguf

Colócalo en la carpeta:
models/

### 5. 📄 Coloca tus PDFs
Guarda tus archivos .pdf en esta carpeta:
data/pdfs/

### 6. ▶️ Ejecuta el chatbot
```bash
python main.py
```
---
## 🌈 Interfaz de consola
Título en ASCII con pyfiglet 🎨

Preguntas y respuestas con colores gracias a termcolor

## 🧠 Créditos
[LangChain](https://python.langchain.com/docs/introduction/)

[GPT4All](https://www.nomic.ai/gpt4all)

[TheBloke GGUF models](https://huggingface.co/TheBloke)
