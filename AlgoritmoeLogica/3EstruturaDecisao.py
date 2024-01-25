# --- EXERCÍCIO 1 ---------------------
# 1.a) Faça um algoritmo que calcule e exiba o salário reajustado 
# de um funcionário.
# De acordo com a seguinte regra: Salário até 500, reajuste de 50%.

salario = float (input('Digite o seu salário: '))
if salario <= 500:
  salario_reaj = (salario * 50 / 100) + salario
  print('O salário reajustado será R$: ',salario_reaj)

# 1.b) Faça um algoritmo que calcule e exiba o salário reajustado 
# de um funcionário de acordo com a seguinte regra: 
#     • Salário até 500, reajuste de 50%; 
#     • Salários maiores que 500, reajuste de 30%.

salario = float (input('Informe o seu salário: '))
if salario <= 500:
  salario_reaj50 = (salario * 50 / 100) + salario
  print('O salário reajustado é R$: ',salario_reaj50)

else:
  salario_reaj30 = (salario * 30 / 100) + salario
  print('O salário reajustado é R$: ',salario_reaj30)

# --- EXERCÍCIO 2 ---------------------
#  Faça um algoritmo que leia o nome e a idade de uma pessoa, 
#  verifique se a idade de uma pessoa é menor ou maior de idade. 
#  Considera-se maior de idade uma pessoa com 18 anos ou mais. 
#  Como saída o algoritmo deve informar o nome e a idade da pessoa 
#  e depois uma mensagem se ela é ou não maior de idade.

nome = str (input('Digite seu nome: '))
idade = int (input('Digite sua idade: '))
if idade >= 18:
    print(f' Informamos que {nome} tem {idade} anos e é maior de idade. ')
else:
    print(f'Informamos que {nome} tem {idade} anos e é menor de idade. ')

# --- EXERCÍCIO 3 ---------------------
# Tendo como dados de entrada a altura e o sexo (M/F) 
# de uma pessoa (M-masculino ou F-feminino), 
# construa um algoritmo que calcule seu peso ideal, 
# utilizando as seguintes fórmulas:
#       • homem: (72.7 * altura) - 58;
#       • mulher: (62.1 * altura) - 44.7

altura = float (input('Digite sua altura (exemplo: 1.70): '))
sexo = str (input('Sexo (masculino/feminino): '))
if sexo == 'masculino' :
  homem = ( 72.7 * altura ) - 58
  print('O seu peso ideal é: ',homem)
elif sexo == 'feminino' :
  mulher = ( 62.1 * altura ) - 44.7
  print('O seu peso ideal é: ',mulher)

# --- EXERCÍCIO 4 ---------------------
# Faça um algoritmo que leia um número inteiro e mostre uma 
# mensagem indicando se este número é par ou ímpar e se é 
# positivo ou negativo.

numero = int (input('Digite um número: '))
if numero % 2 == 0:
  print('Esse número é par')
else:
  print('Esse número é ímpar')

if numero >= 0:
  print('Esse número é positivo')
else:
  print('Esse número é negativo')    

# --- EXERCÍCIO 5 ---------------------
# Elabore um algoritmo que informando a idade de um nadador o mesmo terá condições de classificar em uma das seguintes categorias: 
#        • infantil = 5 - 10 anos;
#        • juvenil = 11-17 anos; 
#        • adulto = maiores de 18 anos.

idade_nadador = int (input('Informe sua idade: '))
if idade_nadador >= 5 and idade_nadador <=10:
  print('Categoria infantil')
elif idade_nadador >= 11 and idade_nadador <= 17:
  print('Categoria juvenil')
elif idade_nadador >= 18:
  print('Categoria adulto')    
else:
  print('Idade não permitida')  

# --- EXERCÍCIO 6 ---------------------
# Um banco concederá um crédito especial aos seus clientes, 
# variável com o saldo médio no último ano. Faça um algoritmo 
# que leia o saldo médio de um cliente e calcule o valor do crédito 
# de acordo com a tabela a seguir. 
# Mostre uma mensagem informando o saldo médio e o valor do crédito.
        
#         Saldo médio
#         • de 0 a 200 nenhum crédito
#         • de 201 a  400 20% do valor do saldo médio
#         • de 401 a  600 30% do valor do saldo médio
#         • acima de 601 40% do valor do saldo médio

saldo_medio = float (input('Digite o saldo médio: '))
credito = -1
porcent = -1

if saldo_medio >= 0 and saldo_medio <= 200:
  credito = 0 
  porcent = 0

elif saldo_medio >= 201 and saldo_medio <= 400:
  porcent = saldo_medio * 20 / 100
  credito = saldo_medio + porcent

elif saldo_medio >= 401 and saldo_medio <= 600:
  porcent = saldo_medio * 30 / 100
  credito = saldo_medio + porcent

elif saldo_medio >= 601:
  porcent = saldo_medio * 40 / 100
  credito = saldo_medio + porcent

if porcent == -1:
  print('Valor digitado inválido')

else:
  print('O valor do crédito é R$: ',credito)
  print(f'O valor do saldo médio é: {porcent} % ')

# --- EXERCÍCIO 7 ---------------------
# A Organização Mundial de Saúde usa a seguinte tabela 
# para determinar a condição de um adulto, para isso 
# desenvolva um algoritmo para calcular o Índice de 
# Massa Corporal (IMC) e apresenta-lo, dado pela fórmula: 
    
#     IMC = peso / (altura)2   (o número 2 significa, elevado ao quadrado)


#      | CONDIÇÃO        |   IMC em adultos  |
#      | Abaixo do peso  |	 Abaixo de 18.5  |
#      | No peso normal	 |	 Entre 18.5 e 25 |
#      | Acima do peso	 |	 Entre 25.1 e 30 |
#      | Obeso		     |	 Acima de 30     |


peso =  float (input('Digite o seu peso: '))
altura = float (input('Digite a sua altura: '))

imc = peso // altura **2 
resposta = str 

if imc < 18.5:
  resposta = '(abaixo do peso)'

elif imc > 18.5 and imc < 25:
   resposta = '(peso normal)'

elif imc > 25.1 and imc < 30:
   resposta = '(Acima do peso)'

elif imc > 30:
   resposta = '(obeso)' 

print('O seu imc é imc',imc ,resposta )   

# --- EXERCÍCIO 8 ---------------------
# A nota final de um estudante é calculada a partir de 
# três notas atribuídas, respectivamente: 
#         • um trabalho de laboratório;
#         • uma avaliação semestral;  
#         • um exame final. 

# A média das três notas mencionadas obedece aos pesos a seguir:

#   |         NOTA             |  PESO |
#   | Trabalho de laboratório  |   2   |
#   | Avaliação semestral      |   3   |
#   | Exame final              |   5   |

# Faça um programa que receba as três notas
# calcule e mostre a média ponderada e o conceito 
# que segue a tabela:

#   |   MÉDIA PONDERADA     |CONCEITO|
#   |  8,0 <= média <= 10   |    A   |
#   |  7,0 <= média < 8,0   |    B   |
#   |  6,0 <= média < 7,0   |    C   |
#   |  5,0 <= média < 6,0   |    D   |
#   |   0,0 <= média < 5,0  |    E   |
       
# media_ponderada = (nota_traballho * 2 + avaliacao_semestral * 3 + exame_final * 5) / 10

trabalho_lab = float (input('Nota do trabalho de laboratório: '))
avaliacao_semestral = float (input('Nota da avaliação semestral: '))
exame_final = float (input('Nota do exame final: '))

media_ponderada = (trabalho_lab * 2 + avaliacao_semestral * 3 + exame_final * 5 ) / 10
conceito = str 

if  8.1 <= media_ponderada and media_ponderada <= 10:
  conceito = 'A'

elif 7.1 <= media_ponderada and media_ponderada < 8.0:
  conceito = 'B'

elif 6.1 <= media_ponderada and media_ponderada < 7.0:
  conceito = 'C'

elif 5.1 <= media_ponderada and  media_ponderada < 6.0:
  conceito = 'D'

elif 0.0 <= media and media < 5.0:
  conceito = 'E'

print(f'Média ponderada: {media_ponderada} conceito: {conceito}')  

