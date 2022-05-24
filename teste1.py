# importando as livrarias necessárias
import os
import requests
import zipfile
from requests_html import HTML, HTMLSession

# descobrindo as urls de onde serão baixados os arquivos
link = 'https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/o-que-e-o-rol-de-procedimentos-e-evento-em-saude'
session = HTMLSession()
r = session.get(link)
# obtendo o url de cada arquivo (elementos filhos de 14 a 19)
urls = []
for index in range(14, 19):
    page = r.html.find('#parent-fieldname-text > p:nth-child('+str(index)+') > a', first=True)
    urls.append(page.absolute_links)
# diretório de saída
output_dir = './Outputs'

# criando o arquivo .zip
zip_file = zipfile.ZipFile('Outputs/archives.zip', 'w')

# baixando os pdfs
for url in urls:
    # convertendo os SETS em string para o link ser baixado
    strippedString = e = next(iter(url))
    response = requests.get(strippedString)
    if response.status_code == 200:
        file_path = os.path.join(output_dir, os.path.basename(strippedString))
        with open(file_path, 'wb') as f:
            f.write(response.content)
            # colocando os arquivos em um zip 
            zip_file.write(file_path, compress_type=zipfile.ZIP_DEFLATED)
# fechando o arquivo zip que foi aberto
zip_file.close()