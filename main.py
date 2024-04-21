from fastapi import FastAPI, HTTPException
from pydantic import ValidationError
import pdfminer
import re

app = FastAPI()

document_directory = "documents"

@app.post("/correct-formulario")
async def correct_formulario(document: Document):
    try:
        # Procesar el documento PDF
        pdf_file = document.file.read()
        pdfminer_handler = pdfminer.PDFHandler(pdf_file)
        text = ""
        for page in pdfminer_handler.get_pages():
            text += page.extractText()

        # Extraer conocimiento relevante del texto
        knowledge = extract_knowledge(text)

    except Exception as e:
        return {"error": str(e)}

    # Corregir el formulario con el conocimiento extraído
    formulario_corregido = correct_formulario(knowledge)

    # Almacenar el documento procesado en el directorio de documentos
    with open(document_directory + "/" + document.file.filename, "wb") as f:
        f.write(pdf_file.read())

    return formulario_corregido

def extract_knowledge(text: str) -> dict:
    knowledge = {}

    # Extraer campo1 y valor1
    pattern = r"Campo 1: (.+)"
    match = re.search(pattern, text)
    if match:
        knowledge["campo1"] = match.group(1)

    # Extraer campo2 y valor2
    pattern = r"Campo 2: (.+)"
    match = re.search(pattern, text)
    if match:
        knowledge["campo2"] = match.group(1)

    # ... extraer otros campos y valores relevantes

    return knowledge

def correct_formulario(knowledge: dict) -> Formulario:
    formulario_corregido = Formulario()

    # Corregir campo1
    if "campo1" in knowledge:
        formulario_corregido.campo1 = knowledge["campo1"]

    # Corregir campo2
    if "campo2" in knowledge:
        formulario_corregido.campo2 = knowledge["campo2"]

    # ... corregir otros campos del formulario

    return formulario_corregido
