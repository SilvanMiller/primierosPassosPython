carro = "Fusca"
preco = 1200.568

#print('carro: ' + carro + ', preco: ' + str(preco))#concatenação

# Versão mais antigas
#print('carro: %s, preço: %d' % (carro, preco))#numeros inteiros
#print('carro: %s, preço: %.2f' % (carro, preco))#numeros fracionados 
#print('carro: {0}, preco: {1}'.format(carro, preco))#um pouco mais nova,

# Versão mais modernas
print(f'carro: {carro}, preco: {preco}') 
