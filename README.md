# TesteIntuitiveCare
##Teste para o processo seletivo
###O teste 1 foi feito em python e utilizou as livrarias importadas assim como o teste 2
###O teste 3 contém os SQLs para o banco de dados e para as pesquisas solicitadas no teste 3 
###O teste 4 foi feito em Python usando Flask e VueJS, além de algumas livrarias auxiliares
###Os testes utilizaram como servidor o localhost (XAMP) usando o banco de dados MySQL 
###Teste 3 utiliza o banco de dados "teste3_db" e o teste 4 utiliza o banco de dados "flask"
###O link para acessar a página do teste 4 é: http://localhost:8080, para o teste de importação de CSV é http://localhost:5000/uploadCsv
###Os testes realizados no postman seguem o link do json do Postman: https://www.getpostman.com/collections/a38ace244a27f5f02ce0 
##os possíveis endereços de teste são: 
 
  localhost:5000/get -> retorna todos os dados do banco de dados
  
  localhost:5000/Search/<texto da pesquisa>/<tipo da pesquisa>/

  <texto da pesquisa> O texto da pesquisa pode ser qualquer texto ou número

  <tipo da pesquisa> O tipo da pesquisa pode ser qualquer uma das seguintes strings: 'Razão Social', 'CNPJ', 'Registro ANS', 'Nome Fantasia', 'Modalidade', 'Logradouro', 'Número', 'Complemento', 'Bairro', 'Cidade', 'UF', 'CEP', 'DDD', 'Telefone', 'Fax', 'Endereço de e-mail', 'Representante', 'Cargo do representante' ou  'Data de registro'
  
###Exemplo de pesquisa: localhost:5000/Search/Unimed/Razão Social/
