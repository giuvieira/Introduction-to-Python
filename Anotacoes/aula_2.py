# exercicio resolvido em aula

humor = input()
senta = int(input())
da_pata = int(input())
fica = int(input())
pega = int(input())

comando = input()

if( comando == 'senta' ):
    
    if( senta >= 3 and humor != 'Brincalhão'):
            print('Byte é o melhor')
    else:
        print('Ele parece estar muito animado para isso!')
    # senta = senta + 1
    senta += 1
    
if( comando == 'da a patinha' ):
    da_pata += 1
    
if( comando == 'fica' ):
    fica += 1
    
if( comando == 'pega' ):
    pega += 1
    
print(f'O nosso novo mascote estava {humor} e aprendeu o(s) seguinte(s) truque(s):')

print(humor)
print(senta)
print(da_pata)
print(fica)
print(pega)

if ( da_pata >= 3 ):
    print('Ele é um bom garoto!')
    
if ( fica >= 3 ):
    print('Ele está aprendendo')
    
if ( pega >= 3 ):
    print('Ele é muito ágil!')