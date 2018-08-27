import json

def gravarArquivo(usuarios):
    with open("users.json", "w") as arquivo:
        json.dump(usuarios, arquivo)

def lerArquivo():
    with open('users.json') as arquivo:
        return json.load(arquivo)