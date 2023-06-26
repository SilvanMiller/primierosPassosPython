from random import randint
from datetime import date
from time import sleep

print('EX001 - Escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5. Peça para o usuário tentar descobrir qual o número escolhido pelo computador.')

jogador = int(input('Digite um numero inteiro qualquer: '))
computador = randint(0, 5)
print('PROCESSANDO...')
sleep(2)

if computador == jogador:
    print(f'Você digitou o número {jogador} e pensei em {computador}, não é que você acertô mizeravi, parabéns ')
else:
    print(f'Você digitou o número {jogador} e pensei em {computador}, é eu ganhei, continue tentando adivinhar. \n\n')
    
    
print('EX002 - Escreva um programa que leia a velocidade de um carro e se ele ultrapassar 80km/h, mostre uma mensagem dizendo que foi multado e a multa custa R$ 7,00 por cada km acima do limite.')
velocidade = float(input('Digite a velocidade atual do carro: '))

if velocidade > 80:
    print('MULTADO! você excedeu o limite permitido que é de 80km/h')
    multa = (velocidade - 80) * 7
    print(f'Você deve pagar uma multa de R$ {multa:.2f} reais')
else:
    print(f'Velocidade de {velocidade}km/h dentro no permitido.\n'
    'Tenha um bom dia! Dirija com Segurança\n\n')
    
    
print('EX003 - leia um programa que leia um número inteiro e mostre na tela se ele e PAR ou IMPAR.')
n1 = int(input('Digite um número inteiro qualquer: '))
resultado = n1 % 2
if resultado == 0:
    print(f'O número que você digitou foi {n1} ele é PAR')
else:
    print(f'O número que você digitou foi {n1} ele é IMPAR\n\n')



print('EX004 - desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$ 0,50 por km rodado ate 200 e R$ 0,45 para viagens mais longas')
distancia = float(input('Digite a distancia da sua viagem: '))

#if distancia <= 200:
#    preco = distancia * 0.50    
#else:
#    preco = distancia * 0.45  

preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45 #resolução em uma linha

print(f'Você vai percorrer {distancia}km')
print(f'E o preço da passagem é de R$ {preco:.2f} reais\n\n')


print('EX005 - faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.')
ano = int(input('Que ano quer analisar? Coloque 0(zero) para analisra ano atual '))
if ano == 0:
    ano = date.today().year
#if ano % 4 == 0:
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: 
    print(f'O ano {ano} é BISSEXTO')
else:
    print(f'O ano {ano} NÃO é BISSEXTO\n\n')
#Ate aqui tudo ok, porem na regra do bissexto os anos que são múltiplos de 100 que não são múltiplos de 400 não são BISSEXTO o if vai ter q mudar né.



print('EX006 - faça um progrma que leia três números e mostre qual é o maior e qual é o menor')
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))
menor = n1 #condição para ver qm é o menor
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1 #condição para ver qm é o maior
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}\n\n')



print('EX007 - escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$ 1.250,00 aumento de 10%, inferirores ou iguais aumento de 15%')
nome2 = str(input('Digite o nome do Funcionário: '))
salario = float(input(f'Digite o valor do salário do {nome2} R$'))
if salario <= 1250:
    aumento = salario + (salario * 15 /100)
else:
    aumento = salario + (salario * 10 /100)
print(f'O funcionário {nome2} com base no seu salário de R${salario:.2f}'
    f' passa a receber R${aumento:.2f}\n\n')
    
    

print('EX007 - faça um program que leia três retas e diga ao usuário se elas podem ou não formar um triangulo')
print('Analisador de Triângulo')
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!\n\n')

