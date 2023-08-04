nome = 'Silvan Miller'
altura = 1.73
peso = 82
imc = peso / altura ** 2

#forma sem a formatação de string (f)
print(nome, 'tem', altura, 'de altura,',)
print('pesa', peso, 'quilos e seu imc é', imc)

#Com a formatção (f)
print(f' {nome} tem {altura:.2f} de altura,')
print(f' pesa {peso} quilos e seu imc é {imc:.1f}.')

# usando o FORMAT 
a = 'A'
b = 'B'
c = 1.1
string = 'a= {nome1} b= {nome2} c= {nome3:.2f}'#{} acresente para ver o erro
#string = 'a= {} b= {} c= {:.2f}'

formato = string.format(nome1=a, nome2=b, nome3=c) #parametro nomeado
#formato = string.format(a, b, c)


print(formato) #vai gerar o erro "out of ranger" qndo colocar um 4 item para buscar algo q já acabou
