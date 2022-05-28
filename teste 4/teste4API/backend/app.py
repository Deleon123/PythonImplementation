from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os 
from os.path import join, dirname, realpath
import pandas as pd
from flask_cors import CORS
import numpy as np

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

UPLOAD_FOLDER = join(dirname(realpath(__file__)), 'static/files')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db = SQLAlchemy(app)
ma = Marshmallow(app)

# Classe para criação das tabelas do banco de dados

class Operadoras(db.Model):
    registro_ans = db.Column(db.String(200), primary_key = True)
    cnpj = db.Column(db.String(200))
    razao_social = db.Column(db.String(200))
    nome_Fantasia  = db.Column(db.String(200))
    modalidade = db.Column(db.String(200))
    logradouro = db.Column(db.String(200))
    numero = db.Column(db.String(200))
    complemento = db.Column(db.String(200))
    bairro = db.Column(db.String(200))
    cidade = db.Column(db.String(200))
    uf = db.Column(db.String(200))
    cep = db.Column(db.String(200))
    ddd = db.Column(db.String(200))
    telefone = db.Column(db.String(200))
    fax = db.Column(db.String(200))
    endereco_eletronico = db.Column(db.String(200))
    representante = db.Column(db.String(200))
    cargo_representante = db.Column(db.String(200))
    data_registro_ans = db.Column(db.String(200))


    def __init__(self, registro_ans, cnpj, razao_social, nome_Fantasia, modalidade, logradouro, numero, complemento, bairro, cidade, uf, cep, ddd, telefone, fax, endereco_eletronico, representante, cargo_representante, data_registro_ans):
        self.registro_ans = registro_ans
        self.cnpj = cnpj
        self.razao_social = razao_social
        self.nome_Fantasia = nome_Fantasia
        self.modalidade = modalidade
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
        self.uf = uf
        self.cep = cep
        self.ddd = ddd
        self.telefone = telefone
        self.fax = fax
        self.endereco_eletronico = endereco_eletronico
        self.representante = representante
        self.cargo_representante = cargo_representante
        self.data_registro_ans = data_registro_ans

# Classe para criação dos esquemas

class OperadorasSchema(ma.Schema):
    class Meta:
        fields = ('registro_ans','cnpj', 'razao_social', 'nome_Fantasia', 'modalidade', 'logradouro', 'numero', 'complemento', 'bairro', 'cidade', 'uf', 'cep', 'ddd', 'telefone', 'fax', 'endereco_eletronico', 'representante', 'cargo_representante', 'data_registro_ans')

operadora_schema = OperadorasSchema()
operadoras_schema = OperadorasSchema(many='true')

# Retorna todas as operadoras
@app.route('/get', methods = ['GET'])
def get_operadoras():
    all_operadoras = Operadoras.query.all()
    results = operadoras_schema.dump(all_operadoras)
    return jsonify(results)