# --- EXERCÍCIO 9 ---------------------
# Faça um programa que receba três notas de um aluno, 
# calcule e mostre a média aritmética e a mensagem constante 
# na tabela a seguir. Aos alunos que ficaram para exame, 
# calcule e mostre a nota que deverão tirar para serem aprovados, 
# considerando que a média exigida é 6,0.

#     |  MÉDIA ARITMÉTICA |   MENSAGEM  |
#     |  0 <= média < 3   |  Reprovado  |
#     |  3 <= média < 6   |  Exame      |
#     |  6 <= média <= 10 |  Aprovado   |

# SE media >= 3 E media < 6
#     ESCREVA “Exame”
#     nota_exame = 12 - media
#     ESCREVA “Você deve tirar a nota”, nota_exame, “para ser aprovado.”

nota1 = float (input('Digite a primeira nota: '))
nota2 = float (input('Digite a segunda nota: '))
nota3 = float (input('Digite a terceira nota: '))

media = (nota1 + nota2 + nota3) // 3

if media >= 0.0 and media < 3.0 :
  resposta = 'reprovado'

elif media >= 3.1 and media < 6.0 :
  nota_exame = 6 - media
  resposta = 'Exame'
  print(f'Você deverá tirar: {nota_exame} para ser aprovado.') 

elif media >= 6.1 and media <= 10.0 :
  resposta = 'aprovado'

print(f'Sua média é: {media}, classificação: {resposta}') 


# --- EXERCÍCIO 10 ---------------------
# Faça um programa que receba dois números e mostre o maior.

numero1 = float (input('Digite um número: '))
numero2 = float (input('Digite outro número: '))
maior = 0

if numero1 > numero2 :
  maior = numero1

elif numero2 > numero1 :
  maior = numero2 

print(f'o número maior é: {maior}') 

# --- EXERCÍCIO 11 ---------------------
# Faça um programa que receba três números e 
# mostre-os em ordem crescente. 
# Suponha que o usuário digitará três números diferentes.


# SE numero1 < numero2 E numero1 < numero3
#     SE numero2 < numero3
#         ESCREVA “A ordem crescente é: “,numero1,“-”,numero2,“-”,numero3
#     SENÃO
#         ESCREVA “A ordem crescente é: “,numero1,“-”,numero3,“-”,numero2
# SE numero2 < numero1 E numero2 < numero3
#     SE numero1 < numero3
#         ESCREVA “A ordem crescente é: “,numero2,“-”,numero1,“-”,numero3
#     SENÃO
#         ESCREVA “A ordem crescente é: “,numero2,“-”,numero3,“-”,numero1
# SE numero3 < numero1 E numero3 < num2
#     SE numero1 < numero2
#         ESCREVA “A ordem crescente é: “,numero3,“-”,numero1,“-”,numero2
#     SENÃO 
#         ESCREVA “A ordem crescente é: “,numero3,“-”,numero2,“-”,numero1
  
numero1 = float (input('Digite um número: '))
numero2 = float (input('Digite outro número: '))
numero3 = float (input('Digite mais um número: '))
r = 0 

if numero1 < numero2 and numero1 < numero3 :
  if numero2 < numero3 :
    print(f'A ordem crescente é: {numero1} - {numero2} - {numero3} ')
  else:
    print(f'A ordem crescente é: {numero1} - {numero3} - {numero2} ')

if numero2 < numero1 and numero2 < numero3:
    if numero1 < numero3:
      print(f'A ordem crescente é: {numero2} - {numero1} - {numero3} ')
    else:
      print(f'A ordem crescente é: {numero2} - {numero3} - {numero1} ')    

if numero3 < numero1 and numero3 < numero2:
  
  if numero1 < numero2:
     print(f'A ordem crescente é: {numero3} - {numero1} - {numero2} ')
  else:
     print(f'A ordem crescente é: {numero3} - {numero2} - {numero1} ')   
  

# --- EXERCÍCIO 12 ---------------------
# Faça um programa que receba três números obrigatoriamente
# em ordem crescente e um quarto número que não siga essa regra. 
# Mostre, em seguida, os quatro números em ordem decrescente. 
# Suponha que o usuário digitará quatro números diferentes.


# SE numero4 > numero3
#     ESCREVA “A ordem decrescente é: “,numero4,“-”,numero3,“-”,numero2,“-”,numero1
# SENÃO SE numero4 > numero2 E numero4 < numero3
#     ESCREVA “A ordem decrescente é: “,numero3,“-”,numero4,“-”,numero2,“-”,numero1
# SENÃO SE numero4 > numero1 E numero4 < numero2
#     ESCREVA “A ordem decrescente é: “,numero3,“-”,numero2,“-”,numero4, “-”,numero1
# SENÃO SE numero4 < numero1
#     ESCREVA “A ordem decrescente é: “,numero3,“-”,numero2,“-”,numero1,“-”,numero4

numero1 = float (input('Digite um número : '))
numero2 = float (input('Digite o número quem vem depois do número anterior: '))
numero3 = float (input('Digite o número que vem depois do número anterior: '))
numero4 = float (input('Digite outro número diferente (não precisa seguir a ordem):'))

if numero4 > numero3:
  print(f'A ordem decrescente é: {numero4} - {numero3} - {numero2} - {numero1} ')

elif numero4 > numero2 and numero4 < numero3:
  print(f'A ordem decrescente é: {numero3} - {numero4} - {numero2} - {numero1} ')

elif numero4 > numero1 and numero4 < numero2:
  print(f'A ordem decrescente é: {numero3} - {numero2} - {numero4} - {numero1} ')

elif numero4 < numero1:
  print(f'A ordem decrescente é: {numero3} - {numero2} - {numero1} - {numero4} ')


# --- EXERCÍCIO 13 ---------------------
# Faça um programa que receba quatro valores: I, A, B e C. 
# Desses valores, I é inteiro e positivo, A, B e C são reais. 
# Escreva os números A, B e C obedecendo à tabela a seguir.

# Suponha que o valor digitado para I seja sempre um valor válido,
# ou seja, 1, 2 ou 3, e que os números digitados sejam diferentes
# um do outro.

#   |    VALOR DE I    |         FORMA A ESCREVER                 |
#   |        1         |A, B e C em ordem crescente.              |
#   |        2         |A, B e C em ordem decrescente             |
#   |        3         |O maior fica entre os outros dois números.|

# SE I == 1
#     SE A<B E A<C
#         SE B<C
#             ESCREVA “A ordem crescente dos números é:”,A,” -”,B,”-”,C
#         SENÃO
#             ESCREVA “A ordem crescente dos números é:”,A,” -”,C,”-”,B
#     SE B<A E B<C
#         SE A<C
#             ESCREVA “A ordem crescente dos números é:”,B,”-”,A,”-”,C
#         SENÃO
#             ESCREVA “A ordem crescente dos números é: “,B,”-”,C,”-”,A
#     SE C<A E C<B
#         SE A<B
#             ESCREVA “A ordem crescente dos números é: “,C,”-”,A,”-”,B
#         SENÃO
#             ESCREVA “A ordem crescente dos números é: “,C,”-”,B,”-”,A
# SE I == 2
#     SE A>B E A>C
#         SE B>C
#             ESCREVA “A ordem decrescente dos números é: “,A,” -”,B,”-”,C
#         SENÃO
#             ESCREVA “A ordem decrescente dos números é: “,A,” -”,C,”-”,B
#     SE B>A E B>C
#         SE A>C
#             ESCREVA “A ordem decrescente dos números é: “,B,” -”,A,”-”,C
#         SENÃO
#             ESCREVA “A ordem decrescente dos números é: “,B,” -”,C,”-”,A
#     SE C>A E C>B
#         SE A>B
#             ESCREVA “A ordem decrescente dos números é: “,C,” -”,A,”-”,B
#         SENÃO
#             ESCREVA “A ordem decrescente dos números é: “,C,” -”,B,”-”,A
# SE I == 3
#     SE A>B E A>C
#         ESCREVA “A ordem desejada é: “,B,”-”,A,”-”,C
#     SE B>A E B>C
#         ESCREVA “A ordem desejada é: “,A,”-”,B,”-”,C
#     SE C>A E C>B
#         ESCREVA “A ordem desejada é: “,A,”-”,C,”-”,B


