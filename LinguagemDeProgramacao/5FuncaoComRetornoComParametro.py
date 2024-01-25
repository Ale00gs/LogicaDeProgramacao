"""
### 1. (Função com retorno com parâmetro) Faça um programa contendo uma função/método que receba por parâmetro um número e o multiplique por 2, retorne e apresente o resultado da função.
"""

def multiplicar(numero):
    r = numero * 2
    return r

def main():
    n = int (     input('Informe o número: ')      )
    print('O resultado da multiplicação é',multiplicar(n))

    # outra forma de chamar a função com retorno
    x = multiplicar(n)
    print('O resultado da multiplicação é...:',x)
    # supondo que fosse necessário utilizar o valor desta função
    # daqui em diante, segue um exemplo
    if x > 5:
        print('É maior que 5')
        w = x + 1000
        print('W = ',w)

main()

def multiplicar(numero):
    r = numero * 2
    return r

def main():
    n = int(input('Informe o número: '))
    print('O resultado da multiplicação é',multiplicar(n))

main()

"""### 2. (Função com retorno com parâmetro) Faça um programa contendo uma função/método que receba dois números via parâmetro, some os dois valores, retorne e apresente o resultado."""

def somar(numero_um, numero_dois):
    soma = numero_um + numero_dois
    return soma


def main(): 
   numero_um = int(input('Digite um número para realizar a soma: '))
   numero_dois = int(input('Digite outro número para realizar a soma: '))
   print(f'O resultado da soma de {numero_um} + {numero_dois} é:' ,somar(numero_um,numero_dois))

main()

"""### 3. (Função com retorno com parâmetro) Faça um programa contendo uma função/método que receba um valor de porcentagem de aumento via parâmetro, aplique este aumento a um salário de um funcionário, retorne e apresente o novo salário."""

def receber_valor(salario,valor):
    aumento = (valor / 100) * salario
    salario_novo = aumento + salario 
   
    return salario_novo

def main():
    valor = int(input('Digite um valor da porcentagem: '))
    salario = float(input('Digite o salário do funcionário: '))
    print('O salário novo do funcionário é: ' ,receber_valor(salario,valor))
  

main()

"""### 4. (Função com retorno com parâmetro) Faça um programa contendo uma função/método que receba duas notas (P1, P2) calcule a média, chame outra função na main que avalie se este aluno esta aprovado ou reprovado retornando a str/string 'Aprovado' ou 'Reprovado'."""

def calcular_media(p1,p2):
    soma = p1 + p2
    media = soma / 2
    return media

def aprovar_reprovar(media):
    if media >= 6:
        result = 'Aprovado'
    else:
        result = 'Reprovado'
        
    return result


def main():
    p1 = float(input('Digite o valor da primeira nota: '))
    p2 = float(input('Digite o valor da segunda nota: ')) 
    calc = calcular_media(p1,p2)
    
    # print('A média das notas é: ',calcular_media(p1,p2))
    print('Você foi: ',aprovar_reprovar(calc))
main()

"""### 5. (Função com retorno com parâmetro) Faça um programa contendo uma função/método que receba um valor de porcentagem de aumento e um salário via parâmetro, aplique este aumento ao salário do funcionário. Na parte principal do programa, na chamada da função, utilize um laço de repetição para ler 10 salários, chame a função para aplicar o aumento e gerar o novo salário, ainda dentro da estrutura de repetição acumule os novos salários e ao final apresente quanto será gasto no novo salário. Também apresente qual será a diferença entre o que se pagava para todos os funcionário e o que será pago após o aumento."""

def calcular_aumento(salario,porcent):
    salario_novo = (salario * porcent / 100) + salario
    return salario_novo

def saber_porcent():
     porcent = (int(input('Digite um valor de porcentagem: ')))
     return porcent

