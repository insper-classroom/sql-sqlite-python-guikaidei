import sqlite3

# Exercício de Python - Sqlite

# Conexão com o banco de dados dentro da pasta "db"
conn = sqlite3.connect('db/database_alunos.db')
cursor = conn.cursor()

# Vamos criar uma tabela chamada "Estudantes" com os seguintes campos:
# ID (chave primária) -  Criado automáticamente pela base de dados
# Nome
# Curso
# Ano de Ingresso

cursor.execute("""
CREATE TABLE IF NOT EXISTS Estudantes (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Curso TEXT NOT NULL,
    AnoIngresso INTEGER
);
""")
               
estudantes = [
    ("Ana Silva", "Computação", 2019),
    ("Pedro Mendes", "Física", 2021),
    ("Carla Souza", "Computação", 2020),
    ("João Alves", "Matemática", 2018),
    ("Maria Oliveira", "Química", 2022)
]

cursor.executemany("""
INSERT INTO Estudantes (Nome, Curso, AnoIngresso)
VALUES (?, ?, ?);
""", estudantes)

conn.commit()

cursor.execute("SELECT Nome FROM Estudantes WHERE AnoIngresso between 2019 and 2020")
print(cursor.fetchall())

cursor.execute("UPDATE Estudantes SET AnoIngresso = ? WHERE Nome = ?", (2022, "Ana Silva"))
conn.commit()

cursor.execute("SELECT * FROM Estudantes")
print(cursor.fetchall())

cursor.execute("DELETE FROM Estudantes WHERE ID = ?", ('1'))
conn.commit()

cursor.execute("SELECT * FROM Estudantes")
print(cursor.fetchall())

cursor.execute("SELECT Nome FROM Estudantes WHERE Curso = 'Computação' and AnoIngresso > 2019")
print(cursor.fetchall())

cursor.execute("UPDATE Estudantes SET AnoIngresso = 2018 WHERE Curso = 'Computação'")
conn.commit()

cursor.execute("SELECT * FROM Estudantes")
print(cursor.fetchall())

conn.close()