# Retorna operadora com registro ANS especificado
@app.route('/Search/<search>/<searchType>/', methods = ['GET'])
def serachOperadoras(search, searchType):
    print(search)
    if searchType == 'Razão Social':
        operadorasPesquisa = Operadoras.query.filter(Operadoras.razao_social.ilike('%'+search+'%'))
    elif searchType == 'CNPJ':
        operadorasPesquisa = Operadoras.query.filter(Operadoras.cnpj.ilike('%'+search+'%'))
    elif searchType == 'Registro ANS':
        operadorasPesquisa = Operadoras.query.filter(Operadoras.registro_ans.ilike('%'+search+'%'))
    elif searchType == 'Nome Fantasia':
        operadorasPesquisa = Operadoras.query.filter(Operadoras.nome_Fantasia.ilike('%'+search+'%'))
    elif searchType == 'Modalidade':
        operadorasPesquisa = Operadoras.query.filter(Operadoras.modalidade.ilike('%'+search+'%'))
    elif searchType == 'Logradouro':
        operadorasPesquisa = Operadoras.query.filter(Operadoras.logradouro.ilike('%'+search+'%'))
    elif searchType == 'Número':
        operadorasPesquisa = Operadoras.query.filter(Operadoras.numero.ilike('%'+search+'%'))
    elif searchType == 'Complemento':
        operadorasPesquisa = Operadoras.query.filter(Operadoras.complemento.ilike('%'+search+'%'))
    elif searchType == 'Bairro':
        operadorasPesquisa = Operadoras.query.filter(Operadoras.bairro.ilike('%'+search+'%'))
    elif searchType == 'Cidade':
        operadorasPesquisa = Operadoras.query.filter(Operadoras.cidade.ilike('%'+search+'%'))
    elif searchType == 'UF':
        operadorasPesquisa = Operadoras.query.filter(Operadoras.uf.ilike('%'+search+'%'))
    elif searchType == 'CEP':
        operadorasPesquisa = Operadoras.query.filter(Operadoras.cep.ilike('%'+search+'%'))
    elif searchType == 'DDD':
        operadorasPesquisa = Operadoras.query.filter(Operadoras.ddd.ilike('%'+search+'%'))
    elif searchType == 'Telefone':
        operadorasPesquisa = Operadoras.query.filter(Operadoras.telefone.ilike('%'+search+'%'))
    elif searchType == 'Fax':
        operadorasPesquisa = Operadoras.query.filter(Operadoras.fax.ilike('%'+search+'%'))
    elif searchType == 'Endereço de e-mail':
        operadorasPesquisa = Operadoras.query.filter(Operadoras.endereco_eletronico.ilike('%'+search+'%'))
    elif searchType == 'Representante':
        operadorasPesquisa = Operadoras.query.filter(Operadoras.representante.ilike('%'+search+'%'))
    elif searchType == 'Cargo do representante':
        operadorasPesquisa = Operadoras.query.filter(Operadoras.cargo_representante.ilike('%'+search+'%'))
    elif searchType == 'Data de registro':
        operadorasPesquisa = Operadoras.query.filter(Operadoras.data_registro_ans.ilike('%'+search+'%'))
    results = operadoras_schema.dump(operadorasPesquisa)
    return jsonify(results)    
    

    



@app.route('/uploadCsv')
def uploadcsv():
    # Template para upar o arquivo CSV
    return render_template('uploadcsv.html')

# Recebendo os arquivos upados
@app.route("/uploadCsv", methods=['POST'])
def uploadFiles():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
            # setando o diretório do arquivo
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
            # salvando o arquivo
            uploaded_file.save(file_path)
            parseCSV(file_path)
    return redirect(url_for('uploadcsv'))

def parseCSV(filePath):

    # nome das colunas do csv
    col_names = ['Registro ANS','CNPJ','Razão Social','Nome Fantasia','Modalidade','Logradouro','Número','Complemento','Bairro','Cidade', 'UF','CEP', 'DDD', 'Telefone', 'Fax', 'Endereço eletrônico', 'Representante', 'Cargo Representante', 'Data Registro ANS']
    # usando Pandas para ler o arquivo CSV (pulando as três primeiras linhas)
    csvData = pd.read_csv(filePath, names=col_names, encoding = "ANSI", sep=';', skiprows=3)
    # Substituindo os "nan" por None
    csvData = csvData.replace(np.nan, 'vazio')
    # fazendo o loop nas linhas e adicionando os dados
    
    for index, row in csvData.iterrows():
        registro_ans = row['Registro ANS']
        cnpj = row['CNPJ']
        razao_social = row['Razão Social']
        nome_Fantasia = row['Nome Fantasia']  
        modalidade = row['Modalidade']
        logradouro = row['Logradouro']
        numero = row['Número']
        complemento = row['Complemento']
        bairro = row['Bairro']
        cidade = row['Cidade']
        uf = row['UF']
        cep = row['CEP']
        ddd = row['DDD']
        telefone = row['Telefone']
        fax = row['Fax']
        endereco_eletronico = row['Endereço eletrônico']
        representante = row['Representante']
        cargo_representante = row['Cargo Representante']
        data_registro_ans = row['Data Registro ANS']
        # preenchendo banco de dados
        operadoras = Operadoras(registro_ans, cnpj, razao_social, nome_Fantasia, modalidade, logradouro, numero, complemento, bairro, cidade, uf, cep, ddd, telefone, fax, endereco_eletronico, representante, cargo_representante, data_registro_ans)
        db.session.add(operadoras)
        db.session.commit()
    
if __name__ == "__main__":
    app.run(debug=True)
