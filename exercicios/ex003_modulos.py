# ---------- EXERCICIOS BASICOS (MODULOS) ------------------------------------
#import pygame
import math
#fron math import radians, sin, cos tan, trunc, hypot


print('EX013 - Faça um programa que leia um número Real qualquer e mostre na tela a sua porção inteira')
num = float(input('Digite um número: '))
print(f'O número {num} tem a parte inteira {math.trunc(num)}\n\n') #aqui o trunc vai cortar a parte real e deixar a inteira. 
#num2 = float(input('Digite um valor '))
#print(f'O valor {num2} tem a sua parte inteira {int(num2)}\n\n') #aqui ja usamos o int se ñ quiser importar o math


print('EX014 - Faça um programa que leia o comprimento do cateto oposto de do cateto adjacente de um TRIANGULO RETANGULO, calcule e mostre o comprimento da hipotenusa.')
cat_oposto = float(input('Comprimento do cateto oposto: '))
cat_adjacente = float(input('Comprimento do cateto adjacente: '))
#hipotenusa = (cat_oposto ** 2 + cat_adjacente ** 2) ** (1/2)
hipotenusa = math.hypot(cat_oposto, cat_adjacente) #com a importação do modulo math e hypot 
print(f'A hipotenusa vai medir {hipotenusa:.2f}\n\n')


print('EX015 - Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno, e tangente desse ângulo')
angulo = float(input('Digite o ângulo de você deseja: '))
seno = math.sin(math.radians(angulo)) #para achar temos q converter o angulo em radianus
cosseno = math.cos(math.radians(angulo)) #cos(radians(angulo)) fron math import exemplos de como deve ficar
tangnt = math.tan(math.radians(angulo)) #tan(radians(angulo)) fron math import exemplos de como deve ficar
print(f'O ângulo de {angulo} tem o seno de {seno:.2f}')
print(f'O ângulo de {angulo} tem o cosseno de {cosseno:.2f}')
print(f'O ângulo de {angulo} tem o tangente de {tangnt:.2f}\n\n')




#print('EX016 - Faça um programa em PYTHON que abra e reproduza o áudio e um arquivo em MP3')
#pygame.init()
#pygame.mixer.music.load('MiguelGrippBeath.mp3')
#pygame.mixer.music.play()
#pygame.event.wait()
#verificar como importar a pygame

