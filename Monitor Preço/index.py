from datetime import datetime
from bs4 import BeautifulSoup
import requests

def verifiicar_preco_produto(url, seletor_css, preco_desejado):
    #Header para simular um navegador
    headers = {
        'User-Agent': (
          'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
          ' (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
      ),
      'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    }