# OBS: É PROIBIDO usar listas para responder essa questão
pedidas = ''
qtd_musicas = 0

setlist = True
while (setlist):
    msc = input()
    if(msc.lower() == 'voa, voa brabuleta'):
        setlist = False
    else:
        qtd_musicas += 1
        if pedidas == "":
            pedidas = msc
        else:
            pedidas = pedidas + " - " + msc
    
print('Bom dia, dona Maria! Aqui vão as músicas mais pedidas de hoje!')
print(f'A quantidade de músicas selecionadas foi {qtd_musicas}')
print(f'Setlist de músicas: {pedidas}')