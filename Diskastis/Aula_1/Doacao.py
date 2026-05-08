# Problem Statement

# conjunto de 64 - stack
# HÁ 3 VILAS. acumulou vários packs de ferro e decidiu dividir todos os packs igualmente entre as vilas
# Para ser justo, ele prometeu jogar fora todo o ferro que sobrasse.

# P - número natural (3 <= P) - input que diz quantos pack tem 
# V - número natural - output que diz o num de pack a ser dividido 
# F - número natural - output que diz o num de pack a ser descartado 

# vila = 3
# p = int(input('Digite a quantidade de packs: '))

# #num_pack = int((p) * 64)

# V = int((p) // (vila))
# F = int((p) % (vila))

# print(f'{V}')
# print(f'{F}')

# p = int(input())

# V = int((p) // 3)
# F = int((p) % (V))

# print(f'{V}')
# print(f'{F}')

# resposta aceita:

p = int(input())

V = p // 3
F = p % 3

print(V)
print(F)