historico_dimensoes = ["C-137", "Planeta Squanch"]

usuario_terminal = input()
dimensao_alvo = input()
fluido_portal = input()
status_federacao = input()
acao_historico = input()

print("Sistema Operacional RickOS v3.14 - Inicializando Arma de Portais...")

if fluido_portal == "Suco de Limão":
    print("BURP Morty, você colocou Suco de Limão onde devia ter número! O sistema pifou!")
    exit()

fluido_portal = int(fluido_portal)

if usuario_terminal == "Rick Prime" or usuario_terminal == "Evil Morty":
    print("Alerta Vermelho: Variante perigosa detectada no terminal!")

sem_espacos = dimensao_alvo.replace(" ", "")
if sem_espacos.isalpha() and dimensao_alvo.isupper():
    print("Não precisa gritar, Morty! O painel da arma não é surdo!")

if acao_historico == "anexar":
    historico_dimensoes.append(dimensao_alvo)
    print("Rastro anexado ao final do histórico.")
elif acao_historico == "esconder":
    historico_dimensoes.pop()
    print("Apagando o último rastro... Federação idiota.")
elif acao_historico == "priorizar":
    historico_dimensoes.insert(0, dimensao_alvo)
    print("Sobrescrevendo prioridades. Nova dimensão no topo da lista!")

tamanho_lista = len(historico_dimensoes)

if fluido_portal >= 50 and status_federacao == "alta" and tamanho_lista > 2:
    print("Fuga tática ativada! Saltando por múltiplas dimensões para despistar os insetos!")
elif fluido_portal < 15:
    print("Ferrou! A Arma de Portais tá quase vazia. Pega a nave, Morty!")
elif status_federacao == "baixa" and (dimensao_alvo in historico_dimensoes):
    print(f"Ah, já estivemos na dimensão {dimensao_alvo}. Bora encher a cara no Blips and Chitz!")
else:
    print("Preparando salto interdimensional... Wubba Lubba Dub Dub!")