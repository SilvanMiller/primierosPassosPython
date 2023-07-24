"""
Estruturas condicionais

if(se)
else(senão)

"""
idade = 10
condicao = idade >= 18

if condicao:#essa é a estrutura do if em python que difere de outras linguagens
    print('Maior de idade')
#print('teste')#essa informação vai ser mostrada, pois o python intnd q a linha de codigo acabou na linha 11
else:
    print('Menor de idade')
    

# condicional aninhada
idade2 = 41
if idade2 <=13:
    print('Criança')
elif idade2 <=18:
    print('Adolescente')
elif idade2 <=30:
    print('Adulto1')
else :
    print('Adulto 2')


#Operadores ternário

idade3 = 50
#resultado = ('Menor de idade', 'Maior de idade')[idade3 >= 18]
resultado = 'Maior idade' if idade3>=18 else 'Menor de idade'
print(resultado)