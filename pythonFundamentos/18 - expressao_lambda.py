'''
Funções lambda ou expressões lambda que é uma finção anomima
'''

def subtrair(a, b):
    return a - b

#variavel = subtrair #aqui tudo normal que foi a atribuição da função a uma variável
#print(variavel(1, 3)) #aqui utilizando a variável para acessar a função e a execução é normal

subtrair2 = lambda a, b: a - b #aqui criamos uma função anonima e vamos simplificar mais 
print(subtrair2(1, 3)) #dando o mesmo resultado de subtrair 

subtrair3 = lambda a, b: print(f'resultado: {a - b}')
subtrair3(1, 3)

lista = [ #dicionario
    {'produto': 'Fone de ouvido', 'preco': 200},
    {'produto': 'Controle video game', 'preco': 400},
    {'produto': 'Celular', 'preco': 1200}
]

def calcular_desconto(lista, funcao):
    total = 0
    for produto in lista:
        item_desconto = funcao(produto['preco'], 10)
        print(item_desconto)
        
        total += item_desconto 
        
        
    print(f'total: {total}')
    
    
calcular_desconto(lista, lambda a, b: a - b)