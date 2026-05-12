doces = int(input())
jogador1 = input()
jogador2 = input()

if jogador1 != 'Arthur' and jogador2 != 'Arthur':
    print('Epa!!! E cadê o dono dos doces??')

else:
    print('A batalha vai começar!')

    rodada = 0
    resto = doces % 10

    while doces > 0:

        rodada += 1

        vida1 = 10
        vida2 = 10

        if rodada == 1 and resto != 0:
            print(f'Pra aquecer, essa primeira vale menos, só {resto} doces!')
            doces -= resto

        else:
            print(f'Batalha número {rodada}!')
            doces -= 10

        while vida1 > 0 and vida2 > 0:

            jogada1 = input()
            jogada2 = input()

            if jogada1 == jogada2:
                print('Eita, jogaram a mesma coisa dessa vez.')

            elif jogada1 == 'papel' and jogada2 == 'tesoura':
                vida1 -= 3
                vida2 += 1

            elif jogada1 == 'tesoura' and jogada2 == 'papel':
                vida2 -= 3
                vida1 += 1

            elif jogada1 == 'pedra' and jogada2 == 'papel':
                vida1 -= 2
                vida2 += 2

            elif jogada1 == 'papel' and jogada2 == 'pedra':
                vida2 -= 2
                vida1 += 2

            elif jogada1 == 'pedra' and jogada2 == 'tesoura':
                vida2 -= 4

            elif jogada1 == 'tesoura' and jogada2 == 'pedra':
                vida1 -= 4

            if vida1 < 0:
                vida1 = 0

            if vida2 < 0:
                vida2 = 0

            if jogada1 != jogada2:
                print(f'Esse turno terminou com {jogador1} tendo {vida1} de vida e {jogador2} tendo {vida2}!')

        if vida1 > 0:
            vencedor = jogador1

        else:
            vencedor = jogador2

        print(f'A rodada {rodada} vai para {vencedor}, que garante seus doces!')