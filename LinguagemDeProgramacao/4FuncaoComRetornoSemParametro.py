### 1. (Função com retorno sem parâmetro) Faça um programa contendo uma função/método que leia um número e o multiplique por 2 retornando o resultado e o apresente.

def multiplicar():
    numero = int(input('Digite um número: '))
    r = numero * 2
    return r
    print('Bom dia')

def main():
    #1ª forma de chamar uma função com retorno....OU...
    resultado = multiplicar()
    print('O resultado é',resultado)

    #2ª forma de chamar uma função com retorno.........
    print('O resultado é',multiplicar())
    
main()

"""### 2. (Função com retorno sem parâmetro) Faça um programa contendo uma função/método para subtrair dois números, retornar o resultado e o apresentando."""

def subtrair():
    numero_um = int(input('Digite um numero: '))
    numero_dois = int(input('Digite outro numero: '))
    sub = numero_um - numero_dois
    return sub

def main():
    print('O resultado da subtração é: ',subtrair())

main()

"""### 3. (Função com retorno sem parâmetro) Faça um programa contendo uma função/método que leia a base e a altura de um triângulo e retorne/apresente sua área A = (base x altura)/2."""

def calcular_triangulo():
    base = int(input('Digite o valor da base: '))
    altura = int(input('Digite o valor da altura: '))
    a = (base * altura) / 2
    return a


def main():
    print(f'O resultado da área é: {calcular_triangulo():.0f}')


main()

"""### 4. (Função com retorno sem parâmetro) Faça um programa contendo uma função/método que leia o lado de um quadrado e retorne sua área, area = lado²."""

def calcular_quadrado():
    lado = int(input('Digite o lado de um quadrado: '))
    area =  lado ** 2
    return area

def main():
    print(f'A área do quadrado é: {calcular_quadrado()}')

main()

"""###5. (Função com retorno sem parâmetro) Faça um programa contendo uma função/método  que verifique se um número é par, retorne mostrando a str/string ‘É par’ ou se ‘É ímpar’."""

def verificar_par():
    numero = int(input('Digite um numero: '))    
    # if numero % 2 == 0:
    #     print('Par')
    # else:
    #     print('Ímpar')
    if numero % 2 == 0:
        numero = 'Par'
    else:
        numero = 'Ímpar'

    return numero

def main():
    print(f'Esse número é: {verificar_par()}')
main()

"""###6. (Função com retorno sem parâmetro) Faça um programa contendo uma função/método  que verifique se um número é par, retorne/mostre o valor bool **True** para par e **False** para ímpar."""

def verificar_par():
    num = 0
    numero = int(input('Digite um numero: '))    
    if numero % 2 == 0:
        num = "True"
    else:
        num = "False"

    return num

def main():
    print(f'O número é: {verificar_par()}')
main()

"""### 7. (Função com retorno sem parâmetro) Faça uma função/método que leia e armazene 5 elementos inteiros no vetor A, deverá ser gerado um vetor B, de mesmo tamanho, que armazenará o fatorial de cada elemento de A. Não use função pronta de cálculo de fatorial. Retorne/apresente o vetor B."""

# Exemplo:a\TAT
# A = [5  ,4 ,3,2,1]
# B = [120,24,6,2,1]

def fatorar():
    a = [ ]
    b = [ ]
    fat = 1
    
    for i in range(5):
        a.append(int(input('Digite um número: ')))
        for b in range(len(a)):
            for a in range(i):
                fat = fat * i
                for i in range(len(a)):
                    b.append(int(fat))         
                    return b   


                
        
def main():
    print(f'Vetor a: {a}')
    print(f'Vetor b: {b}') 

main()

def fatorar():
    vetor_a = [ ]
    vetor_b = [ ]
# codigo para carregar vetor
    # for i in range(2, 5, 1) : # ou mais simples neste caso "for i in range(n)"
        # vetor_a.append(i); # anexe mais um elemento `a lista 
    for i in range(5):
        vetor_a.append(int(input('Digite um número: ')))

    
    for i in range(len(vetor_a)):
        fatorial = 1
        cont = 2
        while cont <= vetor_a[i]:
            fatorial = fatorial * cont
            cont = cont + 1
       
        vetor_b.append(fatorial);
    print(f"Vetor A: {vetor_a}")
    return vetor_b        

def main():
   print(f"Vetor fatorado: {fatorar( )}")
main()

# FATORIAL
def main():
    n = int(input("Digite o valor de n: "))
    fat = 1
    i = 2
    while i <= n:
        fat = fat*i
        i = i + 1

    print("O valor de %d! é =" %n, fat)

main()

"""### 8. (Função com retorno sem parâmetro) Faça uma função/método retorne um vetor com os três primeiros números perfeitos. Sabe-se que um número é perfeito quando é igual a soma de seus divisores (exceto ele mesmo). 
Exemplo: os divisores de 6 são 1, 2 e 3, e 1 + 2 + 3 = 6, logo 6 é perfeito. Não use função pronta.

1º número perfeito: 6

2º número perfeito: 28

3º número perfeito: 496
"""

