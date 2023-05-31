#Operações com textos

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

print('------------------')#\n indica um nova linha(new line) já i \t uma tabulação
frase = "\tMeu nome é 'Silvan'"
frase2 = "\n\tEu sou um programado web e estou aprndendo python"
frase3 = """
---------------------------
Meu nome é 'Silvan'
    Eu sou um programado web
    e estou aprndendo python

"""#aqui ja usamos a ideis do comentario porem ele mantem a quebra de linha e a tabulação que vc digitar.
#print(frase, frase2, frase3)

frase4 = 'meu nome é Silvan'
print('nome' in frase4)#aqui vc verifica se existe alguma coisa dentro do texto(string) usando o operador in 
print('silvan' in frase4)
print('Silvan' in frase4)#ele não difere maisculo de minusculo 
print('Silvan' not in frase4)

print(len(frase4))#Contador de caracteres

print(frase4.lower())#converter tudo para minusculo(caixa baixa)
print(frase4.upper())#Converter tudo em maiusculo(caixa ALTA)
print(frase4.capitalize())#faz o inicio do texto ficar em maiusculo
print(dir(str))

print('------------------')
dados = "Silvan;44anos;1,73;touro" 
print(dados.split(';'))#separando em uma lista para usar como quiser


