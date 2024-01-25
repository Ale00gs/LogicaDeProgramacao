def parabens():
  print('Parabéns para você\nNesta data querida\nMuitas felicidades\nMuitos anos de vida')

parabens()

def temletrau():
  frase = input('Digite uma frase: ')
  if 'u' in frase:
    print('Você utilizou a letra u')
  else:
    print('Você não utilizou a letra u')

temletrau()

def somaQuadrados(a,b):
  somaQ = a**2 + b**2
  return somaQ

somaQuadrados(2,3)

"""# AULA 07/03/22"""

# DEFINIÇÃO DA FUNÇÃO
def mensagem():
  print('olá, tudo bem? ')

def somar():
  n1 = int(input('Informe o primeiro valor: '))
  n2 = int(input('Informe o segundo valor: '))
  res = n1 + n2 
  print('O resultado é ',res)


#Uma função é executada APENAS quanto é chamada
#chamada da função  
mensagem()
somar()

def main(): #Tem o propósito de reunir a chamada de todas as funções

"""# EXERCÍCIOS

### 1. (Função sem retorno sem parâmetro) Faça um programa contendo uma função/método que apresente o valor 1 se o número digitado for positivo e 0 se for negativo.
"""

def avaliar_positivo_negativo():
  num = int(input('Informe o valor: '))
  if num > 0:
    print('1')
  else:
    print('0') 

def main():
  print('Entrei na função main ')
  avaliar_positivo_negativo()

main()

####teste
# valor = int(input( "Digite um valor: "))
# if valor >= 0:
#   print('1')
# else:
#   print('0')

valor = int(input( "Digite um valor: "))
print('1' if valor >= 0 else '0')

"""### 2. (Função sem retorno sem parâmetro) Faça uma função/método que leia dois valores positivos e apresente a soma dos N números existentes entre eles (inclusive). 
    Exemplo: 
        a = 2
        b = 8
        2 + 3 + 4 + 5 + 6 + 7 + 8
        soma = 35
"""

#CRIAR FUNÇÃO 
def somar(): 
    soma = 0 
    numero_um = int(input('Digite o primeiro valor positivo: '))
    numero_dois = int(input('Digite o segundo valor positivo: '))  
    for i in range(numero_um,numero_dois+1):
        soma = soma +i
        print(i, '+' ,end=" ")
    print( )
    print(f'Soma = {soma}' )


def main():
    somar()

main()

"""### 3. (Função sem retorno sem parâmetro) Faça uma função/método que receba três números inteiros *a*, *b*, *c* que sejam divisíveis por ***a***. O valores *b* e *c* representam o intervalo da estrutura de repetição. Apresente a quantidade e os números divisíveis. Não pode usar vetor e função pronta da linguagem Python.
    Exemplo:
        a = 5
        b = 1
        c = 10
        1 % a
        2 % a
        3 % a
        4 % a
        5 % a este valor é divisível
        6 % a
        7
        8
        9
        10 % a este valor é divisível
        qtde = 2
        Números divisíveis 5, 10
"""

def dividir_por_a():
    quantidade = 0
    numeros_div = 0
    a = int(input('Digite o valor de A: '))
    b = int(input('Digite o valor de B (intervalo da estrutura): '))
    c = int(input('Digite o valor de C (intervalo da estrutura): '))

    for i in range(b,c+1):
        if (i % a) == 0:
            quantidade = quantidade +1

            print(f'Números divisíveis por {a}: {i}')
    print(f'Quantidade de números divisíveis: {quantidade} ')
    
            
            
def main():
    dividir_por_a()


main()

"""### 4. (Função sem retorno sem parâmetro) Faça uma função/método que leia um único valor representado em segundos, converta-o e apresente o resultado em horas, minutos e segundos.
    h = segundos / 3600
    r = resto(segundos / 3600)
    m = r / 60
    s = resto(r / 60)
    Observação 1: resto de uma divisão em Python %.
    Observação 2: a hora, o minuto e o segundo devem ser apresentados como números inteiros. 
"""

def converter_horas():
    print('Conversor de segundos')
    valor = int(input("Digite um valor (representado em segundos): "))
    
    horas = valor / 3600
    resto_horas = valor % 3600 
    minutos = resto_horas / 60
    resto_minutos = resto_horas % 60
    #segundos = resto_minutos / 60

    print(f'Resultado: {horas:.0f}h {minutos:.0f}min {resto_minutos:.0f}s ')




def main():
    converter_horas()

main()

"""### 5. (Função sem retorno sem parâmetro) Faça uma função/método que receba o preço antigo e atual de um produto, determine o percentual de acréscimo entre esses valores e apresente-o.
    r = (100 * preco_novo - 100 * preco_antigo) / preco_antigo
"""

def Calcular_percentual():
    preco_inicial = float(input("digite o preço antigo do produto: ")) 
    preco_final = float(input("digite o preço atual do produto: "))
    
    percent = (100 * preco_final - 100 * preco_inicial) / preco_inicial
    
    # cálculo percentual de acréscimo
    # acrescimo = (preco_final - preco_inicial) / preco_inicial
    # percent = acrescimo * 100

    print(f"O percentual de acréscimo entre esses valores é: {percent:.0f}%")

def main():
    Calcular_percentual()

main()

"""### 6. (Função sem retorno sem parâmetro) Faça uma função/método que leia um valor inteiro entre 1 e 9 e mostre a seguinte tabela de **multiplicação**
Neste exemplo foi escolhido o número 9.

    1    
    2     4
    3     6     9
    4     8    12    16
    5    10    15    20    25
    6    12    18    24    30    36
    7    14    21    28    35    42    49
    8    16    24    32    40    48    56    64   
    9    18    27    36    45    54    63    72    81
    for i = 1 até n
       for j = 1 até i
       
    Observação: configure o print para não pular linha
"""

