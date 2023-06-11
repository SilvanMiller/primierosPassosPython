nome = input('Qual seu nome? ')
#print(f'O seu nome e {nome}')

#n_1 = input('Digite um número ')
#n_2 = input('Digite outro número ')

#int_n1 = int(n_1)
#int_n2 = int(n_2)

#print(f'A soma dos numeros é {n_1 + n_2}')# assim ele concatena pois n_1 e n_2 são str
#print(f'A soma dos numeros é {int_n1 + int_n2}')# assim ele soma por n1 e n2 sao int agora.

#input com if e else
entrada = input('Você quer "entrar" ou "sair ' )

if entrada == 'entrar':
    print('Você entrou no Sitema')
    print(f'Seja bem vindo! {nome}')
elif entrada == 'sair':
    print(f'Você saiu do sistema {nome} ')
else:
    print(f'{nome} Você não digitou algo valido, tente novamente com "entrar" ou "sair"')
