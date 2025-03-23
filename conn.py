import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="empresa_financas"
)

if conn.is_connected:
    print("Conexão Completa")
else:
    print("Falha na Conexão")
cursor = conn.cursor()

cursor.execute("SELECT valor FROM despesas")
for line in cursor.fetchall():
    print(line)


cursor.close()
conn.close()
