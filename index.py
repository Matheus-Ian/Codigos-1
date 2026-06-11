from banco import *

criar_tabela()

while True:
    print("\n===== CRUD DE OBJETOS =====")
    print("1 - Cadastrar objeto")
    print("2 - Listar objetos")
    print("3 - Atualizar objeto")
    print("4 - Excluir objeto")
    print("5 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        print("\n--- Cadastro ---")

        nome = input("Nome: ")
        tamanho = input("Tamanho: ")
        cor = input("Cor: ")

        peso = float(input("Peso: "))
        unidade_peso = input("Unidade (kg/g): ")

        quantidade = int(input("Quantidade: "))

        cadastrar_objeto(
            nome,
            tamanho,
            cor,
            peso,
            unidade_peso,
            quantidade
        )

        print("Objeto cadastrado com sucesso!")

    elif opcao == "2":
        print("\n--- Objetos Cadastrados ---")

        objetos = listar_objetos()

        if len(objetos) == 0:
            print("Nenhum objeto cadastrado.")
        else:
            for obj in objetos:
                print(f"""
ID: {obj[0]}
Nome: {obj[1]}
Tamanho: {obj[2]}
Cor: {obj[3]}
Peso: {obj[4]} {obj[5]}
Quantidade: {obj[6]}
---------------------------
""")

    elif opcao == "3":
        print("\n--- Atualizar Objeto ---")

        id_objeto = int(input("ID do objeto: "))

        nome = input("Novo nome: ")
        tamanho = input("Novo tamanho: ")
        cor = input("Nova cor: ")

        peso = float(input("Novo peso: "))
        unidade_peso = input("Nova unidade (kg/g): ")

        quantidade = int(input("Nova quantidade: "))

        atualizar_objeto(
            id_objeto,
            nome,
            tamanho,
            cor,
            peso,
            unidade_peso,
            quantidade
        )

        print("Objeto atualizado com sucesso!")

    elif opcao == "4":
        print("\n--- Excluir Objeto ---")

        id_objeto = int(input("ID do objeto: "))

        excluir_objeto(id_objeto)

        print("Objeto excluído com sucesso!")

    elif opcao == "5":
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida!")