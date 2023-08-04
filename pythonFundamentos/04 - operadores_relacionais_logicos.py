"""
Operadores relacionais (retorna verdadeiro ou falso)
== (igual a)
!= (diferente)
> (maior que)
> (menor que)
>= (maior ou igual)
<= (menor ou igual)
"""

print(1 == 1)  # verifica se é igual em tipo tambem
print(1 == 2)
print(1 == '1')  # numero e string
print('1' == '1')  # String e String
print(1 != '1')
print(1 > 2)
print(1 < 2)
print(3 <= 2)
print(2 >= 2)

idade = 10
#print(idade >= 18)


"""
Operadores lógicos (testa condições com True e False)
and (e) or (ou)
"""

print('or')
print(True or True)# or testa se uma das condições é verdadeira
print(False or True)
print(False or False)# aqui como não tem verdadeiro ele vai retornar False


print('and')
print(True and True)# and testa que as duas(2) condições tem q ser verdadeira
print(False and True)
print(False and False)

#idade > 50 ou totalCompra > 200 20% de desconto
#and
IDADE = 58
TOTALCOMPRA = 200
CONDICAO = IDADE >= 50 and TOTALCOMPRA >= 200

#or
IDADE2 = 58
TOTALCOMPRA2 = 100
CONDICAO2 = IDADE2 >= 50 or TOTALCOMPRA2 >= 200

print(CONDICAO)#aqui tem q atender as duas condições 
print(CONDICAO2)#aqui tem que atender a uma das condições