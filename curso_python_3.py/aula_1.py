"""
Python = linguagem de programação
tipo de tipagem = dinâmica / forte 
str -> string -> "textos"
"""
#USO PARA ALGUNs ESTUDOS PARA AJUDAR NO ENTENDIMENTO

nome = "Silvan"
sobrenome = "Miller"
idade = 44
ano_nascimento = 2023 - idade
maior_idade = idade >= 18
peso = 95
altura_metro = 1.73
imc = peso / altura_metro ** 2

#print('Nome:' , nome)
#print('Sobrenome:' , sobrenome)
print('Nome Completo:' , nome, sobrenome)
print('Idade:' , idade)
print('Ano de Nascimento:' , ano_nascimento)
print('É maior de idade:' , maior_idade)
print('Altura em metros:' , altura_metro, '\n')

linha_1 = f'{nome} {sobrenome} tem {altura_metro:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é {imc:.2f}'

#modo mais atual 
print('Vamos calcular o imc')
print(linha_1)
print(linha_2)

#modo antigo
#print('Vamos calcular o imc')
#print(nome, sobrenome, 'tem', altura_metro, 'de altura,',)
#print('pesa', peso, 'quilos e seu imc é', imc)

nome = "Luiz"
idade = 23
formato = f'{nome} tem {idade:.2f} anos'
print(formato.format(n=nome, i=idade))
print (10 * 20)



