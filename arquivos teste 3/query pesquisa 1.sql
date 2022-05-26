SELECT dc.REG_ANS, roa.Razao_Social, SUM(CAST(dc.VL_SALDO_FINAL as DECIMAL)) despesa FROM demonstracoes_contabeis_2021_4t AS dc 
JOIN relacao_de_operadoras_ativas AS roa 
ON dc.REG_ANS = roa.Registro_ANS 
where dc.DESCRICAO = "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" and CAST(dc.VL_SALDO_FINAL as DECIMAL) < 0
group by dc.REG_ANS 
ORDER BY despesa ASC
LIMIT 10

-- Query que descobre as 10 empresas que mais tiveram gastos em EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR, no último trimestre (data 2021-10-01)