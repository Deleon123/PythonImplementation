SELECT dc.REG_ANS, roa.Razao_Social, SUM(CAST(dc.VL_SALDO_FINAL as DECIMAL(10,2))-CAST(dc.VL_SALDO_INICIAL as DECIMAL(10,2))) FROM demonstracoes_contabeis AS dc 
JOIN relacao_de_operadoras_ativas AS roa 
ON dc.REG_ANS = roa.Registro_ANS 
where dc.DESCRICAO = "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" and LEFT(dc.Data_tempo, 4) = "2021"
group by dc.REG_ANS 
ORDER BY SUM(CAST(dc.VL_SALDO_FINAL as DECIMAL(10,2))-CAST(dc.VL_SALDO_INICIAL as DECIMAL(10,2))) DESC
LIMIT 10

-- Query que descobre as 10 empresas que mais tiveram gastos em EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR, no último ano (ano 2021)