#usr/bin/python3
from cadastrar import armazenarUsuario
import arquivoJson


def main():
        usuarios = {}
        opcao = input("Selecione a opcao \n" + 
                "Digite I para inserir um usuario \n" +
                "Digite A para consultar usuario por nivel de acesso \n" +
                "Digite D para consultar usuario por departamento \n" +
                "Digite L para ler os dados do arquivo JSON \n").upper()

        contador = 0
                
        while opcao == "I" or opcao == "A" or opcao == "D" or opcao == "L":
                
                if opcao == "I" :
                        usuarios[contador] = armazenarUsuario(contador)
                        contador += 1
                        arquivoJson.gravarArquivo(usuarios)
                elif opcao == "A":
                        print("Vc digitou  A")
                elif opcao == "D":
                        print("Vc digitou D")
                elif opcao == "L":
                        lista = arquivoJson.lerArquivo()
                        print(lista)
                        print("Vc digitou L")
                else:
                        print("Opcao Invalida")
                
                opcao = input("O que deseja realizar\n" + 
                "Digite I para inserir um usuario\n" +
                "Digite A para consultar usuario por nivel de acesso\n" +
                "Digite D para consultar usuario por departamento\n" +
                "Digite L para ler os dados do arquivo JSON\n").upper()
        

if __name__ == '__main__':
        main()




