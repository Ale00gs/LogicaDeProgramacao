# --- EXERCÍCIO 1 ---------------------
#      Construir um algoritmo para calcular e apresentar o total de salários pagos de funcionários, 
#      mas não é informado a quantidade de pessoas, então use como critério de parada 
#      (condição da estrutura de repetição, digitar zero no salário para sair).

salario = 0 
total = 0
salario = float(input('Informe o salário R$: (Quando quiser sair da estrutura digite zero): '))
while salario != 0:
    total = total + salario
    salario = float(input('Informe o salário R$: (Quando quiser sair da estrutura digite zero): ')) 
print('O valor total de salários pagos é:' ,total)
if salario == 0:
    print('Fim')


# --- EXERCÍCIO 2 ---------------------
#     Faça um programa que receba a altura de 5 pessoas. 
#     Encontre e apresente a altura da pessoa mais alta e da mais baixa e seus respectivos nomes.

cont = 0
maior = 0
menor = 9
while cont <= 4:
  altura = float (input('Digite a sua altura: '))  
  nome = input('Digite o seu nome: ')
  if altura > maior:
    maior = altura
    nome_maior = nome 
  if altura < menor:
    menor = altura
    nome_menor = nome
  cont = cont + 1
print(f'A maior altura é do(a) {nome_maior}, com {maior} metros. ')
print(f'A menor altura é do(a) {nome_menor}, com {menor} metros. ')


# --- EXERCÍCIO 3 ---------------------
#      Faça um programa que receba a altura de várias pessoas. 
#      Encontre e apresente a altura da pessoa mais alta e da mais baixa. 
#      Para encerrar a entrada de dados, zero na altura, mas esta não poderá ser 
#      considerada como resposta da altura da pessoa mais baixa.

cont = 0
maior = 0 
menor = 9
altura = float (input('Digite sua altura e quando quiser sair do programa digite zero: '))
while altura > 0:
    nome = input('Digite o seu nome: ')
    if altura >= maior:
        maior = altura
        nome_maior = nome
    if altura <= menor:
        menor = altura
        nome_menor = nome  
    altura = float (input('Digite sua altura e quando quiser sair do programa digite zero: '))   
cont = cont + 1
print(f'A maior altura é do(a) {nome_maior}, com {maior} metros. ')
print(f'A menor altura é do(a) {nome_menor}, com {menor} metros. ')

# --- EXERCÍCIO 4 ---------------------
#      Faça um programa que receba a idade e a altura de várias pessoas. 
#      Calcule e exiba a média das alturas das pessoas com mais de 20 anos. 
#      Para encerrar a entrada de dados, digite uma idade negativa ou igual a zero.

cont = 0
idade = int (input('Digite a sua idade: '))
soma = 0
qtde = 0
while idade > 0:
    altura = float (input('Digite a sua altura: '))
    if idade >= 20:
        soma = soma + altura
        qtde = qtde + 1
    idade = int (input('Digite a sua idade: '))
cont = cont + 1
print(f'A média das alturas das pessoas com mais de 20 anos é: {soma/qtde}')


# --- EXERCÍCIO 5 ---------------------
#      Construir um algoritmo para calcular e apresentar a idade atual de 
#      algumas pessoas em relação ao ano atual, mas não é informado a quantidade
#      de pessoas, então use como critério de parada 
#      (condição da estrutura de repetição, digitar zero no ano de nascimento para sair).

cont = 0
ano_atual = int (input('Digite o ano atual: '))
ano_nasc = int (input('Digite o seu ano de nascimento: '))
while ano_nasc > 0:
  ano_nasc = int (input('Digite o seu ano de nascimento: '))
  print(f'A sua idade é: {ano_atual - ano_nasc}')
  if ano_nasc == 0:
    print('Fim.')
cont = cont + 1 

# --- EXERCÍCIO 6 ---------------------
#      Faça um programa que receba um conjunto de valores inteiros, 
#      calcule e exiba o maior e o menor valor do conjunto.

#           • Para encerrar a entrada de dados, deve ser digitado o valor zero;
#           • Para valores negativos, deve ser enviada uma mensagem;
#           • Esses valores (zero e negativos) não entrarão na lógica de encontrar o maior e o menor valor.

cont = 0
maior = 0
menor = 99
conjunto = int (input('Digite um valor e quando quiser sair da estrutura digite zero: '))
while conjunto > 0:
    if conjunto >= maior:
        maior = conjunto
    if conjunto <= menor:
        menor = conjunto
    conjunto = int (input('Digite um valor e quando quiser sair da estrutura digite zero: '))
if conjunto < 0:
    print('ERRO: Digite um valor inteiro. ')
cont = cont + 1
print(f'O maior valor do conjunto é {maior}, e o menor valor do conjunto é {menor}.')
if conjunto <= 0:
    print('Fim.')