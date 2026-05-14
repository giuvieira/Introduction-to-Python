total_recursos = int(input())
povo_piltover = int(input())
povo_zaun = int(input())
povo_total = povo_zaun + povo_piltover

situacao = input()

situacao_zaun = [ 'desastre', 'crise', 'critica', 'normal', 'tranquilo']

def calcular_taxa(situacao):
    if situacao == 'desastre':
        return 0.9
    elif situacao == 'crise':
        return 0.8
    elif situacao == 'critica':
        return 0.7
    elif situacao == 'normal':
        return 0.6
    elif situacao == 'tranquilo':
        return 0.5
    else:
        return povo_zaun / povo_total

taxa = calcular_taxa(situacao)

def distribuir(total_recursos, taxa):
    recursos_zaun = total_recursos * taxa
    recursos_piltover = total_recursos - recursos_zaun
    return recursos_piltover, recursos_zaun

recursos_piltover, recursos_zaun = distribuir(total_recursos, taxa)
razao = recursos_zaun/recursos_piltover

def mensagem():
    if razao >= 0.9:
        print('Zaun receberá uma bolada!!!')
    elif 0.8 <= razao < 0.9:
        print('Quase que Piltover ficava sem nada, pobrezinhos...')
    elif 0.7 <= razao < 0.8:
        print('O negócio vai ficar bom para Zaun hein.')
    elif 0.6 <= razao < 0.7:
        print('Parece que Zaun ainda precisa de ajuda.')
    elif  0.5 <= razao < 0.6:
        print('As coisas estão meio apertadas para Zaun.')
    else:
        print('A situação não está muito favorável para Zaun...')
    
print(f'Foi decidido que será {recursos_piltover:.1f} para Piltover e {recursos_zaun:.1f} para Zaun!')
mensagem()