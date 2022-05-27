from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os 
from os.path import join, dirname, realpath
import pandas as pd


app = Flask(__name__)

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


    def __init__(self, registro_ans, cnpj, razao_social, nome_fantasia, modalidade, logradouro, numero, complemento, bairro, cidade, uf, cep, ddd, telefone, fax, endereco_eletronico, representante, cargo_representante, data_registro_ans):
        self.registro_ans = registro_ans
        self.cnpj = cnpj
        self.razao_social = razao_social
        self.nome_fantasia = nome_fantasia
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
        flieds = ('registro_ans','cnpj', 'razao_social', 'nome_fantasia', 'modalidade', 'logradouro', 'numero', 'complemento', 'bairro', 'cidade', 'uf', 'cep', 'ddd', 'telefone', 'fax', 'endereco_eletronico', 'representante', 'cargo_representante', 'data_registro_ans')

operadora_schema = OperadorasSchema()
operadoras_schema = OperadorasSchema(many='true')

# Retorna todas as operadoras
@app.route('/get', methods = ['GET'])
def get_operadoras():
    all_operadoras = Operadoras.query.all()
    results = operadoras_schema.dump(all_operadoras)
    return jsonify(results)

# Retorna operadora com registro ANS especificado
@app.route('/get/<registro_ans>', methods = ['GET'])
def registros_detale(registro_ans):
    operadora = Operadoras.query.get(registro_ans)
    return operadora_schema.jsonify(operadora)

# Adiciona uma nova operadora
@app.route('/add', methods = ['POST'])
def add_operadoras():
    registro_ans = request.json['registro_ans']
    cnpj = request.json['cnpj']
    razao_social = request.json['razao_social']
    nome_fantasia = request.json['nome_fantasia']
    modalidade = request.json['modalidade']
    logradouro = request.json['logradouro']
    numero = request.json['numero']
    complemento = request.json['complemento']
    bairro = request.json['bairro']
    cidade = request.json['cidade']
    uf = request.json['uf']
    cep = request.json['cep']
    ddd = request.json['ddd']
    telefone = request.json['telefone']
    fax = request.json['fax']
    endereco_eletronico = request.json['endereco_eletronico']
    representante = request.json['representante']
    cargo_representante = request.json['cargo_representante']
    data_registro_ans = request.json['data_registro_ans']

    operadoras = Operadoras(registro_ans, cnpj, razao_social, nome_fantasia, modalidade, logradouro, numero, complemento, bairro, cidade, uf, cep, ddd, telefone, fax, endereco_eletronico, representante, cargo_representante, data_registro_ans)
    db.session.add(operadoras)
    db.session.commit()
    return operadora_schema.jsonify()

@app.route('/')
def index():
    # Template para upar o arquivo CSV
    return render_template('index.html')

# Recebendo os arquivos upados
@app.route("/", methods=['POST'])
def uploadFiles():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
            # setando o diretório do arquivo
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
            # salvando o arquivo
            uploaded_file.save(file_path)
            parseCSV(file_path)
    return redirect(url_for('index'))

def parseCSV(filePath):
    # nome das colunas do csv
    col_names = ['Registro ANS','CNPJ','Razão Social','Nome Fantasia','Modalidade','Logradouro','Número','Complemento','Bairro','Cidade', 'UF','CEP', 'DDD', 'Telefone', 'Fax', 'Endereço eletrônico', 'Representante', 'Cargo Representante', 'Data Registro ANS']
    # usando Pandas para ler o arquivo CSV (pulando as três primeiras linhas)
    csvData = pd.read_csv(filePath, names=col_names, encoding = "ANSI", sep=';', skiprows=3)
    # Substituindo os "nan" por None
    csvData.dropna(inplace=True)
    csvData[(csvData['Registro ANS']!='nan') & (csvData['CNPJ']!='nan') &(csvData['Razão Social']!='nan') &(csvData['Nome Fantasia']!='nan') &(csvData['Modalidade']!='nan') &(csvData['Logradouro']!='nan')&(csvData['Número']!='nan')&(csvData['Complemento']!='nan')&(csvData['Bairro']!='nan')&(csvData['Cidade']!='nan')&(csvData['UF']!='nan')&(csvData['CEP']!='nan')&(csvData['DDD']!='nan') &(csvData['Telefone']!='nan')&(csvData['Fax']!='nan')&(csvData['Endereço eletrônico']!='nan')&(csvData['Representante']!='nan')&(csvData['Cargo Representante']!='nan')&(csvData['Data Registro ANS']!='nan')]
    csvData2 = csvData.where((pd.notnull(csvData)), None)
    # fazendo o loop nas linhas e adicionando os dados
    print('chegou aqui 1')
    for index, row in csvData2.iterrows():
        registro_ans = row['Registro ANS']
        cnpj = row['CNPJ']
        razao_social = row['Razão Social']
        nome_fantasia = row['Nome Fantasia']
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
        print('chegou aqui 2')
        operadoras = Operadoras(registro_ans, cnpj, razao_social, nome_fantasia, modalidade, logradouro, numero, complemento, bairro, cidade, uf, cep, ddd, telefone, fax, endereco_eletronico, representante, cargo_representante, data_registro_ans)
        print('chegou aqui ', index)
        db.session.add(operadoras)
        db.session.commit()

if __name__ == "__main__":
    app.run(debug=True)
