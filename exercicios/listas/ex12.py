"""
Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente". 
"""

questao = 0

resposta = input(f'Telefonou para vítima? (S/N) ').upper()

if resposta == 'S':
    questao += 1
resposta = input(f'Esteve no local do crime? (S/N) ').upper()

if resposta == 'S':
    questao += 1
resposta = input(f'Mora perto da vítima ? (S/N) ').upper()

if resposta == 'S':
    questao += 1
resposta = input(f'Devia para vítima ? (S/N) ').upper()

if resposta == 'S':
    questao += 1
resposta = input(f'Já trabalhou com a vítima ? (S/N)').upper()

if resposta == 'S': 
    questao += 1


if questao < 2:
    print('INOCENTE')
elif questao == 2:
    print('SUSPEITO')
elif questao < 5:
    print('CÚMPLICE')
else:
    print('ASSASINO')
"""
perguntas = ['Telefonou para a vítima?', 'Esteve no local do crime?', 'Mora perto da vítima?', 'Devia para a vítima?', 'Já trabalhou com a vítima?']
respostas = []

# Faz as perguntas e armazena as respostas
for pergunta in perguntas:
    resposta = input(pergunta + ' (sim ou não): ').lower()
    while resposta not in ['sim', 'não']:
        resposta = input('Resposta inválida. ' + pergunta + ' (sim ou não): ').lower()
    respostas.append(resposta == 'sim')

# Classifica a pessoa de acordo com suas respostas
num_sim = respostas.count(True)
if num_sim == 5:
    print('Classificação: Assassino')
elif num_sim >= 3:
    print('Classificação: Cúmplice')
elif num_sim == 2:
    print('Classificação: Suspeita')
else:
    print('Classificação: Inocente')

"""