"""
Introdução ao try/except
try -> tentar executar o código 
except -> ocorreu algum erro ao tentar executar
"""


num = input('Vou dobra o número que vc digitar: ')

try:
    print(f'STR: {num}')
    dobro = float(num)
    print(f'Float: {num}')
    print(f'O dobro de {num} é {dobro * 2:.2f}')
except:
    print(f'você digitou {num}, isso não é um número.')
