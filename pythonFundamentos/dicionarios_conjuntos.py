"""
Lista e Tuplas: indexadas
lista = ["Silvan","Miguel"] 
lista: 0=>"Silvan", 1=>"Miguel" # aqui vc recebe o indice ao add o item
dicionario estrutura de CHAVE(keys) : VALOR(values) 
"""
dicionario = {
    'correr': 'deslocar-se ou mover-se rapidamente', #itens CHAVE(keys) : VALOR(values)
    'ligar' : 'estabelecer uma comunicação'
}
print(dicionario['ligar']) #aqui NÃO pegamos por numero e sim pela chave

carro = {
    'modelo': 'Fusca',
    'marca' : 'volkswagem',
    'ano' : 1973,
    'donos' : ['Silvan', 'Miguel']
}
print(tuple(carro)) #trnsformando as keys em tupla
print(type(carro)) #tipo 
print(dir(carro))

print(carro['modelo']) #acessar as keys e obter os seus valores 
carro['donos'].append('Itamar') #aqui acresentamos um item a lista donos
print(carro['donos'][2]) #aqui pegamos o item na seleção 2 da lista donos

carro ['Km'] = 8500 #acresentando item ao dicionario carro 
carro ['ano'] = 1979 #modificando um valor da keys 

carro.update({'ano':1979, 'Km':6500}) #modificando e acresentando 
carro.pop('ano') #remove o item do dicion/conj
valor = carro.pop('ano') #guarda o valor que foi removido
print(len(carro))

print(carro.keys())
print(carro.values())
print(carro.items()) #aqui ja cria uma tupla
print(carro.get('ano', 'padrão')) #aqui ele buscar o valor do key e se ñ achar, usa o padrão
carro.clear() #novamente limpando o dicio/conj

print(carro)


"""
set => conjunto
"""
itens = {"Miguel", "Micaela", "Thereza", "Thereza"}
print(type(itens))
print(itens)

carros = {"fusca", "golf", "fiat 147"}
carros2 = {"BMW", "fusca", "passat"}
novo = carros.union(carros2) #aqui foi a união, porem ele NÃO repetiu fusca
novo = carros.intersection(carros2) # o que tem em comum entre os 2(carros e carros2)
print(novo)
print(len(novo))
carros.add("passat")
carros.remove("fusca")
print(carros)


