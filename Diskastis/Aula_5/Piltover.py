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
