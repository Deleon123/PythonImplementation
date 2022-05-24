# importando as livrarias necessárias
import os
import requests
import zipfile

# descobrindo as urls de onde serão baixados os arquivos
urls = [
    'https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/Anexo_I_Rol_2021RN_465.2021_RN473_RN478_RN480_RN513_RN536.pdf',
    'https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/Anexo_I_Rol_2021RN_465.2021_RN473_RN478_RN480_RN513_RN536.xlsx',
    'https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/Anexo_II_DUT_2021_RN_465.2021_tea.br_RN473_RN477_RN478_RN480_RN513_RN536.pdf',
    'https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/Anexo_III_DC_2021_RN_465.2021.v2.pdf',
    'https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/Anexo_IV_PROUT_2021_RN_465.2021.v2.pdf'
]
# diretório de saída
output_dir = './Outputs'

# criando o arquivo .zip
zip_file = zipfile.ZipFile('Outputs/archives.zip', 'w')

# baixando os pdfs
for url in urls:
    response = requests.get(url)
    if response.status_code == 200:
        file_path = os.path.join(output_dir, os.path.basename(url))
        with open(file_path, 'wb') as f:
            f.write(response.content)
            # colocando os arquivos em um zip 
            zip_file.write(file_path, compress_type=zipfile.ZIP_DEFLATED)
# fechando o arquivo zip que foi aberto
zip_file.close()