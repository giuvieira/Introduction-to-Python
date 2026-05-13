pedido = []
iten_pedido = pedido.split(", ")

print("Pedido recebido! Vamos alocar os itens nos caminhões disponíveis.")

falta = iten_pedido.copy()

while True:
    hifen = input()
    if hifen == "-":
        break

    caminhao = hifen.split(", ")

    recebeu = []
    for item in caminhao:
        if item in falta:
            recebeu.append(item)
            falta.remove(item)

    if recebeu:
        print(f"Ótimo, esse caminhão trouxe {recebeu}!")  # ', '.join(recebeu)}!"
    else:
        print("Não encontramos nada que a Carol pediu nesse caminhão.")

    if falta:
        print(f"Ainda precisamos de {falta}.")  # ', '.join(falta)}.")

if not falta:
    print("Conseguimos! A Carol ficará muito feliz :)")
else:
    print("Não conseguimos reunir todos os itens que a Carol precisa :(")
