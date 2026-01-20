

while True:
    frase_original = input('Digite uma palavra/frase (ou digite "sair" para encerrar): ').lower().strip()

    if frase_original == "sair":
        print('Encerrando o programa....')
        break

    # --- 1. PREPARAÇÃO DA FRASE ---
    # Converte para minúsculas (já feito) e REMOVE TODOS OS ESPAÇOS
    frase_limpa = frase_original.replace(' ', '')

    e_palindromo = True # FLAG: Assumimos que é palíndromo até provar o contrário

    # --- 2. LÓGICA DE VERIFICAÇÃO ---
    # O loop precisa ir APENAS ATÉ A METADE da frase limpa.
    # Ex: para "arara" (5 letras), loop vai até (5 // 2) = 2. Compara índice 0 com 4, e 1 com 3.
    for i in range(len(frase_limpa) // 2):
        # Compara o caractere na posição 'i' (do começo)
        # com o caractere na posição 'len(frase_limpa) - 1 - i' (do final)

        # Exemplo para "arara":
        # i = 0: frase_limpa[0] ('a') vs frase_limpa[5 - 1 - 0] = frase_limpa[4] ('a')
        # i = 1: frase_limpa[1] ('r') vs frase_limpa[5 - 1 - 1] = frase_limpa[3] ('r')
        if frase_limpa[i] != frase_limpa[len(frase_limpa) - 1 - i]:
            e_palindromo = False # Abaixa a bandeira: não é palíndromo
            break # Sai do loop 'for', não precisa verificar mais

    # --- 3. IMPRESSÃO DO RESULTADO ---
    if e_palindromo:
        # Imprime a frase original para o usuário ver o que ele digitou
        print(f'A frase/palavra "{frase_original}" É um palíndromo!!')
    else:
        print(f'A frase/palavra "{frase_original}" NÃO é um palíndromo.')

    print("-" * 30) # Separador visual para a próxima rodada
    


# while True:
#     palavra = input('Digite uma palavra/frase que deseja(ou "sair" para encerrar o programa): ').lower()
#     if palavra == 'sair':
#         print('Encerrando o programa....Bye bye!!')
#         break
#     letra = input('Digite a letra que deseja buscar dentro da palavra/frase digitada: ').lower()
#     print(f'Buscando a letra "{letra}".....')
#     if letra == 'sair':
#         print('Encerrando o programa....Bye bye!!')
#         break

#     percorrer = 0
#     posicao = ""

#     for indice, char_atual in enumerate(palavra):
#         if char_atual == letra:
#             percorrer = percorrer + 1

#             if posicao:
#                 indice = str(indice)
#                 posicao += ", "
#             posicao += str(indice)
#     print(f'A letra "{letra}" aparece: {percorrer} vezes.')
#     if percorrer > 0:
#         print(f'Foi encontrado nas posições: {posicao}. ')
#     else:
#         print(f'A letra "{letra}" não foi encontrada nesta frase/palavra.')
    



# import random, string
# while True:
#     compri_senha = input('Digite o comprimento da senha que deseja(ou digite "sair" para encerrar o programa): ')
#     if compri_senha == "sair":
#         print('Encerrando o programa....')
#         break
#     caracteres_possiveis = string.ascii_letters + string.digits
#     try:
#         compri_senha = int(compri_senha)
#         if compri_senha < 4 or compri_senha > 16:
#             raise ValueError ('Precisa ser no min 4 ou no max 16, favor digite a quantidade de caracters necessario!!')
#     except ValueError as e:
#         print(f'Entrada de dados não válido, digite apenas numero. DETALHE: {e}')
#         continue
#     senha_gerada = ""
#     for _ in range (compri_senha):
#         caractere_aleatorio = random.choice(caracteres_possiveis)
#         senha_gerada = caractere_aleatorio + senha_gerada
#     print(f"Senha: {senha_gerada}")


# while True:
#     frase = input('Digite uma frase(ou digite "sair" para encerrar o programa): ').lower().strip()
#     if frase == "sair" :
#         print('Encerrando o programa....Bye, Bye!!')
#         break
#     cont_a = 0
#     cont_e = 0
#     cont_i = 0
#     cont_u = 0
#     for frases in frase:
#         if frases == "a":
#             cont_a += 1
#         elif frases == "e":
#             cont_e += 1
#         elif frases == "i":
#             cont_i += 1
#         elif frases == "u":
#             cont_u += 1
#     print(f'A quantidade de letra com A é {cont_a}')
#     print(f'A quantidade de letra com E é {cont_e}')
#     print(f'A quantidade de letra com I é {cont_i}')
#     print(f'A quantidade de letra com U é {cont_u}')
#     continuar = input('Quer continuar a jogar? Se sim, digite "SIM" se não, digite "NÃO" para encerrar o programa.')
#     if continuar != "sim":
#         break
#     else:
#         continue


# import random
# print("----Jogo de adivinhação----") 
# print('O computador pensou em um numero de 1 a 100 tente adivinhar')
# while True:
    
#     numero_secreto = random.randint(1, 2)
#     while True:
#         inicio = input('Digite um numero para adivinhar(ou digite "sair" para encerrar o jogo): ')
#         if inicio == 'sair':
#             print('Encerrando o mini jogo....')
#             break
#         try:
#             inicio = int(inicio)
#             if inicio < 1 or inicio > 100:
#                 raise ValueError('Digite novamente seu chute de 1 ao 100 apenas. ')
#         except ValueError as e:
#             print(f'Digite um valor válido, apenas numeros ou digite apenas números inteiros entre 1 e 100. Detalhe: {e}')
#             continue
#         if inicio == numero_secreto:
#             print('Parabéns você acertou o número secreto!!')
#             break
#         elif inicio > numero_secreto:
#             print('Muito alto, tente novamente!!')
            
#         else:
#             print('Muito baixo, tente novamente!!')
#     while True:
#         continua_jogo = input('Deseja jogar novamente? (sim/não): ').lower().strip()
#         if continua_jogo == 'sim':
#             print("\n--- Nova Rodada ---")
#             break # Sai deste loop interno e volta para o 'while True' principal para uma nova rodada
#         elif continua_jogo == 'não':
#             print('Obrigado por jogar! Até a próxima!')
#             exit() # Sai do programa completamente
#         else:
#             print('Opção inválida. Por favor, digite "sim" ou "não".')





# while True:
#     numero = input('Digite um numero inteiro positivo(ou digite "sair" para encerrar o programa): ')
#     if numero == 'sair':
#         print('Encerrando o programa....')
#         break
#     try:
#         numInt = int(numero)
#         if numInt < 2:
#             raise ValueError('Numeros primos começam a partir do 2. ')
#     except ValueError as e:
#         print(f'Digite um valor válido, digite um numero inteiro. Detalhe: {e}!! ')
#         continue

#     print(f'Números primos até {numInt}: ')
    
#     for numero_atual in range(2, numInt + 1):
#         e_primo = True

#         for divisor in range(2, numero_atual):
#             if numero_atual % divisor == 0:
#                 e_primo = False
#                 break
#         if e_primo: 
#             print(f'{numero_atual} é primo.')
#             print("-" * 30)





# while True:
#     nome = input('Digite um nome(ou "sair" para encerrar o programa):')
#     if nome == 'sair':
#         print('Encerrando o programa....')
#         break
#     if not nome:
#         print('Nome vazio, preencha o campo obrigatório!!')
#         continue
#     tem_caracter_invalido = False
#     for carac in nome:
#         if not carac.isalnum():
#             print('Caracteres especiais inválidos!!')
#             tem_caracter_invalido = True
#             break
#     if tem_caracter_invalido:continue
        
#     if len(nome) <= 5:
#         print('Nome muito curto, por favor digite um nome com mais caracteres que 5!!')
#     elif len(nome) >= 15:
#         print('Nome muito longo, por favor digite um nome com menos caracteres que 15!!')
#     else:
#         print(f'O nome do usuario {nome} é válido!!')
        

# while True:
#     senha = input("Digite sua senha (ou 'sair' para finalizar): ").lower().strip()

#     if senha == 'sair':
#         print('Programa encerrado. Até mais!')
#         break # Sai do loop principal se o usuário digitar 'sair'

#     # Verifica se a senha está vazia
#     if not senha: # 'if not senha' é True se a string 'senha' estiver vazia
#         print('Senha não pode ser vazia. Tente novamente.')
#         continue # Volta para o início do loop para pedir a senha novamente

#     # --- Avaliação da Força da Senha ---
#     score = 0
#     tem_maiuscula = False
#     tem_minuscula = False
#     tem_digito = False
#     tem_especial = False

#     # Percorre cada caractere da senha para verificar as condições
#     # Usamos 'for char in senha:' que é um 'for in' direto nos elementos (caracteres) da string
#     for char in senha:
#         if char.isupper(): # .isupper() verifica se o caractere é uma letra MAIÚSCULA
#             tem_maiuscula = True
#         elif char.islower(): # .islower() verifica se o caractere é uma letra MINÚSCULA
#             tem_minuscula = True
#         elif char.isdigit(): # .isdigit() verifica se o caractere é um DÍGITO (número de 0 a 9)
#             tem_digito = True
#         else:
#             # Se não é maiúscula, minúscula nem dígito, é um caractere especial
#             tem_especial = True

#     # Adiciona pontos com base nas características encontradas
#     if len(senha) >= 8: # len() retorna o COMPRIMENTO (número de caracteres) da string
#         score += 1 # score = score + 1

#     if tem_maiuscula:
#         score += 1
#     if tem_minuscula:
#         score += 1
#     if tem_digito:
#         score += 1
#     if tem_especial:
#         score += 1

#     print(f"Score da senha: {score}")

#     # Classifica a senha com base no score
#     if score <= 2:
#         print("Senha Fraca.")
#     elif score <= 4: # Se não for <= 2, mas for <= 4, significa que é 3 ou 4
#         print("Senha Moderada.")
#     else: # Se não for <= 4, só pode ser 5 (ou mais, se adicionarmos mais pontos)
#         print("Senha Forte!")

#     print("-" * 30) # Apenas para separar visualmente as interações


# try:
#     nome = input("Digite seu nome: ")

#     if nome.strip() == "":
#         raise ValueError("Nome não pode estar vazio.")

#     print(f"Olá, {nome}!")

# except ValueError as erro:
#     print(f"Erro: {erro}")













