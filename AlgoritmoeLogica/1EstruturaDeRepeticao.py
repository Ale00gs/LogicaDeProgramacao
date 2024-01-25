# --- EXERCÍCIO 1 ---------------------
# Faça um algoritmo  que mostre 10 vezes a frase “Bem vindo a Fatec!”.
# Pode implementar com o comando while ou for.

frase = 0
while frase < 11:
  print(frase,'Bem vindo a Fatec! (while)')
  frase = frase + 1
  
for frase in range(11):
  print(frase,'Bem vindos a Fatec! (for)')


# --- EXERCÍCIO 2 ---------------------
# Faça um algoritmo que mostre o cumprimento ‘Olá ‘ para o nome de alguém (4 pessoas). 
# Exemplo ‘Olá Mariana’. Pode implementar com o comando while ou for.

frase = 1
nome = 1
while frase <= 4:
  nome = str (input(' informe o nome (while): '))
  print(f'Olá {nome}')
  frase = frase + 1


for frase in range(4):
  nome = str (input(' Informe o nome (for): '))
  print(f'Olá {nome}')

# --- EXERCÍCIO 3 ---------------------
# Faça um algoritmo que mostre os valores de 0 a 15. 
# Pode implementar com o comando while ou for.

valor = 0
while valor <= 15:
  print('Valor (while): ',valor)
  valor = valor + 1

for valor in range(0,16):
  print('Valor (for):',valor)

# --- EXERCÍCIO 4 ---------------------
# Faça um algoritmo que mostre os valores de 3 a 20. 
# Pode implementar com o comando while ou for.

valor = 3
while valor <= 20:
  print('Valor (while): ',valor)
  valor = valor + 1

for valor in range(3,21):
  print('Valor (for): ',valor)

# --- EXERCÍCIO 5 ---------------------
# Faça um algoritmo que calcule e mostre a tabuada do 5. 
# Pode implementar com o comando while ou for.

conta = 0
n1 = 5
while conta <= 10:
  tabuada = n1 * conta
  print(f'Tabuada do 5 (while): {tabuada}')
  conta = conta + 1 


n1 = 5
for conta in range(0,11):
  tabuada = n1 * conta 
  print(f'A tabuada do 5 (for): {tabuada}')
  
  
# --- EXERCÍCIO 6 ---------------------
# Faça um algoritmo que receba a idade de 10 pessoas, 
# calcule e exiba a quantidade de pessoas maiores de idade, 
# sendo que a maioridade é obtida após completar 18 anos. 
# Pode implementar com o comando while ou for.

maior = 0
cont = 1
while cont <= 10:
  idade = int (input(f'Digite a idade da pessoa {cont}: '))
  if idade >= 18:
    maior = maior + 1
  cont = cont + 1
print('A quantidade maior de 18 anos é: ',maior)


# --- EXERCÍCIO 7 ---------------------
# Escreva um algoritmo que receba 23 números, 
# calcule e exiba a quantidade de números pares e impares. 
# Pode implementar com o comando while ou for.

numero = 0 
resultado = 0
while numero < 23:
  numero = int (input('Digite um número: '))
  resultado = numero % 2 
  if resultado == 0:
    print(f'O número {numero} é par! ')
  else:
    print(f'O número {numero} é impar! ')

# --- EXERCÍCIO 8 ---------------------
# Faça um algoritmo que calcule e exiba o salário reajustado de 
# dez funcionários de acordo com a seguinte regra 
# (pode implementar com o comando while ou for): 
#       • Salário até 300, reajuste de 50%; 
#       • Salários maiores que 300, reajuste de 30%.

for salario in range(0,10):
  salario = float (input('Digite o seu salário R$: ')) 
  if salario <= 300:
    reaj = 50
  elif salario > 300:
    reaj = 30
  salario =  (salario / reaj) + salario

  print(f'O reajuste foi de: {reaj}, e o salário reajustado R$: {salario:.2f} ')    


# --- EXERCÍCIO 9 ---------------------
# Faça um algoritmo que conheça 4 preços de produtos, 
# some-os e mostre o resultado. 
# Pode implementar com o comando while ou for.

soma = 0
for preco in range(4):
  preco = float (input('Digite o preço de um produto R$: '))
  soma = soma + preco
print('A soma dos valores é R$: ',soma) 


# --- EXERCÍCIO 10 ---------------------
# Faça um algoritmo que calcule e informe a média de idades de 5 alunos. 
# Pode implementar com o comando while ou for.

soma = 0
for idade in range(5):
  idade = int (input('Digite a sua idade: '))
  soma = soma + idade 
  media = soma / 5
print('A média das idades é: ',media)  


# --- EXERCÍCIO 11 ---------------------
# Faça um algoritmo que conheça 4 preços de produtos, 
# calcule e mostre a média aritmética dos preços. 
# Pode implementar com o comando while ou for.

soma = 0
for produto in range(4):
  produto = float (input('Digite o preço de um produto R$: '))
  soma = soma + produto 
  media = soma / 4 
print('A média aritmética é: ',media)  


# --- EXERCÍCIO 12 ---------------------
# Faça um algoritmo que leia o preço de 20 TV, 
# determine e apresente a média dos preços que possuem 
# valor maior que R$ 1000. 
# Pode implementar com o comando while ou for.

soma = 0
qtde = 0
for preco in range(20):
  preco = float (input('Digite o preço da tv: '))
  if preco >= 1000:
    soma = soma + preco
    qtde = qtde + 1
print('A média é : ',soma/qtde)    
