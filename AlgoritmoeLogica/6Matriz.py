# --- EXERCÍCIO 1 ---------------------
# Faça um programa que leia uma matriz 2x3 (2 linhas, 3 colunas). 
# Apresenta os elementos da matriz e seus respectivos índices.

vetor_matriz = []
for lin in range(2):
  linha = []
  for col in range(3):
    linha.append(int (input('digite o valor de ['+str(lin)+','+str(col)+ ']: ')))
  vetor_matriz.append(linha)

print( )
print('Matriz:')
for lin in range(2):
  for col in range(3):
    print(vetor_matriz[lin][col],end="\t")
  print( )

# --- EXERCÍCIO 2 ---------------------
# Faça um programa que carregue uma matriz 2 x 2, 
# que representa o salário de 4 funcionários, 
# calcule e mostre a soma total de todos os elementos que 
# será o montante pago pela empresa a esses funcionários.

vetor_matriz = [ ]
soma = 0
for lin in range(2):
  linha = []
  for col in range(2):
    linha.append(float(input('Digite o valor do salário R$: ')))
  vetor_matriz.append(linha)

for lin in range(2):
  for col in range(2):
    soma = soma + vetor_matriz[lin][col]
    print(matriz[lin][col], end= "\t")
  print( ) 
print(f'Soma total dos salários pagos R$: {soma:.3f}')


# --- EXERCÍCIO 3 ---------------------
# Faça um programa que carregue uma matriz 3 x 2, 
# que representa preços de produtos, crie OUTRA 
# matriz que armazene todos os preços com 7% de aumento.

# entrada = criar a matriz  
vetor_matriz = [ ] # matriz apenas com os preços
matriz_nova = [ ] # matriz com o aumento nos preços
lin = 0
col = 0

# processamento = criar a estrutura da matriz 
for lin in range(3): # preencher parênteses com a quantidade de linhas desejadas na matriz/ criação de (x) vetores dentro da matriz
  linha = [ ] # criação do vetor que vai compor a matriz
  for col in range(2): # preencher parênteses com a quantidade de linhas (colunas)
    linha.append(float(input('Digite o valor do produto R$: ')))
  vetor_matriz.append(linha)
 

for lin in range(3):
  linha = [ ]
  for col in range(2):
    linha.append((vetor_matriz[lin][col] * 7 / 100) + vetor_matriz[lin][col])
  matriz_nova.append(linha)
print( )
# criação da nova matriz
print('Matriz com 7% de aumento: ')
for lin in range(3): 
  for col in range(2):
    print(f'{matriz_nova[lin][col]:.2f}',end='\t\t')
  print()

# --------------------------

preco = [] # ................................................... Lendo a matriz
for lin in range(3):
    linha = []
    for col in range(2): 
        linha.append(int(input('Digite o valor ['+ str(lin) + '][' + str(col) + ']: ')))
    preco.append(linha)
aumento = []
for lin in range(3):  # ............................Cálculo do aumento na matriz
    linha = []
    for col in range(2): 
        linha.append(preco[lin][col] + (preco[lin][col] * 7 / 100))
    aumento.append(linha)
for lin in range(3):  # ...................................Apresentando a matriz
    for col in range(2): 
        print(f'{aumento[lin][col]:.2f}',end='\t\t')
    print()



    #outra forma de implementar este mesmo programa 
preco = [] # ........... Lendo a matriz preco e calculando a nova matriz aumento
aumento = []
for lin in range(3):
    linha = []
    linha_aumento = []
    for col in range(2): 
        linha.append(int(input('Digite o valor ['+ str(lin) + '][' + str(col) + ']: ')))
        linha_aumento.append(linha[col] + linha[col] * 7 / 100) # 0.07
    preco.append(linha)
    aumento.append(linha_aumento)
for lin in range(3):  # ...........................Apresentando a matriz aumento
    for col in range(2): 
        print(f'{aumento[lin][col]:.2f}',end='\t\t')
    print()

# --- EXERCÍCIO 4 ---------------------
# Faça um programa para armazenar em uma matriz 5x2 preços. 
# Encontre e apresente os ÍNDICES dos valores menores que 23 reais.

vetor_matriz = [ ]

for lin in range(5):
  linha = [ ]
  for col in range(2):
    linha.append(float(input('Digite o preço do produto R$ ['+ str(lin) + '][' + str(col) + ']: ')))
  vetor_matriz.append(linha) 

print( )
print('Matriz: ')

for lin in range(5):
  for col in range(2):
    if vetor_matriz[lin][col] < 23:
      print('['+ str(lin) + ','+ str(col) +']' ,vetor_matriz[lin][col] ,end= "\t\t")
  print( )

# --- EXERCÍCIO 5 ---------------------
# Faça um programa que leia números inteiros m e n e os 
# elementos de uma matriz A de números inteiros de dimensão 
# m x n e conte o número de elementos que são iguais a zero.

vetor_matriz = [ ]
par = 0
for m in range(3):
  linha = [ ]
  for n in range(3):
    linha.append(int(input('Digite o valor ['+str(m)+','+str(n)+'] da matriz: '))) 
  vetor_matriz.append(linha)

for m in range(3):
  for n in range(3):
    if vetor_matriz[m][n] / 2 == 0:
      par = par + 1

for m in range(3):
  print(vetor_matriz[m])

print(f'Quantidade de números iguais a zero: {par}') 

# --- EXERCÍCIO 6 ---------------------
# Faça um programa que carregue: 
#     • um vetor com oito posições com os nomes das lojas; 
#     • um outro vetor com quatro posições com os nomes dos produtos; 
#     • uma matriz (8 x 4) com os preços de todos os produtos em cada loja. 

# O programa deve mostrar todas as relações (nome da loja - nome do produto e preço), 
# nas quais o preço não ultrapasse R$ 120,00. 
# Escolha qual é o tipo da função que quer implementar

vetor_nome_loja = []
for i in range(2):
  vetor_nome_loja.append(input("Digite o nome da loja: "))

vetor_produtos = []
for i in range(2):
  vetor_produtos.append(input("Digite o nome dos produtos: "))

vetor_preco = []
for lin in range(2):
  linha = []
  for col in range(2):
      linha.append(float(input(f"Digite o preço do produto {vetor_produtos[col]} da loja {vetor_nome_loja[lin]}: ")))
  vetor_preco.append(linha)

print( ) 
print(f" Nome da loja:  Produto:  Preço: ")
print( )
for lin in range(2):
  for col in range(2):
    if vetor_preco[lin][col] < 120:
      print(f'{vetor_nome_loja[lin]:.<5} {vetor_produtos[col]:.<5} {vetor_preco[lin][col]}' )
  print()
print( )

