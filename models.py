from fastapi import FastAPI, UploadFile
from pydantic import BaseModel
import pdfminer
import re

app = FastAPI()

class Document(BaseModel):
    file: UploadFile

class Formulario(BaseModel):
    campo1: str
    campo2: str
    # ... otros campos del formulario
