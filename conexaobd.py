"""
Script de conexão e operações CRUD com MySQL
Realiza inserções, atualizações, exclusões e consultas na tabela 'aula'
"""

# Importação de bibliotecas
import mysql.connector
from mysql.connector import Error

try:
    # ==================== CONEXÃO COM O BANCO ====================
    # Configuração e estabelecimento da conexão
    connection = mysql.connector.connect(
        host='127.0.0.1',        # Endereço do servidor MySQL (localhost)
        database='materia',      # Nome do banco de dados a ser acessado
        user='root',             # Usuário para autenticação
        password=''              # Senha do usuário (vazia neste caso)
    )

    # ==================== OPERAÇÃO DE INSERÇÃO ====================
    while True:
        # Entrada de dados do usuário
        id = int(input("Insira o ID: "))
        nome = input("Insira a matéria: ")

        # Construção e execução da query SQL
        mySql_insert_query = f"""
            INSERT INTO aula (idaula, nome)
            VALUES ({id}, '{nome}')
        """
        cursor = connection.cursor()
        cursor.execute(mySql_insert_query)  # Executa o comando INSERT
        connection.commit()                 # Confirma a transação

        # Feedback ao usuário
        print(cursor.rowcount, "Inserido com sucesso")
        
        # Controle de continuidade
        opc = input("Deseja continuar? s n ")
        if opc.lower() == 'n':
            break

    # ==================== OPERAÇÃO DE ATUALIZAÇÃO ====================
    while True:
        opc = input("Deseja atualizar? s n ")
        if opc.lower() == 'n':
            break
            
        # Dados para atualização
        UpdateID = int(input("Qual ID terá nome atualizado? "))
        UpdateNome = input("Qual o novo nome para a matéria? ")
        
        # Query de atualização
        sql_Update_query = f"""UPDATE aula SET nome = '{UpdateNome}' WHERE idaula = {UpdateID}"""
        cursor.execute(sql_Update_query)
        connection.commit()
        print(cursor.rowcount, "record(s) affected")

    # ==================== OPERAÇÃO DE EXCLUSÃO ====================
    while True:
        opc = input("Deseja deletar? s n ")
        if opc.lower() == 'n':
            break
            
        # ID para exclusão
        DelId = int(input("Insira o ID para deletar: "))
        
        # Query de exclusão
        sql_Delete_query = f"""DELETE FROM aula WHERE idaula = {DelId}"""
        cursor.execute(sql_Delete_query)
        connection.commit()
        print('Número de linhas deletadas:', cursor.rowcount)

    # ==================== CONSULTA DE DADOS ====================
    # Query para selecionar todos os registros
    mySql_select_query = """SELECT * FROM aula"""
    cursor = connection.cursor()
    cursor.execute(mySql_select_query)
    records = cursor.fetchall()  # Obtém todos os registros

    # Exibição dos resultados
    print("\nTotal de registros:", cursor.rowcount)
    print("Conteúdo da tabela:")
    for row in records:
        print(f"ID: {row[0]}, Matéria: {row[1]}")

except Error as e:
    # Tratamento de erros
    print("Erro na conexão ou operação com MySQL:", e)
    
finally:
    # ==================== ENCERRAMENTO DA CONEXÃO ====================
    if connection.is_connected():
        connection.close()  # Fecha a conexão com o banco
        print("Conexão com MySQL encerrada")
