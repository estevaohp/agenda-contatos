import json

produto = [
    {
        "nome" : "Teclado",
        "preco" : 150,
        "quantidade" : 10,
        "categoria" : "Informática"
    },
    {
        "nome" : "Mouse",
        "preco" : 85,
        "quantidade" : 15,
        "categoria" : "Informática"
    },
    {
        "nome" : "Fone",
        "preco" : 200,
        "quantidade" : 5,
        "categoria" : "Informática"
        }

]

with open("produto.json", "w") as arquivo:
    json.dump(produto, arquivo, indent=4, ensure_ascii=False)

with open("produto.json", "r") as arquivo:
    dados = json.load(arquivo)

#print(dados[0]["nome"])
#print(dados[1]["nome"])
#print(dados[2]["nome"])

for produto in dados:
    print(produto["nome"])