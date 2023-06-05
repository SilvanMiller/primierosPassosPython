# Map -> Mapear os dados, percorrer e alterá-los

#lista_numero = [10, 20, 30]

#nova_lista = map(lambda n: n * 3, lista_numero)
#print(type(nova_lista))
#print(type(lista_numero))

#print(nova_lista) #para poder receber os dados preciso fazer a conversão assim.
#print(list(nova_lista)) #aqui sim ele me retorna uma lista com os resultado


#lista = [ #dicionario
#    {'produto': 'Fone de ouvido', 'preco': 200},
#    {'produto': 'Controle video game', 'preco': 400},
#    {'produto': 'Celular', 'preco': 1200}
#]

#def calcular_desconto(produto):
#    produto['preco'] = produto['preco']-10
#    return produto

#nova_lista = list(map(calcular_desconto, lista))
#print(nova_lista)


#numbers = [10, 15, 21, 33, 42, 55]
#mapped_numbers  = list(map(lambda n: n * 2 + 3, numbers))
#print(mapped_numbers)


aquarium_creatures = [
    {'name': 'sammy', 'species': 'shark', 'tank number': 11, 'type': 'fish'},
    {'name': 'ashley', 'species': 'crab', 'tank number': 25, 'type': 'shellfish'},
    {'name': 'jo', 'species': 'guppy', 'tank number': 18, 'type': 'fish'},
    {'name': 'jackie', 'species': 'lobster', 'tank number': 21, 'type': 'shellfish'},
    {'name': 'charlie', 'species': 'clownfish', 'tank number': 12, 'type': 'fish'},
    {'name': 'olly', 'species': 'green turtle', 'tank number': 34, 'type': 'turtle'},
]
def assign_to_tank(aquarium_creatures, new_tank_number):
    def apply(n):
        n['tank number'] = new_tank_number
        return n
    return map(apply, aquarium_creatures)

assigned_tank = assign_to_tank(aquarium_creatures, 42)
print(list(assigned_tank))