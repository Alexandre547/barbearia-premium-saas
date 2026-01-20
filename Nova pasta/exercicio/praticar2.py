usuario = []
par = []
while True:
    num = int(input('Digite os numeros que deseja inserir na lista ou Digite 00 para sair: '))
    if num == 00:
        break
    usuario.append(num)
    for n in usuario:
        if n % 2 == 0:
            if n not in par:
                par.append(n)
            
while True:
    cont = 0
    numero = int(input('Digite o numero que quer saber quantas vezes foram adicionados a lista: '))
    if numero == 00:
        break
    for numeros in usuario:
        if numeros == numero:
            cont +=1
            
    print(f'O {numero} aparece {cont} vez(es) na lista.') # o quesito da dificuldade do pq o 'cont' e o 'num' estava dando zerado, era por causa do escopo
    #como era escopo local dentro do 'for in' eu não conseguia exibir ele no escopo global como eu estava tentando, solucionei colocando print no escopo local
    # Dentro do 'for in'
print('-=-' * 20)
print(usuario)
print('-=-' * 20) 
print(f'Os numeros pares da lista acima são: {par}') 




# lista = [2,2,5,2,5,6,7,8,9]

# while True:
#     c = 0
#     num = int(input('Digite qual numero quer saber se tem repitido na lista(ou digite 99 para sair): '))
#     if num == 99:
#         break
#     for numero in lista: # Para(for) in(cada) essa é a forma para se lê o for in..
#         if num == numero:
#             c +=1
#     print(f'O {num} aparece {c} vezes na lista')
    
# lista = [2,2,5,2,5,6,7,8,9]
# repitido = []
# num = int(input('Digite um numero: '))

# for num in lista:
#     repitido.append(num)
#     if num in repitido:
#         print('Já está adicionado esse numero')
#     break
# print(repitido)