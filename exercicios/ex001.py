"""
-------- ORDEM DE PRECEDÊNCIA ------------
1º PARENTES ( )
2º EXPONENCIAÇÃO ** pow( )
3º O QUE VIER EM PRIMEIRO: MULTIP*, DIVI/, DIViNT//, REST%
4° SOMA E SUBTRAÇÃO +, -
"""
print(5+3*2) #11
print(3*5+4**2) #31
print(3*(5+4)**2) #243

print('Olá Mundos!')

nome = input('Digite seu nome: ')
print('É um prazer te conhecer, {}!'.format(nome))


n1=float(input('digite um número: '))
n2=float(input('digite nais um número: '))
soma = n1 + n2
print('A soma de {} e {} é {}'.format(n1, n2, soma))
print(f'A soma de {n1} e {n2} é {soma:.2f}')


#aqui todo input sempre retorar uma strg(Claro salvo os que vc formatou como no caso acima)
a = input('Digite algo: ')
print(f'O tipo desse valor é {type(a)}') #aqui estamos perguntando o tipo que foi digitado
print(f'Só tem espaços? {a.isspace()}') #aqui estamos perguntando se tem espaços
print(f'É um número? {a.isnumeric()}') #aqui estamos perguntando se é um numero basicamente
print(f'É alfabetico? {a.isalpha()}')
print(f'É alfanumerico? {a.isalnum()}')
print(f'Esta em maiúsculas? {a.isupper()}') #aqui estamos perguntando se esta em maiusculo basicamente
print(f'Esta em minúsculas? {a.islower()}') #aqui estamos perguntando se esta em minusculo basicamente
print(f'Esta capitalizado? {a.istitle()}') #aqui estamos perguntando se esta com a primeira letra maiuscola




