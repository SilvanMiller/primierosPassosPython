"""
List Comprehension (compreensão de lista) -> É uma construção sintatica para criação de uma lista baseada em listas existentes.
"""

#lista = [10, 20, 30] # map 
#nova_lista = list(map(lambda n: n * 2, lista))
#print(nova_lista)

lista = [10, 20, 30] # list comprehension como um map

    #aqui o for vai  percorer cada item na lista e depois armazenar tudo no primeiro item.
#nova_lista_map = [item for item in lista] #[10, 20, 30]
#nova_lista = [item * 2 for item in lista]
#nova_lista = [item + 2 for item in lista]


#nova_lista_filter = [item for item in lista if item >= 20] #[20, 30]
#nova_lista_filter2 = [item for item in lista if item >= 20 if item <30] #[20]

    #aqui é o mesmo do anterior porem ele coloca uma condição fixa para o else por estar a esquerda do for 
#nova_lista_filter3 = [i if i >= 20 and i < 30 else "" for i in lista ] #['', 20, ''] 

#print(nova_lista_map, nova_lista_filter, nova_lista_filter2, nova_lista_filter3)


    #tambem pode ser usada em dicionarios porem é pouco comum, segue o fio 

dicionario = {f'chave{item}': item for item in lista} 
#aqui vamos usar o item para complementar a chave, q Ñ poderia se repetir 
print(dicionario)

#SEM COMPREHENSION 
fruits = ['Maça', 'Banana', 'Uva', 'Laranja', 'kiwi', 'Melão', 'Manga' ]
newlist = []

for item in fruits:
    if "M" in item:
        newlist.append(item)
print(newlist)

#COM COMPREHENSION
fruits2 = ['Maça', 'Banana', 'Uva', 'Laranja', 'kiwi', 'Melão', 'Manga' ]
#SINTAXE
#newlist =[expression for item in iteração if condição == verdadeiro]
newlist2 = [item for item in fruits2 if "a" in item]
print(newlist2)


newlist3 = [item for item in fruits2 if item != "Laranja"]
print(newlist3)


#iterável
newlist4 = [item for item in range(10)]
print(newlist4)


#ITERÁVEL COM CONDIÇÃO
newlist5 = [item for item in range(10) if item < 5]
print(newlist5)

newlist6 = [item if item != "Banana" else "Abacaxi" for item in fruits2]
print(newlist6)


#ITERÁVEL MANIPULAVEL
newlist7 = [item.upper() for item in fruits2]
print(newlist7)


#LISTA EM ORDEM ALFABÉTICA
fruits.sort()
print(fruits)


#LISTA EM ORDEM DECRESCENTE
fruits2.sort(reverse=True)
print(fruits2)


#LISTA QUE NÃO DIFERENCIA MAIÚSCULAS DE MINÚSCULAS
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#COPIAR UMA LISTA
novaListaCopia = list(fruits2)
print(novaListaCopia)
