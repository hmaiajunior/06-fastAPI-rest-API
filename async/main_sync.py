from datetime import datetime 

import requests

def fetch_url(url):
    response = requests.get(url)
    return response.text

def main():
    tempo_inicio = datetime.now()
    urls = ["https://example.com"] * 10  # Lista de URLs para fetch
    responses = [fetch_url(url) for url in urls]
    for response in responses:
        print(response[:100])  # Printa os primeiros 100 caracteres de cada resposta
    tempo_final = datetime.now() - tempo_inicio
    print(tempo_final)

main()