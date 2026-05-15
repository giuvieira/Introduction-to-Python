dia_inicial = int(input())

# etapa 1
def class_alvo(nivel_ameaca, armado):
    if nivel_ameaca >= 7 and armado:
        return "Elite"
    
    elif nivel_ameaca >= 7 and not armado:
        return "Executor"
    
    elif 4 <= nivel_ameaca < 7 and armado:
        return "Veterano"
    
    elif 4 <= nivel_ameaca < 7 and not armado:
        return "Operador"
    
    else:
        return "Iniciante"


# etapa 2
def anal_tentativa(tentativas):
    lista_tentativas = tentativas.split()

    tentativas_int = []

    for tentativa in lista_tentativas:
        tentativas_int.append(int(tentativa))

    soma_tenta = 0

    for tentativa in tentativas_int:
        soma_tenta += tentativa

    qtd_tentativas = len(tentativas_int)

    if soma_tenta % qtd_tentativas == 0:
        return True, qtd_tentativas
    
    else:
        return False, qtd_tentativas


# etapa 3
def ataque_refletido(ataques, favoritos=[3, 5]):
    lista_ataques = ataques.split()

    ataques_int = []

    for ataque in lista_ataques:
        ataques_int.append(int(ataque))

    refletidos = 0

    for ataque_num in ataques_int:
        for favorito in favoritos:
            if ataque_num % favorito == 0:
                refletidos += 1
                break

    return refletidos


print("Entendo… Vamos começar do começo.")

for dia_atual in range(dia_inicial, -1, -1):

    print()

    print(f"====== Restam {dia_atual} dias. ======")

    musica_input = input()
    parte_msc = musica_input.split(" - ")

    musica = parte_msc[0]
    autor = parte_msc[1]

    print(f"Escutando: {musica} - {autor}")

    alvo = input()
    parte_alvo = alvo.split(" - ")

    nome_alvo = parte_alvo[0]
    nivel_ameaca = int(parte_alvo[1])

    armado_str = parte_alvo[2]

    if armado_str == "sim":
        armado = True
    else:
        armado = False

    if autor == "DJ Electrohead" and nome_alvo == "DJ Electrohead":
        print("DJ Electrohead é morto na sua frente. Lhe avisaram para NÃO FALAR com ele.")
        continue

    classificacao = class_alvo(nivel_ameaca, armado)

    print(f"Analisando alvo: {nome_alvo}... Classificação: {classificacao}")

    tentativas = input()

    sucesso, qtd_tentativas = anal_tentativa(tentativas)

    if sucesso:
        print(f"Missão Completa. | Manipulação temporal: {qtd_tentativas} tentativa(s)")

    else:
        print("Missão Fracassou! ZERO não foi capaz de assassinar o alvo e acabou morrendo. Nunca descobrirá o que realmente aconteceu.")
        break

    ataques = input()

    refletidos = ataque_refletido(ataques)

    print(f"Dragão refletiu {refletidos} ataque(s)!")

else:
    print()
    print("====== FIM DAS MISSÕES ======")
    print("Parabéns Subject ZERO! Seu trabalho deve ser recompensado. Nova dose do seu remédio esta aqui.")