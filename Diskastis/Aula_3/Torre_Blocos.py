# torre que Imprima os blocos usando o “#” e nos espaços vazios use "⠀" 
N = (int(input()))

bloco = 1
espaco = N
for i in range(N):
    print(("⠀" * espaco) + ("#" * bloco))
    bloco = bloco + 2
    espaco = espaco - 1