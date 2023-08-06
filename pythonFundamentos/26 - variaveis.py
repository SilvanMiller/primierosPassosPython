'''
CONSTANTES = 'Variáveis' que não vão mudar.
Muitas condições no mesmo if. ex if blabla == bla and blabla => bla or ... :

'''

velocidade = 61 #velocidade atual do carro
local_carro = 198 #local em que o carro está na estrada

# são CONSTANTES e são sempre em maiusculo para ñ ter mudança no código.
RADAR_1 = 60 #velocidade máxima do radar1
LOCAL_1 = 100 #local onde o radar 1 está
RADAR_RANGE = 1 #a distância onde o radar pega o carro

#variáveis para melhorar o código
dentro_r1 = LOCAL_1 - RADAR_RANGE
fora_r1 = LOCAL_1 + RADAR_RANGE
vel_carro_passou_r1 = velocidade > RADAR_1
carro_passou_r1 = local_carro >= dentro_r1 and local_carro <= fora_r1
carro_multado = carro_passou_r1 and vel_carro_passou_r1

if vel_carro_passou_r1:
    print(f'{velocidade}km, carro passou no Radar 1')
if carro_passou_r1:
    print('Carro passou no Radar 1')
if carro_multado:
    print('Carro multado no Radar 1')

#VARIAVEIS EM UMA LINHA -------------------------------
x, y, z = 'Orange', 'Banana', 'Cherry'
print(z, x, y)

#UM VALOR PARA VÁRIAS VARIAVEIS -------------------------------
x = y = z = 'Silvan'
print(x)
print(y)
print(z)

#DESCOMPACTAR UMA COLEÇÃO EM VARIAVEIS -------------------------------
fruits = ['maça', 'banaba', 'uva']
x, y, z = fruits
print(x)
print(y)
print(z)

#GERAR VÁRIAS VARIAVEIS -----------------------------------------
x = 5
y = 'Jhon'
print(y, x)

#CRIAR UMA VARIAVEL DENTRO DA FUNÇÃO -----------------------------------------
x = 'global'

def minhaFuncao():
    x = 'local'
    print('Variavel ' + x)

minhaFuncao()

print('Variavel ' + x)

#TIPOS DE VARIAVEIS - e = potencia de 10 ------------------------------------
x = 3+5j
y = 12E4
z = -87.7e100

print(type(x), x)
print(type(y), y)
print(type(z), z)





