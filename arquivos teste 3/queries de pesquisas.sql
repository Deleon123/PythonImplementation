SELECT * FROM demonstracoes_contabeis AS dc 
JOIN relacao_de_operadoras_ativas AS roa 
ON dc.REG_ANS = roa.Registro_ANS 
where dc.DESCRICAO = "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" and dc.Data_tempo = "2021-10-01"
