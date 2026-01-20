def fatorial(n):
    f = 1
    for c in range(1, n+1):
        f *=c
    return f

num = int(input('Digite o numero que deseja saber o fatorial: '))
fat = fatorial(num)
print(f' O fatorial do numero {num} é {fat} ')

# nomes = []
# pesos = []
# menor = 0
# maior = 0
# while True:
#     nome = input('Digite o nome das pessoas que deseja adicionar a lista: ')
#     nomes.append(nome)
#     peso = float(input('Digite o pesos dessas pessoas que adicionou: '))
#     pesos.append(peso)
#     continuar = input('Deseja continuar a adicionando: [S/N] ')
#     if continuar in 'Nn':
#         break


# for i in pesos:
#     if i > maior :
#         maior = i
#     elif i > menor:
#         menor = i



# print(f'Foram {len(nomes)} adicionadas a lista. ')
# print(f'O maior peso é {menor}')
# print(f'O menor peso é {maior}')

# print(pesos)


# import bisect
# numbers = []
# for i in range(5):
#     n = int(input('Type a number: '))
#     bisect.insort(numbers, n)
#     print(f'Number {n} included in position {numbers.index(n)}')
# print(f'Numbers typed: numbers')
# print(f'{numbers}')

# numero = int(input('Qual numero deseja saber a tabuada: '))
# cont = 0
# while True:
#     cont += 1
#     tabuada = numero * cont
#     print(f'{numero} x {cont} = {tabuada}' )
#     if numero == 00:
#         break
    
#     if cont >= 10:
#         opcao = input('Desejar continuar? ou deseja parar? Digite: [CONT/PARAR]').upper()
#         if opcao == 'CONT':
#             numero = int(input('Qual numero deseja saber a tabuada: '))
#             cont = 0
#             cont += 1
#             tabuada = numero * cont
#             print(f'{numero} x {cont} = {tabuada}')
#             continue
#         else:
#             break




    #     opcao = input('Desejar continuar? ou deseja parar? Digite: [CONT/PARAR]').upper()
    #     if opcao == 'CONT':
    #         numero = int(input('Qual numero deseja saber a tabuada: '))
    #         continue
    # else: 
    #     break
        
        
    
    
    


# numero = int((input('Digite os valores que deseja, para soma: ')))
# cont = 0
# acumulador = 0
# while numero != 999:
#     cont += 1
#     acumulador += numero 
#     numero = int(input('Digite os valores que deseja, para soma: '))
# print(f'Você digitou {cont} numeros, e a soma deles é {acumulador}')

# n1 = int(input('Digite um numero: '))
# n2 = int(input('Digite um numero: '))

# while True:
#     print(30*'=-')
#     print('Escolha as opções abaixo: ')
#     print('Digite [1] Somar ')
#     print('Digite [2] Multplicar ')
#     print('Digite [3] Maior ')
#     print('Digite [4] novos números ')
#     print('Digite [5] Sair do programa ')
#     menu = int(input('Digite o numero da opção que deseja: '))
#     if menu == 1:
#         soma = n1 + n2
#         print(f'A soma dos valores {n1} e {n2} é {soma}')

#     elif menu == 2:
#         multiplicar = n1 * n2
#         print(f'A multiplicação dos valores {n1} e {n2} é {multiplicar}')
#     elif menu == 3:
#         if n1 > n2:
#             print(f' O valor {n1} é maior do que o valor {n2}')
#         else:
#             print(f'O valor {n2} é maior que o valor {n1}')
#     elif menu == 4:
#         n1 = int(input('Digite o novo valor que você deseja: '))
#         n2 = int(input('Digite o novo valor que você deseja: '))
#         continue
#     elif menu == 5:
#         print('Finalizando o programa....')
#         break
#     else:
#         print('Opção inválida, digite um número válido!!')
# print('Programa finalizado!!')





