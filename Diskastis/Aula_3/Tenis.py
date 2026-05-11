materias  = 'Uniforme', 'Isotônico', 'Raquete', 'Toalha'

nf_uniforme = 0
nf_isotonico = 0
nf_raquete = 0
nf_toalha = 0

cont_materias = 0
cont_sabotagem = 0

Entrada = True
while Entrada:
    opcao = input()
    if(materias != opcao):
        if(opcao == 'Uniforme'):
            nf_uniforme += 1
        elif(opcao == 'Isotônico'):
            nf_isotonico += 1
        elif(opcao == 'Raquete'):
            nf_raquete += 1
        elif(opcao == 'Toalha'):
            nf_toalha += 1
        elif(opcao == 'Sabotagem'):
            cont_sabotagem += 1
        break

cont_materias = (nf_uniforme + nf_isotonico + nf_raquete + nf_toalha)

print('Bora ver o relatório final dos materiais!')
print('Uniforme: {nf_uniforme} unidade(s).')
print('Isotônico: {nf_isotonico} unidade(s).')
print('Raquete: {nf_raquete} unidade(s).')
print('Toalha: {nf_toalha} unidade(s).')

if(cont_materias == 0 and cont_sabotagem <= 0):
    print('Droga... Truls Möregårdh conseguiu sabotar os materiais completamente!')
elif(cont_materias == 0 and cont_sabotagem < 0):
    print('Vish... Parece que vão faltar materiais para garantir a vitória do nosso atleta.')
elif cont_materias <= 0 and (uniforme <= 1 and isotonico <= 1 and raquete <= 1 and toalha <= 1) and cont_sabotagem < 0:
    print('Ta faltando algumas coisas, mas para Hugo Calderano tudo é possível!!!')
else:
    print('Tudo pronto! Não vai faltar nada para mais um título de Hugo Calderano!')