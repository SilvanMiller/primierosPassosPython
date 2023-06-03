"""
Funções 
"""
# Calculando a média Silvan
# totalNotas = 5 + 7 + 5
# media = totalNotas / 3
# print(f'Média nota = {media}')# ate aqui tudo normal

# FUNÇÂO
# função e aqui esta passando o nome e notas por parâmetro
#def calcular_media(nota1, nota2, nota3):
#    totalNotas = nota1 + nota2 + nota3
#    media = totalNotas / 3
#    return media
    # print(f'Média nota {nome} é {media}')


# Calculando a média Miguel
#retorno = calcular_media(8, 9, 10)
# print(retorno)
#print(f'Média nota Silvan é {media}')

# Calculando a média Micaela
#retorno = calcular_media(10, 5, 9)
#print(f'Média nota Anna é {media}')


alunos = [
    {'nome': 'Silvan', 'notas': [8, 9]},
    {'nome': 'Miguel', 'notas': [6, 7, 9]},
    {'nome': 'Micaela', 'notas': [7, 8, 9, 10]},
]


def calcular_media(notas: float):
    total_notas = 0
    #len(notas) #se as notas estão vazias, o lens vai retornar zero
    #if len(notas) < 0: #podemos fazer essa verificação
    for nota in notas:
        total_notas += nota
    media = total_notas / len(notas)
    return media


#Assim se eu tiver menos notas ou mais ele vai funcinar normalmente independente da qnt de nts
for aluno in alunos:
    nome = aluno["nome"]
    notas = aluno["notas"]
    media = calcular_media(notas)
    #print(nome, notas)
    print(f'Média do(a) {nome} é {media}')