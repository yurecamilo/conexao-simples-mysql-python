# 🐍💾 Script Python: Operações CRUD com MySQL

Este projeto contém um script em **Python** para realizar operações **CRUD** (_Create, Read, Update, Delete_) em uma tabela chamada `aula` de um banco de dados **MySQL**. O objetivo é possibilitar a inserção, atualização, exclusão e consulta de registros de forma interativa via terminal.

---

## ✨ Funcionalidades

- 🔗 **Conexão** com o banco de dados MySQL
- 📝 **Inserção** de novos registros na tabela `aula`
- 🔄 **Atualização** de registros existentes
- 🗑️ **Exclusão** de registros por ID
- 🔍 **Consulta** e exibição de todos os registros da tabela

---

## 🛠️ Pré-requisitos

- Python 3.x instalado
- MySQL Server ativo
- Biblioteca `mysql-connector-python` instalada:
  
  ```sh
  pip install mysql-connector-python
  ```

- Banco de dados `materia` criado contendo a tabela `aula` com a seguinte estrutura:

  ```sql
  CREATE DATABASE IF NOT EXISTS materia;
  USE materia;

  CREATE TABLE IF NOT EXISTS aula (
    idaula INT PRIMARY KEY,
    nome VARCHAR(100)
  );
  ```

---

## ⚙️ Configuração

No início do script, configure as credenciais de acesso ao banco de dados conforme necessário:

```python
connection = mysql.connector.connect(
    host='127.0.0.1',
    database='materia',
    user='root',
    password=''
)
```

---

## ▶️ Como usar

1. Execute o script Python no terminal:

    ```sh
    python nome_do_arquivo.py
    ```

2. Siga as instruções interativas para inserir, atualizar, excluir ou consultar dados na tabela.

3. O script respeita a seguinte ordem de operações:
   - 📝 Inserção de registros (enquanto desejar)
   - 🔄 Atualização de registros (opcional)
   - 🗑️ Exclusão de registros (opcional)
   - 🔍 Consulta e exibição de todos os registros presentes na tabela

---

## 🧩 Estrutura do Script

- **Conexão**: Realiza a conexão com o banco de dados MySQL
- **Inserção**: Permite inserir novos registros na tabela `aula`
- **Atualização**: Permite atualizar o nome de uma matéria a partir do ID
- **Exclusão**: Permite excluir um registro pelo seu ID
- **Consulta**: Exibe todos os registros da tabela
- **Tratamento de Erros**: Captura e exibe possíveis erros de conexão ou execução
- **Encerramento**: Fecha a conexão com o banco após a execução

---

## 💡 Exemplo de uso

```
Insira o ID: 1
Insira a matéria: Matemática
1 Inserido com sucesso
Deseja continuar? s n s
Insira o ID: 2
Insira a matéria: História
1 Inserido com sucesso
Deseja continuar? s n n
Deseja atualizar? s n n
Deseja deletar? s n n

Total de registros: 2
Conteúdo da tabela:
ID: 1, Matéria: Matemática
ID: 2, Matéria: História
Conexão com MySQL encerrada
```

---

## ⚠️ Observações

- O script utiliza comandos SQL construídos dinamicamente. Para ambientes de produção, recomenda-se o uso de **queries parametrizadas** para evitar SQL Injection.
- A senha do usuário `root` está configurada como vazia. Altere conforme a configuração do seu banco de dados.
- Certifique-se de que o serviço MySQL está ativo antes de executar o script.

---

## 📜 Licença

Este projeto é livre para uso educacional e pessoal.

---

## 👨‍💻 Autor

- **Yure Campos Camilo**  
- 📧 ccamposcamilo@gmail.com
