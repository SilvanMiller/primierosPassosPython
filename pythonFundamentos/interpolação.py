CARRO = "Fusca"
PRECO = 1200.568

print('carro: ' + CARRO + ', preco: ' + str(PRECO))#concatenação

# Versão mais antigas
print('carro: %s, preço: %d' % (CARRO, PRECO))#numeros inteiros
print('carro: %s, preço: %.2f' % (CARRO, PRECO))#numeros fracionados 
print('carro: {0}, preco: {1}'.format(CARRO, PRECO))#um pouco mais nova,

# Versão mais modernas
print(f'carro: {CARRO}, preco: {PRECO}')