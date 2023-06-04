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