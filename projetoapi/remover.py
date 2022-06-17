import sqlite3
from sqlite3 import Error

# Excluir um pokemon no banco de dados com base no id informado

def criar_conexao(db_file): # Cria uma conexão com o banco de dados SQLite do Django
    
    conexao = None
    try:
        conexao = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conexao


def delete_task(conexao, id): # Deleta um pokemon no banco de dados com base no id informado

    sql = 'DELETE FROM api_pokemon WHERE id=?'
    cur = conexao.cursor()
    cur.execute(sql, (id,))
    conexao.commit()

def main():
    database = r"db.sqlite3"

    conexao = criar_conexao(database)
    with conexao:
        delete_task(conexao, 3); # Trocar aqui o ID do pokemon que deseja excluir


if __name__ == '__main__':
    main()