def main():
    qtd_f = 0
    soma_salario_novo = 0
    soma_salario_antigo = 0
    
    while (qtd_f < 10):
        salario = (float(input('Digite o salário: ')))
        # print('o salário novo é: ',calcular_aumento(salario,porcent))
        soma_salario_novo = soma_salario_novo + calcular_aumento(salario,saber_porcent())
        soma_salario_antigo = soma_salario_antigo + salario
        qtd_f = qtd_f + 1
         
    print('Soma dos salários novos: ',soma_salario_novo)
    print('Soma dos salários antigos: ',soma_salario_antigo)
    dif = soma_salario_novo - soma_salario_antigo
    print(f'Diferença entre o que se pagava para todos os funcionário e o que será pago após o aumento {soma_salario_antigo} - {soma_salario_novo}: {dif}')
    
main()

# ajuda 6, 7 e 8
# def menu():
#     print('\n*** Minha Calculadora ***')
#     print('+ Soma dois números ')
#     print('- Subtrai dois números')
#     print('* Multiplica dois números')
#     print('/ Divide dois números')
#     opcao = input('\nQual opção deseja? ')
#     return opcao
 
# def somar(num1, num2):
#     # desenvolva a lógica de cálculo
 
# def subtrair(num1, num2):
#     # desenvolva a lógica de cálculo
 
# def multiplicar(num1, num2):
#     # desenvolva a lógica de cálculo
 
# def dividir(num1, num2):
#     # desenvolva a lógica de cálculo, cuidado com a divisão por zero
 
# def main():
#     op = menu()
#     while op == '+' or op == '-' or op == '*' or op == '/':
#         n1 = int(input('\nDigite um número.....: '))
#         n2 = int(input('Digite outro número..: '))
#         if op == '+':
#             # chame a função que calculará
#         if op == '-':
#             # chame a função que calculará
#         if op == '*':
#             # chame a função que calculará
#         if op == '/':
#             # chame a função que calculará)
#         op = menu()
 
#     print('\nTermino do programa...............')
 
# main()

"""### 6. (Função com retorno com parâmetro) Faça um programa contendo algumas funções:
a) Função para construir um menu de opções para uma calculadora, como neste exemplo:

    Menu de cálculos
    1.   Número ao quadrado
    2.   Número ao cubo
    3.   Raiz do número
    4.   Raiz cúbica do número
    Qual é a opção desejada?

b) Desenvolva uma função para cada opção de cálculo.

Observação: Na chamada da função deve-se utilizar uma estrutura de repetição que permita diversos cálculos, quando o usuário quiser sair da calculadora digitará qualquer valor diferente dos **números** do menu.

A função da construção do menu, chamará todas as outras passando a elas o valor digitado.

"""

def menu():
    print('-='*50)
    print('MENU DE CÁLCULOS')   
    print()
    print('1. Número ao quadrado \n2. Número ao cubo \n3. Raiz do número \n4. Raiz cúbica do número')
    print('-='*50)
    opcao = input('\nQual opção deseja? (Para sair, digite um valor diferente dos números do menu) ')
    return opcao

def calcular_quadrado(numero): #print(n ** 2)
    quadrado = numero ** 2 
    return quadrado

def calcular_cubo(numero): #print(n ** 3)
    cubo = numero ** 3
    return cubo

def calcular_raiz(numero): #print(n ** (1/2))
    raiz_qua = numero ** (1/2)
    return raiz_qua

def calcular_raiz_cubica(numero): #print(n** (1/3))
    raiz_cub = numero ** (1/3)
    return raiz_cub

def main():
    opc = menu()
    
    while opc == '1'or opc == '2'or opc == '3'or opc == '4':
        numero = int(input('Digite um número: '))

        if opc == '1':
           print('Resultado de' ,numero, 'ao quadrado: ' ,calcular_quadrado(numero))
            
        if opc == '2':
             print('Resultado de',numero, 'ao cubo: ' ,calcular_cubo(numero))


        if opc == '3':
             print('Resultado da raiz quadrada de' ,numero, ':'  ,calcular_raiz(numero))

        if opc == '4':
            print('Resultado da raiz cúbica de' ,numero, ':' ,calcular_raiz_cubica(numero))
        
        opc = menu()
        

       
