"""
escreva um programa que leia um valor em metros e o
exiba convertido em  centimetros e milimetros 

faça um programa que leia um número inteiro qualquer e 
mostre a sua tabuada 

crie um programa que leia gnto dinheiro uma pessoa 
tem na carteira e mostre gntos dólares ela pode comprar 
dolar a 3,27

faça um programa q leia a largura e a altura de uma parede em metros,
calcule a sua area e a qntdd de tinta necessária para pinta-lo,
sabendo que cada litro de tinta pinta uma área de 2m² 

faça um algoritimo q leia o preço de um produto e meostre seu 
novo preço, com 5% de desconto 

faça um algoritimo que leia o salário de um funcioanrio e 
mostre seu novo salario com 15% de aumento

"""

print('EX001 - Faça um programa que leia um número inteiro e mostre na tela seu sucessor e seu antecessor.')
n = int(input('Digite um númro inteiro: '))
print(f'O número {n} te como seu antecessor o número {n - 1} e seu sucessor é {n + 1}\n\n')


print('EX002 - Crie um algoritimo que leia um número e mostre o seu dobro, triplo e raiz quadrada.')
print(f'O número {n} o seu dobro é {n * 2}, e seu triplo é {n * 3} e sua raiz quadrado é {n ** (1/2):.2f}\n\n')



print('EX003 - desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua media. ')
nome = input('Digite o nome do aluno: ')
nota_1 = float(input(f'Digite a primeira nota do aluno {nome}: '))
nota_2 = float(input(f'Digite a segunda nota: '))
print(f'As notas do aluno {nome} são {nota_1} e {nota_2} e a sua media é {(nota_1 + nota_2) / 3}\n\n')

