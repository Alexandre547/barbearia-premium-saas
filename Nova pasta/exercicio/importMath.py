lista = [1, 5, 7, 10]
soma = 0
# Aqui, len() só serve para dizer ao 'range' até onde ele deve contar (0, 1, 2, 3)
for i in range(len(lista)):
    soma = soma + lista[i] # A soma de verdade é feita aqui
print(soma)

# numeros = [10, 20, 30, 40]

# soma_manual = 0
# for numero in numeros:
#     soma_manual = soma_manual + numero

# print(f'A soma dos valores é {soma_manual}')

# No final, soma_manual será 100

# lista = [78, 98, 45, 27]

# soma_total = sum(lista)
# print(f'Os valores total são: {soma_total}')

# import random
# nome1 = input('Digite o nome do primeiro aluno: ')
# nome2 = input('Digite o nome do segundo aluno: ')
# nome3 = input('Digite o nome do terceiro aluno: ')
# nome4 = input('Digite o nome do quarto aluno: ')

# lista = [nome1, nome2, nome3, nome4]
# random.shuffle(lista)
# # ou ordem = random.sample(lista, k=4) para selecionar a quantidade exata q vai ser sorteada pelo "k" podendo limita em 2,3 e etc...
# print(f'A nova ordem da lista dos alunos: ')
# print(lista)

# import random
# aluno1 = input('Digite o nome do primeiro aluno: ')
# aluno2 = input('Digite o nome do segundo aluno: ')
# aluno3 = input('Digite o nome do terceiro aluno: ')
# aluno4 = input('Digite o nome do quarto aluno: ')

# lista = [aluno1, aluno2, aluno3, aluno4]
# aluno_selecionado = random.choice(lista)

# print(f'O aluno que apagará o quadro é a/o {aluno_selecionado}')

# import math
# angulo = float(input('Digite o ângulo que você deseja: '))
# seno = math.sin(math.radians(angulo))
# co = math.cos(math.radians(angulo))
# tang = math.tan(math.radians(angulo))
# print(f'O angulo é {angulo:.2f}')
# print(f'E o seno é {seno:.2f}')
# print(f'O cosseno é {co:.2f}')
# print(f'O tangete é {tang:.2f}')

# from math import hypot
# co = float(input('Digite o cateto oposto: '))
# ca = float(input('Digite o cateto adjacente: '))
# hi = hypot(co, ca)
# print(f'A hipotenusa vai medir {hi:.2f}')

# import math
# num = int(input('Digite um numero: '))
# raiz = math.sqrt(num)
# arredondado = math.floor(raiz)
# print(f'A raiz de {num} é {raiz} e arredondado pra baixo é {arredondado}')