import mysql.connector
from mysql.connector import Error
try:
    # Tenta estabelecer uma conexão com o banco de dados MySQL
    connection = mysql.connector.connect(
        host='127.0.0.1',        # Nome do host (localhost = máquina local)
        database='materia',      # Nome do banco de dados
        user='root',             # Usuário do banco de dados
        password=''              # Senha (em branco nesse caso)
    )
    while True:
        id = int(input(f"Insira o ID: "))
        nome = input(f"Insira a matéria: ")

        mySql_insert_query = f"""
            INSERT INTO aula (idaula, nome)
            VALUES ({id}, '{nome}')
        """
        cursor = connection.cursor()
        cursor.execute(mySql_insert_query)  # Executa o comando SQL
        connection.commit()                 # Confirma as mudanças no banco de dados

        # Mostra o número de registros inseridos
        print(cursor.rowcount, "Inserido com sucesso")
        opc = input("deseja continuar? s n ")
        if opc in 'n':
            break

    while True:
        opc = input("deseja atualizar? s n ")
        if opc in 'n':
            break
        UpdateID = int(input("Qual ID terá nome atualizado? "))
        UpdateNome = input("Qual o novo nome para a matéria?  ")
        sql_Update_query = f"""UPDATE aula SET nome = '{UpdateNome}' WHERE idaula = {UpdateID}"""
        cursor.execute(sql_Update_query)
        connection.commit()
        print(cursor.rowcount, "record(s) affected")

    while True:
        opc = input("deseja deletar? s n ")
        if opc in 'n':
            break
        DelId = int(input(f"Insira o ID para deletar: "))
        sql_Delete_query = f"""Delete from aula where idaula = {DelId}"""
        cursor.execute(sql_Delete_query)
        connection.commit()
        print('number of rows deleted', cursor.rowcount)

    mySql_select_query = f"""
            SELECT * FROM aula
        """
    cursor = connection.cursor()
    cursor.execute(mySql_select_query)

    # get all records
    records = cursor.fetchall()

    print("Total de registros: ", cursor.rowcount)
    print("\nPrinting cada linha")

    for row in records:
        print("idaula = ", row[0], )
        print("nome = ", row[1], "\n")

except Error as e:
    # Caso ocorra um erro na conexão ou execução do SQL
    print("Erro no MySQL", e)
finally:
    # Garante que a conexão será encerrada corretamente
    if connection.is_connected():
        connection.close()
        print("MySQL conexão fechada")