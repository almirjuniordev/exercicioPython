#usr/bin/python3

import datetime

def armazenarUsuario(id):
    usuario = {
        "ID": id,
        "Nome" : input("Digite o nome: "),
        "Nome Reduzido": input("Digite o nome reduzido: "),
        "Cargo" : input("Digite o cargo: "),
        "Acesso": nivelAcesso(),
        "Data": getData(),
        # "Data": datetime.datetime.now().day +"/"+ datetime.datetime.now().month +"/"+ datetime.datetime.now().year,
        "Departamento": input("Digite o departamento: "),
        "Historico": input("Digite o historico: "),
    }

    return usuario

def nivelAcesso():
        opcao = input("Selecione o nivel de acesso\n" + 
            "Digite V para Visitante\n" +
            "Digite U para Usuario\n" +
            "Digite A para Administrativo\n" +
            "Digite T para Tecnico\n" +
            "Digite S para SuperUsuario\n").upper()
                
        while opcao != "V" or opcao != "U" or opcao != "A" or opcao != "T" or opcao != "S":
                
            if opcao == "V" :
                return "Visitante"
            elif opcao == "U":
                return "Usuario"
            elif opcao == "A":
                return "Administrativo"
            elif opcao == "T":
                return "Tecnico"
            elif opcao == "S":
                return "SuperUsuario"
            else:
                print("Opcao Invalida")
                opcao = input("Selecione o nivel de acesso\n" + 
                "Digite V para Visitante\n" +
                "Digite U para Usuario\n" +
                "Digite A para Administrativo\n" +
                "Digite T para Tecnico\n" +
                "Digite S para SuperUsuario\n").upper()

def getData():
    return   datetime.datetime.now().day +"/"+ datetime.datetime.now().month +"/"+ datetime.datetime.now().year + " " + datetime.datetime.now().hour + ":" + datetime.datetime.now().minute,              


