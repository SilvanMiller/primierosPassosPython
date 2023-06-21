#Operações com textos

"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(> < ^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 

Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::] #inicio fim passo
Obs.: a função len retorna a qtd 
de caracteres da str

"""

#variavel = 'ABC'
#print(f'{variavel}')
#print(f'{variavel: >10}')
#print(f'{variavel: <10}.')
#print(f'{variavel: ^10}.')
#print(f'{variavel:$^10}.') #faz o preenchimento tanto de um lado qnt do outro
#print(f'{1000.4873648123746:0=+10,.1f}')
#print(f'O hexadecimal de 1500 é {1500:08X}')
#print(f'{variavel!r}')

TEXTO = 'carro'
print(TEXTO[0])
print(TEXTO[1])
print(TEXTO[2])
print(TEXTO[3])
print(TEXTO[4])

print('------------------')
print(TEXTO[-1])
print(TEXTO[-3])
print(TEXTO[-2])
print(TEXTO[-4])
print(TEXTO[-0])

print('------------------')
print(TEXTO[:2])#aqui ele vai pegar a psção 0 e 1, pegando tudo q vier antes da posição indicada(ex[:3], [:4])
print(TEXTO[:4])
print(TEXTO[:5])

print('------------------')
print(TEXTO[3:])#aqui ja acontece o contratio, pgndo a psção e o q for depois da psção indicada
print(TEXTO[4:])

print('------------------')#aqui os :: indica para ele pular conforme o indicado de 2 em 2 ou de 3 em 3
print(TEXTO[::2])#pegou o 0(C) pulou o 1, pegou o 2(R) pulou o 3, pegou o 4(O)
print(TEXTO[::-1])#vamos inverter e pgr do final para o onicio sem pular

print('------------------')
    #\n indica um nova linha(new line) já i \t uma tabulação
frase = "\tMeu nome é 'Silvan'"
frase2 = "\n\tEu sou um programado web e estou aprendendo python"
frase3 = """
---------------------------
Meu nome é 'Silvan'
    Eu sou um programado web
    e estou aprndendo python

"""#aqui ja usamos a ideis do comentario porem ele mantem a quebra de linha e a tabulação que vc digitar.
#print(frase, frase2, frase3)

dados = "Silvan;44anos;1,73;touro" 
frase4 = '   meu nome é Silvan  '
print('nome' in frase4)#aqui vc verifica se existe alguma coisa dentro do texto(string) usando o operador in 
print('silvan' in frase4)
print('Silvan' in frase4)#ele não difere maisculo de minusculo 
print('Silvan' not in frase4)

print(len(frase4))#Contador de caracteres

print(frase4.lower())#converter tudo para minusculo(caixa baixa)
print(frase4.upper())#Converter tudo em maiusculo(caixa ALTA)
print(frase4.capitalize())#faz o inicio do texto ficar em maiusculo
print(frase4.title()) #faz as inicias de cada palavra ficar maiusculo
print(frase4.strip()) #aqui estamos removendo espços antes da string ou ao final
print(frase4.rstrip()) #aqui estamos removendo espços a direita(rigth) da string 
print(frase4.lstrip()) #aqui estamso removendo espços a esquerda(left) da string
print(frase4.split()) #
print(dados.split(';'))#separando em uma lista para usar como quiser


print(frase.replace('Silvan', 'Luke'))
print(frase4.count('m'))
print(frase4.find('Sil'))
print(frase4.lower().find('sil'))
print(frase4.find('cara')) #-1 diz que não foi localizado

print('''

    Bem-vindo ao tutorial interativo de Python do LearnPython.org.
Seja você um programador experiente ou não, este site é destinado a todos que desejam aprender a linguagem de programação Python.
Você está convidado a se juntar ao nosso grupo no Facebook para perguntas, discussões e atualizações.
Depois de concluir os tutoriais, você pode obter a certificação no LearnX e adicionar sua certificação ao seu perfil do LinkedIn.
Basta clicar no capítulo que deseja começar e seguir as instruções. Boa sorte!
''') 



print('------------------')
#print(dir(str))