main()

"""### 7. (Função com retorno com parâmetro) Faça um programa contendo algumas funções:
a) Função para construir um menu de opções para uma calculadora:

    *** Minha Calculadora ***
    Digite um número.....: 
    Digite outro número..: 
        + Soma dois números
        - Subtrai dois números
        * Multiplica dois números
        / Divide dois números
    Qual opção deseja? 

b) Desenvolva uma função para cada opção de cálculo, **mas estas não terão retorno**.

Observação: Na chamada da função deve-se utilizar uma estrutura de repetição que permita diversos cálculos, quando o usuário quiser sair da calculadora digitará qualquer valor diferente dos **caracteres** do menu.

A função da construção do menu, chamará todas as outras passando a elas os valores digitados.

"""

def menu():
    print('-='*50)
    print('Minha calculadora')   
    print()
    print('+ Soma de dois números \n- Subtração de dois números \n* Multiplicação de dois números \n/ divisão de dois números')
    print('-='*50)
    opcao = input('\nQual opção deseja? (Para sair, digite um valor diferente dos números do menu) ')
    return opcao

def somar(numero_um,numero_dois): 
    soma = numero_um + numero_dois 
    print('Resultado da soma de' ,numero_um, '+' ,numero_dois, ':' ,soma)
   
   
def subtrair(numero_um,numero_dois): 
    sub = numero_um - numero_dois  
    print('Resultado da subtração de' ,numero_um, '-' ,numero_dois, ':' ,sub)

def multiplicar(numero_um,numero_dois): 
    mult = numero_um * numero_dois  
    print('Resultado da multiplicação de' ,numero_um, 'x' ,numero_dois, ':' ,mult)
    
def dividir(numero_um,numero_dois): 
    if numero_dois != 0:
        div = numero_um / numero_dois 
        print('Resultado da divisão de' ,numero_um, '/' ,numero_dois, ':' ,div)
    else:
        print('Indivisível')
    

def main():
    opc = menu()
    
    while opc == '+'or opc == '-'or opc == '*'or opc == '/':
        numero_um = int(input('Digite um número: '))
        numero_dois = int(input('Digite outro número: '))

        if opc == '+':
           somar(numero_um,numero_dois)
            
        if opc == '-':
           subtrair(numero_um,numero_dois)

        if opc == '*':
            multiplicar(numero_um,numero_dois)

        if opc == '/':
            dividir(numero_um,numero_dois)

        opc = menu()

       
main()

"""### 8. (Função com retorno com parâmetro) Faça um programa contendo algumas funções:
a) Função para construir um menu de opções para uma calculadora:

    *** Minha Calculadora ***
    Digite um número.....: 
    Digite outro número..: 
        + Soma dois números
        - Subtrai dois números
        * Multiplica dois números
        / Divide dois números
    Qual opção deseja? 

b) Desenvolva uma função para cada opção de cálculo, que deverá ter retorno.

Observação: Na chamada da função deve-se utilizar uma estrutura de repetição que permita diversos cálculos, quando o usuário quiser sair da calculadora digitará qualquer valor diferente dos **caracteres** do menu.

A função de desenho/construção do menu, chamará todas as outras passando a elas os valores digitados.
"""

def menu():
    print('-='*50)
    print('Minha calculadora')   
    print()
    print('+ Soma de dois números \n- Subtração de dois números \n* Multiplicação de dois números \n/ divisão de dois números')
    print('-='*50)
    opcao = input('\nQual opção deseja? (Para sair, digite um valor diferente dos números do menu) ')
    return opcao

def somar(numero_um,numero_dois): 
    soma = numero_um + numero_dois 
    return soma

def subtrair(numero_um,numero_dois): 
    sub = numero_um - numero_dois  
    return sub

def multiplicar(numero_um,numero_dois): 
    mult = numero_um * numero_dois  
    return mult

