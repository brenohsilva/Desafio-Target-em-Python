SP = '67836.43'
RJ = '36678.66'
MG = '29229.88'
ES = '27165.48'
Outros = '19849.53'

Valor_Total = (float(SP) + float(RJ) + float(MG) + float(ES) + float(Outros))

print(f'Valor total mensal: {Valor_Total:,.2f}\n')

SP_porcentagem = ((float(SP) / Valor_Total)) 
RJ_porcentagem = ((float(RJ) / Valor_Total))
MG_porcentagem = ((float(MG) / Valor_Total))
ES_porcentagem = ((float(ES) / Valor_Total))

print("Percentual de cada Estado: \n")
print(f'São Paulo: {SP_porcentagem:,.2%}')
print(f'Rio de Janeiro: {RJ_porcentagem:,.2%}')
print(f'Minas Gerais: {MG_porcentagem:,.2%}')
print(f'São Espirito Santo: {ES_porcentagem:,.2%}\n')
