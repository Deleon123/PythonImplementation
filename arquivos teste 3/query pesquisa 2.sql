select dc.REG_ANS, roa.Razao_Social,sum(CAST(dc.VL_SALDO_FINAL as float)) despesa
from
(
    select REG_ANS,VL_SALDO_FINAL, CD_CONTA_CONTABIL, Data_tempo 
    from demonstracoes_contabeis_2021_4t
    union all
    select REG_ANS,VL_SALDO_FINAL, CD_CONTA_CONTABIL, Data_tempo 
    from demonstracoes_contabeis_restante
) dc inner join relacao_de_operadoras_ativas AS roa 
ON dc.REG_ANS = roa.Registro_ANS  
where dc.CD_CONTA_CONTABIL = "41181" and (LEFT(dc.Data_tempo, 4) = "2021" or RIGHT(dc.Data_tempo, 4) = "2021" )and CAST(dc.VL_SALDO_FINAL as float) < 0
group by dc.REG_ANS
ORDER BY despesa ASC
LIMIT 10

-- Query que descobre as 10 empresas que mais tiveram gastos em EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR, no último ano (ano 2021)