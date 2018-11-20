'''

adulto  = Mae ou Pai
crianca = Paciente
tipo    = Pediatria e tals
data    = Dia Formatado
hora    = Hora que Estiver no Banco
unidade = Nome do Hospital
local   = Endereço Completo


'''

adulto  = "Marly"
crianca = "Matheus Oliveira"
tipo    = "Pediatria"
data    = "24/11/2018"
hora    = "14:30"
unidade = "Metropolitano"
local   = "Av.Civit, nº 45"


falabot = f" Caro(a) {adulto}, responsável pelo(a) paciente {crianca}, não esqueça da consulta médica {tipo} marcada para o dia {data}, às {hora}, na Unidade de Saúde {unidade}, localizada no endereço {local}. Até mais. "

print(falabot)