"""
while(condicao)
    executa enguanto a condição é verdadeira
"""

#contador = 1
#while contador <= 4:
#    print(f'execultou{contador}')
#    contador += 1

postagens = [
    "Hoje passeamos pela orla da praia, no posto 10",#0
    "Ontem fizemos trilha na pedra da Gavia",#1
    "Amanhã começo o curso de criação de sistemas",#2
    "Na casa da mamãe, almoçamos todos juntos",#3
]
#totalPostagens = len(postagens) #aqui usando o contador vc pode incluir mais pstgns e vai continuar fnciondo
#post = 0
#while post < totalPostagens:
#    print(postagens[post])
#    print("°°°°°°°°°°°°°°°°°°°°")
#    post += 1
    
#totalPostagens = len(postagens) #aqui nesse exemplo e p/ imprimir o indice na tela junto com a frase
#post = 0
#while post < totalPostagens:
#    print(f'{post} - {postagens[post]}')
#    print("°°°°°°°°°°°°°°°°°°°°")
#    post += 1
    
    
#TOTAL_PSTGNS = len(postagens) #usando um if para decisão
#POST = 0 
#while POST < TOTAL_PSTGNS:
#    print(f'{POST} - {postagens[POST]}')
#    POST += 1
#    if POST != TOTAL_PSTGNS:
#        print("°°°°°°°°°°°°°°°°°°°°")
        
        
TOTAL_PSTGNS = len(postagens) #usando o break para interromper o códgo
POST = 0 
while POST < TOTAL_PSTGNS:
    print(f'{POST} - {postagens[POST]}')
    print("°°°°°°°°°°°°°°°°°°°°")
    POST += 1
    if POST == 2:
        break
print("fim")


TOTAL_PSTGNS = len(postagens) #usando o if e continue
POST = 0 
while POST < TOTAL_PSTGNS:
    print(f'{POST} - {postagens[POST]}')
    POST += 1
    if POST == 1:
        continue
    print("°°°°°°°°°°°°°°°°°°°°")
print("fim")