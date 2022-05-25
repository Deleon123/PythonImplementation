# importando livarias necessárias
import tabula

# Conversão do PDF em CSV
tabula.convert_into('Outputs/Anexo_I_Rol_2021RN_465.2021_RN473_RN478_RN480_RN513_RN536.pdf','Outputs/Teste_Deleon.csv', output_format='csv', pages='all')

