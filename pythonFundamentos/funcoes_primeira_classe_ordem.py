'''
Funções como objetos de primeira classe, são funções que se comportam
como qualquer tipo nativo de uma determinada linquagem 
'''

def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b

#lista = [somar, subtrair] #aqui estamos atribuindo a lista duas funções
#for funcao in lista: #a funcao vai percorer os item da lista
#    print(funcao(1, 2))

#a = somar #sequindo o mesmo conceito de atribuir a função 
#print(a(2, 2))


#Funções de ordem superior são funções que recebem funções como parâmetros 
#e/ou retornam funções como resposta

carrinhos_compras = [ #dicionario
    {'produto': 'Fone de ouvido', 'preco': 200},
    {'produto': 'Controle video game', 'preco': 400},
    {'produto': 'Celular', 'preco': 1200}
]

#print(carrinhos_compras)


def calcular_desconto(lista, funcao):
    total = 0
    for produto in lista:
        #print(produto['preco'])
        
        item_aumento_preco = funcao(produto['preco'], 10)
        print(item_aumento_preco)
        
        #item_desconto = funcao(produto['preco'], 10)
        #print(item_desconto)
        
        total += item_aumento_preco #item_desconto 
        
        
    print(f'total: {total}')
    
    
calcular_desconto(carrinhos_compras, somar)
#calcular_desconto(carrinhos_compras, subtrair)
