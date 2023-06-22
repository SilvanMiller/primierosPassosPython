# ---------- EXERCICIOS Basicos (String) ------------------------------------
from random import shuffle, choice


print('EX001 - Crie um programa que leia o nome completo de uma pessoa e mostre:' 
      'O nome em maiúsculo, minúsculo, número de letras e o tamanho do primeiro nome')
nome = str(input('Digite seu nome completo ')).strip()
separa = nome.split()
print('Hummm... estou analizando sua solicitação...\n')

print(f'Seu nome em maiúsculo fica assim: {nome.upper()}')
print(f'Seu nome em minúsculo vai fica assim: {nome.lower()}\n')

print(f'Seu nome completo tem {len(nome) - nome.count(" ")} letras')
print(f'Seu primeiro nome que é {separa[0]} tem {len(separa[0])}\n\n')


print('EX002 - Uma mãe quer sortear um dos seus quatros filhos para lavar a louça. Faça um programa que leia os nomes e sortei o escolhido')
nome1 = input('Digite o nome do seu filho: ')
nome2 = input('Digite o nome do seu outro filho: ')
nome3 = input('Digite o nome do e outro filho: ')
nome4 = input('Digite o nome e ainda tem filho: ')
lavar_louca = [nome1, nome2, nome3, nome4]
escolhido = choice(lavar_louca)
print(f'E o felizardo(a) foi, trum trum trum {escolhido}\n\n')



print('EX003 - Uma professora quer sortear a ordem de apresentação dos trabalhos. Faça um programa que leia o nome dos trabalhos e mostre a ordem sorteada ')
trab_1 = input('Digite o nome do grupo 1: ')
trab_2 = input('Digite o nome do grupo 2: ')
trab_3 = input('Digite o nome do grupo 3: ')
trab_4 = input('Digite o nome do grupo 4: ')
apresentacao = [trab_1, trab_2, trab_3, trab_4]
shuffle(apresentacao)
print(f'E a ordem de apresentação vai ser, {apresentacao}\n\n')