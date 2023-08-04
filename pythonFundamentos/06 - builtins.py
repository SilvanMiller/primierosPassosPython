#builtins (integrado, imbutido )
#print(type('Miller'))
#print(dir())

#recurso.aplicarfiltro('Miller')#um objeto que acessa um metodo

"""
Conversão de tipos
Tipos: str, int, float, list
"""
print(type('Miller'))#str
print(type(1))#int
print(type(1.5))#float
print(type([10, 20, 30, 40, 50]))#list
#print( 1 + '2')#erro por ser operações com tipos diferentes 
print( 1 + int('2'))#conversão, agora a string é convertida em numero inteiro(int)
print( 1 + float('2.5'))#conversão, agora a string é convertida em numero fracionado(float)
print( '1 - ' + '50')#concatenando coloca um item ao lado do outro
NUMERO = 5
print( str(NUMERO) + '50')#concatenou fazendo a conversão do numero 5 em string

#Conversão automatica

print(10/2)# dois int e o resultado vai ser um float(5.0)


