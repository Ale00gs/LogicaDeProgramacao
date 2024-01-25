"""### 1. (Função sem retorno com parâmetro) Faça um programa contendo uma função/método que leia um número e o multiplique por 2, apresente o resultado. Este é um exemplo de PASSAGEM DE PARÂMETRO POR VALOR.
"""

def multiplicar(num):# a variável num é nomeada como parâmetro na DEFINIÇÃO
# DA FUNÇÃO, ocorre num = numero, implicitamente, ou seja, o valor de numero é
# COPIADO/ATRIBUÍDO na num, isto é chamado de passagem de parâmetro por valor
    r = num * 2
    print('O resultado da multiplicação é',r)

def main():
    numero = int(input('Digite um número: '))
    multiplicar(numero) # a variável numero nomeada como argumento NA CHAMADA DA FUNÇÃO

main()

"""###2. (Função sem retorno com parâmetro) Faça um programa contendo uma função/método, sem parâmetro, que leia um nome e diga 'Olá nome, tudo bem?'. Crie outra função com o parâmetro nome, para que a mesma receba da main o nome digitado e apresente a mesma frase, este é um exemplo de PASSAGEM DE PARÂMETRO POR VALOR. """

def ler():
    nome = str(input('Digite um nome: '))
    print(f'Olá {nome}, tudo bem? ')

def ler_novamente(nome):
    print(f'Olá {nome}, tudo bem? ')

def main():
    ler()
    nome = str(input('Digite um nome: '))
    ler_novamente(nome)

main()

"""### 3. (Função sem retorno com parâmetro) Faça um programa contendo uma função/método para subtrair dois números e apresentar o resultado. Aqui deverá ocorrer, PASSAGEM DE PARÂMETRO POR VALOR. """

def subtrair(numero_um,numero_dois):
    sub = numero_um - numero_dois
    print(f'Resultado da subtração de {numero_um} - {numero_dois}: {sub}')

def main():
    numero_um = int(input('Digite um número: '))
    numero_dois = int(input('Digite outro número: '))
    subtrair(numero_um,numero_dois)

main()

"""### 4. (Função sem retorno com parâmetro) Faça uma função/método para a partir de um preço de um produto informado, calcular e apresentar o novo preço reajustado em 9%. Aqui deverá ocorrer, PASSAGEM DE PARÂMETRO POR VALOR. """

# Digite seu código aqui.
def calcular_reaj(preco_antigo):
    preco = (preco_antigo * 9) / 100
    preco_novo = preco + preco_antigo
    print(f'Novo preço reajustado é R$: {preco_novo:.2f}')


def main():
    preco_antigo = float(input('Digite o preço de um produto: '))
    calcular_reaj(preco_antigo)
    
main()

"""### 5. (Função sem retorno com parâmetro) Faça uma função/método para a partir de um preço de um produto informado, calcular e apresentar o novo preço reajustado em alguma porcentagem que deve ser informada (digitada) pelo usuário. Aqui deverá ocorrer, PASSAGEM DE PARÂMETRO POR VALOR. """

def calcular_reajuste(preco_antigo,porcent):
    preco = (preco_antigo * porcent) / 100
    preco_novo = preco + preco_antigo
    print(f'Novo preço reajustado é R$: {preco_novo:.2f}')


def main():
    preco_antigo = float(input('Digite o preço de um produto: '))
    porcent = float(input('Digite a porcentagem de aumento do preço do produto: '))
    calcular_reajuste(preco_antigo,porcent)
    
main()

"""### 6. (Função sem retorno com parâmetro) Faça uma função/método para a partir de um valor inicial e um valor final realizar o acumulo desse valores e apresentar o resultado. Não use vetor. Aqui deverá ocorrer para as duas variáveis, PASSAGEM DE PARÂMETRO POR VALOR. 
    Exemplo:
        a = 2
        b = 8
        // 2 + 3 + 4 + 5 + 6 + 7 + 8 = 35
        r = 35
"""

def calcular_soma(valor_inicial,valor_final):
    soma = 0
    for i in range(valor_inicial,valor_final+1):
        # print(i,"+", end=" ")
        soma = soma + i
      
    print(f'Resultado da soma: {soma}')

def main():
    valor_inicial = int(input('Digite um valor: '))
    valor_final = int(input('Digite outro valor: '))
    calcular_soma(valor_inicial,valor_final)

main()

"""### 7. (Função sem retorno com parâmetro) Faça uma função/método para calcular a tabuada de um número informado pelo usuário. Crie outra função que calcule a tabuada de um intervalo, por exemplo realize as taduabas do 3 ao 8. Aqui deverá ocorrer para as duas funções, PASSAGEM DE PARÂMETRO POR VALOR. """

def calcular_tab(numero):
    for i in range(1,11):
        resultado = numero * i 
        print(f'{numero} x {i} = {resultado} ')
    print()    

def calcular_tab_inter(num_um,num_dois):
    for i in range(num_um,num_dois+1):
        calcular_tab(i)
     
   
