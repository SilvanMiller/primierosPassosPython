# Múltiplos parâmetros (Packing) # empacotar/embalar

#função normal sem o empacotamento passado como parâmetro
#def somar(n1, n2, n3):
#    total = n1 + n2 + n3
#    print(f'total: {total}')
    
def somar(*numeros):
    #print(type(numeros)) #tuple, para saber o tipo
    total = 0
    for numero in numeros:
        total += numero 
    print(f'total: {total}')
    
somar(1, 1, 1, 1) # se vc add mais parâmetros(numeros) ele vai continuar somando


# Múltiplos parâmetros (Unpacking) desempacotar/desembalar

#def calcular_media(n1: flot, n2: flot): #aqui Ñ seria bem assim q é melhor dinamico, + vms deixr assim
#    media = (n1 + n2) / 2
#    print(f'total: {media}')
    

#notas = [10, 9] #funciona com listas
#notas = (10, 9) #funciona com tuplas
#notas = {10, 9} #funciona com set
#calcular_media(*notas) #aqui ele desempacota, e como numa lista determina as notas para n1 e n2 


#parâmetros opcionais & nomeados

#aqui estamos add o p_e que sendo = 0(zero) ele é opcional, o cdg Ñ quebra 
def calcular_media2(n1: float, n2: float, nota_extra=0, ponto_extra=0): #parâmetro opcionais  
    media = (n1 + n2) /2 + nota_extra
    print(f'Média: {media} ponto extra: {ponto_extra}') #aqui já vai ser para aparecer o que teve de nota ou pode ser um ponto extra.
    

#assim vc pode determinar o que vai passar se um ponto_extra e ser somado ou 
calcular_media2(8, 9, 3,  ponto_extra=3 ) 
