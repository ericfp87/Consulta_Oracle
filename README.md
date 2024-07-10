# Consulta_Oracle
 Consulta no banco de dados Oracle e geração de arquivo .csv


```markdown
# Extração e Armazenamento de Dados do Banco de Dados Oracle com PyODBC

Este repositório contém um script Python que se conecta a um banco de dados Oracle, executa consultas SQL para diferentes datas e salva os resultados em arquivos CSV.

## Requisitos

- Python 3.x
- PyODBC
- Drivers Oracle

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd seu-repositorio
   ```
3. Instale as dependências necessárias:
   ```bash
   pip install pyodbc
   ```

## Configuração do Ambiente

1. Certifique-se de ter os drivers Oracle instalados e configurados corretamente no seu sistema.

2. Atualize a string de conexão `conn` no script com as credenciais corretas do banco de dados Oracle:
   ```python
   conn = pyodbc.connect('DRIVER={Oracle em OraClient11g_home1};DBQ=Ora-bi/ORP11;UID=USCM_CONSULTA;PWD=sua_senha')
   ```

## Uso

1. Defina a lista de datas no script conforme necessário.
2. Execute o script:
   ```bash
   python seu_script.py
   ```

## Descrição do Script

O script realiza as seguintes operações:

1. **Definição da Lista de Datas**:
   ```python
   dates = [
       20220701,
       20220801,
       20220901,
       20221001,
       20221101,
       20221201,
       20230101,
       20230201,
       20230301,
       20230401,
       20230501,
       20230601,
       20230701,
       20230801,
       20230901,
       20231001,
       20231101,
       20231201,
       20240101,
       20240201,
       20240301,
       20240401,
       20240501
   ]
   ```

2. **Conexão ao Banco de Dados Oracle**:
   ```python
   conn = pyodbc.connect('DRIVER={Oracle em OraClient11g_home1};DBQ=Ora-bi/ORP11;UID=USCM_CONSULTA;PWD=sua_senha')
   print("Conexão Realizada")
   ```

3. **Criação do Cursor**:
   ```python
   cursor = conn.cursor()
   ```

4. **Iteração sobre Cada Data na Lista**:
   - Definição da consulta SQL:
     ```python
     sql_query = f"""
         SELECT      
             LEI.id_tempo_referencia "REFER",
             UNI.SUPERINTENDENCIA "UNIDADE",
             UNI.DISTRITO "GERENCIA",
             UNI.NOME_LOCALIDADE "NOME-LOCALIDADE",
             count(LEI.matricula_cliente_imovel) QTD_LEITURAS,
             LEI.cod_ocorrencia COD_OCORRENCIA,
             LEI.MATRICULA_CLIENTE_IMOVEL MATRICULA
         FROM    
             DW.FATO_GL_LEITURAS_GERAL LEI INNER JOIN
             DW.DIM_IEC_UNIDADE_ORGANIZACIONAL UNI ON  lei.ID_UNIDADE = uni.id_unidade_organizacional
         WHERE
             lei.id_tempo_referencia = {date}
         GROUP BY 
             LEI.id_tempo_referencia,
             UNI.SUPERINTENDENCIA,
             UNI.DISTRITO,
             UNI.NOME_LOCALIDADE,
             LEI.cod_ocorrencia,
             LEI.MATRICULA_CLIENTE_IMOVEL
         ORDER BY LEI.id_tempo_referencia;
     """
     ```

   - Execução da consulta SQL:
     ```python
     cursor.execute(sql_query)
     ```

   - Escrita dos resultados em um arquivo CSV:
     ```python
     with open(f'C:\\Files\\INDICADORES DE LEITURAS - COPASA\\DATABASE\\ARQUIVOS\\{date}.csv', 'w', newline='') as csvfile:
         writer = csv.writer(csvfile, delimiter=';')
         writer.writerow([column[0] for column in cursor.description])  # Escreva o cabeçalho
         for row in cursor:
             writer.writerow(row)  # Escreva os dados
     ```

   - Impressão de mensagem de conclusão para cada arquivo:
     ```python
     print(f"Arquivo {date}.csv Criado")
     ```

5. **Fechamento da Conexão com o Banco de Dados**:
   ```python
   conn.close()
   ```

## Contribuição

1. Faça um fork do projeto
2. Crie uma nova branch (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova funcionalidade'`)
4. Envie para a branch (`git push origin feature/nova-funcionalidade`)
5. Crie um novo Pull Request

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
```
