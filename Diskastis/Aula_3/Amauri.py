dinheiro = int(input())

print(f'A família possui {dinheiro} ainda, talvez ele fique tranquilo hoje')

qtd_compras = 0
custo_total = 0

while dinheiro > 0:

    compra = input()

    if compra == 'Amauri':
        print('Sabia que vocês estão loucos, hora de encerrar essa loucura!')
        break

    custo = int(input())
    qtd_compras += 1
    custo_total += custo
    dinheiro -= custo

    if custo > 500000:
        print(f'Enlouqueceram de vez {custo} reais num(a) {compra}')

    elif custo < 1000:
        print(f'Será que se acalmaram?! {compra} por "somente" {custo} reais')

    else:
        print(f'Gastaram {custo} reais para comprar um(a) {compra}')

    if compra == 'carro':

        modelo = input()

        if modelo == 'chevette':
            print('Relembrando as origens será?')

        elif modelo == 'jeep':
            print('jeep : Será que ele tá se preparando para outra aventura que não irá?')

        elif modelo == 'bmw':
            print('Já to vendo o facebook dele cheio de foto me marcando 🙁')

    if dinheiro <= 0:
        print('Enlouqueceram? Vocês estão falidos')
        break

print(f'{qtd_compras} - {custo_total} reais')