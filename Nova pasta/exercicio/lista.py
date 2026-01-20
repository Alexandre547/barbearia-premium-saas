lista_nome = []
lista_nota = []

lista_aprovado = []
lista_reprovado = []

while True:
    aluno = input('Digite o nome dos alunos: ').lower()
    if aluno == 'sair':
        break
    lista_nome.append(aluno)
    

    nota = float(input('Digite a notas de cada aluno: '))
    lista_nota.append(nota)

for n in range(len(lista_nome)):
    nome_do_aluno = lista_nome[n]
    nota_do_aluno = lista_nota[n]
    if nota_do_aluno < 7.0:
        lista_reprovado.append(nome_do_aluno)
    else:
        lista_aprovado.append(nome_do_aluno)
        
soma_das_notas = 0    
for item in lista_nota:
    soma_das_notas += item
media = soma_das_notas / len(lista_nota)

print(f'Lista de alunos: {lista_nome}')
print(f'Notas dos alunos: {lista_nota}')
print(f'Os alunos aprovados são: {lista_aprovado}')
print(f'Os alunos reprovados são: {lista_reprovado}')
print(f'Média da turma {media}')



# nomes = ["Ana", "Marcos", "Leo", "Bia", "Alexandre", "Fernanda", "Gil"]

# compressao  = ['longo' if len(item) >= 4 else "curto" for item in nomes]

# print(f'O tamanho de cada nome: {compressao}')

# for i in range(3, 0, -1):
#     nome = input('Digite seu nome: ').lower()
#     senha = input('Digite sua senha: ').lower()
#     if nome == senha:
#         print(f'Erro de dados, nome e senha são iguais por medida de segurança digite ambos diferente para reforça a segurança!! Restam apenas {i} tentativas!!')
#         continue
#     else:
#         break
# print(f'Seu nome e sua senha são válidos! Olá {nome}!!')


# lista = []
# while True:
#     menu = input('Digite qual opção deseja: 1 -ADICIONAR, 2 -LISTAR, 3 -ATUALIZAR, 4 -REMOVER E 5 -SAIR. ')
#     if menu == "5":
#         print('Encerrando o programa, até logo....')
#         break
#     try:
#         menu = int(menu)
#     except ValueError:
#         print('Digite um NUMERO para selecionar uma das opções')
#         continue

#     if menu == 1:
#         item = input('Digite qual item deseja adicionar: ')
#         lista.append(item)
#         print(f'O produto {item} foi adicionado com sucesso!!')
#     elif menu == 3:
#         if not lista:
#             print('Não há produtos para atualizar. Adicione um primeiro. ')
#             continue
#         print(f'Lista de itens atuais:')
#         for i, item_lista in enumerate(lista):
#             print(f'{i + 1}. {item_lista}')
#         try:
#             atualizar_num = input('Digite um NÚMERO do produto que deseja atualizar: ')
#             atualizar_indice = int(atualizar_num) - 1
#             if atualizar_indice < 0 or atualizar_indice >= len(lista):
#                 print(f'Número do produto inválido. Digite um número entre 1 e {len(lista)}. ')
#                 continue
#             novo_nome = input('Digite o NOVO nome para o produto: ').strip()
#             if novo_nome:
#                 lista[atualizar_indice] = novo_nome
#                 print(f'Produto atualizado para "{novo_nome}" com sucesso!!')
#             else:
#                 print('O novo nome do produto não pode ser vazio. Atualização cancelada. ')
#         except ValueError:
#             print('Entrada inválida. Digite um NÚMERO para o produto que deseja atualizar. ')
#         print("-" * 30)

