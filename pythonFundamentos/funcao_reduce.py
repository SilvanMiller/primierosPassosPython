from functools import reduce

# Reduce(reduzir) -> acumula e reduz uma lista em um unico valor
# não vem dentro do bultins 

#lista = [10, 2, 2]
#acumula = 0
#for item in lista_numero:
#    acumula += item
#print(acumula)
#
#funcao = lambda acumulador, item: acumulador + item #soma
#funcao = lambda acumulador, item: acumulador * item #multiplicação
#funcao = lambda acumulador, item: acumulador - item  #subtração
#resultado = reduce(funcao, lista, 0)
#print(resultado)


lista = [ #dicionario
    {'produto': 'Fone de ouvido', 'preco': 200},
    {'produto': 'Controle video game', 'preco': 400},
    {'produto': 'Celular', 'preco': 1200}
]
funcao = lambda acumulador, produto: acumulador + produto['preco']  
resultado = reduce(funcao, lista, 0)
print(resultado)

