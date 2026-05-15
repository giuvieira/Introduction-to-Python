caminho = input().split()

def resgate_principe(caminho, resistencia=6, bugigangas=0, posicao=0):
    if resistencia <= 0:
        print("A correnteza está muito forte... não consigo continuar.")
        return False, bugigangas
    
    if posicao == len(caminho):
        return True, bugigangas

    local = caminho[posicao]
    
    if local == "Linguado":
        print("Obrigada, Linguado! Vamos rápido!")
        resistencia -= 1
        resistencia += 2
        
    elif local == "Polvo":
        print("Cuidado com os servos da bruxa!")
        resistencia -= 3
    
    elif local == "~":
        resistencia -= 1

    else:
        resistencia -= 1
        bugigangas += int(local)

    return resgate_principe(caminho, resistencia, bugigangas, posicao + 1)

sucesso, itens = resgate_principe(caminho)

if sucesso:
    print(f"Eric foi salvo! E Ariel ainda guardou {itens} bugigangas na sua gruta.")
else:
    print("O príncipe afundou... Úrsula venceu desta vez.")