materias = "Uniforme", "Isotônico", "Raquete", "Toalha"

nf_uniforme = 0
nf_isotonico = 0
nf_raquete = 0
nf_toalha = 0

cont_sabotagem = 0

while True:
    opcao = input()

    if opcao == "FIM":
        break

    if opcao == "Uniforme":
        nf_uniforme += 1
        print(f"Tava faltando camisa! Agora temos {nf_uniforme} uniforme(s)")

    elif opcao == "Isotônico":
        nf_isotonico += 1
        print(f"Bora garantir a hidratação! Agora temos {nf_isotonico} isotônico(s)")

    elif opcao == "Raquete":
        nf_raquete += 1
        print(f"Mais uma raquete saindo! Agora temos {nf_raquete} raquete(s)")

    elif opcao == "Toalha":
        nf_toalha += 1
        print(f"Mais uma toalha saindo! Agora temos {nf_toalha} toalha(s)")

    elif opcao == "Sabotagem":
        material = input()
        cont_sabotagem += 1

        if material == "Uniforme" and nf_uniforme > 0:
            nf_uniforme -= 1
            print("O sueco está roubando as camisas de Hugo!")

        elif material == "Isotônico" and nf_isotonico > 0:
            nf_isotonico -= 1
            print("O sueco está sabotando a hidratação de Hugo!")

        elif material == "Raquete" and nf_raquete > 0:
            nf_raquete -= 1
            print("O sueco está roubando as raquetes de Hugo!")

        elif material == "Toalha" and nf_toalha > 0:
            nf_toalha -= 1
            print("O sueco está roubando as toalhas de Hugo!")


cont_materias = nf_uniforme + nf_isotonico + nf_raquete + nf_toalha

print("Bora ver o relatório final dos materiais!")
print(f"Uniforme: {nf_uniforme} unidade(s).")
print(f"Isotônico: {nf_isotonico} unidade(s).")
print(f"Raquete: {nf_raquete} unidade(s).")
print(f"Toalha: {nf_toalha} unidade(s).")

if cont_materias == 0 and cont_sabotagem > 0:
    print("Droga... Truls Möregårdh conseguiu sabotar os materiais completamente!")
elif cont_materias == 0:
    print(
        "Vish... Parece que vão faltar materiais para garantir a vitória do nosso atleta."
    )
elif nf_uniforme == 0 or nf_isotonico == 0 or nf_raquete == 0 or nf_toalha == 0:
    print("Ta faltando algumas coisas, mas para Hugo Calderano tudo é possível!!!")
else:
    print("Tudo pronto! Não vai faltar nada para mais um título de Hugo Calderano!")