#     elif menu == 2:
#         if not lista:
#             print('Lista vazia, favor adicione um produto!! ')
#         else:
#             print(f'Sua lista de item: {lista}')
#             for i, men in enumerate(lista):
#                 print(f"{i + 1}. {men}")
#     elif menu == 4:
#         if not lista:
#             print('Não há produtos para remover. Adicione um primeiro. ')
#             continue
#         print(f"Lista de itens atuais: ")
#         for i, item_lista in enumerate(lista):
#             print(f'{i + 1}. {item_lista}')
#         try:
#             remover_num = input('Digite um NÚMERO do produto que deseja remover: ')
#             remover_indice = int(remover_num) - 1
#             if remover_indice < 0 or remover_indice >= len(lista):
#                 print(f'Número do produto inválido. Digite um número entre 1 e {len(lista)}')
#                 continue
#             item_removido = lista.pop(remover_indice)
#             print(f'Produto "{item_removido}" removido com sucesso!!')
#         except ValueError:
#             print('Entrada inválida. Digite um NÚMERO para o produto que deseja remover. ')
#             continue
#         print("-" * 30)
#     else:
#         print('Opção inválida. Por favor, escolha um número entre 1 e 5. ')
#         print("-" * 30)

        # lista = []
# while True:
#     nota = input('Digite a nota dos alunos de 0 a 100(ou digite sair para encerra o programa): ')
#     if nota == 'sair':
#         break
#     try:
#         nota = int(nota)
#         if nota < 0 or nota > 100:
#             raise ValueError ('ERRO!! Valores aceito apenas entre 0 a 100!!')
#     except ValueError as e:
#         print(f'Digite um NUMERO, textos são inválidos!!, Detalhe: {e}')
#         continue
#     lista.append(nota)
#     print(f'Nota {nota} adicionada com sucesso!!')
#     ver = input('Deseja ver a lista de notas(digite "sim" para ver ou "não"? ').lower() 

#     if ver == 'ver':
#         if not lista:
#             print('Lista de notas vazia!!')
#     else:
#         print(f'Suas notas {lista}')
#         for indice, n in enumerate(lista):
#             print(f'{indice + 1}. {n}')
#         print('-' * 30)

#     soma_total = 0
#     for n in lista:
#         soma_total += n
#     media = soma_total / len(lista)

#     acima_da_media = 0
#     abaixo_da_media = 0

#     for n in lista:
#         if n >= media:
#             acima_da_media +=1
#         else:
#             abaixo_da_media +=1

#     print(f'Todas a notas {lista}')        
#     print(f'A média da turma é {media:.2f}')
#     print(f'Quantos alunos estão acima da média {acima_da_media}')
#     print(f'Quantos alunos estão abaixo da média {abaixo_da_media}')
            
# lista = []
# while True:
#     op1 = input('Menu de opções: 1 para adicionar, 2 para ver, 3 para remover e 4 para sair: ')
#     if op1 == '4':
#         print('Encerrando o programa....')
#         break
#     try:
#         opçao = int(op1)
#     except ValueError:
#         print ('Não é aceito texto apenas numero, tente novamente!! ')
#         continue
#     if opçao == 1:
#         print('Qual tarefa deseja adicionar a lista?')
#         adc = input('Digite a tarefa para adicionar: ')
#         if adc:
#             lista.append(adc)
#             print(f'Tarefa "{adc}" adicionada com sucesso!')
#         else:
#             print('A tarefa não pode ser vazia.')

#     elif opçao == 2:
#         if not lista:
#             print('Não há tarefas adicionada, tente adicionar.')
#             continue
#         else:
#             print('Sua lista de tarefas:')
#             for indice, tarefa in enumerate(lista):
#                 print(f'{indice + 1}. {tarefa}')
#     elif opçao == 3:
#         if not lista:
#             print('Não há tarefas adicionada, tente adicionar.')
#             continue
#         else:
#             print('Tarefas atuais:')
#             for indice, tarefa in enumerate(lista):
#                 print(f'{indice + 1}. {tarefa}')

#         try:
#             remover = int(input('Digite o numero da tarefa que deseja remover: '))
#             indice_real = remover - 1
#             if indice_real < 0 or indice_real >= len(lista):
#                 print(f'Número de tarefa inválido. Digite um número entre 1 e {len(lista)}.')
#                 continue
#             tarefa_removida = lista.pop(indice_real)
#             print(f'Tarefa "{remover}" removida com sucesso!')
#         except ValueError:
#             print('Opção inválida, digite um NUMERO! ')
#             continue
#         else:
#             print('Opção inválida. Por favor, escolha 1, 2, 3 ou 4.')