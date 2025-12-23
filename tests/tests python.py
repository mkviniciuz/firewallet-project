import sqlite3

conn = sqlite3.connect("./data/auth.db")
cursor = conn.cursor()

cursor.execute("SELECT current_balance from users WHERE cpf = '12345678900'")
resultado = cursor.fetchone()

print(resultado[0])