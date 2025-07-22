import requests
import json
URL =  "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"
# requests.get para pegar os dados da URL
response = requests.get(URL)
# quando pedimos o print(response) ele indica 200 no caso foi pego com sucesso
if response.status_code == 200:
    dados_restaurantes = {}
    for item in response.json():
        if item['Company'] not in dados_restaurantes:
            dados_restaurantes[item['Company']] = []

        dados_restaurantes[item['Company']].append({
        "item": item['Item'],
        "price": item['price'],
        "description": item['description']
        })
else:
    print(f"Error: {response.status_code}")

for nome, dados in dados_restaurantes.items():
    nome_do_arquivo = f"{nome}.json"
    with open(nome_do_arquivo, "w") as arquivo:
        json.dump(dados, arquivo, indent=4)
