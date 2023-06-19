# ---------- EXERCICIOS BASICOS E VAI MELHORAR --------------------


print('EX001 - Faça um programa que leia um número inteiro e mostre na tela seu sucessor e seu antecessor.')
n = int(input('Digite um númro inteiro: '))
print(f'O número {n} te como seu antecessor o número {n - 1} e seu sucessor é {n + 1}\n\n')


print('EX002 - Crie um algoritimo que leia um número e mostre o seu dobro, triplo e raiz quadrada.')
print(f'O número {n} o seu dobro é {n * 2}, e seu triplo é {n * 3} e sua raiz quadrado é {n ** (1/2):.2f}\n\n')



print('EX003 - desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua media. ')
nome = input('Digite o nome do aluno: ')
nota_1 = float(input(f'Digite a primeira nota do aluno {nome}: '))
nota_2 = float(input('Digite a segunda nota: '))
print(f'As notas do aluno {nome} são {nota_1} e {nota_2} e a sua media é {(nota_1 + nota_2) / 2}\n\n')


print('EX004 - escreva um programa que leia um valor em metros e o exiba convertido em  centimetros e milimetros')
metros = float(input('Digite a sua medida em metros: '))
cm = metros * 100
mm = metros * 1000
print(f'Sua medida {metros}m corresponde a {cm:.0f}cm e a {mm:.0f}mm\n\n')


print('EX005 - faça um programa que leia um número inteiro qualquer e mostre a sua tabuada ')
num = int(input('Digite um número e veja sua tabuada: '))
#depois vai ter com for 
print(f'{num} x 1 = {num * 1}')
print(f'{num} x 2 = {num * 2}')
print(f'{num} x 3 = {num * 3}')
print(f'{num} x 4 = {num * 4}')
print(f'{num} x 5 = {num * 5}')
print(f'{num} x 6 = {num * 6}')
print(f'{num} x 7 = {num * 7}')
print(f'{num} x 8 = {num * 8}')
print(f'{num} x 9 = {num * 9}')
print(f'{num} x 10 = {num * 10}\n\n')


print('EX006 - crie um programa que leia gnto dinheiro uma pessoa tem na carteira e mostre gntos dólares ela pode comprar dolar a 4.82')
real = float(input('Quanto você tem na carteira R$ '))
dolar = real / 4.82
euro = real / 5.29
print(f'Com R${real}reais você pode comprar US${dolar:.2f}dolar e em EU${euro:.2f}euro\n\n')



print('EX007  - faça um programa q leia a largura e a altura de uma parede em metros,calcule a sua area e a qntdd de tinta necessária para pinta-lo, sabendo que cada litro de tinta pinta uma área de 2m² ')
larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
area = larg * alt
tinta = area / 2 
print(f'Sua parede tem {larg:.2f}m X {alt:.2f}m e sua área é {area:.2f}m²')
print(f'Para pintar esta parede, você precisará de {tinta:.2f}l de tintas \n\n')



print('EX008 - faça um algoritimo q leia o preço de um produto e mostre seu novo preço, com 5% de desconto ')
preco = float(input('Digite o preço do produto R$ '))
novo_preco = preco - (preco * 5 /100)
print(f'O protuto com valor de R${preco:.2f} com 5% de desconto vai sair por R${novo_preco:.2f}\n\n')


print('EX009 - faça um algoritimo que leia o salário de um funcioanrio e mostre seu novo salario com 15% de aumento')
funcioanrio = input('Digite o nome do Funcionario ')
salario = float(input('Digite o Salário do Funcionario R$ '))
nv_salario = salario + (salario * 15 /100)
print(f'O colaborador {funcioanrio} teve um aumento \nde 15% em seu salario de R${salario:.2f} para R${nv_salario:.2f}\n\n')



print('EX010 - Excreva um programa que comverta uma temperatura digitada em °C e converta para °F.')
celsius = float(input('Informe a temperatura em °C: '))
fahrenheit = ((9*celsius) /5) + 32
print(f'A temperatura de {celsius}°c corresponde a {fahrenheit}°f\n\n')



print('EX11 - Excreva um programa que pergunte a qntdd de km percorridos por um carro alugado e a gntdd de dias pelos quais ele foi alugado, calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 o km rodado')
dias = int(input('Quantos dias alugados? '))
km = float(input('Quantidade de Km rodado? '))
pago = (dias * 60) + (km * 0.15)
print(f'O total a pagar por {dias} dias alugados e R${pago:.2f}reais\n\n')


