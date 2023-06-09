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