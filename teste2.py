# importando livarias necessárias
import tabula
import zipfile

# Conversão do PDF em CSV
tabula.convert_into('Outputs/Anexo_I_Rol_2021RN_465.2021_RN473_RN478_RN480_RN513_RN536.pdf','Outputs/Teste_Deleon.csv', output_format='csv', pages='all')

# Manipulando CSV (BÔNUS) - Substituindo OD E AMB por suas respectivas descrições
    # Criando uma função para substituir os itens
def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text
    # dicionário de substituição
od_dic = {'OD':'Seg. Odontológica'}
amb_dic = {'AMB':'Seg. Ambulatorial'}

    # lendo o arquivo para as substituições
with open('Outputs/Teste_Deleon.csv') as f:
    text = f.read()
    # criando o arquivo 2 com os textos formatados
    with open('Outputs/TesteFormatado_Deleon.csv', 'w') as w:
        text = replace_all(text, od_dic)
        text = replace_all(text, amb_dic)
        w.write(text)


# Compactando o arquivo CSV em .zip
    # Criando o arquivo ZIP
zipf = zipfile.ZipFile('Outputs/Teste_Deleon.zip', 'w', zipfile.ZIP_DEFLATED)
    # guardando o arquivo dentro do ZIP
zipf.write('Outputs/TesteFormatado_Deleon.csv')
zipf.close()