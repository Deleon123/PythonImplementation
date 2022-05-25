# importando livarias necessárias
import tabula
import zipfile

# Conversão do PDF em CSV
tabula.convert_into('Outputs/Anexo_I_Rol_2021RN_465.2021_RN473_RN478_RN480_RN513_RN536.pdf','Outputs/Teste_Deleon.csv', output_format='csv', pages='all')

# Compactando o arquivo CSV em .zip
    # Criando o arquivo ZIP
zipf = zipfile.ZipFile('Outputs/Teste_Deleon.zip', 'w', zipfile.ZIP_DEFLATED)
    # guardando o arquivo dentro do ZIP
zipf.write('Outputs/Teste_Deleon.csv')
zipf.close()