i = int (input('I: Escolha 1 para mostrar a ordem crescente, 2 para mostrar a ordem decrescente ou 3 para mostrar o maior número entre os outros dois números: '))
a = float (input('Digite um número qualquer: '))
b = float (input('Digite um outro número: '))
c = float (input('Digite mais um número: '))

if i == 1:
  if a < b and a < c:
    if b < c :
      print(f'a ordem crescente dos números é: {a} - {b} - {c} ')
    else:
      print(f'a ordem crescente dos números é: {a} - {c} - {b} ') 
  elif b < a and b < c:
    if a < c:
      print(f'A ordem crescente dos números é: {b} - {a} - {c} ')
    else:
      print(f'A ordem crescente dos números é: {b} - {c} - {a} ')
  elif c < a and c < b:
    if a < b:
      print(f'A ordem crescente dos números é: {c} - {a} - {b} ')
    else:
      print(f'A ordem crescente dos números é: {c} - {b} - {a} ')

if i == 2:
  if a > b and  a > c:
    if b > c:
      print(f'A ordem decrescente dos números é: {a} - {b} - {c} ')
    else:
      print(f'A ordem decrescente dos números é: {a} - {c} - {b} ')
  elif b > a and b > c:
    if a > c:
      print(f'A ordem decrescente dos números é: {b} - {a} - {c} ')
    else:
      print(f'A ordem decrescente dos números é: {b} - {c} - {a} ')
  elif c > a and c > b:
    if a > b:
      print(f'A ordem decrescente dos números é: {c} - {a} - {b} ')
    else:
      print(f'A ordem decrescente dos números é: {c} - {b} - {a} ')


if i == 3:
  if a > b and a > c:
      print(f'A ordem desejada é: {b} - {a} - {c}')
  elif b > a and b > c:
      print(f'A ordem desejada é: {a} - {b} - {c}') 
  elif c > a and c > b:
      print(f'A ordem desejada é: {a} - {c} - {b}')

if i <= 0 or i >= 4:
  print(f'o dígito {i} é inválido, digite 1, 2 ou 3.') 

# --- EXERCÍCIO 14 ---------------------
# Faça um programa que mostre o menu de opções a seguir, 
# receba a opção do usuário e os dados necessários para 
# executar cada operação.

#     Menu de opções:
#     1. Somar dois números.
#     2. Raiz quadrada de um número.

# Observação: raiz = numero ** (1/2), ou 
# import math
# raiz = math.sqrt(numero)

menu = int (input('MENU DE OPÇÕES: Digite 1 para somar dois números ou digite 2 para obter a raíz quadrada de um número: '))

if menu == 1:
  numero1 = float (input('Digite um número: '))
  numero2 = float (input('Digite outro número: '))
  soma = numero1 + numero2
  print('A soma do número é: ',soma)

if menu == 2:
  numero1 = float (input('Digite um número: '))
  raiz = numero1 ** (1/2)
  print(f'A raiz quadrada do {numero1} é: {raiz}')
  
if menu <= 0 or menu >= 3:
  print(f'Digite apenas números correspondentes ao menu de opções: 1 ou 2')

# --- EXERCÍCIO 15 ---------------------
# Faça um programa que mostre a data e a hora do sistema 
# nos seguintes formatos: dia/mês/ano 
#     • mês por extenso
#     • hora:minuto.

# Observação: 
#     from: carrega um módulo/biblioteca da linguagem Python 
#     import: é usado para informar qual objeto desta biblioteca 
#     queremos importar/carregar no nosso programa

#     from datetime import datetime
#     captura a data e hora de hoje de algum país onde esta o 
#     servidor que executa nosso programa em Python
#     quando eu testei, o servidor era de Dacar-Senegal

#     hoje = datetime.now()
#     print ('Ano atual.:',hoje.year)
#     print ('Mês.......:',hoje.month)
#     print ('Dia.......:',hoje.day)
#     print ('Hora......:',hoje.hour)
#     print ('Minuto....:',hoje.minute)
#     print ('Segundos..:',hoje.second)

from datetime import datetime
hoje = datetime.now()
print ('Ano atual.:',hoje.year)
print ('Mês.......:',hoje.month)
print ('Dia.......:',hoje.day)
print ('Hora......:',hoje.hour)
print ('Minuto....:',hoje.minute)
print ('Segundos..:',hoje.second)
if hoje.month == 1:
    print(hoje.day,'/Janeiro/',hoje.year)


# --- EXERCÍCIO 16 ---------------------
# Faça um programa que determine a data cronologicamente 
# maior entre duas datas fornecidas pelo usuário. 
# Cada data deve ser composta por três valores inteiros: 
#     • o primeiro representa o dia;
#     • o segundo, o mês;
#     • o terceiro, o ano.

  
#   SE ano1 > ano2
#       ESCREVA “A maior data é: “,dia1,”-”,mes1,”-”,ano1
#   SENÃO SE ano2>ano1
#       ESCREVA “A maior data é: “,dia2,”-”,mes2,”-”,ano2
#   SENÃO SE mes1>mes2
#       ESCREVA “A maior data é: “,dia1,”-”,mes1,”-”,ano1
#   SENÃO SE mes2>mes1
#       ESCREVA “A maior data é: “,dia2, “-”,mes2,”-”,ano2
#   SENÃO SE dia1>dia2
#       ESCREVA “A maior data é: “-”,dia1,”-”,mia1,” -”,ano1
#   SENÃO SE dia2>dia1
#       ESCREVA “A maior data é: “,dia2,” -”,mes2,”-”,ano2
#   SENÃO
#       ESCREVA “As datas são iguais!”
  
dia1 = int (input('Digite um dia: '))
mes1 = int (input('Digite um mês: '))
ano1 = int (input('Digite um ano: '))
dia2 = int (input('Digite um dia: '))
mes2 = int (input('Digite um mês: '))
ano2 = int (input('Digite um ano: '))

if ano1 > ano2:
    print(f'A maior data é: {dia1} - {mes1} - {ano1}') 
if ano2 > ano1:
    print(f'A maior data é: {dia2} - {mes2} - {ano2}') 
elif mes1 > mes2:
    print(f'A maior data é: {dia1} - {mes1} - {ano1}') 
elif mes2 > mes1:
    print(f'A maior data é: {dia2} - {mes2} - {ano2}') 
elif dia1 > dia2:
    print(f'A maior data é: {dia1} - {mes1} - {ano1}')       
elif dia2 > dia1:
    print(f'A maior data é: {dia2} - {mes2} - {ano2}') 
else:
    print('As datas são iguais!')

# --- EXERCÍCIO 17 ---------------------
# Faça um programa que receba a hora do início de um jogo 
# e a hora do término cada hora é composta por duas 
# variáveis inteiras: 
#     • hora 
#     • minuto. 

# Calcule e mostre a duração do jogo (horas e minutos), 
# sabendo que o tempo máximo de duração do jogo é de 
# 24 horas e que ele pode começar em um dia e 
# terminar no dia seguinte.

#     SE min_inicial > min_f
#         minuto_final = minuto_final + 60
#         hora_final = hora_final – 1
#     SE hora_inicial > hora_final
#         hora_final = hora_final + 24
#     minuto_duracao = minuto_final - minuto_inicial
#     hora_duracao = hora_final - hora_inicial

hora_inicial = int (input('Digite a hora inicial: '))
minuto_inicial = int (input('Digite o minuto inicial: '))
hora_final = int (input('Digite a hora final: '))
minuto_final = int (input('Digite o minuto final: '))

if minuto_inicial > minuto_final:
  minuto_final = minuto_final + 60
  hora_final = hora_final - 1

if hora_inicial > hora_final:
  hora_final = hora_final + 24

minuto_duracao = minuto_final - minuto_inicial
hora_duracao = hora_final - hora_inicial

print(f'O jogo durou {hora_duracao} horas e {minuto_duracao} minutos. ')

# --- EXERCÍCIO 18 ---------------------
# Faça um programa que receba o código correspondente ao cargo de um funcionário e seu salário atual e mostre o cargo, o valor do aumento e seu novo salário. Os cargos estão na tabela a seguir.

#   |CÓDIGO|   CARGO    |   PERCENTUAL   |
#   |   1  |Escriturário|      50%       |
#   |   2  |Secretário  |      35%       |
#   |   3  |Caixa       |      20%       |
#   |   4  |Gerente     |      10%       |
#   |   5  |Diretor     |Não tem aumento |


