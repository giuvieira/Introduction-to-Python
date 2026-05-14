N = int(input())

gasto_total = 0
gasto_max = 0

for x in range(N):
    H = int(input())
    P = float(input())
    I = int(input())
    G = float(input())
    
    def consumo():
        energia_inicial = H * P
        perdas = energia_inicial * (I / 100)
        total_energia = energia_inicial + perdas
        return total_energia
    
    gasto = consumo() * G
    
    if consumo() == 0:
        print("Parece que essa coisa nem ao menos funciona")
    elif consumo() <= 100:
        print(f"Temos aqui uma máquina formidável, seu consumo de energia é {consumo():.2f}")
    elif consumo() <= 300:
        print(f"Você tem certeza que essa coisa não vai explodir? seu consumo de energia é {consumo():.2f}")
    else:
        print("Você se importaria de jogar seus explosivos em qualquer outro lugar?")
        
    gasto_total += gasto
    
    if gasto > gasto_max:
        gasto_max = gasto
    
    print(f"Os gastos totais com as maquinas foi de {gasto_total}")
    print(f"A máquina mais cara gasta um total de {gasto} para os cofres de Piltover")