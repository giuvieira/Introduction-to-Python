print('Olá, eu sou o BMO! Prazer em te conhecer, estranho!')
print('Qual é o seu nome?')
Nome = input()

if Nome == "Finn" or Nome == "Jake":
    print('Caramba, que coincidência! Você tem o mesmo nome de um amigo meu!')
print('Gostei do seu nome!') 

print('Quantos anos você tem?')
Idade = int(input())

if Idade == 12:
    print('Nossa, você tem a mesma idade do meu amigo Finn')
print('Entendi!')

print('Ei, qual princesa desse mundo é a mais bonita pra você?')
Princesa = input()

if Princesa == 'Princesa de Fogo' or Princesa == 'Princesa Jujuba' :
    print('Meu amigo Finn vai ficar com ciúmes de você!')
    
print('Finalmente chegamos!')
print(f'Foi um prazer te conhecer, {Nome}! Boa sorte para encontrar a {Princesa} :)')