# SE cargo == 1
#     ESCREVA “O cargo é Escriturário”
#     aumento = salario * 50 / 100
#     ESCREVA “O valor do aumento é: “, aumento
#     novo_sal = salario + aumento
#     ESCREVA “O novo salário é: “, novo_sal
# SENÃO SE cargo == 2
#     ESCREVA “O cargo é Secretário”
#     aumento = salario * 35 / 100
#     ESCREVA “O valor do aumento é: “, aumento
#     novo_sal = salario + aumento
#     ESCREVA “O novo salário é: “, novo_sal
# SENÃO SE cargo == 3
#     ESCREVA “O cargo é Caixa”
#     aumento = salario * 20 / 100
#     ESCREVA “O valor do aumento é: “, aumento
#     novo_sal = salario + aumento
#     ESCREVA “O novo salário é: “,novo_sal
# SENÃO SE cargo == 4
#     ESCREVA “O cargo é Gerente”
#     aumento = salario * 10 / 100
#     ESCREVA “O valor do aumento é: “, aumento
#     novo_sal = salario + aumento
#     ESCREVA “O novo salário é: “, novo_sal
# SENÃO SE cargo == 5
#     ESCREVA “O cargo é Diretor”
#     aumento = salario * 0 / 100
#     ESCREVA “O valor do aumento é: “, aumento
#     novo_sal = salario + aumento
#     ESCREVA “O novo salário é: “, novo_sal

codigo = int (input('Digite o código correspondente ao cargo (1, 2, 3, 4 ou 5):  '))
salario = float (input('Digite o seu salário: '))

if codigo == 1:
  print('O cargo é Escrituário')
  aumento = salario * 50 / 100
  print('O valor do aumento é: ',aumento) 
  novo_sal = salario + aumento
  print('O novo salário é: ',novo_sal)

elif codigo == 2:
  print('O cargo é Secretário')
  aumento = salario * 35 / 100
  print('O valor do aumento é: ',aumento) 
  novo_sal = salario + aumento
  print('O novo salário é: ',novo_sal)

elif codigo == 3:
  print('O cargo é Caixa')
  aumento = salario * 20 / 100
  print('O valor do aumento é: ',aumento) 
  novo_sal = salario + aumento
  print('O novo salário é: ',novo_sal)

elif codigo == 4:
  print('O cargo é Gerente')
  aumento = salario * 10 / 100
  print('O valor do aumento é: ',aumento) 
  novo_sal = salario + aumento
  print('O novo salário é: ',novo_sal)

elif codigo == 5:
  print('O cargo é Diretor')
  print('Sem aumento.') 


if codigo <= 0 or codigo >= 6:
  print('Digite um código válido (1, 2, 3, 4 ou 5)') 

# --- EXERCÍCIO 19 ---------------------
# Faça um programa que apresente o menu a seguir, 
# permita ao usuário escolher a opção desejada, 
# receba os dados necessários para executar a operação 
# e mostre o resultado. Verifique a possibilidade de opção 
# inválida e não se preocupe com restrições, como salário negativo.

#     Menu de opções
#     1. Imposto
#     2. Novo salário
#     3. Classificação
#     Digite a opção desejada:

# Na opção 1: receber o salário de um funcionário, 
# calcular e mostrar o valor do imposto usando as regras a seguir.

#   |           SALÁRIO                          |PERCENTUAL DO IMPOSTO|
#   |Menor que 500,00                            |         5%          |
#   |De 500,00 (inclusive) a  850,00 (inclusive) |        10%          |
#   |Acima de  850,00                            |        15%          |

# Na opção 2: receber o salário de um funcionário, 
# calcular e mostrar o valor do novo salário, 
# usando as regras a seguir.

#   |           SALÁRIO                            |AUMENTO|
#   |Maior que  1.500,00                           | 25,00 |
#   |De  750,00 (inclusive) a  1.500,00 (inclusive)| 50,00 |
#   |De  450,00 (inclusive) a  750,00              | 75,00 |
#   |Menor que  450,00                             | 100,00|

# Na opção 3: receber o salário de um funcionário e
# mostrar sua classificação usando a tabela a seguir.

#   |        SALÁRIO        |CLASSIFICAÇÃO |
#   |Até  700,00 (inclusive)|Mal remunerado|
#   |Maiores que  700,00    |Bem remunerado|


print('Menu de opções: 1.Imposto/ 2.Novo salário/ 3.Classificação ')
menu = int (input('Digite a opção desejada: '))

if menu == 1:
  salario = float (input('Digite seu salário: '))
  if salario < 499.99:
    percent_imp = (salario * 5 / 100) 
  elif salario >= 500.00 and salario < 849.99:
    percent_imp = (salario * 10 / 100) 
  elif salario >= 850.00:
    percent_imp = (salario * 15 / 100) 
    print('O valor do imposto é:',percent_imp)  

if menu == 2:
  salario = float (input('Digite seu salário: '))
  if salario > 1500.00:
    aumento = salario + 25.00
  elif salario <= 1499.90 and salario >= 750.00:
    aumento = salario + 50.00
  elif salario < 749.99 and salario >= 450.00:
    aumento = salario + 75.00
  elif salario < 450.00:
    aumento = salario + 100.00
  print('O valor do novo salário é: ',aumento)

if menu == 3:
  salario = float (input('Digite seu salário: '))
  if salario <= 699.99:
    print('De acordo com seu salário, você é mal remunerado.')
    
  elif salario > 700.00:   
    print('De acordo com seu salário, você é bem remunerado.')

if menu <= 0 or menu >= 4:
  print('Digite uma opção válida do menu (1, 2 ou 3)')

# --- EXERCÍCIO 20 ---------------------
# Faça um programa que receba o salário inicial de um funcionário, 
# calcule e mostre o novo salário, acrescido de bonificação e de 
# auxílio escola.

# |SALÁRIO                 |BONIFICAÇÃO    |
# |Até  500,00             |5% do salário  |
# |Entre  500,00 e 1.200,00|12% do salário |
# |Acima de  1.200,00      |Sem bonificação|

# |SALÁRIO         |AUXÍLIO ESCOLA|
# |Até  600,00     | 150,00       |
# |Acima de  600,00| 100,00       |

# novo_salario = salario + bonificacao + auxílio escola

 salario = float (input('Digite seu salário: '))
 
if salario >= 0 and salario <= 500.00:
  bonificacao = (salario * 5) / 100

elif salario > 501.00 and salario < 1199.00:  
  bonificacao = (salario * 12) / 100 

elif salario >= 1200.00:
  bonificacao = 0

if salario <= 600.00:
  auxilio = 150.00

elif salario > 600.01:
  auxilio = 100.00

novo_salario = salario + bonificacao + auxilio 
print('O seu novo salário é R$:',novo_salario)


# --- EXERCÍCIO 21 ---------------------
# Faça um programa que receba o valor do salário mínimo, 
# o número de horas trabalhadas, o número de dependentes 
# do funcionário e a quantidade de horas extras trabalhadas. 
# Calcule e mostre o salário a receber do funcionário de acordo 
# com as regras a seguir:

#   • O valor da hora trabalhada é igual a 1/5 do salário mínimo.
#   • O salário do mês é igual ao número de horas trabalhadas multiplicado pelo valor da hora trabalhada.
#   • Para cada dependente, acrescentar  32,00.
#   • Para cada hora extra trabalhada, calcular o valor da hora * trabalhada acrescida de 50%.
#   • O salário bruto é igual ao salário do mês mais o valor dos dependentes mais o valor das horas extras.
#   • Calcular o valor do impostoosto de renda retido na fonte de acordo com a tabela a seguir:

#     |IRFF  |SALÁRIO BRUTO        |
#     |Isento|Inferior a  200,00   |
#     |10%   |De  200,00 até 500,00|
#     |20%   |Superior a  500,00   |

#   O salário líquido é igual ao salário bruto menos IRRF.
#   A gratificação é de acordo com a tabela a seguir:

#     |SALÁRIO LÍQUIDO|GRATIFICAÇÃO|
#     |Até 350,00     | 100,00     |
#     |Superior a  350| 50,00      |

#   * O salário a receber do funcionário é igual ao salário líquido mais a gratificação.