def verificar_perfeito(numero):
    cont = 0
    for i in range(1, numero-1):
        if (numero % i) == 0: #divisores do número
            cont = cont + 1

        if cont >= 3:
            return True     
    return False              

def calcular_perfeito():
    vet = [ ]

    resp = int(input('Digite um número: '))
    while resp != 0:
        vet.append(resp)
        resp = int(input('Digite um número: '))
    
    if verificar_perfeito(vet[0]) and verificar_perfeito(vet[1]) and verificar_perfeito(vet[2]):
            return True 
   
    return False   
  

def main():
    resp = bool
    resp = calcular_perfeito( )
    if resp == True:
        print("Três primeiros números perfeitos")
    else:    
        print("Números imperfeitos")
main()

# número 1 não é perfeito
# ...
# número 4 não é perfeito, exemplo: 4 % 1 == 0, 4 % 2 == 0, 4 % 3 != 0, a soma 
# resulta em 2
# ...
# número 6 é perfeito  6 % 1 == 0, 6 % 2 == 0, 6 % 3 == 0, 6 % 4 != 0, 6 % 5 != 0
# quando é perfeito a soma de seus divisores da o mesmo valor de número que é 6

for n in range (1, 497)
    div outro laço de repetição 1 até n:
        desenvolva a lógica aqui

"""### 9. (Função com retorno sem parâmetro) Foi realizada uma pesquisa sobre algumas características físicas de cinco habitantes de uma região. Foram coletados os seguintes dados de cada habitante: idade, sexo (M - masculino ou F - feminino), cor dos olhos (A - azuis ou C - castanhos), cor dos cabelos (L - louros, P - pretos ou C - castanhos).

1.   Faça uma função/método que leia esses dados, armazenando-os em vetores (listas);
2.   Faça uma função/método que determine e devolva a função principal a média de idades das pessoas com olhos castanhos e cabelos pretos;
3. Faça uma função/método que determine e devolva a função principal a maior idade entre os habitantes;
4.  Faça uma função/método que determine e devolva a função principal a quantidade de indivíduos do sexo feminino com idade entre 18 e 35 anos(inclusive) e que tenham olhos azuis e cabelos louros.

"""

idade = [ ]
sexo = [ ] # (M - masculino ou F - feminino)
cor_olhos = [ ] # (A - azuis ou C - castanhos)
cor_cabelo = [ ] # (L - louros, P - pretos ou C - castanhos)


def ler_dados():
    for i in range(5):
        idade.append(int(input('Digite a sua idade: ')))
        sexo.append(str(input('Digite seu sexo (M - masculino ou F - feminino): ')))
        cor_olhos.append(str(input('Digite a cor dos seus olhos (A - azuis ou C - castanhos): ')))
        cor_cabelo.append(str(input('Digite a cor do seu cabelo (L - louros, P - pretos ou C - castanhos): ')))

def calcular_media_idade():
    soma_idade = 0
    qtd_pessoas_idade = 0
    media_idade = 0

    for i in range(5):
        if cor_olhos[i] == 'c' or cor_olhos[i] == 'C':
            if cor_cabelo[i] == 'p' or cor_cabelo[i] == 'P':
                soma_idade = idade[i] + soma_idade
                qtd_pessoas_idade = qtd_pessoas_idade + 1
    media_idade = soma_idade / qtd_pessoas_idade
    # print('Soma idade:' ,soma_idade)
    # print('quantidade de pessoas: ' ,qtd_pessoas_idade)
    # print(f'A média de idades das pessoas com olhos castanhos e cabelos pretos: {media_idade}')

    
    return media_idade

def calcular_maior_idade():
    idade_maior = idade[0]
    idade_menor = idade[0]


    for i in range(5):
    
        if idade_maior < idade[i]:
            idade_maior = idade[i]
        
        if idade_menor > idade[i]:
            idade_menor = idade[i]

    # print(f'A maior idade entre os habitantes é: {idade_maior}')
    return idade_maior

def calcular_quantidade_individuos():
    qtd_ind = 0
    for i in range(5):
        if sexo[i] == 'F' or sexo[i] == 'f':
            if idade[i] >= 18 or idade[i] <= 35:
                if cor_olhos[i] == 'a' or cor_olhos[i] == 'A':
                    if cor_cabelo[i] == 'l' or cor_cabelo[i] == 'L':
                        qtd_ind = qtd_ind+1
    # print(f'Quantidade de indivíduos do sexo feminino com idade entre 18 e 35 anos e que tenham olhos azuis e cabelos louros: {qtd_ind} pessoa(s).')                   
    return qtd_ind


def main():
    
    ler_dados()
    print(f'A média de idades das pessoas com olhos castanhos e cabelos pretos: {calcular_media_idade()}')
    print(f'A maior idade entre os habitantes é: { calcular_maior_idade()}')
    print(f'Quantidade de indivíduos: { calcular_quantidade_individuos()} pessoa(s).')                   
   
    

main()

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