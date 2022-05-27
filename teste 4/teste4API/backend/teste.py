import pandas as pd
col_names = ['Registro ANS','CNPJ','Razão Social','Nome Fantasia','Modalidade','Logradouro','Número','Complemento','Bairro','Cidade', 'UF','CEP', 'DDD', 'Telefone', 'Fax', 'Endereço eletrônico', 'Representante', 'Cargo Representante', 'Data Registro ANS']

df = pd.read_csv('Relatorio_cadop teste 4.csv', names=col_names, encoding = "ANSI", sep=';', skiprows=3)

print(df)