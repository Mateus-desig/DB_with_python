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
value= cursor.fetchall()

all_vall = []

# Filtrar e converter os valores válidos.
for i in value:
    if i[0] is not None:
        try:
            vall_num = float(i[0])# Tenta converter diretamente para float
            all_vall.append(i[0]) # Valor valido adicionar a lista.

        except ValueError:
            print(f"Valor inválido{i[0]}") # Se não for possível converter, ignora.
            

# Verificando valores.
if value:
    
    # Calculando media.
    average = sum(all_vall) / len(all_vall)

    print(f"A média das despesas é: R${round(average,2)}")

else: print("Nenhum valor encontrado ou não e numerico.")

cursor.close()
conn.close()
