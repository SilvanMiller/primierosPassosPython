"""
Operadores Aritméticos(binários)
Somar(+)
Subtrair(-)
Multiplicar(*)
Dividir(/)
Exponenciação(**)
Módulo (%) -> resto da divisão
"""
NUMERO1 = 10
NUMERO2 = 3

RESULTADO = NUMERO1 + NUMERO2
RESULTADO1 = NUMERO1 - NUMERO2
RESULTADO2 = NUMERO1 * NUMERO2
RESULTADO3 = NUMERO1 / NUMERO2
RESULTADO4 = NUMERO1 ** NUMERO2
RESULTADO5 = NUMERO1 % NUMERO2

# print(RESULTADO, RESULTADO1, RESULTADO2, RESULTADO3, RESULTADO4, RESULTADO5)

# Operadores Unários
VALOR = 10
# VALOR += 1 #incrementação (valor = valor + 1)
# VALOR -= 2 #decremento (valor = valor - 2)
# VALOR /= 2
VALOR *= 2
print(VALOR)



#Precedência de operadores
#0º parêntes(prioridade)
#1º multiplicação e divisão
#2º adição e subtração


RESULTADO = 2 + 2 * 2
RESULTADO1 = 2 + 2 / 2 * 3  # sempre da esquerda para direita
RESULTADO2 = 2 + 2 * 2 // 3 #com duas // ele tira o .333333333
RESULTADO2_1 = 2 + 2 * 2 / 3 #com duas // ele tira o .333333333
RESULTADO3 = 2 + 2 - 2 + 3
RESULTADO4 = (2 - 10) * 3
RESULTADO5 = 2 - 10 * 3

repeticao_string = "A" * 10

print(RESULTADO, RESULTADO1, RESULTADO2, RESULTADO3, RESULTADO4, RESULTADO5, RESULTADO2_1)
print(10 % 8 == 0)
print(repeticao_string)