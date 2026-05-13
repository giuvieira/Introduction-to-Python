tripulantes = ["Zaphod Beeblebrox", "Ford Prefect", "Arthur Dent", "Marvin"]

n = int(input())

print("Édipo: Inicializando sistema de embarque. Tripulantes atuais: Zaphod Beeblebrox, Ford Prefect, Arthur Dent, Marvin")

for _ in range(n):
    evento = input().split()
    tipo = evento[0]
    
    if tipo == "embarcar":
        nome = " ".join(evento[1:])
        tripulantes.append(nome)
        if nome == "Trillian":
            print("Finalmente alguém sensata a bordo! Bem-vinda, Trillian!")
    
    elif tipo == "priorizar":
        nome = " ".join(evento[1:])
        if nome in tripulantes:
            tripulantes.remove(nome)
            tripulantes.insert(0, nome)
            if nome == "Zaphod Beeblebrox":
                print("EU SOU O PRESIDENTE DA GALAXIA! Primeiro lugar é pouco!")
            elif nome == "Ford Prefect":
                print("Sou um escritor do Guia! Mereço destaque!")
    
    elif tipo == "remover":
        nome = " ".join(evento[1:])
        if nome in tripulantes:
            tripulantes.remove(nome)
            if nome == "Marvin":
                print("Ninguem se importa comigo mesmo. Tchau")
            elif nome == "Arthur Dent":
                print("Eu só queria poder tomar chá... vou descer no próximo planeta")
    
    elif tipo == "mover":
        indice = int(evento[-1])
        nome = " ".join(evento[1:-1])
        if nome in tripulantes:
            tripulantes.remove(nome)
            if indice <= len(tripulantes):
                tripulantes.insert(indice, nome)
            else:
                tripulantes.append(nome)

if len(tripulantes) == 0:
    print("Édipo: Graças à improbabilidade, os novos comandantes são: ninguém... a nave está vazia!")
else:
    comandantes = tripulantes[:3]
    if len(comandantes) == 1:
        print(f"Édipo: Graças à improbabilidade, os novos comandantes são: {comandantes[0]}.")
    elif len(comandantes) == 2:
        print(f"Édipo: Graças à improbabilidade, os novos comandantes são: {comandantes[0]} e {comandantes[1]}.")
    else:
        print(f"Édipo: Graças à improbabilidade, os novos comandantes são: {comandantes[0]}, {comandantes[1]} e {comandantes[2]}.")
    
    restantes = tripulantes[3:]
    if restantes:
        print("Convocando tripulantes:")
        for passageiro in restantes:
            print(f"- {passageiro}")