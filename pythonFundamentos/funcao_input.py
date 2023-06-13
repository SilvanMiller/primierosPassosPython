#nome = input('Qual seu nome? ')
#print(f'O seu nome e {nome}')

#n_1 = input('Digite um número ')
#n_2 = input('Digite outro número ')

#int_n1 = int(n_1)
#int_n2 = int(n_2)

#print(f'A soma dos numeros é {n_1 + n_2}')# assim ele concatena pois n_1 e n_2 são str
#print(f'A soma dos numeros é {int_n1 + int_n2}')# assim ele soma por n1 e n2 sao int agora.

#---------------------------------------------------------------

#input com if e else
#entrada = input('Você quer "entrar" ou "sair ' )

#if entrada == 'entrar':
#    print('Você entrou no Sitema')
#    print(f'Seja bem vindo! {nome}')
#elif entrada == 'sair':
#    print(f'Você saiu do sistema {nome} ')
#else:
#    print(f'{nome} Você não digitou algo valido, tente novamente com "entrar" ou #"sair"')


#-----------------------------------------------------------------------

#nome = input('Qual seu nome? ')#
#primeiro_valor = input('Digite um valor: ')#
#segundo_valor = input('Digite outro valor: ')

#if primeiro_valor >= segundo_valor:
#    print(
#        f'{primeiro_valor} é maior ou igual ao {segundo_valor}'
#        )
#else:#
#    print(
#        f'{segundo_valor} é maior do que {primeiro_valor}'
#        )


#deseja_somar = input('Deseja somar os valores? " sim" ou " não" ')

#if deseja_somar == "sim":#
#    primeiro_valor = int(primeiro_valor)
#    segundo_valor = int(segundo_valor)
#    print(
#        f'{nome} A soma dos números : {primeiro_valor} + {segundo_valor}' 
#        f' é {primeiro_valor + segundo_valor}'
#        )

#elif deseja_somar == "não":
#    print(
#        f'{nome} então obrigado por sua interação'
#        )

#else:
#    print(f'{nome} continuando...')


#-----------Operador lógico AND -------------------------

#entrada = input('[E]entrar [S]sair ')
#senha_digitada = input('Senha: ')
#senha_permitida = '123456' #só para teste, nunca a senha fica assim.

#if entrada == 'E' and senha_digitada == senha_permitida:#
#    print('Entrada permitida')
    
#else:
#    print('Sair')
    
#-----------Operador lógico OR -------------------------

#entrada = input('[E]entrar [S]sair ')
#senha_digitada = input('Senha: ')
#senha_permitida = '123456' #só para teste, nunca a senha fica assim.

#if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:#
#    print('Entrada permitida')
    
#else:
#    print('Sair')

#----AVALIAÇÃO DE CURTO CIRCUITO----
#senha = input('Senha: ') or 'Sem senha' #aquifoi feito uma condição similar a um if
#print(senha)

#-----------Operador lógico NOT  -------------------------
# Para inversão de valores onde é true se torna false e vise e versa 

#print(not True) #False invertendo os valores 
#print(not False) #True invertendo os valores

#senha = input('Senha: ')
#if senha != '123456':
#if not senha:
    #print('Senha incorreta')
    #print('Você não digitou nada')
    
#-----------Operador in e not in  -------------------------
# esta entre = in / não esta entre = not in
# Strings são interaveis 
#  0 1 2 3 4 5  
#  S I L V A N 
# -6-5-4-3-2-1

nome = 'Silvan'
print(nome[1])
print(nome[-4])
print('v' in nome)
print('van' in nome) #van esta em nome(Silvan) = True
print('mi' not in nome) #mi não esta em nome(Silvan) = True(sim não esta)

nome2 = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome2:
    print(f'{encontrar} esta em {nome2}')
else:
    print(f'{encontrar} não esta em {nome2}')
    
