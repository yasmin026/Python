from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

#Inicializando a aplicação FastAPI  
app = FastAPI(
    title = "Minha API de Catálogo",
    description ="Una API simples criada com FastAPI para portofólio",
    version = "1.0.0"
)


