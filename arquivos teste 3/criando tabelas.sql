CREATE TABLE Relacao_de_Operadoras_Ativas (
    Registro_ANS int,
    CNPJ varchar(255),
    Razao_Social varchar(255),
    Nome_Fantasia varchar(255),
    Modalidade varchar(255),
    Logradouro varchar(255),
    Numero varchar(255),
    Complemento varchar(255),
    Bairro varchar(255),
    Cidade varchar(255),
    UF varchar(255),
    CEP varchar(255),
    DDD varchar(255),
    Telefone varchar(255),
    Fax varchar(255),
    Endereco_eletronico varchar(255),
    Representante varchar(255),
    Cargo_representante varchar(255),
    Data_registro_ANS varchar(255)
);

CREATE TABLE Demonstracoes_contabeis (
    Data_tempo varchar(255),
    REG_ANS varchar(255),
    CD_CONTA_CONTABIL varchar(255),
    DESCRICAO varchar(255),
    VL_SALDO_INICIAL varchar(255),
    VL_SALDO_FINAL varchar(255)

);
