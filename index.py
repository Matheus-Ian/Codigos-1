import sqlite3

# Conectar ao banco
conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

# Criar tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS objetos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    tamanho TEXT NOT NULL,
    peso REAL NOT NULL,
    quantidade INTEGER NOT NULL
)
""")

# Receber dados
nome = input("Nome do objeto: ")
tamanho = input("Tamanho: ")
peso = float(input("Peso: "))
quantidade = int(input("Quantidade: "))

# Inserir no banco
cursor.execute("""
INSERT INTO objetos (nome, tamanho, peso, quantidade)
VALUES (?, ?, ?, ?)
""", (nome, tamanho, peso, quantidade))

conexao.commit()

print("Objeto cadastrado com sucesso!")

conexao.close()