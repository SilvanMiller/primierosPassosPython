postagens = [
    "Hoje passeamos pela orla da praia, no posto 10",  # 0
    "Ontem fizemos trilha na pedra da Gavia",  # 1
    "Amanhã começo o curso de criação de sistemas",  # 2
    "Na casa da mamãe, almoçamos todos juntos",  # 3
]

# TOTAL_PSTGNS = len(postagens) #usando o if e continue
# POST = 0
# while POST < TOTAL_PSTGNS: #enquanto essa condição for verdadeira, faça
#    print(f'{POST} - {postagens[POST]}')
#    POST += 1
#    print("##############")
# print("fim")

# for postagem in postagens: #forma simplificada
#    print(postagem)
#    print("------------------------")

# for indice, postagem in enumerate(postagens): #enumerate vai enumerar as pstgns
#    print(f'{indice} - {postagem}')
#    print("------------------------")


# for indice in range(0, 11): #testando o range (0 a 10)
#    print(indice)


# TOTAL_PSTGNS = len(postagens)
# for indice in range(TOTAL_PSTGNS): #testando o range (0 a 10)
#    print(postagens[indice])


"""
Percorrendo textos, tuplas, set
"""
PALAVRA = "Silvan"
for letra in PALAVRA: #Percorrendo textos
    print(f'- {letra} -')

meses = ('Janeiro', 'Fevereiro', 'Março')
for mes in meses: #percorrendo tuplas 
    print(mes)
    
    
frutas = ('Banana', 'Maça', 'abacaxi', 'Melancia')
for fruta in frutas: #percorrendo tuplas 
    print(fruta)
