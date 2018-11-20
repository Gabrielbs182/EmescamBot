import sqlite3

#Conecçao com o Banco
conn = sqlite3.connect('dados.db')

#Ponteiro de Açoes
cursor = conn.cursor()








#Desconctar do Banco
conn.close()
