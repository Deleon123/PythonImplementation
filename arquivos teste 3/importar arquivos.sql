LOAD DATA LOCAL INFILE 'arquivos teste 3/Relatorio_cadop teste 3.csv'
INTO TABLE relacao_de_operadoras_ativas
character set utf8
FIELDS TERMINATED BY ';'
ENCLOSED BY ''
LINES TERMINATED BY '\r\n'
IGNORE 3 ROWS;

LOAD DATA LOCAL INFILE 'arquivos teste 3/1T2020.csv'
INTO TABLE Demonstracoes_contabeis_restante 
character set utf8
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE 'arquivos teste 3/2T2020.csv'
INTO TABLE Demonstracoes_contabeis_restante 
character set utf8
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE 'arquivos teste 3/3T2020.csv'
INTO TABLE Demonstracoes_contabeis_restante 
character set utf8
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE 'arquivos teste 3/4T2020.csv'
INTO TABLE Demonstracoes_contabeis_restante 
character set utf8
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE 'arquivos teste 3/1T2021.csv'
INTO TABLE Demonstracoes_contabeis_restante 
character set utf8
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE 'arquivos teste 3/2T2021.csv'
INTO TABLE Demonstracoes_contabeis_restante 
character set utf8
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE 'arquivos teste 3/3T2021.csv'
INTO TABLE Demonstracoes_contabeis_restante 
character set utf8
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE 'arquivos teste 3/4T2021.csv'
INTO TABLE Demonstracoes_contabeis_2021_4T 
character set utf8
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;


