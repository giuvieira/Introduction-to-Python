# print('Jojo, Guardiã das Frases de Poder, sua missão é reunir todas as frases lendárias para restaurar a harmonia do reino. A cada frase adicionada, um novo feitiço se ativa.')

qnt_nova_frase = int(input())

grimorio = ['Que tiro foi esse?', 'Segura a marimba', 'Tá com raiva? Morde as costas', 'Bateu de frente é só rajadão']

for i in range(qnt_nova_frase):
    nova_frase = input()
    grimorio.append(nova_frase)

elemento = []

for frase in grimorio:
    if frase not in elemento:
        elemento.append(frase)
        print(f'"{frase}": {grimorio.count(frase)}')

grimorio.sort()
print(f'{grimorio}')