def main():
    numero = int(input('Digite um número: '))
    print('-='*70)
    calcular_tab(numero)
    print('-='*70)
    num_um = int(input('Digite o primeiro número do intervalo, para calcular a tabuada: '))
    num_dois = int(input('Digite o segundo número do intervalo, para calcular a tabuada: '))
    calcular_tab_inter(num_um,num_dois)


main()

"""### 8. (Função sem retorno com parâmetro) Faça uma função/método que calcule a média de um aluno que realizou duas provas (P1 e P2), a partir desta média, chame/crie OUTRA função que verifique se esta média aprova ou reprova o aluno. Aqui deverá ocorrer nas duas funções, PASSAGEM DE PARÂMETRO POR VALOR. 

"""

def avaliar(med):
    print('Aluno(a) aprovado(a)' if med >= 6 else "Aluno(a) reprovado(a)")

def calcular(p1,p2):
    media = (p1 + p2) / 2
    print(f'A média do aluno é: {media:.1f}')
    avaliar(media)

def main():
    nota_um = float(input('Informe a primeira nota: '))
    nota_dois = float(input('Informe a segunda nota: '))
    calcular(nota_um,nota_dois)
    

main()

"""### 9. (Função sem retorno com parâmetro) Faça uma função/método sem parâmetro, para ler um valor e chamar/criar OUTRA função (com parâmetro) que mostre se o valor é par ou ímpar."""

def apresentar_valor(valor):
    print('Esse número é par' if valor % 2 == 0 else 'Esse número é impar')

def ler():
    valor = int(input('Digite um valor: '))
    apresentar_valor(valor)

def main():
    ler()
main()

"""### 10. (Função sem retorno com parâmetro) Faça uma função/método para verificar se um nome digitado é igual a ‘Ana’, mostre o valor True ou False como resposta. Aqui deverá ocorrer, PASSAGEM DE PARÂMETRO POR VALOR. """

def verificar_ana(nome): 
    #if 'Ana' in nome or 'ana' in nome:
    if nome == 'ana' or nome == 'Ana':
        print('True')
    else:
        print('False')

def main():
    nome = str(input('Digite um nome: '))
    verificar_ana(nome)

main()

"""### 11. (Função sem retorno com parâmetro) Faça uma função/método para verificar e contar quantas letras **a** tem numa frase. Não use NENHUMA função pronta da linguagem Python. Aqui deverá ocorrer, PASSAGEM DE PARÂMETRO POR VALOR. """

def verificar_letra_a(frase):
    qtde = 0
    # for i in frase:
    #     if i =='a' or i == 'A' :
    for i in range(0,len(frase)):
        if frase[i] == 'a' or frase[i] == 'A':
            qtde = qtde +1
    print(f'Quantidade de letras A na frase: {qtde}')
    

def main():
    frase = str(input('Digite uma frase: '))
    verificar_letra_a(frase) 

main()

"""###12. Faça uma função/método para verificar uma senha, contando/apresentando quantos dígitos numéricos e quantas letras existem. Aqui deverá ocorrer, PASSAGEM DE PARÂMETRO POR VALOR. """

def verificar(senha):
    digito_num = 0
    letras = 0
    for i in range(len(senha)):
        if senha[i].isalpha():
            letras = letras + 1
        if senha[i].isdecimal():
            digito_num = digito_num + 1
        

    print(f'Quantidade de digitos numéricos: {digito_num} \nQuantidade de letras: {letras} ')    

def main():
    senha = input('Digite uma senha: ')
    verificar(senha)
main()

# while True:
#  texto = input("Digite uma string: ")

# if texto.isalpha():
#   print("Tudo tudo letra")
#  elif texto.isdecimal():
#   print("Tudo numero")
#  elif texto.isalnum():
#   print("Numeros e letras")
#  else:
#   print("Vazia ou caractere especial")

"""###13. Uma senha deve ser criada a partir da seguinte regra:
*   Dois primeiros números
*   Um caracter especial
*   Cinco letras

### Faça uma função/método para verificar esta senha esta correta ou não, use FATIAMENTO DE STR Aqui deverá ocorrer, PASSAGEM DE PARÂMETRO POR VALOR. 
"""

def verificar_senha(senha):
    cont_letras = 0
    if senha[:2].isnumeric(): # se 2 primeiros são numéricos
        for i in range(len(senha)):
            if senha[i].isalpha():
                cont_letras = cont_letras + 1
                
            if cont_letras == 5: # Se existem 5 letras

               if not senha[2:8].isnumeric() and not senha[2:8].isalpha(): # caracter especial
                return True
    return False                 




    print('Programa finalizado com sucesso')         

def main():
    resultado = bool
    p = input('REGRA DA SENHA: Dois primeiros números, um caracter especial e cinco letras \nDigite uma senha (Se quiser sair do programa, digite 0): ')
    resultado = verificar_senha(p) 
    if resultado == True:
        print('A sua senha está correta.')
    else:
         print('A sua senha está incorreta.')
main()