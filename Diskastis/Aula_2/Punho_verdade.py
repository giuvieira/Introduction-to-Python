# dois números inteiros de 1 a 1000 para as ações que Lara e Irmão do Jorel irão fazer 
# um número inteiro de 1 a 100 para o nível de dificuldade dos inimigos.

velocidade_IJ = int(input())
velocidade_LR = int(input())
dificuldade_inimigos = int(input())

# produto das velocidades dos dois jogadores dividido pela dificuldade dos inimigos que aparecerão.
PF = velocidade_IJ * velocidade_LR / dificuldade_inimigos

if( PF <= 65000):
    print('BRUTAL! Ninguém jamais conseguiu alcançar as pontuações fantásticas do Jorel.')
elif( 65000 < PF <= 99000):
    print('INCRÍVEL! A dupla conseguiu alcançar o top 10 nas pontuações do jogo.')
elif( 99000 < PF <= 153000 ):
    print('SENSACIONAL!! Os jogadores conseguiram alcançar o pódio do jogo ao lado das outras pontuações do Jorel.')
else:
    print('IMPOSSÍVEL!!! A DUPLA IMPLACÁVEL FOI CAPAZ DE QUEBRAR O RECORDE INALCANÇÁVEL DO JOREL!')