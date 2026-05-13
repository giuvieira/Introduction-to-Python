print('Espelho, espelho meu, quantas maçãs a árvore deu?')

dia_colheita = int(input())

def calculo_macas(dia_colheita):
    if dia_colheita == 0:
        return 0
    elif dia_colheita == 1:
        return 1
    else:
        return calculo_macas(dia_colheita - 1) + calculo_macas(dia_colheita - 2)
    
qnt_macas = calculo_macas(dia_colheita)

print(f'A árvore rendeu {qnt_macas} maçãs no dia {dia_colheita}.')

if qnt_macas < 7:
    print('Oh não! A colheita não foi suficiente para os sete anões.')
else:
    macas_anoes = qnt_macas // 7
    sobra_branca = qnt_macas % 7
    print(f'Cada anão receberá {macas_anoes} maçã(s) e Branca de Neve ficará com a sobra de {sobra_branca} maçã(s).')
    
    if sobra_branca == 0:
        print('A divisão foi perfeita! Nenhuma maçã sobrou para a torta da Branca de Neve.')