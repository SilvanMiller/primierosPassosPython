from datetime import date


print('EX032 - Escreva um progrma para aprovar o emprèstimo bancário para a compra de uma casa. O progrma vai perguntar o valor da casa, o salário do comprador e em qnts anos ele ai pagar. - calcule o valor da prestação mensal sabendo que ela não pode exceder 30/100To do salário ou então o emprestimo é negado')

casa = float(input("Digite o valor da casa: R$ "))
salario = float(input("Digite o seu salário: R$ "))
tempoApagar = int(input("Digite em quantos anos quer pagar a casa? "))
parcelas = casa / (tempoApagar*12)
minino_parcela = salario * 30 / 100

print(f'Para comprar uma casa de R$ {casa:.2f} em {tempoApagar} anos, a prestação será de R$ {parcelas:.2f}')

if parcelas <= minino_parcela:
    print(f'Empréstimo com parcelas de {parcelas:.2f} ao mês pode ser CONCEDIDO!!\nn')
else:
    print(f'Empréstimo com parcelas de {parcelas:.2f}, maior que 30% do seu Salário, NEGADO!! ')

print('\n\n')
# -------------------------------

print('EX034 - Escreva um programa que leia dois números interiros e compare-os, mostrando na tela uma msg: "Primeiro número é maior - Segndo número é maior" - Os número são iguais')

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o Segundo numero: '))
if num1 > num2:
    print('O PRIMEIRO valor é MAIOR')
elif num1 < num2:
    print('O SEGUNDO valor é MAIOR')
else:
    print('Os DOIS valores são IGUAIS')

print('\n\n')
# -------------------------------

print('EX035 - Escreva um programa que leia o ano de nascimento de uma jovem e informe, de acordo coma sua idade: Se ele ainda vai se alistar - Se é a hora de se alistar - Se já passou do tempo de se alistar. Mostrar o tempo que falta ou que passou do prazo.')

#importa a data atual
#from datetime import date

atual = date.today().year
anoNascimento = int(input('Digite o ano de nascimento: '))
idade = atual - anoNascimento

print(f'Quem nasceu em {anoNascimento} tem {idade} anos em {atual}')

if idade == 18:

    print(f'Você esta com {idade} anos e tem q se Alistar IMEDIATAMENTE.')
elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} anos para o seu alistamento.')
    ano = atual + saldo
    print(f'Seu alistamento será em {ano}')
elif idade > 18:
    saldo = idade - 18
    print(f'Você já deveria ter se alistado há {saldo} anos')
    ano = atual - saldo
    print(f'Seu alistamento foi em {ano}')
    


print('\n')
# -------------------------------

print('EX036 - Escreva um programa que leia duas notas de um aluno e calcule sua média, mostrando uma msg no final: Menor que 5.0 REPROVADO - Entre 5.0 e 6.9 RECUPERAÇÃO - Maior que 7.0 APROVADO')

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2 

print(f'Sua Média foi {media:.1f}')
if 7 > media >= 5:
    print('aluno em RECUPERAÇÃO')
elif media < 5:
    print('nós vemos ano que vem, REPROVADO')
else:
    print('aluno em APROVADO')
    

print('\n')
# -------------------------------

print('EX037 - A confereração nacional de natação precisa de um progrma que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a sua idade: até 9 anos MIRIM - até 14 anos INFANTIL - até 19 anos JUNIOR - até 20 anos SÊNIOR - Acima MASTER')

anoAtual = date.today().year
nasc = int(input('Digite o ano que você nasceu: '))
idade = anoAtual - nasc
#print(f'Você nasceu em {nasc} e hoje tem {idade} anos.')

if idade <= 9:
    print(f'Sua idade é {idade} anos, e sua categoria é MIRIN.')
elif idade <= 14:
    print(f'Sua idade é {idade} anos, e sua categoria é INFANTIL.')
elif idade <= 19:
    print(f'Sua idade é {idade} anos, e sua categoria é JUNIOR.')
elif idade <= 25:
    print(f'Sua idade é {idade} anos, e sua categoria é SÊNIOR.')
else:
    print(f'Sua idade é {idade} anos, e sua categoria é MASTER.')
    
    
print('\n')
# -------------------------------

print('EX039 - Refaça o desafio dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado: equilatero - isósceles - escaleno')

print('Analisador de Triângulo')
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo! ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')

print('\n')
# -------------------------------

print('EX033 - Escreva um progrma que leia um número inteiro qualquer e peça para o usuário escolher qual sera a base de conversão: 1 para binário - 2 para octal - 3 para hexadecimal')
num = int(input('Digite um número inteiro qualquer: '))
print('''#Escolha uma das base para conversão: [1] BINÁRIO [2] OCTAL [3] HEXADECIMAL''')

opcao = int(input('Sua opção: '))
if opcao == 1:
    print(f'{num} concertido para BINÁRIO fica assim {bin(num)[2:]}')
elif opcao == 2:
    print(f'{num} convertido para OCTAL fica assim {oct(num)[2:]}')
elif opcao == 3:
    print(f'{num} convertido para HEXADECIMAL fica assim {hex(num)}[2:]')
else:
    print(f'Opção fora dos parametros para converter o número {num}.')
print('\n\n')

