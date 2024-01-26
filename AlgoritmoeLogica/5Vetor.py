# --- EXERCÍCIO 1 ---------------------
# Faça um programa que calcule e apresente a média de idades de uma sala de 35 alunos.​​

print('Exemplo de leitura de vetor com o for')
vetor_idade = [] 
soma_idade = 0
for i in range(35):
    idade = int(input('Informe a idade: '))
    vetor_idade.append(idade)
    soma_idade += idade

media = soma_idade / len(vetor_idade)
print('Quantidade de elementos:', len(vetor_idade))
print('Média de idades:', media)

print('Idades dos alunos:')
for idade in vetor_idade:
    print(idade, end='  ')

print('\n', vetor_idade)

print('\n\nExemplo de leitura de vetor com o while')
vetor_idade = [] 
soma_idade = 0
indice = 0
while indice < 35:
    idade = int(input('Informe a idade: '))
    vetor_idade.append(idade)
    soma_idade += idade
    indice += 1

media = soma_idade / len(vetor_idade)
print('Quantidade de elementos:', len(vetor_idade))
print('Média de idades:', media)

indice = 0
print('Idades dos alunos:')
while indice < 35:
    print(vetor_idade[indice], end='  ')
    indice += 1

# --- EXERCÍCIO 2 ---------------------
# Faça um programa que calcule e apresente a média de 
# alturas de uma sala de 35 alunos. Informe também quantos 
# alunos e quais (índice/posição) são os que possuem idade 
# superior a 25 anos.​ Use dois vetores, um para altura e 
# outro para idade. Não use nenhuma função pronta da linguagem Python.

#A posição é sua variável i
#print(i)
vetor_idade = [ ]
vetor_altura = [ ]
soma_altura = 0
for i in range(35):
  vetor_idade.append(float(input('Digite a sua idade: ')))
  vetor_altura.append(float(input('Digite a sua altura: ')))
  soma_altura = soma_altura + vetor_altura[i]
media = soma_altura / len(vetor_altura)
print('Média de alturas: ',media)

cont = 0 
for i in range(len(vetor_idade)):
  if vetor_idade[i] > 25:
    cont += 1
    print(f'O aluno n° {i + 1}, possui idade superior a 25 anos. A idade é {vetor_idade[i]} anos. ' )
print(f'Total de alunos com idade superior a 25 anos: {cont}')  

# --- EXERCÍCIO 3 ---------------------
# Faça um programa que carregue um vetor de dez elementos 
# que contenha o nome de pessoas e outro que contenha o peso, 
# encontre qual a pessoa com maior peso e a pessoa com menor peso e apresente o 
# nome e o peso das mesmas.​ Use dois vetores, um para peso e outro para nome. 
# Não use nenhuma função pronta da linguagem Python.

#gambiarra ---------------------
vetor_nome = [ ]
vetor_peso = [ ]
maior = 0
menor = 999999999

for i in range(10):
  vetor_nome.append(str(input('Digite o seu nome: ')))
  vetor_peso.append(float(input('Digite o seu peso em Kg: ')))
  if vetor_peso[i] > maior:
    maior = vetor_peso[i]
    nome_maior = vetor_nome[i]
  if vetor_peso[i] < menor:
    menor = vetor_peso[i]
    nome_menor = vetor_nome[i] 


print(f'O maior peso é do(a) {nome_maior}, com {maior} kg. ')
print(f'o menor peso é do(a) {nome_menor}, com {menor} kg. ')

# maneira correta ---------------------
vetor_nome = []
vetor_peso = []
maior = 0
menor = float('inf') 

for i in range(10):
    nome = input('Digite o seu nome: ')
    peso = float(input('Digite o seu peso em Kg: '))
    vetor_nome.append(nome)
    vetor_peso.append(peso)
    
    if peso > maior:
        maior = peso
        nome_maior = nome
    if peso < menor:
        menor = peso
        nome_menor = nome

print(f'O maior peso é do(a) {nome_maior}, com {maior:.2f} kg.')
print(f'O menor peso é do(a) {nome_menor}, com {menor:.2f} kg.')


# --- EXERCÍCIO 4 ---------------------
# Faça um programa que carregue um vetor com a média de dez alunos, 
# calcule e mostre a MÉDIA DA SALA e quantos alunos estão acima e 
# abaixo da média da sala.

vetor_media = [ ]
soma = 0

for i in range(10):
  vetor_media.append(float(input('Digite a média: ')))
  soma = soma + vetor_media[i]
media_sala = soma / len(vetor_media)
print('Média da sala: ',media_sala)

cont_acima = 0
cont_abaixo = 0
for i in range(10):
  if vetor_media[i] >= media_sala:
    cont_acima = cont_acima + 1
  else:
    cont_abaixo = cont_abaixo + 1  
    