#   LEIA salario_minimo, numero_horas_trabalhadas, numero_dependentes, numero_horas_extras
  
#   valor_hora = 1/5 * salario_minimo
#   salario_mes = numero_horas_trabalhadas * valor_hora
#   valor_dependentes = 32 * numero_dependentes
#   valor_hora_extra = numero_horas_extras * (valor_hora + (valor_hora * 50/100))
#   salario_bruto =salario_mes + valor_dependentes + valor_hora_extra
  
#   SE salario_bruto < 200
#         imposto = 0
#   SENÃO SE salario_bruto >= 200 E salario_bruto <= 500
#         imposto = salario_bruto * 10/100
#   SENÃO SE salario_bruto > 500
#         imposto = salario_bruto * 20/100
#   salario_liquido = salario_bruto – imposto
#   SE salario_liquido <= 350
#         gratificacao = 100
#   SENÃO
#         gratificacao = 50
#   salario_a_receber = salario_liquido + gratificacao
  
#   ESCREVA salario_a_receber

salario_minimo = float (input('Digite valor do salário mínimo: '))
numero_horas = float (input('Digite o número de horas trabalhadas: '))
horas_dependentes = float (input('Digite o número de horas dependentes:'))
hora_extra = float (input('Digite a quantidade de horas extras trabalhadas: '))

valor_hora = 1/5 * salario_minimo
salario_mes = numero_horas * valor_hora
valor_dependentes = 32 * horas_dependentes
valor_hora_extra = hora_extra * (( valor_hora * 50 / 100 ) + valor_hora)
salario_bruto = salario_mes + valor_dependentes + valor_hora_extra
 
if salario_bruto < 200:
    imposto = 0
elif salario_bruto >= 200 and salario_bruto <= 500:
    imposto = (salario_bruto * 10) / 100
elif salario_bruto > 500:
    imposto = (salario_bruto * 20) / 100
 
salario_liquido = salario_bruto - imposto

if salario_liquido >= 0 and salario_liquido <= 350:
    gratificacao = 100
else:
    gratificacao = 50

salario_a_receber = salario_liquido + gratificacao
 
print('Seu salário é: ',salario_a_receber) 
  
# --- EXERCÍCIO 22 ---------------------
# Um supermercado deseja reajustar os preços de seus produtos 
# usando o seguinte critério: o produto poderá ter seu preço 
# aumentado ou diminuído. Para o preço ser alterado, 
# o produto deve preencher pelo menos um dos requisitos a seguir:
 
# |VENDA MÉDIA MENSAL |PREÇO ATUAL        |% DE AUMENTO|% DE DIMINUIÇÃO|
# |< 500              |<  30000           |     10     |       -       |
# | >= 500 e <1200    | >= 30.00 e < 80.00|     15     |       -       |
# | >= 1200           | >=  80.00         |      -     |      20       |

# Faça um programa que receba o preço atual e a venda 
# média mensal do produto, calcule e mostre o novo preço.

# LEIA preco_atual, media_mensal_vendas

# SE media_mensal_vendas < 500 OU preco_atual < 30
#     novo_preco = preco_atual + 10/100 * preco_atual
# SENÃO SE media_mensal_vendas >= 500 E media_mensal_vendas < 1200 OU preco_atual >= 30 E preco_atual<80
#     novo_preco = preco_atual + 15 / 100 * preco_atual
# SENÃO SE venda >= 1200 OU preco_atual >= 80
#     novo_preco = preco_atual – 20 / 100 * preco_atual
      
# ESCREVA novo_preco

preco_atual = float (input('Digite o preço atual do produto: '))
media_mensal = float (input('Digite o valor da média mensal do produto: '))

if media_mensal < 500 or preco_atual < 30:
  novo_preco = ( preco_atual * 10/100 ) + preco_atual

elif media_mensal >= 500 and media_mensal < 1200 or preco_atual >= 30 and preco_atual < 80:
  novo_preco = ( preco_atual * 15 / 100 ) + preco_atual

elif media_mensal >= 1200 or preco_atual >= 80:
  novo_preco = ( preco_atual * 20 / 100 ) - preco_atual

print('O novo preço do produto será R$: ',novo_preco)


# --- EXERCÍCIO 23 ---------------------
# Faça um programa para resolver equações do 2 o grau.

# ax² + bx + c = 0

# A variável a deve ser diferente de zero

#   • delta = b ** 2 - 4 * a * c
#   • delta < 0.  Não existe raiz real
#   • delta = 0. Existe uma raiz real
#     ◦ x = (-b) / (2 * a)
#   • delta > 0. Existem duas raízes reais
#     ◦ x1 = -b + raiz(delta)/ (2 * a)
#     ◦ x2 = -b  - raiz(delta)/ (2 * a)

# LEIA a, b, c
# SE a = 0
#     ESCREVA “Estes valores não formam uma equação de segundo grau” 
# SENÃO
#     delta = (b * b) – ( 4 * a * c)
#     SE delta < 0
#         ESCREVA “Não existe raiz real”
#     SE delta = 0
#         ESCREVA “Existe uma raiz real”
#         x1 = (– b) / (2 * a)
#         ESCREVA x1
#     SE delta > 0
#         ESCREVA “Existem duas raízes reais”
#         x1 = (– b) + raiz(delta) / (2 * a)
#         x2 = (– b) - raiz(delta) / (2 * a)
#         ESCREVA(x1, x2)

a = float (input('Digite o valor de a: '))
b = float (input('Digite o valor de b: '))
c = float (input('Digite o valor de c: '))
import math

if a == 0:
  print('Estes valores não formam uma equação de segundo grau') 
else:
  delta = (b ** 2) - (4 * a * c)

  if delta < 0:
        print('Não existe raiz real')

  if delta == 0:
    x1 = (- b) / (2 * a)
    print('Existe uma raiz real: ',x1)
  
  if delta > 0:
    x1 = ((- b) + math.sqrt(delta)) / (2 * a)
    x2 = ((- b) - math.sqrt(delta)) / (2 * a)
    print(f'Existem duas raízes reais: {x1} e {x2} ')

# --- EXERCÍCIO 24 ---------------------
# Dados três valores X, Y e Z, verifique se eles podem ser 
# os comprimentos dos lados de um triângulo e, se forem, 
# verifique se é um triângulo equilátero, isósceles ou escaleno. 
# Se eles não formarem um triângulo, escreva uma mensagem.
# Considere que:

#     • o comprimento de cada lado de um triângulo é menor que a soma dos outros dois lados;
#     • chama-se equilátero o triângulo que tem três lados iguais;
#     • denomina-se isósceles o triângulo que tem o comprimento de dois lados iguais;
#     • recebe o nome de escaleno o triângulo que tem os três lados diferentes.

# LEIA x, y, z
# SE x < y + z E y < x + z E z < x + y
#     SE x = y E y = z
#         ESCREVA “Triângulo Equilátero”
#     SENÃO SE x = y OU x = z OU y = z
#         ESCREVA “Triângulo Isósceles”
#     SENÃO SE x ≠ y E x ≠ z E y ≠ z
#         ESCREVA “Triângulo Escaleno”
# SENÃO
#     ESCREVA “Essas medidas não formam um triângulo”

x = float (input('Digite a medida de x: '))
y = float (input('Digite a medida de y: '))
z = float (input('Digite a medida de z: '))

if (x < (y + z)) and (y < (x + z)) and (z < (x + y)):
  if (x == y) and (y == z):
    print('Triângulo Equilátero')
    
  elif x == y or x == z or y == z:
    print('Triângulo Isósceles')

  elif x != y and x != z and y != z:
    print('Triângulo Escaleno')
else:
    print('Essas medidas não formam um triângulo')

# --- EXERCÍCIO 25 ---------------------
# Faça um programa que receba a altura e peso de uma pessoa. 
# De acordo com a tabela a seguir, verifique e mostre a 
# classificação dessa pessoa.

# |ALTURA          |ATÉ 60|ENTRE 60 E 90 (INCLUSIVE)|ACIMA DE 90|
# |Menores que 1,20|A     |D                        |G          |
# |De 1,20 a 1,70  |B     |E                        |H          |
# |Maiores que 1,70|C     |F                        |I          |

