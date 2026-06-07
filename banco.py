import sqlite3

def criar_banco():
    conexao = sqlite3.connect("database.db")
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS objetos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        tamanho TEXT NOT NULL,
        cor TEXT NOT NULL,
        peso REAL NOT NULL,
        unidade_peso TEXT NOT NULL,
        quantidade INTEGER NOT NULL
    )
    """)

    conexao.commit()
    conexao.close()

def inserir_objeto(nome, tamanho, cor, peso, unidade_peso, quantidade):
    conexao = sqlite3.connect("database.db")
    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO objetos
    (nome, tamanho, cor, peso, unidade_peso, quantidade)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (nome, tamanho, cor, peso, unidade_peso, quantidade))

    conexao.commit()
    conexao.close()