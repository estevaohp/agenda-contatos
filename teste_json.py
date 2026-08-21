import json

pessoa = {
    "nome": "Estevão",
    "idade": 22,
    "cidade": "São Paulo"
}

with open("dados.json", "w") as arquivo:
    json.dump(pessoa, arquivo, indent=4, ensure_ascii=False)

with open("dados.json", "r") as arquivo:
    dados = json.load(arquivo)

print(dados)
