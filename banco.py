import sqlite3

def conectar():
    return sqlite3.connect("database.db")


def criar_tabela():
    conexao = conectar()
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


def cadastrar_objeto(nome, tamanho, cor, peso, unidade_peso, quantidade):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO objetos
    (nome, tamanho, cor, peso, unidade_peso, quantidade)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (nome, tamanho, cor, peso, unidade_peso, quantidade))

    conexao.commit()
    conexao.close()


def listar_objetos():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM objetos")
    objetos = cursor.fetchall()

    conexao.close()
    return objetos


def atualizar_objeto(id_objeto, nome, tamanho, cor, peso, unidade_peso, quantidade):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    UPDATE objetos
    SET nome = ?,
        tamanho = ?,
        cor = ?,
        peso = ?,
        unidade_peso = ?,
        quantidade = ?
    WHERE id = ?
    """, (
        nome,
        tamanho,
        cor,
        peso,
        unidade_peso,
        quantidade,
        id_objeto
    ))

    conexao.commit()
    conexao.close()


def excluir_objeto(id_objeto):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "DELETE FROM objetos WHERE id = ?",
        (id_objeto,)
    )

    conexao.commit()
    conexao.close()