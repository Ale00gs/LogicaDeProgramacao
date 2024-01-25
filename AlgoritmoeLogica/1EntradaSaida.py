# --- EXERCÍCIO 1 ---------------------
# Faça um programa que leia um número, multiplique ele por 2 e apresente o resultado.

#entrada
numero = int (input('Informe um valor: '))
#processamento
resultado = numero * 2
#saída
print('O resultado é ',resultado)

# --- EXERCÍCIO 2 ---------------------
# Faça um programa que:

#     receba quatro números inteiros
#     calcule e mostre a soma desses números.

#entrada
numero1 = int (input('informe o valor 1: '))
numero2 = int (input('informe o valor 2: '))
numero3 = int (input('informe o valor 3: '))
numero4 = int (input('informe o valor 4: '))
#processamento
resultado = numero1 + numero2 + numero3 + numero4 
#saida
print ('o resultado da soma é ',resultado)

# --- EXERCÍCIO 3 ---------------------
# Faça um programa que receba três notas, calcule e mostre a média aritmética.

#entrada
nota1 = float (input('informe a nota 1: '))
nota2 = float (input('informe a nota 2: '))
nota3 = float (input('informe a nota 3: '))
#processamento
resultado_media = (nota1 + nota2 + nota3) / 3
#saida
print ('o resultado da média é ',resultado_media)

# --- EXERCÍCIO 4 ---------------------
# Faça um programa que:

#     receba o salário de um funcionário

#     calcule e mostre o novo salário, sabendo-se que este sofreu um aumento de 25%.

#entrada 
salario_funcionario = float (input('Digite o seu salário atual: '))
#processamento
resultado = (salario_funcionario * 25 / 100) + salario_funcionario
#saida
print('Novo salário: ' ,resultado)

# --- EXERCÍCIO 5 ---------------------
# Faça um programa que receba o salário de um funcionário e o percentual de aumento, 
# calcule e mostre o valor do aumento e o novo salário.

#entrada
salario_funcionario = float (input('Digite o seu salário atual: '))
percentual_aumento = float (input('Digite o percentual de aumento: '))
#processamento
aumento = salario_funcionario * percentual_aumento / 100
novo = salario_funcionario + aumento
#saida
print('o valor do aumento será de: ' ,aumento)
print('Seu novo salário será: ' ,novo)

# --- EXERCÍCIO 6 ---------------------
# Faça um programa que receba o salário base de um funcionário, 
# calcule e mostre o salário a receber, sabendo-se que o funcionário 
# tem gratificação de 5% sobre o salário base e paga imposto de 7% também sobre o salário base.

#entrada
salario_base =  float (input('Digite o seu salário: '))
#processamento
imposto = salario_base * 7 / 100
gratificacao = (salario_base * 5 / 100) + salario_base
salario_final = gratificacao - imposto
#saida 
print('Salário a receber: ' ,salario_final)

# --- EXERCÍCIO 7 ---------------------
# Faça um programa que receba o salário base de um funcionário, 
# calcule e mostre seu salário a receber, sabendo-se que o funcionário 
# tem gratificação de 50,00 sobre o salário base e paga imposto que deve 
# ser lido e é aplicado sobre o salário base.
#entrada

salario_base = float (input('Digite o seu salário: '))
per_imposto = float (input('Digite o percentual de imposto: '))
#processamento
imposto = salario_base * per_imposto/ 100
salario_imp =  salario_base - imposto
salario_a_receber = salario_imp + 50
#saida
print('Salário a receber: ' ,salario_a_receber)

# --- EXERCÍCIO 8 ---------------------
# Faça um programa que receba o valor de um depósito e o valor 
# da taxa de juros, calcule e mostre o valor do rendimento e o 
# valor total depois do rendimento de um mês.

#entrada
valor_deposito = float (input('Digite o valor do depósito: '))
valor_taxaj = float (input('Digite o valor da taxa de juros: '))
#processamento
valor_rendimento = valor_deposito * valor_taxaj / 100
valor_mes1 = valor_rendimento + valor_deposito 
#saida
print ('O valor do rendimento é: ',valor_rendimento)
print ('Valor total depois do rendimento de um mês: ',valor_mes1 )

# --- EXERCÍCIO 9 ---------------------
# Faça um programa que calcule e mostre a área de um triângulo. 
# Sabe-se que: Área = (base * altura) / 2.

#entrada
base = float (input('Digite o valor da base: '))
altura = float (input('Digite o valor da altura: '))
#processamento
area = (base * altura) / 2
#saida
print('A área do triângulo é: ' ,area )

# --- EXERCÍCIO 10 ---------------------
# Faça um programa que calcule e mostre a área de um círculo. 
# Sabe-se que: Área = p * raio 2 (o número 2 significa potência, 
# ou seja, raio é elevado ao quadrado)

