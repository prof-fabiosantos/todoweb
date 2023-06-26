import sqlite3

conn = sqlite3.connect('todo.db')
cursor = conn.cursor()

# Cria a tabela tasks se não existir
cursor.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT)")

# Insere algumas tarefas de exemplo
cursor.execute("INSERT INTO tasks (title) VALUES ('Tarefa 1')")
cursor.execute("INSERT INTO tasks (title) VALUES ('Tarefa 2')")

conn.commit()
conn.close()
