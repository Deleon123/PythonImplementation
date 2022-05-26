select dc.REG_ANS, roa.Razao_Social,sum(CAST(dc.VL_SALDO_FINAL as DECIMAL(10,2))) total
from
(
    select REG_ANS,VL_SALDO_FINAL, DESCRICAO, Data_tempo 
    from demonstracoes_contabeis_2021_4t
    union all
    select REG_ANS,VL_SALDO_FINAL, DESCRICAO, Data_tempo 
    from demonstracoes_contabeis_restante
) dc inner join relacao_de_operadoras_ativas AS roa 
ON dc.REG_ANS = roa.Registro_ANS  
where dc.DESCRICAO = "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" and LEFT(dc.Data_tempo, 4) = "2021"
group by dc.REG_ANS
ORDER BY total ASC
LIMIT 10

-- Query que descobre as 10 empresas que mais tiveram gastos em EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR, no último ano (ano 2021)