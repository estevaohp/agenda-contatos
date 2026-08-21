import json

print("=" * 30) 
print("AGENDA DE CONTATOS")
print("=" * 30)

opcao = ""

def carregar_contatos():
    try:
        with open("contatos.json", "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        print("Arquivo de contatos não encontrado. Criando uma nova agenda.")
        return []

    except json.JSONDecodeError:
        print("O arquivo de contatos está inválido. Iniciando uma nova agenda.")
        return[]

contatos = carregar_contatos()

def salvar_contatos():
    try:
        with open("contatos.json", "w") as arquivo:
            json.dump(contatos, arquivo, indent=4)
    except TypeError:
        print("Contato não salvo. Tente novamente")
        

def listar_contatos():
    if not contatos:
        print("Nenhum contato foi cadastrado.")

    else:
        for indice, contato in enumerate(contatos):
            print(
                f"{indice + 1}. "
                f"{contato['nome']} | "
                f"{contato['telefone']} | "
                f"{contato['email']}"
            )

def buscar_contatos(nome_busca):
    encontrou = False

    for indice, contato in enumerate(contatos):
        if nome_busca.lower() in contato["nome"].lower():
            print(
                f"{indice + 1}. "
                f"{contato['nome']} | "
                f"{contato['telefone']} | "
                f"{contato['email']}"
            )
            encontrou = True

    if not encontrou:
        print("Contato não encontrado!")

def excluir_contato(indice):
    del contatos[indice]
    salvar_contatos()
    print("Contato excluido com sucesso!")

def cadastrar_contato():
    nome = input("Digite o nome: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite o e-mail: ")

    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email
    }

    contatos.append(contato)
    salvar_contatos()

    print("Contato cadastrado com sucesso!")

def editar_contato():
    print("Editando o contato...")

    if not contatos:
        print("Nenhum contato cadastrado.")

    else:
        indice = escolher_contato()

        if indice is not None:
                
                print("\nO que deseja alterar?")
                print("1 - Nome")
                print("2 - Telefone")
                print("3 - E-mail")
                print("4 - Todos")

                alterar = input("Escolha uma opção: ")

                alterado = False

                if alterar == "1":
                    novo_nome = input("Digite o novo nome: ")
                    contatos[indice]["nome"] = novo_nome
                    alterado = True

                elif alterar == "2":
                    novo_telefone = input("Digite o novo telefone: ")
                    contatos[indice]["telefone"] = novo_telefone
                    alterado = True

                elif alterar == "3":
                    novo_email = input("Digite o novo e-mail: ")
                    contatos[indice]["email"] = novo_email
                    alterado = True

                elif alterar == "4":
                    novo_nome = input("Digite o novo nome: ")
                    novo_telefone = input("Digite o novo telefone: ")
                    novo_email = input("Digite o novo e-mail: ")

                    contatos[indice]["nome"] = novo_nome
                    contatos[indice]["telefone"] = novo_telefone
                    contatos[indice]["email"] = novo_email

                    alterado = True

                else:
                    print("Opção inválida!")

                if alterado:
                    salvar_contatos()
                    print("Contato alterado com sucesso!")

def escolher_contato():
    if not contatos:
        print("Nenhum contato cadastrado.")
        return None
    
    listar_contatos()

    escolha = input("Digite o número do contato: ")

    try:
        indice = int(escolha) - 1

        if indice >= 0 and indice < len(contatos):
            return indice
        else:
            print("Contato inválido. Tente novamente.")

    except ValueError:
        print("Digite apenas números!")

    return None

while opcao != "0":

    print("1 - Cadastrar contato")
    print("2 - Listar contatos")
    print("3 - Buscar contatos")
    print("4 - Editar contatos")
    print("5 - Excluir contatos")
    print("0 - Sair")

    opcao = input("\n Escolha uma opção: ")    

    print(f"\n Você escolheu a opção {opcao}")

    
    if opcao == "1":
        cadastrar_contato()

    elif opcao == "2":
        print("Listando os contatos...")
        listar_contatos()

    elif opcao == "3":
        print("Buscando contato...")

        nome_busca = input("Digite o nome desejado: ")

        buscar_contatos(nome_busca)
            
    elif opcao == "4":
        editar_contato()

    elif opcao == "5":
        print("Apagando o  contato...")

        indice = escolher_contato()

        if indice is not None:
            confirmacao = input(
                f"Tem certeza que deseja excluir{contatos[indice]['nome']}? (s/n)"
            )

        if confirmacao.lower() == "s":
            excluir_contato(indice)

        elif confirmacao.lower() == "n":
            print("Exclusão cancelada.")

        else:
            print("Opção invalida.")

    elif opcao == "0":
        print("Saindo!")
    else:
        print("Opção Inválida")