#  --- Nossos Dados de Exemplo ---
# presenca_segunda = ['ana', 'carlos', 'bia', 'daniel']
# presenca_terca = ['ana', 'bia', 'daniel']
# presenca_quarta = ['carlos', 'bia', 'daniel', 'ana']
# presenca_quinta = ['ana', 'carlos', 'bia']
# presenca_sexta = ['ana', 'carlos', 'bia', 'daniel']

# presencas_da_semana = [
#     presenca_segunda,
#     presenca_terca,
#     presenca_quarta,
#     presenca_quinta,
#     presenca_sexta
# ]

# # --- Função 1: Contar Presenças ---
# def contar_presencas(lista_da_semana):
#     contagem = {}
#     for lista_diaria in lista_da_semana:
#         for nome in lista_diaria:
#             if nome in contagem:
#                 contagem[nome] += 1
#             else:
#                 contagem[nome] = 1
#     return contagem

# # --- Função 2: Achar quem veio sempre ---
# def encontrar_presentes_sempre(dicionario_presencas, total_de_dias):
#     alunos_100_porcento = []
#     for aluno, total in dicionario_presencas.items():
#         if total == total_de_dias:
#             alunos_100_porcento.append(aluno)
#     return alunos_100_porcento

# # --- Função 3: Achar quem faltou ---
# def encontrar_quem_faltou(dicionario_presencas, total_de_dias):
#     alunos_que_faltaram = []
#     for aluno, total in dicionario_presencas.items():
#         if total < total_de_dias:
#             alunos_que_faltaram.append(aluno)
#     return alunos_que_faltaram


# # --- Executando o programa e mostrando os resultados ---
# print("--- Relatório de Presença da Semana ---")

# # 1. Contagem total
# total_de_presencas_por_aluno = contar_presencas(presencas_da_semana)
# print(f"\nTotal de presenças por aluno: {total_de_presencas_por_aluno}")

# # 2. Alunos 100% presentes
# total_dias_letivos = len(presencas_da_semana)
# alunos_presentes_sempre = encontrar_presentes_sempre(total_de_presencas_por_aluno, total_dias_letivos)
# print(f"Alunos presentes todos os dias: {alunos_presentes_sempre}")

# # 3. Alunos com faltas
# alunos_com_falta = encontrar_quem_faltou(total_de_presencas_por_aluno, total_dias_letivos)
# print(f"Alunos que faltaram pelo menos um dia: {alunos_com_falta}")



# num1 = 20
# num2 = 1100

# if num1 > num2:
#     print(f'O numero {num1} é o numero maior')
# else:
#     print(f'O numero {num2} é o numero maior')








# distancia = float(input('Qual distância? '))
# if distancia <= 200:
#     valor = 0.5 * distancia
# else:
#     valor = 0.45 * distancia

# print(f'Pela distância {distancia}Km o valor da viagem ficou {valor:.2f}')

# for i in range(3, 0, -1):
#     nome = input('Digite seu nome: ').lower()
#     senha = input('Digite sua senha: ').lower()
#     if nome == senha:
#         print(f'Erro de dados, nome e senha são iguais por medida de segurança digite ambos diferente para reforça a segurança!! Restam apenas {i} tentativas!!')
#         continue
#     else:
#         break
# print(f'Seu nome e sua senha são válidos! Olá {nome}!!')

# homens = 0
# mulheres = 0
# grupo = 0
# for x in range(4):
#     sexo = input('Digite o sexo: ').lower()
#     idade = int(input('Digite a idade: '))
#     if sexo == 'm':
#         homens += 1
#         grupo = idade + grupo

#     if sexo == 'f':
#         mulheres += 1
#         grupo = idade + grupo
# print(f'Quantidade de homens: {homens} e quantidade de mulheres: { mulheres}')
# print(f'A media de idade do grupo é = {grupo/4}')
# print(grupo)

# maior = 0
# menor = 9999
# soma = 0
# for x in range(5):
#     num = int(input('Digite um numero: '))
#     if num > maior:
#         maior = num
        
#     if num < menor:
#         menor = num
#     soma = num + soma
# print(f'O maior numero dentre a lista é : {maior}')  
# print(f'O menor numero dentre a lista é : {menor}')  
# print(f'Media é = {soma/10}')