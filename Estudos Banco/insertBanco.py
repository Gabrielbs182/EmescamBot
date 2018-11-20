import sqlite3

#Conecçao com o Banco
conn = sqlite3.connect('dados.db')

#Ponteiro de Açoes
cursor = conn.cursor()


cursor.execute("""
INSERT INTO dados (nome, adulto, cpf, tipo, data, hora, unidade, local)
VALUES ('Matheus', 'Marly Oliveira', '14756424740', 'Pediatria', '24/11/2018', '14:30', 'Metropolitano', 'Av.Civit nº 45')
""")

cursor.execute("""
INSERT INTO dados (nome, adulto, cpf, tipo, data, hora, unidade, local)
VALUES ('Gabriel', 'Maria Bonita', '12365478950', 'Pediatria', '12/11/2018', '14:30', 'Metropolitano', 'Av.Civit nº 45')
""")

cursor.execute("""
INSERT INTO dados (nome, adulto, cpf, tipo, data, hora, unidade, local)
VALUES ('Thiago', 'Isabela Aparecida', '32145698760', 'Pediatria', '15/11/2018', '14:30', 'Metropolitano', 'Av.Civit nº 45')
""")



#Forma de Inserir as Alteraçoes no Banco
conn.commit()


#Desconctar do Banco
conn.close()