#entrada
raio = float (input('digite o valor do raio : '))
#processamento
import math 
area = math.pi * raio ** 2
#saida (area)
print('A área do círculo é: ' ,area)

# --- EXERCÍCIO 11 ---------------------
# Faça um programa que receba um número, calcule e mostre:

#     O número digitado ao quadrado

#     O número digitado ao cubo

#     A raiz do número digitado

#     A raiz cúbica do número digitado

#entrada
numero = int (input('Digite um número: '))
#processamento
num_quad = numero ** 2
num_cubo = numero ** 3
raiz_quad = numero ** (1/2)
raiz_cub = numero ** (1/3)
#saida
print('Número ao quadrado: ' ,num_quad)
print('Número ao cubo: ' ,num_cubo)
print('Raiz quadrada: ' ,raiz_quad)
print('Raiz cúbica : ' ,raiz_cub)

# --- EXERCÍCIO 12 --------------------
#  Faça um programa que receba dois números, 
#  calcule e mostre um elevado ao outro. Use os caracteres **

#entrada
numero1 = int (input('Digite o valor 1: '))
numero2 = int (input('Digite o valor 2: '))
#processamento
elevado = numero1 ** numero2
#saida
print('O resultado é : ' ,elevado)

# --- EXERCÍCIO 13 ---------------------
# Sabe-se que:

#     pé = 12 polegadas
#     1 jarda = 3 pés
#     1 milha = 1760 jarda

# Faça um programa que receba uma medida em pés, faça as conversões a seguir e mostre os resultados.

#     Polegadas;
#     Jardas;
#     Milhas.

#entrada
medida_pe = float (input('Digite a medida: '))
#processamento
pole = medida_pe * 12
jard = medida_pe / 3
mil = medida_pe / 1760
#saida
print('Polegadas: ' ,pole)
print('Jardas: ' ,jard)
print('Milhas: ' ,mil)

# --- EXERCÍCIO 14 ---------------------
# Faça um programa que receba o ano de nascimento de uma pessoa 
# e o ano atual, calcule e mostre:

#     a idade atual da pessoa;
#     quantos anos ela terá em 2050.

#entrada
ano_nasc = int (input('Digite o seu ano de nascimento: '))
ano_atual = int (input('Digite o ano atual: '))
#processamento
idade = ano_atual - ano_nasc
idade_fut = 2050 - ano_atual + idade
#saida
print('Sua idade: ' ,idade)
print('Sua idade em 2050: ',idade_fut)

# --- EXERCÍCIO 15 ---------------------
# O custo ao consumidor de um carro novo é a soma do preço de 
# fábrica com o percentual de lucro do distribuidor e dos impostos 
# aplicados ao preço de fábrica. Faça um programa que receba o preço 
# de fábrica de um veículo, o percentual de lucro do distribuidor e o
# percentual de impostos, calcule e mostre:

#     o valor correspondente ao lucro do distribuidor;
#     o valor correspondente aos impostos;
#     o preço final do veículo.

#entrada
preco_fabrica = float (input('Digite o preço de fábrica: '))
percentual_lucro = float (input('Digite o percentual de lucro: '))
percentual_imposto = float (input('digite o percentual de imposto: '))
#processamento 
lucro_distribuidor = preco_fabrica * percentual_lucro / 100
valor_imposto = preco_fabrica * percentual_imposto/ 100
preco_final = preco_fabrica + lucro_distribuidor + valor_imposto
#saída
print ('Lucro do distribuidor: ',lucro_distribuidor)
print ('Valor correspondente ao imposto: ',valor_imposto)
print ('O preço final do veículo será: ',preco_final)

# --- EXERCÍCIO 16 ---------------------
# Faça um programa que receba o número de horas trabalhadas e o
# valor do salário mínimo, calcule e mostre o salário a receber, seguindo estas regras:

#     a hora trabalhada vale a metade do salário mínimo.
#     o salário bruto equivale ao número de horas trabalhadas multiplicado pelo valor da hora trabalhada.
#     o imposto equivale a 3% do salário bruto.
#     o salário a receber equivale ao salário bruto menos o imposto.

#entrada
qte_horas_trabalhadas = float (input('Quantidade de horas trabalhadas: '))
valor_salario_minimo = float (input('Valor do salário mínimo: '))
#processamento
valor_hora_trabalhada = valor_salario_minimo / 2
valor_salario_bruto = valor_hora_trabalhada * qte_horas_trabalhadas
imposto = valor_salario_bruto * 3 / 100
valor_salario_liquido = valor_salario_bruto - imposto
#saida
print('Salário a receber: ',valor_salario_liquido)