def dividir(numero_um,numero_dois): 
    while numero_dois != 0:
        div = numero_um / numero_dois 
    i = i + 1
    return div

def main():
    opc = menu()
    
    while opc == '+'or opc == '-'or opc == '*'or opc == '/':
        numero_um = int(input('Digite um número: '))
        numero_dois = int(input('Digite outro número: '))

        if opc == '+':
           print('Resultado da soma de' ,numero_um, '+' ,numero_dois, ':' ,somar(numero_um,numero_dois))
            
        if opc == '-':
             print('Resultado da subtração de' ,numero_um, '-' ,numero_dois, ':' ,subtrair(numero_um,numero_dois))


        if opc == '*':
             print('Resultado da multiplicação de' ,numero_um, 'x' ,numero_dois, ':' ,multiplicar(numero_um,numero_dois))

        if opc == '/':
            print('Resultado da divisão de' ,numero_um, '/' ,numero_dois, ':' ,dividir(numero_um,numero_dois))

        opc = menu()

       
main()

# vetor_matriz = []
# for lin in range(2):
#   linha = []
#   for col in range(3):
#     linha.append(int (input('digite o valor de ['+str(lin)+','+str(col)+ ']: ')))
#   vetor_matriz.append(linha)

# print( )
# print('Matriz:')
# for lin in range(2):
#   for col in range(3):
#     print(vetor_matriz[lin][col],end="\t")
#   print( )

# vetor_matriz = [ ]
# linha = int(input('Informe a quantidade de linha(s): '))
# coluna = int(input('Informe a quantidade de coluna(s):'))

# for lin in range (linha):
#   linha = [ ]
#   for col in range(coluna):
#     linha.append(input('Digite os elementos da coluna: '))
#   vetor_matriz.append(linha)

# print( )
# print("Matriz : ")
# print( )

# for lin in range(len(vetor_matriz)):
#   for col in range(len(vetor_matriz[lin])):
#     print(vetor_matriz[lin][col], end="\t")
#   print()
# print( )
# if lin == col:
#   print('A matriz é simetrica.')
# else:
#   print('A matriz não é simetrica.')

# vetor_idade = [ ]
# vetor_sexo = [ ]
# vetor_cor_olhos = [ ]
# qtde_olhos_castanhos = 0
# qtde_sex = 0
# qtde_idade = 0
# qtde_olhos_azuis = 0
# qtde_sex_idade = 0
# soma = 0
# media_olho_cas = 0
# total_entrevistados = 0

# idade = int(input(' Digite a sua idade para entrar no programa: '))

# while idade != 0:
#   vetor_sexo.append(str(input(' Digite seu sexo: "f" para feminino ou "m" para masculino: ')))
#   vetor_cor_olhos.append(str(input(' Digite a cor dos seus olhos: "a" para azul e "c" para castanho: ')))
  
#   vetor_idade.append(idade)

#   if vetor_cor_olhos[i] == "c" or vetor_cor_olhos[i] == "C":
#     soma = vetor_idade[i] + soma
#     qtde_olhos_castanhos = qtde_olhos_castanhos + 1
#     media_olho_cas = soma/qtde_olhos_castanhos

#   else:
#     if vetor_cor_olhos[i] == "a" or vetor_cor_olhos[i] == "A":
#       if vetor_idade[i] >= 18 and vetor_idade[i] < 35:
#         if vetor_sexo[i] == "F" or vetor_sexo[i] =="f":
#           qtde_sex_idade = +1

  
#   total_entrevistados = total_entrevistados + 1
#   idade = int(input(' Digite a sua idade e quando quiser sair do programa digite 0: '))

# print( )
# print(f'A quantidade de total de cadastrados é: {total_entrevistados} ')
# print(f'Média de idades das pessoas com olhos castanhos: {media_olho_cas} ')
# print(f'Quantidade de pessoas do sexo feminino com idade entre 18 e 35 anos e que tenham olhos azuis: {qtde_sex_idade} ')