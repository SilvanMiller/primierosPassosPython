"""
Listas são como arrays em Javascript
são mutaveis e dinâmicas, heterogênea e indexada
"""
#lista = ["Silvan", "Miguel", "Micaela", "Itamar", "Thereza"]
#print(type(lista))
#print(dir(lista))
#print(lista[0]) #acessar o primeiro elemento da lista 
#print(lista[-1]) #acessar o ultimo elemento da lista
#print(lista[:2]) #aqui ele vai pegar a psção 0 e 1, pegando tudo q vier antes da posição indicada(ex[:3], [:4])
#print(lista[2:5]) #aqui ele vai pegar apartit do 2(Micaela) ate a 5 posição.
#print(lista[::2])#pegou o 0 pulou o 1, pegou o 2 pulou o 3, pegou o 4
print('------------------')
lista = ["Silvan", "Miguel", "Micaela", "Itamar", "Thereza"]
#lista[0] = "Silborg" #alteração na lista
#lista.append("Silvan") #add elementos ao final da lista 
#lista.remove("Novo") #remove um elemento pelo texto e ñ pelo indice

#del lista[0] #assim remove pelo indice 
#del lista[0:2]# aqui deleta essa seleção de indice
#print(lista[0:2]) #uma seleção de indice 

#print(len(lista))#conta qntos itens tem na lista
#print(lista.count("Silvan"))#conta qntos itens desse("Silvan") tem na lista 
#print(lista.index("Itamar")) #aqui tenho o posição do indice

#lista.clear()#limpa a lista completamente
#lista.reverse()#inverte a lista do ultimo para o primeiro
#lista.sort()#Ordena a lista em ordem alfabetica  

print(lista)#pode ver que foi feita a alteração no item 0 da lista(mutavel)