# LEIA altura, peso
# SE altura < 1.20
#     SE peso <= 60
#         ESCREVA “A”
#     SENÃO SE peso > 60 E peso <= 90
#         ESCREVA “D”
#     SENÃO SE peso > 90
#         ESCREVA “G”
# SENÃO SE altura >= 1.20 E altura <= 1.70
#     SE peso <= 60
#         ESCREVA “B”
#     SENÃO SE peso > 60 E peso <= 90
#         ESCREVA “E”
#     SENÃO SE peso > 90
#         ESCREVA “H”
# SENÃO SE altura > 1.70
#     SE peso <= 60
#         ESCREVA “C”
#     SENÃO SE peso > 60 E peso <= 90
#         EESCREVA “F”
#     SENÃO SE peso > 90
#         ESCREVA “I”

altura = float (input('Digite sua altura: '))
peso = float (input('Digite seu peso: '))

if altura < 1.20:
  if peso <= 60:
    print('Classificação A') 
    
  elif peso > 60 and peso <= 90:
    print('Classificação D') 

  elif peso > 90:
    print('Classificação G') 
    
elif altura >= 1.20 and altura <= 1.70:
  if peso <= 60:
    print('Classificação B')

  elif peso > 60 and peso <= 90:
    print('Classificação E')
    
  elif peso > 90:
    print('Classificação H')

elif altura > 1.70:
  if peso <= 60:
    print('Classificação C') 

  elif peso > 60 and peso <= 90:
    print('Classificação F') 

  elif peso > 90:
    print('Classificação I') 

# --- EXERCÍCIO 26 ---------------------
# Faça um programa que receba:

# • O código de um produto comprado, supondo que a 
#   digitação do código do produto seja sempre válida, 
#   isto é, um número * inteiro entre 1 e 10.
# • O peso do produto em quilos.
# • O código do país de origem, supondo que a digitação 
#   do  código seja sempre válida, isto é, um número inteiro entre 1 e 3.

#   |CÓDIGO DO PAÍS DE ORIGEM|IMPOSTO|
#   |1                       |0%     |
#   |2                       |15%    |
#   |3                       |25%    |

#   |CÓDIGO DO PAÍS DO PRODUTO|PREÇO POR GRAMA|
#   |1 a 4                    |10             |
#   |5 a 7                    |25             |
#   |8 a 10                   |35             |

# Calcule e mostre:
# • o peso do produto convertido em gramas;
# • o preço total do produto comprado;
# • valor do imposto, sabendo que ele é cobrado sobre o 
#   preço total do produto comprado e dependendo país de origem;
# • o valor total, preço total do produto mais imposto.

# LEIA codigo_produto, peso_quilos, codigo_pais
# peso_em_gramas = peso_quilos * 1000
# ESCREVA peso_em_gramas
# SE codigo_produto >= 1 E codigo_produto <= 4
#    preco_por_grama = 10
# SENÃO SE codigo_produto >= 5 E codigo_produto <= 7
#    preco_por_grama = 25
# SENÃO SE codigo_produto >= 8 E codigo_produto <= 10
#    preco_por_grama = 35    
# preco_total = peso_em_gramas *preco_por_grama
# ESCREVA preco_total
# SE codigo_pais = 1
#     imposto = 0
# SENÃO SE codigo_pais = 2
#     imposto = preco_total * 15/100
# SENÃO SE codigo_pais = 3
#     imposto = preco_total * 25/100    
# ESCREVA imposto
# valor_total = preco_total + imposto
# ESCREVA valor_total

codigo_produto = int (input('Digite o código do produto comprado: '))
peso_quilos = float (input('Digite o peso do produto (em quilos): '))
codigo_pais = int (input('Digite o código do país de origem: '))

peso_grama = peso_quilos * 1000
print('O peso em gramas é: ',peso_grama)

if codigo_produto < 1 or codigo_produto > 10:
  print('Digite um valor válido para o código do produto (número inteiro entre 1 e 10)')

if codigo_pais < 1 or codigo_pais > 3:
  print('Digite um valor válido para o código do país de origem (número inteiro entre 1 e 3)')

if codigo_produto >= 1 and codigo_produto <= 4:
   preco_por_grama = 10

elif codigo_produto >= 5 and codigo_produto <= 7:
   preco_por_grama = 25

elif codigo_produto >= 8 and codigo_produto <= 10:
   preco_por_grama = 35    

preco_total = peso_grama * preco_por_grama
print('O preço total do produto comprado é R$: ',preco_total)

if codigo_pais == 1:
    imposto = 0
elif codigo_pais == 2:
    imposto = (preco_total * 15) / 100
elif codigo_pais == 3:
    imposto = (preco_total * 25) / 100    
print('O imposto é R$: ',imposto)

valor_total = preco_total + imposto
print('O valor total é R$: ',valor_total)


# --- EXERCÍCIO 27 ---------------------
# Faça um programa que receba:
# • o código do estado de origem da carga de um caminhão, 
#   supondo que a digitação do código do estado seja sempre 
#   válida, isto é, um número inteiro entre 1 e 5;
# • o peso da carga do caminhão em toneladas;
# • o código da carga, supondo que a digitação do código seja 
#   sempre válida, isto é, um número inteiro entre 10 e 40.

#     | CÓDIGO DO ESTADO| IMPOSTO|
#     |1                |35%     |
#     |2                |25%     |
#     |3                |15%     |
#     |4                |5%      |
#     |5                |Isento  |


#     |CÓDIGO DA CARGA|PREÇO POR QUILO |
#     |10 a 20        |100             |
#     |21 a 30        |250             |
#     |31 a 40        |400             |

# Calcule e mostre:
# • o peso da carga do caminhão convertido em quilos;
# • o preço da carga do caminhão;
# • o valor do imposto, sabendo que o imposto é cobrado sobre o preço da carga do caminhão e depende do estado de origem;
# • o valor total transportado pelo caminhão, preço da carga mais imposto.

# LEIA codigo_estado, peso_em_toneladas, codigo_carga
# peso_em_quilos = peso_em_toneladas * 1000
# ESCREVA peso_em_quilos
# SE codigo_carga >= 10 E codigo_carga <= 20
#     preco_da_carga = 100 * peso_em_quilos
# SENÃO SE codigo_carga >= 21 E codigo_carga <= 30
#     preco_da_carga = 250 * peso_em_quilos
# SENÃO SE codigo_carga >= 31 E codigo_carga <= 40
#     preco_da_carga = 340 * peso_em_quilos   
# ESCREVA preco_da_carga
# SE codigo_estado = 1
#     imposto = 35/100 * preco_da_carga
# SENÃO SE codigo_estado = 2
#     imposto = 25/100 * preco_da_carga
# SENÃO SE codigo_estado = 3
#     imposto = 15/100 * preco_ds_carga
# SENÃO SE codigo_estado = 4
#     imposto = 5/100 * preco_da_carga
# SENÃO SE codigo_estado = 5
#     imposto = 0
# ESCREVA imposto
# valor_total = preco_da_carga + imposto
# ESCREVA valor_total

codigo_estado = int (input('Digite o código do estado de origem da carga do caminhão: '))
peso_em_toneladas = float (input('Digite o peso da carga do caminhão (em toneladas): '))
codigo_carga = int (input('Digite o código da carga: '))

if codigo_estado < 1 or codigo_estado > 5:
  print('Digite um valor válido para o código do estado (número inteiro entre 1 e 5)')

if codigo_carga < 10 or codigo_carga > 40:
  print('Digite um valor válido para o código da carga (número inteiro entre 10 e 40)')

peso_em_quilos = peso_em_toneladas * 1000
print('O peso em quilos é: ',peso_em_quilos)

if codigo_carga >= 10 and codigo_carga <= 20:
  preco_da_carga = 100 * peso_em_quilos

elif codigo_carga >= 21 and codigo_carga <= 30:
  preco_da_carga = 250 * peso_em_quilos

elif codigo_carga >= 31 and codigo_carga <= 40:
  preco_da_carga = 340 * peso_em_quilos   
  print('O preço da carga é R$: ',preco_da_carga)

if codigo_estado == 1:
  imposto = (35 / 100) * preco_da_carga

elif codigo_estado == 2:
  imposto = (25 / 100) * preco_da_carga

elif codigo_estado == 3:
  imposto = (15 / 100) * preco_da_carga