print('Quantidade de alunos acima da média da sala: ',cont_acima )
print('Quantidade de alunos abaixo da média da sala: ',cont_abaixo )

# --- EXERCÍCIO 5 ---------------------
# Faça um programa que carregue um vetor de oito elementos
# numéricos inteiros, calcule e mostre os números pares e suas 
# respectivas índices/posições. Não use nenhuma função pronta 
# da linguagem Python.

numeros = []

for i in range(8):
  numeros.append(int(input("Informe um numero inteiro: ")))

for i in range(len(numeros)):
  if numeros[i] % 2 == 0:
    print("O numero",numeros[i],"é par e está na posição",i+1)

# --- EXERCÍCIO 6 ---------------------
# Faça um programa que carregue um vetor com dez nomes e 
# faça uma verificação se um determinado nome esta nesse vetor. 
# Não use nenhuma função pronta da linguagem Python.

vetor_nome = [ ]
procurar = 0

for i in range(10):
  vetor_nome.append(str(input('Digite o nome: ')))
procurar = str(input('digite um nome para saber se ele pertence ao vetor: '))
if procurar in(vetor_nome):
  print(f'O nome {procurar} está dentro do vetor! ')
else:
  print(f'O nome {procurar} não está dentro do vetor! ')


# --- EXERCÍCIO 7 ---------------------
# Faça um algoritmo que calcule e apresente a média de alturas 
# superior a 1,80 de 10 alunos. Informe também quantos e quais 
# (índice/posição) são os alunos. Não use nenhuma função pronta 
# da linguagem Python.

alturas = []

# altura dos 10 alunos
for i in range(1, 11):
    altura = float(input(f"Digite a altura do aluno {i}: "))
    alturas.append(altura)

# média das alturas superiores a 1,80
soma_alturas = 0
contador = 0
alunos_altos = []

for i in range(len(alturas)):
    if alturas[i] > 1.80:
        soma_alturas += alturas[i]
        contador += 1
        alunos_altos.append(i + 1)  

# alturas superiores a 1,80
if contador == 0:
    print("Não há alunos com altura superior a 1,80.")
else:
    media_alturas = soma_alturas / contador
    print(f"A média das alturas dos alunos superiores a 1,80 é: {media_alturas:.2f}")
    print(f"Total de alunos com altura superior a 1,80: {contador}")
    print("Alunos com altura superior a 1,80 (índice/posição):", alunos_altos)

# --- EXERCÍCIO 8 ---------------------
# Criar um algoritmo que a partir de um vetor de 10 
# elementos inteiros, crie outros dois vetores que 
# receberão os elementos positivos e negativos e ao 
# final apresente-os. Não use nenhuma função pronta 
# da linguagem Python.

vetor_int = [ ]
vetor_posit = [ ]
vetor_negat = [ ]

for i in range(10):
  vetor_int.append(int(input('Digite um número inteiro [' + str(i) + ']: ')))
  if vetor_int[i] >= 0:
    vetor_posit.append(vetor_int[i])
  else:
    vetor_negat.append(vetor_int[i])

print(f'Os números positivos são: {vetor_posit}. ')
print(f'Os números negativos são: {vetor_negat}. ')

# --- EXERCÍCIO 9 ---------------------
# Criar um algoritmo que leia dados para um vetor de 100 
# elementos inteiros, imprimir o maior, o menor, o percentual 
# de números pares e a média dos elementos do vetor. 
# Obs.: percentual = quantidade contada * 100 / quantidade total. 
# Não use nenhuma função pronta da linguagem Python.

vetor_int = [ ]
maior = 0
menor = 99999999
par = 0
resultado = 0
soma = 0
media = 0

for i in range(100):
  vetor_int.append(int(input('Digite um número inteiro [' + str(i) + ']: ')))
  if vetor_int[i] > maior:
    maior = vetor_int[i]
  if vetor_int[i] < menor:
    menor = vetor_int[i] 

for i in range(100):
  resultado = vetor_int[i] % 2
  if resultado == 0:
    par = par + 1  

  soma = soma + vetor_int[i]


print(f'O maior número é: {maior}, e o menor número é {menor}. ')
print(f'Percentual de números pares: {(par * 100)/ len(vetor_int)} %. ')
print(f'Média dos elementos do vetor: {soma / len(vetor_int) } ')

# --- EXERCÍCIO 10 ---------------------
# Faça um programa que:

#     preencha um vetor com seis elementos numéricos inteiros.

# Calcule e mostre:

#     todos os números pares;
#     a quantidade de números pares;
#     todos os números ímpares;
#     a quantidade de números ímpares

vetor_int = [ ]
vetor_par = [ ]
vetor_impar = [ ]
resultado = 0

