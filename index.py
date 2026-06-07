from banco import criar_banco, inserir_objeto

criar_banco()

print("=== Cadastro de Objetos ===")

nome = input("Nome do objeto: ")
tamanho = input("Tamanho: ")
cor = input("Cor: ")

peso =float(input("Peso: "))
unidade_peso = input("Unidade (kg/g): ")

quantidade = int(input("Quantidade: "))

inserir_objeto(
    nome,
    tamanho,
    cor,
    peso,
    unidade_peso,
    quantidade
)

print("\nObjeto cadastrado com sucesso!")