def multiplicar():
    numero = int(input('Digite um valor inteiro entre 1 e 9: '))

    for i in range(1,numero+1):
        for j in range(1,i+1):
            print(j * i , end = '\t')
        print()

def main():
    multiplicar()

main()

# Digite seu código aqui. 
# Para ter a mesma forma de apresentação use assim o print(r, end = '\t')

"""### 7. (Função sem retorno sem parâmetro) Faça uma função/método que leia três notas de um aluno e uma letra, se a letra for igual a *A*, deverá calcular a média aritimética das notas dos alunos, se for *P*, deverá calcular a média ponderada, com pesos 5, 3 e 2. A média deve ser mostrada ao final.
N1, N2 e N3 são notas.

P1, P2 e P3 são pesos.

Média ponderada = (N1 * P1 + N2 * P2 + N3 * P3 ) / (P1 + P2 + P3)
"""

def calcular_media():
    Soma = 0
    p1 = 5
    p2 = 3
    p3 = 2
    nota_um = float(input('Digite a primeira nota: ')) 
    nota_dois = float(input('Digite a segunda nota: ')) 
    nota_tres = float(input('Digite a terceira nota: ')) 
    letra = str(input('Digite a letra A para calcular a média aritmética ou P para calcular a média ponderada: ')) 
    
    # for i in range(letra != 'p' and letra != 'a' and letra != 'P' and letra != 'A'):
    #     print('Digite uma letra válida' ) #mensagem de erro
    
    if letra == 'a' or letra == 'A':
        media = (nota_um + nota_dois + nota_tres) / 3
    
    if letra == 'p' or letra == 'P':
        media = (nota_um * p1) + (nota_dois * p2) + (nota_tres * p3) / (p1 + p2 + p3)
    
    print(f'A sua média é: {media:.1f}')

def main():
    calcular_media()

main()

"""### 8. (Função sem retorno sem parâmetro) Faça uma função/método que leia uma hora de início e de término de um jogo, ambas divididas em dois valores distintos: hora e minuto. Deverá ser apresentado a duração expressa em minutos, considerando que o tempo máximo de duração de um jogo é de 24 horas e que ele pode começar em um dia e terminar no outro.
    se m_f < m_i
        m_f = m_f + 60
        h_f = h_f - 1
    se h_f < h_i
        h_f = h_f + 24
    tot_m = m_f - m_i
    tot_h = h_f - h_i
    total = tot_h * 60 + tot_m 
"""

def converter_para_minuto():
    hora_inicial = int(input('Digite a hora inicial: '))
    minuto_inicial = int(input('Digite o minuto inicial: '))
    hora_final = int(input('Digite a hora final: '))
    minuto_final = int(input('Digite o minuto final: '))
    total_minuto = 0
    total_hora = 0 
    total = 0

    if minuto_final < minuto_inicial:
        minuto_final = minuto_final + 60
        hora_final = hora_final - 1 
    if hora_final < hora_inicial:
        hora_final = hora_final + 24
    total_minuto = minuto_final - minuto_inicial
    total_hora = hora_final - hora_inicial
    total = (total_hora * 60) + total_minuto       

    print(f"Resultado: {total} minutos.")





def main():
    converter_para_minuto()

main()

"""### 9. (Função sem retorno sem parâmetro) Faça uma função/método que leia cinco valores inteiros, determine e mostre o maior e o menor deles. Não pode usar vetor e função pronta da linguagem Python."""

# Digite seu código aqui.
def classificar_menor_maior():
    menor = 0
    maior = 0
    for i in range(5):
        valor = int(input('Digite um valor: '))
        
        if i == 0:
            menor = valor
            maior = valor
        
        if maior < valor:
            maior = valor
            
        if menor > valor:
            menor = valor     

    print('O menor valor: ',menor)
    print('O maior valor: ',maior)

def main():
    classificar_menor_maior()

main()

#teste com gambiarra
# def classificar_menor_maior():
#     menor = 0
#     maior = 0
#     valor_maior = 0
#     valor_menor = 999999999
#     for i in range(3):
#         valor = int(input('Digite um valor: '))
        
#         if maior < valor_maior:
#             maior = valor_maior
            
#         if menor > valor_menor:
#             menor = valor_menor     

#     print('O menor valor: ',menor)
#     print('O maior valor: ',maior)

# def main():
#     classificar_menor_maior()

# main()

"""### 10. (Função sem retorno sem parâmetro) Faça uma função/método que leia um valor inteiro e positivo N e mostre o valor de S, obtido pelo seguinte cálculo: 
###S = 1  +  1/1!  +  1/2!  +  1/3!  + ... +  1/N!

Observvação: Não pode usar vetor e função pronta da linguagem Python.
"""

# Digite seu código aqui.

# S = 1 + 1 + 1/2! + 1/3 + 1/4!
# S = 1 + 1 + 0.5 + 0.16 + 0.041
# S = 2.66 + 0.041
# 3! = 3 * 2 * 1 = 6
# 4! = 1 * 2 * 3 * 4 = 24    1/4!   1/24  = 0.041

# N = int(input('Informe o valor de N termos: '))

# S = 1

def calcular_fatorial():
    numero = int(input('Digite o valor de N termos: '))
    s = 1 
    n = 1
    while n <= numero:
        fatorial = 1
        for i in range(1,n+1):
            fatorial = fatorial * i

        print(f'Fatorial de {n}: {fatorial}')
        n = n + 1
        s = s + (1/fatorial) 

    print(f'Resultado: {s:.2f}')   

    
 

def main():
    calcular_fatorial()

main()