elif codigo_estado == 4:
  imposto = (5 / 100) * preco_da_carga

elif codigo_estado == 5:
    imposto = 0
print('O valor do imposto é R$: ',imposto)

valor_total = preco_da_carga + imposto
print('O valor total é R$: ',valor_total)


# --- EXERCÍCIO 28 ---------------------
# Faça um programa que receba o salário base e o tempo de serviço 
# de um funcionário. Calcule e mostre: O imposto, conforme a tabela a seguir.

#   |SALÁRIO BASE    |% SOBRE O SALÁRIO BASE|
#   | < 200          |isento                |
#   | >= 250 E <= 450|3%                    | 
#   | >  450 E < 700 |8%                    |
#   | >=  700        |12%                   |

#  A gratificação, de acordo com a tabela a seguir.

# |SALÁRIO BASE R$  |TEMPO DE SERVIÇO|GRATIFICAÇÃO|
# |Superior a 500,00|Até 3 anos      |20          |
# |Mais de 3 anos   |30              |            |
# |        -        |      -         |    -       |
# |Até 500,00       |Até 3 anos      |23          |
# |Entre 3 e 6 anos |35              |            |
# |Acima de 6 anos  |33              |            |

# • O salário líquido, ou seja, salário base menos imposto mais gratificação.
# • A categoria, que está na tabela a seguir.

# LEIA salario_base, tempo

# SE salario_base < 200
#     imposto = 0
# SENÃO SE salario_base <= 450
#     imposto = 3/100 * salario_base
# SENÃO SE sal_base < 700
#     imposto = 8/100 * salario_base
# SENÃO
#     imposto = 12/100 * salario_base
# ESCREVA imposto
# SE salario_base > 500
#     SE tempo <= 3
#          gratificacao = 20
#     SENÃO 
#         gratificacao = 30
# SENÃO
#     SE tempo <= 3
#         gratificacao = 23
#     SENÃO SE tempo < 6
#         gratificacao = 35
#     SENÃO gratificacao = 33
# ESCREVA gratificacao
# salario_liquido = salario_base – imposto + gratificacao
# ESCREVA salario_liqquido
# SE salario_liquido <= 350
#     ESCREVA “Classificação A”
# SENÃO SE salario_liqquido < 600
#     ESCREVA “Classificação B”
# SENÃO
#     ESCREVA “Classificação C”

salario_base = float (input('Digite o salário base R$: '))
tempo = float (input('Digite o tempo de serviço (anos): '))

if salario_base < 200:
  imposto = 0

elif salario_base <= 450:
  imposto = 3 / 100 * salario_base

elif salario_base < 700:
    imposto = 8 / 100 * salario_base 

else:
  imposto = 12 / 100 * salario_base
  print('O valor do imposto é R$: ',imposto)

if salario_base > 500:
    if tempo <= 3:
      gratificacao = 20
    else:
        gratificacao = 30
else:
  if tempo <= 3:
      gratificacao = 23
      
  elif tempo < 6:
    gratificacao = 35
  else: 
    gratificacao = 33

print('A gratificação é de R$: ',gratificacao) 

salario_liquido = salario_base - imposto + gratificacao
print('O salário liquido é R$: ',salario_liquido)

if salario_liquido <= 350:
  print('Classificação A')

elif salario_liquido < 600:
  print('Classificação B')

else: print('Classificação C')


# --- EXERCÍCIO 29 ---------------------
# Faça um programa que:
# • receba o valor do salário mínimo,
# • o turno de trabalho (M — matutino; V — vespertino; ou N — noturno),
# • a categoria (O — operário; G — gerente) 
# • número de horas trabalhadas no mês de um funcionário. 

# •Suponha a digitação apenas de dados válidos e, quando houver digitação de letras, utilize maiúsculas.*

# Calcule e mostre:

# • O coeficiente do salário, de acordo com a tabela a seguir.

# TURNO DE TRABALHO|VALOR DO COEFICIENTE
# M - Matutino     |10% do salário mínimo
# V - Vespertino   |15% do salário mínimo
# N - Noturno      |20% do salário mínimo

# • O valor do salário bruto, ou seja, o número de horas trabalhadas multiplicado pelo valor do coeficiente do salário.

# • O imposto, de acordo com a tabela a seguir.

# CATEGORIA   | SALÁRIO BRUTO|IMPOSTO SOBRE O SALÁRIO BRUTO
# O - Operário| >= 300,00    |5%
# O - Operário| < 300,00     |3%
# G - Gerente | >= 300,00    |6%
# G - Gerente | < 300,00     |4%

# • A gratificação, de acordo com as regras a seguir. Se o funcionário preencher todos os requisitos a seguir, sua gratificação será de 50,00; caso contrário, será de 30,00. Os requisitos são:
#  • Turno: Noturno
#   • Número de horas trabalhadas: Superior a 80 horas
#   • O auxílio alimentação, de acordo com as seguintes regras.
# • Auxilio alimentação, um terço do seu salário bruto; caso contrário, será de metade do seu salário bruto. Os requisitos são:
#   • Se o funcionário preencher algum dos requisitos a seguir, seu auxílio alimentação será de 
#   • Categoria: Operário
#   • Coeficiente do salário: < = 25
# • O salário líquido, ou seja, salário bruto menos imposto mais gratificação mais auxílio alimentação.
# • A classificação, de acordo com a tabela a seguir:

# SALÁRIO LÍQUIDO   |MENSAGEM
# Menor que 350,00  |Mal remunerado
# Entre 350 e 600,00|Normal
# Maior que 600,00  |Bem remunerado

# LEIA salario_minino, turno, categoria, numero_de_horas_trabalhadas
# SE turno = “M”
#      coeficiente = 10/100 * salario_minino
# SENÃO SE turno = “V”
#      coeficiente = 15/100 * salario_minino
# SENÃO SE turno = “N”
#      coeficiente = 12/100 * salario_minino
     
# ESCREVA coeficiente

# salario_bruto = numero_de_horas_trabalhadas * coeficiente

# ESCREVA salario_bruto

# SE categoria = “O”
#     SE sal_bruto >= 300
#         imposto = 5/100 * sal_bruto
#     SENÃO
#         imposto = 3/100 * sal_bruto
# SENÃO 
#     SE salario_bruto >= 400
#         imposto = 6/100 * salario_bruto
#     SENÃO
#          imposto = 4/100 * salario_bruto
         
# ESCREVA imposto

# SE turno = “N” E numero_de_horas_trabalhadas > 80
#     gratificacao = 50
# SENÃO
#     gratificacao = 30
    
# ESCREVA gratificacao

# SE categoria = “O” OU coeficiente <= 25
#     auxilio = 1/3 * salario_bruto
# SENÃO
#     auxilio = 1/2 * salario_bruto
    
# ESCREVA auxilio

# salario_liquido = salario_bruto – imposto + gratificacao + auxilio

# ESCREVA salario_liquido

# SE salario_liquido < 350
#      ESCREVA “Mal Remunerado”
# SENÃO SE salario_liquido >= 350 E salario_liqquido <= 600
#      ESCREVA “Normal”
# SENÃO SE salario_liquido > 600
#      ESCREVA “Bem Remunerado”

salario_minimo = float (input('Digite o salário mínimo R$: '))
turno = str (input('Digite o turno trabalho: M-matutino, V-vespertino, N-noturno (Apenas a letra maiúscula): '))
categoria = str (input('Digite a categoria: O-operário; G-gerente (Apenas a letra maiúscula): '))
numero_de_horas_trabalhadas = float (input('Digite as horas trabalhadas no mês: '))

if turno == 'M':
  coeficiente = 10 / 100 * salario_minimo

elif turno == 'V':
  coeficiente = 15 / 100 * salario_minimo

elif turno == 'N':
  coeficiente = 12 / 100 * salario_minimo
  print('Coeficiente: ',coeficiente)

salario_bruto = numero_de_horas_trabalhadas * coeficiente
print('O salário bruto é R$: ',salario_bruto)

if categoria == 'O':
    if salario_bruto >= 300:
        imposto = 5 / 100 * salario_bruto
    else:
        imposto = 3 / 100 * salario_bruto
else: 
    if salario_bruto >= 400:
        imposto = 6 / 100 * salario_bruto
    else:
         imposto = 4 / 100 * salario_bruto
