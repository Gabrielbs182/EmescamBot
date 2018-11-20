import sqlite3

#Conecçao com o Banco
conn = sqlite3.connect('dados.db')

#Ponteiro de Açoes
cursor = conn.cursor()

#Cria tabela com elementos programados por SQL
cursor.execute("""
CREATE TABLE IF NOT EXISTS dados (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome    TEXT NOT NULL,
        adulto  TEXT NOT NULL,
        cpf     VARCHAR(11) NOT NULL,
        tipo    TEXT NOT NULL,
        data    TEXT NOT NULL,
        hora    TEXT NOT NULL,
        unidade TEXT NOT NULL,
        local   TEXT NOT NULL

);
""")

#Desconctar do Banco
conn.close()
