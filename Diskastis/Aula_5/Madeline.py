vida = 100

def ataque_bad(vida):
    ataque = input()
    if ataque == "Você não tem o que é necessário para escalar.":
        vida -= 20
        print("Eu nunca vou conseguir chegar ao topo :(")
    elif (ataque == "NÓS NUNCA DEVERÍAMOS TER SAÍDO DE CASA! VAMOS MORRER NESSA MONTANHA!"):
        vida -= 50
        print("NAAÃO EU NUNCA DEVERIA TER INVENTADO DE ESCALAR ESSA MONTANHA!")
    return vida

def reacao_mad(vida):
    reacao = input()
    if reacao == "Calma Badeline, nós vamos conseguir.":
        vida += 25
    elif reacao == "Eu sei que somos capazes! Vamos em frente!":
        respiracao = int(input())
        vida += respiracao * 10
    elif reacao == "Madeline, nós estamos com você. Continue!":
        vida += 60
    return vida

while vida > 0 and vida < 150:
    vida = ataque_bad(vida)

    if vida <= 0:
        break
    if vida >= 150:
        break
    vida = reacao_mad(vida)

if vida >= 150:
    print("Madeline chegou ao topo! Ela se senta em um banco para descansar e apreciar a vista.")
elif vida <= 0:
    print("Madeline e Badeline não conseguiram se entender... parece que elas nunca vão ver a cidade de cima.")