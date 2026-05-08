# Aliens disponíveis: Chama , XLR8, Diamante, Besta e Ultra-T
#  só pode usar esses 5 aliens, se isso acontecer ele não poderá se transformar.

aliens = ('Chama' , 'XLR8', 'Diamante', 'Besta', 'Ultra-T')

Aliens = input()
print('Ben: Tá na hora de virar herói!')

if(Aliens in aliens):
    print(f'Ben: Bora lá, {Aliens}!')
    print('Gwen: Boa, Ben, agora vamos, temos que encontrar Azmuth.')
else:
    print(f'Ben: Droga, Não consigo me transformar no {Aliens}.')
    print('Gwen: Ben Tennyson! Pare com a Bobeira.')

if(Aliens == 'Insectoide'):
    print('Gwen: Ben, de todos os seus bichos, você tentou escolher esse?')
elif(Aliens == 'Fantasmático'):
    print("Ben: Zs'skayr... Ainda bem que o relógio não funcionou.")
elif(Aliens == 'XLR8'):
    print('Ben: Vamos encontrar ele bem rápido com o XLR8!')
elif(Aliens == 'Chama'):
    print('Ben: Eu tô pegando fogo!')