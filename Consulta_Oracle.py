import pyodbc
import csv

# Define a list of dates
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

# Conecte-se ao banco de dados Oracle
conn = pyodbc.connect('DRIVER={Oracle em OraClient11g_home1};DBQ=Ora-bi/ORP11;UID=USCM_CONSULTA;PWD=copasa')
print("Conexão Realizada")

# Crie um cursor
cursor = conn.cursor()

# Iterate over each date in the list
for date in dates:
    # Defina a consulta SQL
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

    print(f"Executando Consulta para a data {date}")
    # Execute a consulta SQL e salve o resultado em um DataFrame do pandas
    cursor.execute(sql_query)

    # Abra o arquivo CSV e escreva os resultados da consulta
    with open(f'C:\\Files\\INDICADORES DE LEITURAS - COPASA\\DATABASE\\ARQUIVOS\\{date}.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow([column[0] for column in cursor.description])  # Escreva o cabeçalho
        for row in cursor:
            writer.writerow(row)  # Escreva os dados

    print(f"Arquivo {date}.csv Criado")

# Feche a conexão com o banco de dados
conn.close()