for i in range(6):
  vetor_int.append(int(input('Digite um número inteiro [' + str(i) + ']: ')))
  resultado = vetor_int[i] % 2
  if resultado == 0:
    vetor_par.append(vetor_int[i])
  else:
    vetor_impar.append(vetor_int[i])

print(f'Números pares: {vetor_par}. Quantidade de números pares: {len(vetor_par)} ')
print(f'Números ímpares: {vetor_impar}. Quantidade de números impares: {len(vetor_impar)} ')

# --- EXERCÍCIO 11 ---------------------
# Faça um programa que:

#     preencha um vetor com sete números inteiros

# Calcule e mostre:

#     os números múltiplos de 2;
#     os números múltiplos de 3;
#     os números múltiplos de 2 e de 3.

vetor_int = [ ]
multiplo_dois = [ ]
multiplo_tres = [ ]
multiplo_dois_e_tres = [ ]
resultado = 0

for i in range(7):
  vetor_int.append(int(input('Digite um número inteiro [' + str(i) + ']: ')))
  if vetor_int[i] % 2 == 0:
    multiplo_dois.append(vetor_int[i])
  if vetor_int[i] % 3 == 0:
    multiplo_tres.append(vetor_int[i]) 
  if vetor_int[i] % 2 == 0 and vetor_int[i] % 3 == 0:
    multiplo_dois_e_tres.append(vetor_int[i]) 
  
print(f'Os números múltiplos de 2 são: {multiplo_dois} ')
print(f'Os números múltiplos de 3 são: {multiplo_tres} ')
print(f'Os números múltiplos de 2 e 3 são: {multiplo_dois_e_tres} ')

  # for x in range(1, n):
  # if (n % x == 0): #se o resto da divisão de n/x for 0 (múltiplo)
  #  print x #múltiplo

# --- EXERCÍCIO 12 ---------------------
# Faça um programa que:

#     preencha um vetor com quinze elementos inteiros
#     verifique a existência de elementos iguais a 30, mostrando os índices/posições em que apareceram.

vetor_int = [ ]
vetor_posi = [ ]
numero = 0
for i in range(15):
  vetor_int.append(int(input('Digite um número inteiro [' + str(i) + ']: '))) 
  if vetor_int[i] == 30:
    numero = numero + 1  
    vetor_posi.append([i])
print(f'O número 30 se repete {numero} vez(es), e está na posição: {vetor_posi} ! ')  

# --- EXERCÍCIO 13 ---------------------
# Faça um programa que:

#     preencha um vetor com dez números reais

# Calcule e mostre:

#     a quantidade de números negativos
#     a soma dos números positivos desse vetor
#     não use nenhuma função pronta da linguagem Python

vetor_real = [ ]
negativo = 0
positivo = 0

for i in range(10):
  vetor_real.append(int(input('Digite um número real [' + str(i) + ']: ')))
  if vetor_real[i] < 0:
    negativo = negativo + 1

  else:
    positivo = positivo + vetor_real[i]

print(f'Quantidade de números negativos: {negativo} ')    
print(f'Soma dos números positivos desse vetor: {positivo} ')    

# --- EXERCÍCIO 14 ---------------------
# Faça um programa que:

#     receba dez números inteiros e armazene-os em um vetor
#     classifique os números em dois vetores, um com números pares e o outra com os ímpares
#     não use nenhuma função pronta da linguagem Python

vetor_int = [ ]
vetor_par = [ ]
vetor_impar = [ ]
resultado = 0

for i in range(10):
  vetor_int.append(int(input('Digite um número inteiro [' + str(i) + ']: ')))
  resultado = vetor_int[i] % 2
  if resultado == 0:
    vetor_par.append(vetor_int[i])
  else:
    vetor_impar.append(vetor_int[i])

print(f'Números pares: {vetor_par}.')
print(f'Números ímpares: {vetor_impar}.')

# --- EXERCÍCIO 15 ---------------------
# Faça um programa que:

#     preencha um vetor com quinze números

# Determine e mostre:

#     o maior número e a posição por ele ocupada no vetor
#     o menor número e a posição por ele ocupada no vetor
#     Não use nenhuma função pronta da linguagem Python

vetor_num = [ ]
maior = 0
menor = 99999999999
posicao_menor = 0
posicao_maior = 0

for i in range(5):
  vetor_num.append(int(input('Digite um número inteiro: ')))
  if vetor_num[i] > maior:
    maior = vetor_num[i]
    posicao_maior = i
  if vetor_num[i] < menor:
    menor = vetor_num[i] 
    posicao_menor = i

print(f'O maior número é: {maior}, e a posição ocupada no vetor é: {posicao_maior}')
print(f'O menor número é: {menor}, e a posição ocupada no vetor é: {posicao_menor}')
