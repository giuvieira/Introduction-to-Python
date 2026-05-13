N = int(input())

for x in range(N):
    H = int(input())
    P = float(input())
    I = int(input())
    G = float(input())

    energia_inicial = H * P
    perdas = energia_inicial * (I / 100)
    total_energia = energia_inicial - perdas
    gasto = G * total_energia
    print(f"Máquina {x + 1}: {gasto:.2f} moedas")
    
    def consumo_maquina():
        return 0
    
    def gasto_total():
        return 0
    
for x in range(N):
    if total_energia == 0:
        print("Parece que essa coisa nem ao menos funciona")
    elif total_energia >= 0 and total_energia >= 100:
        print(f'"Temos aqui uma máquina formidável, seu consumo de energia é {consumo_maquina}"')
    elif total_energia >= 100 and total_energia >= 300:
        print(f"Você tem certeza que essa coisa não vai explodir? seu consumo de energia é {consumo_maquina}")
    elif total_energia > 300:
        print("Você se importaria de jogar seus explosivos em qualquer outro lugar?")
        break
    
    print(f"Os gastos totais com as maquinas foi de {gasto_total}")
    print(f"A máquina mais cara gasta um total de {gasto} para os cofres de Piltover")