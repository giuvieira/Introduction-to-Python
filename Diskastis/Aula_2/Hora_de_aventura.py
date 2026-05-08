# O BMO vai querer saber 3 coisas sobre você:

# Seu nome (string)
# Sua idade (int)
# A princesa que você acha mais bonita (string)

print('Olá, eu sou o BMO! Prazer em te conhecer, estranho!')
print('Qual é o seu nome?')
Nome = input()

# if (Nome == "Finn" | "finn" | "Jake" | "jake") {
#     return('Caramba, que coincidência! Você tem o mesmo nome de um amigo meu!')
# } else {
#     print('Gostei do seu nome!')
# }

# > dois pontos, indentação e 'or'
if Nome == "Finn" or "finn" or Nome == "Jake" or "jake":
    print('Caramba, que coincidência! Você tem o mesmo nome de um amigo meu!')
print('Gostei do seu nome!') 

print('Quantos anos você tem?')
Idade = int(input())

# if ( Idade = 12) {
#     return('Nossa, você tem a mesma idade do meu amigo Finn')
# } else {
#     print('Entendi!')
# }

if Idade == 12:
    print('Nossa, você tem a mesma idade do meu amigo Finn')
print('Entendi!')

print('Ei, qual princesa desse mundo é a mais bonita pra você?')
Princesa = input()

if Princesa == 'Princesa de Fogo' or 'princesa de fogo' or Princesa == 'Princesa Jujuba' or 'princesa jujuba' :
    print('Meu amigo Finn vai ficar com ciúmes de você!')
    
print('Finalmente chegamos!')
print(f'Foi um prazer te conhecer, {Nome}! Boa sorte para encontrar a {Princesa} :)')