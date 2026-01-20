funcionarios = [
    {'nome': 'Carla', 'cargo': 'Vendedora', 'vendas': 180},
    {'nome': 'Marcos', 'cargo': 'Gerente', 'vendas': 95},
    {'nome': 'Joana', 'cargo': 'Vendedora', 'vendas': 210},
    {'nome': 'Pedro', 'cargo': 'Vendedor', 'vendas': 120},
    {'nome': 'Sofia', 'cargo': 'Gerente', 'vendas': 150}
]

for funcionario in funcionarios:
    cargo = funcionario['cargo']
    vendas = funcionario['vendas']
    aumento = 0

    if cargo == 'Vendedor' or cargo == 'Vendedora':
        if vendas >=200:
            aumento = vendas * 0.15

        elif vendas >= 150 and vendas <= 199:
            aumento = vendas * 0.10
        else:
            aumento = vendas * 0.05
    elif cargo == 'Gerente':
        if vendas >= 100:
            aumento = 1000
        else:
            aumento = 500
    funcionario['bonus'] = aumento

for f in funcionarios:
    print(f)

# lista_de_compras = [
#     {'produto': 'Maçã', 'categoria': 'Hortifruti'},
#     {'produto': 'Sabão em pó', 'categoria': 'Limpeza'},
#     {'produto': 'Banana', 'categoria': 'Hortifruti'},
#     {'produto': 'Arroz', 'categoria': 'Mercearia'},
#     {'produto': 'Detergente', 'categoria': 'Limpeza'},
#     {'produto': 'Uva', 'categoria': 'Hortifruti'},
# ]
# produtos_por_categoria = {}
# # Para cada dicionário de produto na nossa lista de compras...
# for itens in lista_de_compras:
#     # 1. Primeiro, vamos pegar as informações que nos interessam
#     categoria = itens['categoria']
#     produto = itens['produto']
#     # 2. A pergunta-chave: Essa categoria já existe no nosso dicionário final?
#     if categoria in produtos_por_categoria:
#         # 3. Se SIM: Acesse a lista que já existe e adicione o novo produto nela.
#         produtos_por_categoria[categoria].append(produto)
#     else:
#         # 4. Se NÃO: Crie a chave com a categoria e o valor será uma NOVA lista já com o produto.
#         produtos_por_categoria[categoria]= [produto]

# print(produtos_por_categoria)


# votos = [
#     'joao', 'maria', 'pedro', 'maria', 'joao',
#     'joao', 'maria', 'ana', 'pedro', 'maria'
# ]

# # 1. Começamos com o dicionário de contagem vazio.
# contagem_votos = {}

# # 2. Percorremos a lista de votos, um por um.
# for nome in votos:
#     # 3. A pergunta-chave: O nome já existe no nosso dicionário de contagem?
#     if nome in contagem_votos:
#         # 4. Se SIM: Pegue o valor atual e some 1.
#         contagem_votos[nome] += 1
#     else:
#         # 5. Se NÃO: Crie a chave com este nome e coloque o valor 1.
#         contagem_votos[nome] = 1

# # 6. No final, imprimimos o resultado.
# print(contagem_votos)

# estoque_produtos = [
#     {'produto': 'Camiseta P', 'preco': 49.90, 'quantidade': 15},
#     {'produto': 'Calça Jeans M', 'preco': 119.90, 'quantidade': 10},
#     {'produto': 'Tênis 42', 'preco': 299.00, 'quantidade': 0},
#     {'produto': 'Boné', 'preco': 35.00, 'quantidade': 25},
#     {'produto': 'Meia G', 'preco': 15.00, 'quantidade': 0},
# ]
# produtos_esgotado = []

# for estoque in estoque_produtos:
#     pro = estoque['produto']
#     quanti = estoque['quantidade']

#     if quanti == 0:
#         produtos_esgotado.append(pro)


# valor_total = 0
# for estoq in estoque_produtos:
#     preco = estoq['preco']
#     quantidade = estoq['quantidade']
#     multiplicacao = preco * quantidade
#     valor_total += multiplicacao

# print(f'Os produtos que estão com estoque 0 são: {produtos_esgotado}')
# print(f'O valor total do estoque: {valor_total}')




# turma = []
# alunos_aprovados = []
# alunos_reprovados = []

# while True:
#     aluno = input('Digite o nome dos alunos: ').lower()
#     if aluno == 'sair':
#         break

#     nota = float(input('Digite a notas de cada aluno: '))
    
#     aluno_atual = {'nome': aluno, 'nota' : nota}
#     turma.append(aluno_atual)

# for teste in turma:
#     nome_atual = teste['nome']
#     nota_atual = teste['nota']

#     if nota_atual >= 7.0:
#         alunos_aprovados.append(nome_atual)
#     else:
#         alunos_reprovados.append(nome_atual)

# soma_das_notas = 0
# for aluno_dicionario in turma:
#     soma_das_notas += aluno_dicionario['nota']

# if len(turma) > 0:
#     media = soma_das_notas / len(turma)
# else:
#     media = 0


# print(f'Lista de alunos & Notas: {turma}')
# print(f'Os alunos aprovados são: {alunos_aprovados}')
# print(f'Os alunos reprovados são: {alunos_reprovados}')
# print(f'Média da turma {media}')


    




# meu_carro = {'marca' : 'Volkswagen', 
#             'modelo' : 'Nivus',
#             'ano' : 2023,
#             'cor' : 'preto'}
# meu_carro['km'] = 15000
# meu_carro['cor'] = 'branca'

# for chave in meu_carro:
#     print(chave)

# for valores in meu_carro.values():
#     print(valores)

# for chave, valores in meu_carro.items():
#     print(f'{chave}: {valores}')
    




# lista_nome = []
# lista_nota = []

# lista_aprovado = []
# lista_reprovado = []

# while True:
#     aluno = input('Digite o nome dos alunos: ').lower()
#     if aluno == 'sair':
#         break
#     lista_nome.append(aluno)
    

#     nota = float(input('Digite a notas de cada aluno: '))
#     lista_nota.append(nota)

# for n in range(len(lista_nome)):
#     nome_do_aluno = lista_nome[n]
#     nota_do_aluno = lista_nota[n]
#     if nota_do_aluno < 7.0:
#         lista_reprovado.append(nome_do_aluno)
#     else:
#         lista_aprovado.append(nome_do_aluno)
        
# soma_das_notas = 0    
# for item in lista_nota:
#     soma_das_notas += item
# media = soma_das_notas / len(lista_nota)

# print(f'Lista de alunos: {lista_nome}')
# print(f'Notas dos alunos: {lista_nota}')
# print(f'Os alunos aprovados são: {lista_aprovado}')
# print(f'Os alunos reprovados são: {lista_reprovado}')
# print(f'Média da turma {media}')