# --- EXERCÍCIO 17 ---------------------
# Um trabalhador recebeu seu salário e o depositou em sua conta bancária. 
# Esse trabalhador emitiu dois cheques e agora deseja saber seu saldo atual. 
# O banco criou uma taxa para a operação bancária de retirada que tem que 
# pagar um imposto de 0.38% e o saldo inicial da conta está zerado.

#entrada
salario = float (input('Digite seu salário: '))
valor_cheque1 = float (input('Digite o valor do cheque 1 : '))
valor_cheque2 = float (input('Digite o valor do cheque 2 : '))
#processamento
imposto_cheque1 = valor_cheque1 * 0.38 / 100
saque1 = valor_cheque1 + imposto_cheque1
imposto_cheque2 = valor_cheque2 * 0.38 / 100
saque2 = valor_cheque2 + imposto_cheque2
saldo = salario - saque1 - saque2
#saida
print('Seu saldo: ',saldo)

# --- EXERCÍCIO 18 ---------------------
# Faça um programa que receba a medida do ângulo (em graus) formado por 
# uma escada apoiada no chão e encostada na parede e a altura da parede 
# onde está a ponta da escada. Calcule e mostre a medida dessa escada. 
# Observação: as funções trigonométricas implementadas nas linguagens de 
# programação trabalham com medidas de ângulos em radianos.

# Observação: Para usar seno em Python, deve-se usar esta linha de código import math e esta, no cálculo, math.sin(numero)

# import math
# escada = altura / math.sin(numero)

#entrada
angulo = float (input( 'Digite o ângulo: '))
altura = float (input( 'Digite a altura: '))

#processamento
import math 
radiano = angulo * math.pi / 180
escada = altura / math.sin (radiano)
  
#saida
print('A medida da escada é: ',escada)

# --- EXERCÍCIO 19 ---------------------
# Sabe-se que o quilowatt de energia custa um quinto do salário mínimo. 
# Faça um programa que receba o valor do salário mínimo e a quantidade de 
# quilowatts consumida por uma residência. Calcule e mostre:

#     o valor de cada quilowatt;
#     o valor a ser pago por essa residência;
#     o valor a ser pago com desconto de 15%

#entrada
valor_salario = float (input('Digite o salário: '))
qtde_quilowatt = float (input('Digite a quantidade de quilowatt: '))
#processamento
valor_quilowatt = valor_salario / 5
valor_em_reais = valor_quilowatt * qtde_quilowatt
valor_descontado = valor_em_reais * 15 / 100
valor_com_descon = valor_em_reais - valor_descontado
#saida
print('O valor de cada quilowatt: ',valor_quilowatt)
print('Valor a ser pago por essa residência: ',valor_em_reais)
print('Valor a ser pago com desconto de 15%: ',valor_com_descon)

# --- EXERCÍCIO 20 ---------------------
# Faça um programa que receba um número real, encontre e mostre:

#     a parte inteira desse número;

#     a parte fracionária desse número;

#     o arredondamento desse número.

# Observação: Para arredondar um número em Python, 
# usa-se a função round(numero), onde se o número real/float estiver 
# em igual distância entre o inteiro de cima e o inteiro de baixo, 
# esta função arredonda para o número par mais próximo.

#entrada
numero = float (input('Digite um número real: '))
#processamento
parte_inteira = numero // 1
parte_fracionaria = numero - parte_inteira
numero_arredondado = round(numero)
#saída
print('A parte inteira do número: ',parte_inteira)
print('A parte fracionária do número: ',parte_fracionaria)
print('O arredondamento do número: ',numero_arredondado)

# --- EXERCÍCIO 21 ---------------------
# Faça um programa que receba uma hora formada por hora e minutos (um número real), calcule e mostre a hora digitada apenas em minutos. Lembre-se de que:

#     para quatro e meia, deve-se digitar 4.30;
#     os minutos vão de 0 a 59.

#entrada
hora = float (input('Digite a hora: '))
#processamento
h = hora // 1
minutos = hora - h
conversao = (h * 60 ) + (minutos * 100)
#saida
print('Conversão da hora em minutos: ',conversao )


# --- EXERCÍCIO 22 ---------------------
# Faça um programa que receba o custo de um espetáculo teatral 
# e o preço do convite desse espetáculo. Esse programa deverá 
# calcular e mostrar a quantidade de convites que devem ser vendidos 
# para que, pelo menos, o custo do espetáculo seja alcançado.

#entrada
custo_espet = float (input('Custo de um espetáculo teatral: '))
preco_conv = float (input('Preço do convite: '))
#processamento
quant_conv = custo_espet / preco_conv 
#saida 
print('Quantidade de convites que devem ser vendidos: ',quant_conv)