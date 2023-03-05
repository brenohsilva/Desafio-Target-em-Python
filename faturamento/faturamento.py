import json
import numpy as np

f = open('Desafio Target em Python\\faturamento\dados.json', 'r')
faturamento = json.load(f)

faturamento_diario = [d['valor'] for d in faturamento]

while 0.0 in faturamento_diario:
    faturamento_diario.remove(0.0)

print(faturamento_diario)

menor_valor = np.min(faturamento_diario)
maior_valor = np.max(faturamento_diario)



media_mensal = np.mean(faturamento_diario)

dias_acima_media = 0
for fat in faturamento_diario:
    if fat > media_mensal:
        dias_acima_media += 1


print("Menor Valor ocorrido em um dia do mês: ", menor_valor)
print("Maior Valor ocorrido em um dia do mês: ", maior_valor)
print("Numero de dias no mês em que o valor de faturamento foi superior à media mensal: ", media_mensal)

