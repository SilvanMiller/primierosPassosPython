# Filter -> filtrar dados
# ele retorna expressões verdadeiras ou falso ex:
# (condição)numero >= 20 / [10(false), 20(true), 30(true)] #e assim criando uma lista com os true ou false


#lista_numero = [10, 20, 25, 30, 35, 40]
#nova_lista = list(filter(lambda n: n >= 20 , lista_numero)) #se essa espressão for true(vrdd) ele cria uma lista
#print(nova_lista)


#lista = [ #dicionario
#    {'produto': 'Fone de ouvido', 'preco': 200},
#    {'produto': 'Controle video game', 'preco': 400},
#    {'produto': 'Celular', 'preco': 1200}
#]
#nova_lista = list(filter(lambda produto: produto['preco'] >= 400, lista))
#print(nova_lista)

#-------------------------------------------

# Aqui estamos percorrendo a lista de nomes e os nomes que tiverem as inicias a e i o u serão enviado a uma nova lista, usando filter e lambda
people_names = ['Silvan', 'Anna', 'João', 'Olivio', 'Eduarda', 'Deborah', 'Ilma', 'Ucrania' ]

# names[0] aqui indica o local que vai acontecer a verificação na ordem de um array onde zero[0] é as primeiras vogais de cada item
print(list(filter(lambda names: names[0].lower() in 'aeiou', people_names))) 

#----------------------------------------------

people_names2 = ['Silvan', 'Alma', 'João', 'Otavio', 'Eddy', 'Deborah', 'India', 'Udison' ]
def names_vowels(names):
    return names[0].lower() in 'aeiou'

filtered_names = filter(names_vowels, people_names2)
print(list(filtered_names))


#----------------------------------------------

#aquarium_creatures = [
#    {'name': 'sammy', 'species': 'shark', 'tank number': 11, 'type': 'fish'},
#    {'name': 'ashley', 'species': 'crab', 'tank number': 25, 'type': 'shellfish'},
#    {'name': 'jo', 'species': 'guppy', 'tank number': , 'type': 'fish'},
#    {'name': 'jackie', 'species': 'lobster', 'tank number': 21, 'type': 'shellfish'},
#    {'name': 'charlie', 'species': 'clownfish', 'tank number': 12, 'type': 'fish'},
#    {'name': 'olly', 'species': 'green turtle', 'tank number': 34, 'type': 'turtle'},
#]

#agora vamos retornar uma sequência de números, digamos que foi um resultado(lista) dos tanques acima com
# inteiros, sequências vazias, booleano e etc
aquarium_tanks  = [11, 25, False, 21, '', 12, 34, 0, [], {}]
# aqui não tivemos uma condição par testar, como nas anteriores, porem com o None ele avalia o que equivale - 
# a 0(zero) de comprimento, e o que é falso Ñ entra na nova lista
filtered_tanks = filter(None, aquarium_tanks )
print(list(filtered_tanks))



aquarium_creatures = [
    {"name": "sammy", "species": "shark", "tank number": "11", "type": "fish"},
    {"name": "ashley", "species": "crab", "tank number": "25", "type": "shellfish"},
    {"name": "jo", "species": "guppy", "tank number": "18", "type": "fish"},
    {"name": "jackie", "species": "lobster", "tank number": "21", "type": "shellfish"},
    {"name": "charlie", "species": "clownfish", "tank number": "12", "type": "fish"},
    {"name": "olly", "species": "green turtle", "tank number": "34", "type": "turtle"}
]

def filter_set(aquarium_creatures, search_string):
    def iterator_func(items):
        for valor in items.values():
            if search_string in valor:
                return True
        return False
    return filter(iterator_func, aquarium_creatures) 

filtered_records = filter_set(aquarium_creatures, '2') #com a string de pesquisa 2, retornou os tanques com 2, o uso da função aninhada permitiu acessar todos os itens e comparar com a string de busca  

print(list(filtered_records))