print('O valor do imposto é R$: ',imposto)

if turno == 'N' and numero_de_horas_trabalhadas > 80:
  gratificacao = 50
else:
  gratificacao = 30
print('O valor da gratificação é: ',gratificacao)

if categoria == 'O' or coeficiente <= 25:
    auxilio = 1 / 3 * salario_bruto
else:
    auxilio = 1 / 2 * salario_bruto
print('O valor do auxilio é R$: ',auxilio)

salario_liquido = salario_bruto - imposto + gratificacao + auxilio
print('O salário líquido é R$: ',salario_liquido)

if salario_liquido < 350:
  print('Mal remunerado') 

elif salario_liquido >= 350 and salario_liquido <= 600:
  print('Normal')

elif salario_liquido > 600:
     print('Bem Remunerado')
     
# --- EXERCÍCIO 30 ---------------------
# Faça um programa que receba de um produto:
# • o preço
# • o tipo (A — alimentação; L — limpeza; e V — vestuário)
# • a refrigeração (S — produto que necessita de refrigeração; 
#   e N — produto que não necessita de refrigeração) .

# Suponha que haverá apenas a digitação de dados válidos e, 
# quando houver digitação de letras, utilize maiúsculas. 
# Calcule e mostre:

# • O valor adicional, de acordo com a tabela a seguir:

# REFRIGERAÇÃO|TIPO        |PREÇO       |VALOR ADICIONAL
# N           |A           | <  15,00   |2,00
#      -      | >= 15,00   |5,00        | -
#      -      | -          |   -        | -
# L           |< 10,00     |1,50        | - 
#      -      | >= 10,00   |2,50        | -
#      -      | -          |   -        | -
# V           |< 30,00     |3,00        | -
#             | >= 30,00   |2,50        | -
#      -      | -          |   -        | -  
# S           |A           |   -        |8,00
# L           | -          |0,00        | -  
# V           | -          |0,00        | - 

# • O valor do imposto, de acordo com a regra a seguir.

# PREÇO   |PERCENTUAL SOBRE O PREÇO
# < 25,00 |5%
# >= 25,00|8%

# O preço de custo, ou seja, preço mais imposto.
# O desconto, de acordo com a regra a seguir.

# O produto que não preencher nenhum dos requisitos a seguir 
#terá desconto de 3%, caso contrário, 0 (zero). Os requisitos são:
# • Tipo: A
# • Refrigeração: S

# • O novo preço, ou seja, preço de custo mais adicional menos desconto.
# • A classificação, de acordo com a regra a seguir.

# NOVO PREÇO          |CLASSIFICAÇÃO
# <= 50,00            |Barato
# Entre 50,00 e 100,00|Normal
# >= 100,00           |Caro

# LEIA pre, tipo, refrig
# SE refrig = “N”
#     SE tipo = “A”
#         SE pre < 15
#            valor_adic = 2
#         SENÃO 
#            valor_adic = 5
#     SE tipo = “L”
#         SE pre < 10
#            valor_adic = 1.5
#         SENÃO 
#            valor_adic = 2.5
#     SE tipo = “V”
#         SE pre < 30
#            valor_adic = 3
#         SENÃO 
#            valor_adic = 2.5
# SENÃO SE tipo = “A”
#     valor_adic = 8
#     SE tipo = “L”
#         valor_adic = 0
#     SE tipo = “V”
#         valor_adic = 0
# ESCREVA valor_adic
# SE pre < 25
#     imposto = 5/100 * pré
# SENÃO 
#     imposto = 8/100 * pre
# ESCREVA imposto
# pre_custo = pre + imposto
# ESCREVA pre_custo
# SE tipo != “A” E refrig != “S”
#   desconto = 3/100 * pre_custo
# SENÃO 
#   desconto = 0
# ESCREVA desconto
# novo_pre = pre_custo + valor_adic – desconto
# ESCREVA novo_pre
# SE novo_pre <= 50
#     ESCREVA “Barato”
# SENÃO SE novo_pre < 100
#     ESCREVA “Normal”
# SENÃO 
#     ESCREVA “Caro”

preco = float (input('Digite o preço do produto R$: '))
tipo = str (input('Digite o tipo do produto: A — alimentação, L — limpeza, e V — vestuário (Apenas a letra maiúscula): '))
refrigeracao = str (input('Digite "S" se o produto necessita de refrigeração e "N" se o produto não necessita de refrigeração.' ))
  
if tipo == 'L':
    if preco < 10 :
       valor_adic = 1.5

else: 
    valor_adic = 2.5

if tipo == 'V':
    if preco < 30 :
      valor_adic = 3

else: 
    valor_adic = 2.5

if tipo == 'A':
    valor_adic = 8
  
if tipo == 'L':
      valor_adic = 0
    
if tipo == 'V':
    valor_adic = 0

print('O valor adicional é: ',valor_adic)

if refrigeracao == 'S':
  valor_adic = 5

elif refrigeracao == 'N':
  if tipo == 'A':
    if preco < 15 :
      valor_adic = 2

if preco < 25:
    imposto = 5 / 100 * preco

else: imposto = 8 / 100 * preco

print('O valor do imposto é: ',imposto)

pre_custo = preco + imposto
print('O preço do custo é R$: ',pre_custo)

if tipo != 'A' and refrigeracao != 'S':
  desconto = 3 / 100 * pre_custo

else: desconto = 0

print('Desconto: ',desconto)

novo_pre = pre_custo + valor_adic - desconto
print('Novo preço: ',novo_pre)


if novo_pre <= 50:
   print('Barato')

elif novo_pre < 100:
    print('Normal')

else:
    print('Caro') 
    

# --- EXERCÍCIO 31 ---------------------
# Faça um programa que receba a medida de um ângulo em graus. 
# Calcule e mostre o quadrante em que se localiza esse ângulo. 
# Considere os quadrantes da trigonometria e, 
# para ângulos maiores que 360° ou menores que −360o, 
# reduzí-los, mostrando também o número de voltas e o 
# sentido da volta (horário ou anti-horário).

# SE angulo > 360 OU angulo < -360
#     voltas = parte inteira(angulo / 360)    
#     angulo = RESTO(angulo / 360)
# SENÃO 
#     voltas = 0
# SE angulo = 0 OU angulo = 90 OU angulo = 180
#            OU angulo = 270 OU angulo = 360
#            OU angulo = -90 OU angulo = -180
#            OU angulo = -270 OU angulo = -360
#   ESCREVA “Está em cima de algum dos eixos”
#   SE (angulo > 0 E angulo < 90) OU (angulo < -270 E angulo > -360)
#     ESCREVA “1o Quadrante”
#   SENÃO SE (angulo > 90 E angulo < 180) OU (angulo < -180 E angulo > -270)
#     ESCREVA “2o Quadrante”
#   SENÃO SE (angulo > 180 E angulo < 270) OU (angulo < -90 E angulo > -180)
#     ESCREVA “3o Quadrante”
#   SENÃO SE (angulo > 270 E angulo < 360) OU (angulo < 0 E angulo > -90)
#     ESCREVA “4o Quadrante”
#   ESCREVA voltas, “ volta(s) no sentido “
# SE angulo < 0
#     ESCREVA “horário”
# SENÃO 
#     ESCREVA “anti-horário”

angulo = float (input('Digite a medida de um ângulo (em graus): '))

if angulo > 360 or angulo < -360:
  voltas = angulo // 360    
  angulo = angulo % 360

else: 
  voltas = 0

if angulo == 0 or angulo == 90 or angulo == 180 or angulo == 270 or angulo == 360 or angulo == -90 or angulo == -180 or angulo == -270 or angulo == -360:
  print('Está em cima de algum dos eixos')

if (angulo > 0 and angulo < 90) or (angulo < -270 and angulo > -360):
  print('1º Quadrante')

elif (angulo > 90 and angulo < 180) or (angulo < -180 and angulo > -270):
  print('2º Quadrante')

elif (angulo > 180 and angulo < 270) or (angulo < -90 and angulo > -180):
  print('3º Quadrante')

elif (angulo > 270 and angulo < 360) or (angulo < 0 and angulo > -90):
  print('4º Quadrante')
print(f'Número de volta(s): {voltas}')

if angulo < 0:
    print('horário') 

else:
    print('anti-horário')

# -----------------------
