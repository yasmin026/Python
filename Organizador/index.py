import os
import shutil
from pathlib import Path

# Mapeamento de categorias e suas respectivas extensões
CATEGORIAS = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp", ".psd", ".ai"],
    "Documentos": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv"],
    "Codigos": [".py", ".html", ".css", ".js", ".php", ".json", ".sql", ".java"],
    "Compactados": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Instaladores": [".exe", ".msi", ".apk"],
    "Audios_Videos": [".mp3", ".wav", ".mp4", ".mkv", ".avi"]
}