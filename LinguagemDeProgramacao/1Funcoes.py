### 1. Elabore uma estrutura para representar um produto (código, nome, preço). Aplique 10% de aumento no preço do produto e apresente.

class Representar_produto_um:
    nome = ' '
    codigo = 0
    preco = 0.0

def main(): #principal
    estrutura = Representar_produto_um()
    estrutura.nome = str(input('Digite o nome do produto: '))
    estrutura.codigo = int(input('Digite o código do produto: '))
    estrutura.preco = float(input('Digite o preço do produto: '))
    estrutura.preco = ((10 * estrutura.preco) / 100) + estrutura.preco

    print(f' \nPreço do {estrutura.nome} com 10% de aumento: {estrutura.preco}')
    print( )
    print(50*'-=')
        
main()

# class Representar_produto_um:
#     nome = ' '
#     codigo = 0
#     preco = 0.0

# def main(): #principal
#     estrutura = Representar_produto_um()
#     estrutura.nome = str(input('Digite o nome do produto: '))
#     estrutura.codigo = int(input('Digite o código do produto: '))
#     estrutura.preco = float(input('Digite o preço do produto: '))
#     aumento = ((10 * estrutura.preco) / 100) + estrutura.preco
#     print(50*'-=')
#     print(f'Produto: {estrutura.nome}\nPreço antigo: {estrutura.preco}\nPreço atual: {aumento}')

# main()

"""### 2. Elabore uma estrutura para representar um produto (código, nome, preço). Cadastre 5 produtos, use vetor/lista. Aplique 10% de aumento no preço do produto e apresente todos os dados do preço."""

class Representar_produto_dois:
    nome = ' '
    codigo = 0
    preco = 0.0

def main(): #principal
    vetor = [ ]
    for i in range(2):
        estrutura = Representar_produto_dois()
        estrutura.nome = str(input('Digite o nome do produto: '))
        estrutura.codigo = int(input('Digite o código do produto: '))
        estrutura.preco = float(input('Digite o preço do produto: '))
        estrutura.preco = ((10 * estrutura.preco) / 100) + estrutura.preco
        vetor.append(estrutura)

        print( )
        print(f'Produto: {estrutura.nome}\nPreço do produto com 10% de aumento: {estrutura.preco}')
        print( )
        print(50*'-=')
        
main()

"""### 3. Elabore uma estrutura para representar um produto (código, nome, preço). **Crie uma função** para cadastrar 5 produtos. **Crie outra função** para aplicar 10% de aumento no preço do produto e apresente, por meio **de outra função**, todos os dados do produtos cadastrados, após o aumento. Construa uma função para cada opção do menu a seguir:
Menu do Sistema
1. Cadastrar
2. Reajustar
3. Visualizar
4. Sair

Qual opção deseja?
"""

class Representar_produto_tres:
    nome = ' '
    codigo = 0
    preco = 0.0

def menu():
    print(50*'-=')
    print('Sistema de gerenciamento de produtos') 
    print('1.Cadastrar')
    print('2.Reajustar')
    print('3.Visualizar')
    print('4.Sair')
    opcao = int(input('Qual opção deseja? '))
    print(50*'-=')
    print()
    return opcao

def cadastrar(v_prod):
    for i in range(2):
        cadastro = Representar_produto_tres( )
        cadastro.nome = str(input("Digite o nome do produto: "))
        cadastro.codigo = int(input('Digite o código do produto: '))
        cadastro.preco = float(input('Digite o preço do produto: '))
        print()
        v_prod.append(cadastro)
    return v_prod

def aplicar_reajuste(v_prod):
   for i in range(2):
       v_prod[i].preco = ((10 * v_prod[i].preco) / 100) + v_prod[i].preco
   print('Reajuste realizado com sucesso! \t')
   print()
   return v_prod
 
def visualizar(v_prod):
    #print(f'Código: {v_prod[i].codigo}\tNome do produto: {v_prod[i].nome}\tPreço: {v_prod[i].nome}')s
    print(30*'¨¨') 
    print('Relação de produtos' ) 
    print(30*'¨¨')
    print()
    #print('Código\tNome do produto\t\tPreço')
    for i in range(2):
        print(f'Nome do produto: {v_prod[i].nome}\t\tCódigo: {v_prod[i].codigo}\t\tPreço: {v_prod[i].preco}')
        print()
        #print(v_prod[i].codigo, '\t',v_prod[i].nome,'\t\t\t',v_prod[i].nome)
        #print()
        


def main():
    v_produto = [ ] #Declaração do vetor
    opc = menu()
    while opc >= 1 and opc <= 3:
        if opc == 1:
            v_produto = cadastrar(v_produto)
        elif opc == 2:
            v_produto = aplicar_reajuste(v_produto)
        elif opc == 3:
            visualizar(v_produto)
        opc = menu()
        

main()

"""### 4. Uma escola precisa montar o cadastro geral de seus alunos. Este cadastro deverá conter as seguintes informações por aluno: nome completo, data de nascimento, telefone, endereço e série atual. Levando em conta que esta escola possui no máximo 500 alunos, como você faria para estruturar estas informações num sistema de gerenciamento para a escola? Implemente utilizando estrutura. Também **use a criação de funções para cada operação**. Use o menu a seguir:
Menu de opções:
1. Cadastrar alunos
2. Consulta por nome
3. Visualizar todos os dados
4. Sair

"""

class Representar_escola:
    nome = ' '
    data_nascimento = ' '
    telefone = ' '
    endereco = ' '
    serie_atual = ' '


def apresentar_menu():
    print(50*'-=')
    print('Sistema de gerenciamento da escola') 
    print('1.Cadastrar alunos')
    print('2.Consulta por nome')
    print('3.Visualizar todos os dados')
    print('4.Sair')
    opcao = int(input('Qual opção deseja? '))
    print(50*'-=')
    print()
    return opcao

def cadastrar_alunos(vet_escola):
    
    for i in range(2): 
        
        cadastro = Representar_escola( )
        cadastro.nome = str(input('Digite o nome completo do aluno: '))
        cadastro.data_nascimento = str(input('Digite a data de nascimento: '))
        cadastro.telefone = str(input('Digite o telefone: '))
        cadastro.endereco = str(input('Digite o endereço: '))
        cadastro.serie_atual = str(input('Digite a série: '))
       
        vet_escola.append(cadastro)
        
        print()
    return vet_escola

def consulta_por_nome(vet_escola):
    cont = 0
    if len(vet_escola)> 0:
        digitar = input('Digite o nome do aluno para realizar a consulta: ')
        for i in range(len(vet_escola)):
            if vet_escola[i].nome == digitar:
                print('Consulta realizada com sucesso! ')
                print()
            else:
                cont = cont+1
        if cont == len(vet_escola):
            print("Esse nome não está cadastrado no sistema!")
            print()
    else:
        print('Não há produtos cadastrados! \n')                
    return vet_escola
 
def visualizar_todos_os_dados(vet_escola):
    print(50*'-=')
    print('\nVisualização dos dados: ')
    print()
    for i in range(2):
        
        print(f'Nome do aluno: {vet_escola[i].nome}\nData de aniversário: {vet_escola[i].data_nascimento}\nTelefone:{vet_escola[i].telefone}\nEndereco:{vet_escola[i].endereco}\nSérie atual do aluno:{vet_escola[i].serie_atual} ')
        print()
        

def main():
    vet_escola = [ ] #Declaração do vetor
    opc = apresentar_menu()
    while opc >= 1 and opc <= 3:
        if opc == 1:
            vet_escola = cadastrar_alunos(vet_escola)
        if opc == 2:
            vet_escola = consulta_por_nome(vet_escola)
        if opc == 3:
            visualizar_todos_os_dados(vet_escola)
        opc = apresentar_menu()
        

main()

#exemplo do tipo bool
def consulta_por_nome_bool(vet_escola):
    achou = False
    if len(vet_escola)> 0:
        digitar = input('Digite o nome do aluno para realizar a consulta: ')
        for i in range(len(vet_escola)):
            if vet_escola[i].nome == digitar:
                print('Consulta realizada com sucesso! ')
                print()
            else:
                achou = True
        if achou:
            print("Esse nome não está cadastrado no sistema!")
            print()
    else:
        print('Não há produtos cadastrados! \n')                
    return vet_escola



# resp = bool
#     resp = consulta_por_nome(vet_escola)
#     if resp == True:
#         print("Esse nome não está cadastrado no sistema!")
#     else:    
#         print("Consulta realizada com sucesso!")

"""### 5. Faça um programa que realize o cadastro de contas bancarias com as seguintes informações: numero da conta, nome do titular e saldo. O banco permitirá o cadastramento de 15 contas. **Crie uma função para cada opção do menu** a seguir. Utilize a estrutura na passagem de parâmetro:
Menu de opções:
1. Cadastrar contas
2. Visualizar todas as contas
3. Consultar por nome
4. Alterar nome e/ou saldo de um número de conta
5. Excluir a conta com menor saldo
6. Sair

Observação: 

* No item de menu 4. Alterar nome e/ou saldo de um número de conta, entenda que apenas pode ser alterado o nome e o saldo depois que você pesquisar pelo número da conta.
* No item 5 do menu, encontre o menor saldo dentre todos cadastrados, **depois exclua esta ÚNICA conta.**. O assunto de excluir algo de um vetor foi dado na disciplina de Algoritmo.


"""

# Percorra todo os vetor e quando a condição de encontrar um menor saldo for executada, guarde o índice
# Fora do laço de repetição, exclua pelo índice, por exemplo com o comando pop(índice), vimos em Vetor/Algoritmo

class Representar_banco:
    numero_conta = 0
    nome = ""
    saldo = 0.0

def apresentar_menu_conta():
    print(50*'-=')
    print('MENU') 
    print('1.Cadastrar contas')
    print('2.Visualizar todas as contas')
    print('3.Consultar por nome')
    print('4.Alterar nome e/ou saldo de um número de conta')
    print('5.Excluir a conta com menor saldo')
    print('6.Sair')
    opcao = int(input('Qual opção deseja? '))
    print(50*'-=')
    print()
    return opcao

def cadastrar_conta(vet_conta):
    for i in range(2): #mudar para 15 depois
        cadastro = Representar_banco( )
        cadastro.nome = str(input('Digite o nome do titular: '))
        cadastro.numero_conta = int(input('Digite o número da conta: '))
        cadastro.saldo = float(input('Digite o saldo: '))

        vet_conta.append(cadastro)
        print(50*'---')
    return vet_conta
    
def visualizar__todas_as_contas(vet_conta):
    print(50*'-=')
    print('\nVisualização da conta: ')
    print()
    for i in range(len(vet_conta)):
        print(f'Nome: {vet_conta[i].nome}\nNumero da conta do(a) {vet_conta[i].nome} : {vet_conta[i].numero_conta}\nSaldo: {vet_conta[i].saldo}\n ')
        print()

             

def consultar_por_nome(vet_conta): 
    cont = 0
    if len(vet_conta)> 0:
        digitar = input('Digite o nome do aluno para realizar a consulta: ')
        for i in range(len(vet_conta)):
            if vet_conta[i].nome == digitar:
                print('Consulta realizada com sucesso! ')
                print()
            else:
                cont = cont+1
        if cont == len(vet_conta):
            print("Esse nome não está cadastrado no sistema!")
            print()
    else:
        print('Não há produtos cadastrados! \n')                
 


def alterar_nome(vet_conta, codigo_pesquisar):
    if len(vet_conta) > 0:
        for i in range(len(vet_conta)):
            if vet_conta[i].codigo == codigo_pesquisar:
                vet_conta[i].nome = input('Digite o nome do titular: ')
                vet_conta[i].saldo = float(input('Digite o novo saldo:'))
               
    else:
        print('Nenhum nome cadastrado! \n')                
    return vet_conta

def excluir_conta(vet_conta): 
    if len(vet_conta) > 0: # verificação se está cadastrado
        for i in range(len(vet_conta)):
            if i == 0: #faz a inicialização apenas uma vez
                menor_saldo = vet_conta[i].saldo
                indice = i

            if vet_conta[i].saldo <= menor_saldo:
                menor_saldo = vet_conta[i].saldo
                indice = i
        vet_conta.pop(indice)         
    else:
        print('Nenhuma conta cadastrado! \n')                
    return vet_conta

def main():
    vet_conta = [ ] #Declaração do vetor
    opc = apresentar_menu_conta()
    while opc >= 1 and opc <= 5:
        if opc == 1:
            vet_conta = cadastrar_conta(vet_conta)
        if opc == 2:
           visualizar__todas_as_contas(vet_conta)
        if opc == 3:
            consultar_por_nome(vet_conta)
        if opc == 4:
            codigo_pesquisar = input('Digite o número da conta para realizar a alteração: ')
            vet_conta = alterar_nome(vet_conta, codigo_pesquisar)
        if opc == 5:
            vet_conta = excluir_conta(vet_conta)
        
        
        opc = apresentar_menu_conta()


main()

# def alterar_nome(vet_conta,cadastrar_conta(cadastro.numero_conta)):
#     digitar_numero_conta = input('Digite o número da conta para realizar a alteração do nome e/ou saldo no sistema: ')
#         for i in range(len(vet_conta)):
#             if vet_conta[i].cadastro.numero_conta == digitar_numero_conta:
#                 mudar = input('Digite 1 para mudar o saldo, 2 para mudar o nome e 0 para voltar ao menu:  ')
#                 while mudar >= 1 and mudar <= 2:
#                     if mudar == 1:
#                         cadastro.numero_conta = float(input('Digite o número da conta: '))
#                     if mudar == 2:
#                         cadastro.nome = str(input('Digite o nome: ')
                
#         vet_conta.append(cadastro)  
#     return vet_conta  

def alterar_nome(vet_conta, codigo_pesquisar):
    if len(vet_conta) > 0:
        for i in range(len(vet_conta)):
            if vet_conta[i].codigo == codigo_pesquisar:
                vet_conta[i].nome = input('Digite o nome do titular: ')
                vet_conta[i].saldo = float(input('Digite o novo saldo:'))
                
    else:
        print('Nenhum nome cadastrado! \n')                
    return vet_conta

def excluir_conta(vet_conta): 
    if len(vet_conta) > 0: # verificação se está cadastrado
        for i in range(len(vet_conta)):
            if i == 0: #faz a inicialização apenas uma vez
                menor_saldo = vet_conta.saldo
                indice = i

            if vet_conta[i].saldo <= menor_saldo:
                menor_saldo = vet_conta[i].saldo
                indice = i
       vet_conta.pop(indice)         
                
                
    else:
        print('Nenhuma conta cadastrada! \n')                
    return vet_conta

"""### 6. Elabore uma estrutura para representar um Funcionario (código, nome, endereço, salário). Para o membro endereço deve-se criar outra estrutura Endereço (logradouro, número, bairro, cidade). Utilize aninhamento de estruturas para resolver este desenvolvimento. Construa uma função para cada opçao do menu a seguir:

Menu de opções:
1. Cadastrar funcionários
2. Visualizar todos os dados
3. Sair
"""

class Representar_endereco:
    rua = ''
    numero = 0
    bairro = ''
    cidade = ''

class Representar_funcionario:
    nome = ''
    endereco = Representar_endereco()
    codigo = 0
    salario = 0.0


def menu():
    print(50*'-=')
    print('Sistema de gerenciamento da escola') 
    print('1.Cadastrar funcionário')
    print('2.Visualizar todos os dados')
    print('3.Sair')
    opcao = int(input('Qual opção deseja? '))
    print(50*'-=')
    return opcao

def cadastrar_funcionarios(vet_funcionario):
    for i in range(1):
        cadastro = Representar_funcionario( )
        cadastro.nome = str(input('Digite o nome do funcionário: '))
        cadastro.salario = int(input('Digite o salário do funcionário: '))
        cadastro.codigo = float(input('Digite o código do funcionário: '))
        cadastro.endereco.rua = str(input('Digite a rua: '))
        cadastro.endereco.numero = int(input('Digite o número: '))
        cadastro.endereco.bairro = str(input('Digite o bairro: '))
        cadastro.endereco.cidade = str(input('Digite a cidade: '))
       
        vet_funcionario.append(cadastro)
    return vet_funcionario

def Visualizar_todos_os_dados(vet_funcionario):
    print()
    print('\n=-=-=-=-=-=-=- Dados do funcionário =-=-=-=-=-=-=- ')
    for i in range(1):
        print(f'Nome do funcionário: {vet_funcionario[i].nome}')
        print(f'Salário do funcionário: R$ {vet_funcionario[i].salario:.2f}')
        print(f'Código do funcionário: {vet_funcionario[i].codigo}')
        print(f'=-=-=-=-=-=-=- Endereço do(a) {vet_funcionario[i].nome} =-=-=-=-=-=-=-')
        print(f'Rua: {vet_funcionario[i].endereco.rua}')
        print(f'Número: {vet_funcionario[i].endereco.numero}')
        print(f'Bairro: {vet_funcionario[i].endereco.bairro}')
        print(f'Cidade: {vet_funcionario[i].endereco.cidade}')

        # print(vet_funcionario[i].nome, '\n',vet_funcionario[i].salario,'\n',vet_funcionario[i].codigo, '\n',vet_funcionario[i].endereco)
        print()
        


def main():
    vet_funcionario = [ ] #Declaração do vetor
    opc = menu()
    while opc >= 1 and opc <= 2:
        if opc == 1:
            vet_funcionario = cadastrar_funcionarios(vet_funcionario)
        elif opc == 2:
            vet_funcionario = Visualizar_todos_os_dados(vet_funcionario)
        
        opc = menu()
        
        

main()

"""### 7. Elabore uma estrutura para representar um Produto (código, nome, data_fabricacao, data_validade, preço). Para o membro data_fabricacao e data_validade, deve-se criar outra estrutura Data (dia, mês, ano). Utilize aninhamento de estruturas para resolver este desenvolvimento. Construa uma função para cada opçao do menu a seguir:

Menu de opções:
1. Cadastrar produtos
2. Visualizar todos os dados
3. Sair
"""

class Estrutura_data:
    dia = ''
    mes = ''
    ano = '' 

class Estrutura_produto:
    codigo = 0
    nome = ''
    data_fabricacao = Estrutura_data()
    data_validade = Estrutura_data() 
    preco = 0.0 

def menu():
    print(50*'-=')
    print('Menu de opções') 
    print('1.Cadastrar produtos')
    print('2.Visualizar todos os dados')
    print('3.Sair')
    opcao = int(input('Qual opção deseja? '))
    print(50*'-=')
    return opcao

def cadastrar_produtos(vet_produto):
    for i in range(1):
        cadastro = Estrutura_produto( )
        cadastro.codigo = int(input('Digite o código do produto: '))
        cadastro.nome = str(input('Digite o nome do produto: '))
        cadastro.preco = float(input('Digite o preço do produto: '))
        cadastro.data_fabricacao = Estrutura_data()
        cadastro.data_fabricacao.dia = str(input('Digite o dia da fabricação: '))
        cadastro.data_fabricacao.mes = str(input('Digite o mes da fabricação: '))
        cadastro.data_fabricacao.ano = str(input('Digite o ano da fabricação: '))
        cadastro.data_validade = Estrutura_data()
        cadastro.data_validade.dia = str(input('Digite o dia da validade: '))
        cadastro.data_validade.mes = str(input('Digite o mes da validade: '))
        cadastro.data_validade.ano = str(input('Digite o ano da validade: '))

        vet_produto.append(cadastro)
    return vet_produto

def Visualizar_todos_os_dados_prod(vet_produto): 
    print()
    print('\n=-=-=-=-=-=-=- Dados do produto =-=-=-=-=-=-=- ')
    for i in range(1):
        print(f'Nome do produto: {vet_produto[i].nome}')
        print(f'Código do produto: {vet_produto[i].codigo}')
        print(f'Preço do produto: R$ {vet_produto[i].preco:.2f}')
        print(f'Data de fabricação: {vet_produto[i].data_fabricacao.dia}/{vet_produto[i].data_fabricacao.mes}/{vet_produto[i].data_fabricacao.ano}')
        print(f'Data de validade: {vet_produto[i].data_validade.dia}/{vet_produto[i].data_validade.mes}/{vet_produto[i].data_validade.ano}')
       

        print()
        


def main():
    vet_produto = [ ] #Declaração do vetor
    opc = menu()
    while opc >= 1 and opc <= 2:
        if opc == 1:
            vet_produto = cadastrar_produtos(vet_produto)
        elif opc == 2:
            Visualizar_todos_os_dados_prod(vet_produto)
        
        opc = menu()
main()

"""### 8. Elabore duas estruturas, como é apresentado a seguir:

CLIENTE |  DOCUMENTOS |
 -------|--------------
cod_cli |   num_doc   |
nome    |   cod_cli   |
fone    |   dia_venc  |
        |   dia_pag   |
        |   valor     |
        |   juros     |

* Sabe-se que um documento só pode ser cadastrado para um cliente que já exista. 
* Considere que podem existir, no máximo, 15 clientes e 30 documentos. Crie um vetor para clientes e outro para documentos. 

* Crie um menu para a realização de cada uma das operações especificadas a seguir:

**** SISTEMA GERENCIADOR DE CLIENTES E DOCUMENTOS ****

1. Cadastrar clientes

2. Relatório de clientes

3. Cadastrar documentos 

4. Relatório de documentos

5. Excluir clientes sem documentos

6. Excluir documentos individuais pelo número

7. Excluir documentos por cliente

8. Excluir documentos por período 

9. Alterar as informações dos clientes 

10. Mostrar o total de documentos de determinado cliente

11. Sair

Qual opção deseja?

.................................................................................................

Para cada item do menu, desenvolva uma função.

A seguir são apresentados os detalhes de implementação de cada opção do menu:

1. Cadastrar clientes — não pode existir mais que um cliente com o mesmo código.

2. Relatório de clientes - listar todos os clientes cadastrados.

3. Cadastrar documentos — ao cadastrar um documento, **se o dia de pagamento for maior que o dia de vencimento, calcular o campo ‘juros’ do registro documentos (5% sobre o valor original do documento)**.

4. Relatório de documentos - listar todos os documentos cadastrados.

5. Excluir clientes — um cliente só poderá ser excluído se não existir nenhum documento associado a ele.

6. Excluir documentos individuais — por meio de seu número. Caso o documento não exista, o programa deverá mostrar a mensagem "Documento não encontrado".

7. Excluir documentos por cliente — o programa deverá informar o código do cliente e excluir todos os seus documentos. Caso o cliente não exista, deverá mostrar a mensagem "Cliente não encontrado".

8. Excluir documentos por período — o programa deverá informar o dia inicial e o dia final e excluir todos os documentos que possuam data de vencimento nesse período.

9. Alterar as informações sobre os clientes — **só NÃO altere o código do cliente**.

10. Mostrar o total de documentos de determinado cliente.
"""

class Estrutura_cliente:
    cod_cliente = 0
    nome = " "
    fone =  " "

class Estrutura_documentos:
    num_doc = 0
    cod_cliente = 0
    dia_pagamento = 0
    dia_vencimento = 0
    valor = 0.0
    juros = 0
   
def menu():
    print(50*'-=')
    print('SISTEMA GERENCIADOR DE CLIENTES E DOCUMENTOS') 
    print('1. Cadastrar clientes')
    print('2. Relatório de clientes')
    print('3. Cadastrar documentos')
    print('4. Relatório de documentos')
    print('5. Excluir clientes sem documento')
    print('6. Excluir documentos individuais pelo número')
    print('7. Excluir documentos por cliente ')
    print('8. Excluir documentos por período')
    print('9. Alterar as informações dos clientes')
    print('10. Mostrar o total de documentos de determinado cliente  ')
    # print('11. Cadastrar clientes automático')
    # print('12. Cadastrar documento automático')
    print('11. Sair') 
    opcao = int(input('Qual opção deseja? '))
    print(50*'-=')
    return opcao   
    

def busca_clientes(vet_cli,codigo,tam_cli): 
    busca = 0
    for i in range(tam_cli):
        if vet_cli[i].cod_cliente == codigo:
            busca = 1
    return busca

def cadastrar_clientes(vet_cli,tam_cli): 
    codigo = int(input('Digite o código do cliente: '))
    if busca_clientes(vet_cli,codigo,tam_cli) == 0:
        cadastro_cli = Estrutura_cliente()
        cadastro_cli.cod_cliente = codigo
        cadastro_cli.nome = str(input('Digite o nome do cliente: '))
        cadastro_cli.fone = str(input('Digite o telefone do cliente: '))
        vet_cli.append(cadastro_cli)
        codigo = 1
    else:      
        codigo = 0

    return codigo

# ex9
def alterar_clientes(vet_cli,tam_cli): 
    codigo = int(input('Digite o código do cliente: '))
    if busca_clientes(vet_cli,codigo,tam_cli) == 1:
        print(50*'-=')
        print('ALTERAR CLIENTE................')
        cadastro_cli = Estrutura_cliente()
        vet_cli[codigo].nome =  str(input('Digite o NOVO nome do cliente: '))
        vet_cli[codigo].fone = str(input('Digite o NOVO telefone do cliente: '))       
       
        codigo = 1
    else:      
        codigo = 0

    return codigo

def cadastrar_clientes_automatico(tam_cli): 
    cadastro_cli = Estrutura_cliente()
    cadastro_cli.cod_cliente = tam_cli
    cadastro_cli.nome = str(tam_cli)
    cadastro_cli.fone = str(tam_cli)

    return cadastro_cli 


def cadastrar_documentos_automatico(tam_doc): 
    cadastro_doc = Estrutura_documentos()
    cadastro_doc.cod_cliente = tam_doc
    cadastro_doc.num_doc = str(tam_doc) 
    cadastro_doc.dia_pagamento = tam_doc
    cadastro_doc.dia_vencimento = tam_doc+5
    cadastro_doc.valor = tam_doc
    cadastro_doc.juros = 0

    return cadastro_doc    

def inicializa_clientes(vet_cli,tam_cli): 
    for i in range(tam_cli):
        vet_cli[i].cod_cliente = -1
        vet_cli[i].nome = '' 
        vet_cli[i].fone = ''

def listar_relatorio_de_clientes(vet_cli,tam_cli): 
    print(50*'-=')
    print('RELATÓRIO DE CLIENTES.................')
    for i in range(tam_cli):
        if vet_cli[i].cod_cliente != -1:
            print(f'Código do cliente:  {vet_cli[i].cod_cliente}')
            print(f'Nome do cliente:  {vet_cli[i].nome}')
            print(f'Telefone do cliente:  {vet_cli[i].fone}')
            print(50*'-=')
        

def cadastrar_documentos(vet_doc,tam_doc,vet_cli,tam_cli): 
    codigo = int(input('Digite o código do cliente: '))
    if busca_clientes(vet_cli,codigo,tam_cli) == 1:
        cadastro_doc = Estrutura_documentos()
        cadastro_doc.cod_cliente = codigo
        cadastro_doc.num_doc = float(input('Digite o número do documento: ')) 
        cadastro_doc.dia_pagamento = int(input('Digite o dia do pagamento do documento: '))
        cadastro_doc.dia_vencimento = int(input('Digite o dia do vencimento do documento: '))
        cadastro_doc.valor = float(input('Digite o valor do documento: ')) 
        if cadastro_doc.dia_pagamento > cadastro_doc.dia_vencimento: 
            calculo = (5 * cadastro_doc.valor) / 100 #cáculo juros 5%
            cadastro_doc.juros = calculo + cadastro_doc.valor
        else:
            cadastro_doc.juros = 0

        
        vet_doc.append(cadastro_doc)

        codigo = 1
    else:      
        codigo = 0

    return codigo


def excluir_clientes_com_documento(vet_doc,tam_doc,vet_cli,tam_cli):   
    for i in range(tam_cli):
        busca = 0
        for x in range(tam_doc):
            if vet_cli[i].cod_cliente == vet_doc[x].cod_cliente:
                busca = 1
        if busca == 0:
            print('CLIENTE EXCLUIDO.................')
            print(f'Código do cliente:  {vet_cli[i].cod_cliente}')
            print(f'Nome do cliente:  {vet_cli[i].nome}')
            print(f'Telefone do cliente:  {vet_cli[i].fone}')
            vet_cli[i].cod_cliente = -1
            vet_cli[i].nome = '' 
            vet_cli[i].fone = ''

def excluir_documento_por_clientes(vet_doc,tam_doc,vet_cli,tam_cli):
    
    numero = int(input("Digite o código do cliente: "))  
    if busca_clientes(vet_cli,numero,tam_cli) == 0:
        print('Cliente não encontrado')    
    else:
        for i in range(tam_doc):                
            if vet_doc[i].cod_cliente == numero:
                print('DOCUMENTO EXCLUIDO.................')           
                print(f'Código do documento: {vet_doc[i].num_doc}')
                print(f'Código do cliente: {vet_doc[i].cod_cliente}')         
                print(f'Dia do pagamento do documento:  {vet_doc[i].dia_pagamento}')
                print(f'Dia do vencimento do documento:  {vet_doc[i].dia_vencimento}')
                print(f'Valor do documento:  {vet_doc[i].valor}')
                print(f'Valor do documento com juros de 5% : {vet_doc[i].juros}')   
                vet_doc[i].cod_documento = -1
                vet_doc[i].cod_cliente = -1
                vet_doc[i].num_doc = -1
                vet_doc[i].dia_pagamento = -1
                vet_doc[i].dia_vencimento = -1
                vet_doc[i].valor = -1
                vet_doc[i].juros = -1 

#ex 8       
def excluir_documento_data(vet_doc,tam_doc): 
    busca = -1
    inicio = int(input("Digite o dia inicial do vencimento: "))   
    fim = int(input("Digite o dia final do vencimento: "))      
      
    for busca in range(tam_doc): 
        if vet_doc[busca].dia_vencimento >= inicio and vet_doc[busca].dia_vencimento <= fim:
            print('DOCUMENTO EXCLUIDO.................')           
            print(f'Código do documento: {vet_doc[busca].num_doc}')
            print(f'Código do cliente: {vet_doc[busca].cod_cliente}')         
            print(f'Dia do pagamento do documento:  {vet_doc[busca].dia_pagamento}')
            print(f'Dia do vencimento do documento:  {vet_doc[busca].dia_vencimento}')
            print(f'Valor do documento:  {vet_doc[busca].valor}')
            print(f'Valor do documento com juros de 5% : {vet_doc[busca].juros}')    
            vet_doc[busca].cod_documento = -1
            vet_doc[busca].cod_cliente = -1
            vet_doc[busca].num_doc = -1
            vet_doc[busca].dia_pagamento = -1
            vet_doc[busca].dia_vencimento = -1
            vet_doc[busca].valor = -1
            vet_doc[busca].juros = -1 
            print(50*'-=')
      
       
def excluir_documento_numero(vet_doc,tam_doc): 
    busca = -1
    numero = str(input("Digite o número do documento: "))       
      
    for i in range(tam_doc): 
        if vet_doc[i].num_doc == numero:
            busca = i
             

    if busca != -1:
            print('DOCUMENTO EXCLUIDO.................')           
            print(f'Código do documento: {vet_doc[busca].num_doc}')
            print(f'Código do cliente: {vet_doc[busca].cod_cliente}')         
            print(f'Dia do pagamento do documento:  {vet_doc[busca].dia_pagamento}')
            print(f'Dia do vencimento do documento:  {vet_doc[busca].dia_vencimento}')
            print(f'Valor do documento:  {vet_doc[busca].valor}')
            print(f'Valor do documento com juros de 5% : {vet_doc[busca].juros}')    
            vet_doc[busca].cod_documento = -1
            vet_doc[busca].cod_cliente = -1
            vet_doc[busca].num_doc = -1
            vet_doc[busca].dia_pagamento = -1
            vet_doc[busca].dia_vencimento = -1
            vet_doc[busca].valor = -1
            vet_doc[busca].juros = -1 
   

    else:
        print('Documento não encontrado')            

# exercicio 7
 def excluir_documento_por_clientes(vet_doc,tam_doc,vet_cli,tam_cli):
    
    numero = int(input("Digite o código do cliente: "))  
    if busca_clientes(vet_cli,numero,tam_cli) == 0:
        print('Cliente não encontrado')    
    else:
        for i in range(tam_doc):                
            if vet_doc[i].cod_cliente == numero:
                print('DOCUMENTO EXCLUIDO.................')           
                print(f'Código do documento: {vet_doc[i].num_doc}')
                print(f'Código do cliente: {vet_doc[i].cod_cliente}')         
                print(f'Dia do pagamento do documento:  {vet_doc[i].dia_pagamento}')
                print(f'Dia do vencimento do documento:  {vet_doc[i].dia_vencimento}')
                print(f'Valor do documento:  {vet_doc[i].valor}')
                print(f'Valor do documento com juros de 5% : {vet_doc[i].juros}')   
                vet_doc[i].cod_documento = -1
                vet_doc[i].cod_cliente = -1
                vet_doc[i].num_doc = -1
                vet_doc[i].dia_pagamento = -1
                vet_doc[i].dia_vencimento = -1
                vet_doc[i].valor = -1
                vet_doc[i].juros = -1  
          

def listar_relatorio_de_documentos(vet_doc,tam_doc): 
    print('RELATÓRIO DE DOCUMENTOS.................')
    for i in range(tam_doc):
        print(50*'-=')
        if vet_doc[i].num_doc != -1:
                print(f'Código do documento: {vet_doc[i].num_doc}')
                print(f'Código do cliente: {vet_doc[i].cod_cliente}')
                print(f'Número do documento:  {vet_doc[i].num_doc}')
                print(f'Dia do pagamento do documento:  {vet_doc[i].dia_pagamento}')
                print(f'Dia do vencimento do documento:  {vet_doc[i].dia_vencimento}')
                print(f'Valor do documento:  {vet_doc[i].valor}')
                print(f'Valor do documento com juros de 5% : {vet_doc[i].juros}')    
                print(50*'-=')

# ex 10
def exibir_documento_por_clientes(vet_doc,tam_doc,vet_cli,tam_cli):
    
    numero = int(input("Digite o código do cliente: "))  
    if busca_clientes(vet_cli,numero,tam_cli) == 0:
        print('Cliente não encontrado')    
    else:
        for i in range(tam_doc):                
            if vet_doc[i].cod_cliente == numero:
                print('DOCUMENTO.................')           
                print(f'Código do documento: {vet_doc[i].num_doc}')
                print(f'Código do cliente: {vet_doc[i].cod_cliente}')         
                print(f'Dia do pagamento do documento:  {vet_doc[i].dia_pagamento}')
                print(f'Dia do vencimento do documento:  {vet_doc[i].dia_vencimento}')
                print(f'Valor do documento:  {vet_doc[i].valor}')
                print(f'Valor do documento com juros de 5% : {vet_doc[i].juros}')   
               
def main():
    vet_doc = [] #Declaração do vetor documentos
    vet_cli = [] #Declaração do vetor clientes
    tam_doc = 0
    tam_cli = 0    
    #vet_cadastro = [ ]

# CARREGAR AUTOMÁTICO --------------------------------------------------------------
    # for i in range(13):
    #     vet_cli.append(cadastrar_clientes_automatico(tam_cli))
    #     tam_cli = tam_cli + 1

    # for i in range(0):
    #     vet_doc.append(cadastrar_documentos_automatico(tam_doc))
    #     tam_doc = tam_doc + 1
    
    # tam_doc = 0
    # for i in range(27):
    #     vet_doc.append(cadastrar_documentos_automatico(tam_doc))
    #     tam_doc = tam_doc + 1        

# --------------------------------------------------------------

    opc = menu()
    while opc >= 1 and opc <= 10:
    #while opc != 0:
        if opc == 1:
           if tam_cli <= 14:
                if cadastrar_clientes(vet_cli,tam_cli) == 1:                 
                    tam_cli = tam_cli + 1
                    print('Cliente cadastrado com sucesso ')
                else:
                    print('Código já cadastrado')
           else:
                print('Limite de clientes excedido')
                   

        elif opc == 2:
            listar_relatorio_de_clientes(vet_cli,tam_cli)

        elif opc == 3:
            if tam_doc <=29:
                if cadastrar_documentos(vet_doc,tam_doc,vet_cli,tam_cli) == 1:                 
                    tam_doc = tam_doc + 1
                    print('Documento cadastrado com sucesso ')
                else:
                    print('Código de cliente não cadastrado')
            else:
                print('Limite de documento excedido')

        # elif opc == 11:
        #    for i in range(10):
        #        vet_cli.append(cadastrar_clientes_automatico(tam_cli))
        #        tam_cli = tam_cli + 1

        #    for i in range(5):
        #         vet_doc.append(cadastrar_documentos_automatico(tam_doc))
        #         tam_doc = tam_doc + 1
           
        
        elif opc == 4:
            listar_relatorio_de_documentos(vet_doc,tam_doc)
            
        elif opc == 5:
            excluir_clientes_com_documento(vet_doc,tam_doc,vet_cli,tam_cli)
        
        elif opc == 6:
            excluir_documento_numero(vet_doc,tam_doc)
        
        elif opc == 7:
            excluir_documento_por_clientes(vet_doc,tam_doc,vet_cli,tam_cli)

        elif opc == 8:
            excluir_documento_data(vet_doc,tam_doc)
        
        elif opc == 9:
            if alterar_clientes(vet_cli,tam_cli) == 1: 
                print('Cliente alterado com sucesso ')
            else:
                 print('Código não cadastrado')

        elif opc == 10:
             exibir_documento_por_clientes(vet_doc,tam_doc,vet_cli,tam_cli)

        opc = menu()
main()

# class Estrutura_cliente:
#     cod_cliente = 0
#     nome = " "
#     fone =  " "

# class Estrutura_documentos:
#     num_doc = 0
#     cod_cliente = 0
#     dia_pagamento = 0
#     dia_vencimento = 0
#     valor = 0.0
#     juros = 0

# tam_max_cli = 15
# tam_max_doc = 30

    
# def menu():
#     print(50*'-=')
#     print('SISTEMA GERENCIADOR DE CLIENTES E DOCUMENTOS') 
#     print('1. Cadastrar clientes\n2. Relatório de clientes\n3. Cadastrar documentos\n4. Relatório de documentos\n5. Excluir clientes sem documento\n6. Excluir documentos individuais pelo número\n7. Excluir documentos por cliente\n8. Excluir documentos por período\n9. Alterar as informações dos clientes\n10. Mostrar o total de documentos de determinado cliente\n11. Sair\n)
#     opcao = int(input('Qual opção deseja? '))
#     print(50*'-=')
#     return opcao

# def cadastrar_clientes(vet_cli): #não pode existir mais que um cliente com o mesmo código.
#     for i in range(1):
#         cadastro_cli = Estrutura_cliente()
#         cadastro_cli.cod_cliente = int(input('Digite o código do cliente: '))
#         cadastro_cli.nome = str(input('Digite o nome do cliente: '))
#         cadastro_cli.fone = str(input('Digite o telefone do cliente: '))
#         vet_cli.append(cadastro_cli)

#     return vet_cli

# def listar_relatorio_de_clientes(vet_cli): #listar todos os clientes cadastrados.
#     print('RELATÓRIO DE CLIENTES.................')
#     print(f'Código do cliente:  {vet_cli[i].cod_cliente}')
#     print(f'Nome do cliente:  {vet_cli[i].nome}')
#     print(f'Telefone do cliente:  {vet_cli[i].fone}')
#     print(\n)

# def cadastrar_documentos(vet_doc, vet_cli): #ao cadastrar um documento, se o dia de pagamento for maior que o dia de vencimento, calcular o campo ‘juros’ do registro documentos (5% sobre o valor original do documento).
#     for i in range(1):
#             cadastro_doc = Estrutura_documentos()
#             cadastro_doc.cod_cliente = float(input('Digite o código do cliente: '))
#             if cadastro_doc.cod_cliente[i] ==  cadastro_cli.cod_cliente[i]
#                 cadastro_doc.num_doc = float(input('Digite o número do documento: ')) 
#                 cadastro_doc.dia_pagamento = int(input('Digite o dia do pagamento do documento: '))
#                 cadastro_doc.dia_vencimento = int(input('Digite o dia do vencimento do documento: '))
#                 cadastro_doc.valor = float(input('Digite o valor do documento: ')) #Pedir o valor  aqui mesmo ou no segundo if?
#                 if cadastro_doc.dia_pagamento[i] > cadastro_doc.dia_vencimento[i]: 
#                     calculo = (5 * cadastro_doc.valor) / 100 #cáculo juros 5%
#                     cadastro_doc.juros = calculo + cadastro_doc.valor
#             vet_doc.append(cadastro_doc)

#         return vet_doc #o que fazer para retornar dois paramentros?

# def  listar_relatorio_de_documentos(vet_doc): #listar todos os documentos cadastrados.
#     print('RELATÓRIO DE DOCUMENTOS.................')
#     print(f'Código do documento: {vet_doc[i].cod_cliente}')
#     print(f'Número do documento:  {vet_doc[i].num_doc}')
#     print(f'Dia do pagamento do documento:  {vet_doc[i].dia_pagamento}')
#     print(f'Dia do vencimento do documento:  {vet_doc[i].dia_vencimento}')
#     print(f'Valor do documento:  {vet_doc[i].valor}')
#     print(f'Valor do documento com juros de 5% : {cadastro_doc.juros}')
#     print(\n)

# def excluir_clientes_sem_documento(vet_cli, vet_doc): # um cliente só poderá ser excluído se não existir nenhum documento associado a ele.

#  if len(vet_doc) > 0: # verificação se está cadastrado
#         for i in range(len(vet_doc)):
#             if i == 0: #faz a inicialização apenas uma vez
#                 indice = i
#             vet_cli.pop(indice)  
                       
#     return vet_conta


# def excluir_documentos_ind_pelo_numero(): #por meio de seu número. Caso o documento não exista, o programa deverá mostrar a mensagem "Documento não encontrado".
#     num_doc = int(input("Digite o número do documento: "))
#     if documento não existe
#     if vet_doc[i].num_doc 
#     print('Documento não encontrado.')
#     else 
#     apagar documento
#     num_doc


#      if len(vet_conta) > 0: # verificação se está cadastrado
#         for i in range(len(vet_conta)):
#             if i == 0: #faz a inicialização apenas uma vez
#                 menor_saldo = vet_conta.saldo
#                 indice = i

#             if vet_conta[i].saldo <= menor_saldo:
#                 menor_saldo = vet_conta[i].saldo
#                 indice = i
#        vet_conta.pop(indice)        
# def excluir_documentos_por_cliente(): #o programa deverá informar o código do cliente e excluir todos os seus documentos. Caso o cliente não exista, deverá mostrar a mensagem "Cliente não encontrado".

# def excluir_documentos_por_periodo(): #o programa deverá informar o dia inicial e o dia final e excluir todos os documentos que possuam data de vencimento nesse período.

# def alterar_as_informacoes_dos_clientes(): #só NÃO altere o código do cliente.

# def mostrar_o_total_de_documentos_determinado_cliente(): #Mostrar o total de documentos de determinado cliente.

# def main():
#     vet_doc = [] #Declaração do vetor documentos
#     vet_cli = [] #Declaração do vetor clientes
#     #vet_cadastro = [ ]
#     opc = menu()
#     while opc >= 1 and opc <= 10:
#         if opc == 1:
#             vet_cadastro = cadastrar_produtos(vet_cli)
#             if vet_cli[i].cod_cliente == vet_cli[i].cod_cliente:  #não pode existir mais que um cliente com o mesmo código.
#                 print('Não pode existir mais que um cliente com o mesmo código')
#                 vet_cadastro = cadastrar_produtos(vet_cli)
#             else:
#                 opc = menu()

#         elif opc == 2:
#             listar_relatorio_de_clientes(vet_cli)
        
#         elif opc == 3:
#              cadastrar_documentos(vet_doc)

#         elif opc == 4:

#         elif opc == 5:

#         elif opc == 6:

#         elif opc == 7:

#         elif opc == 8:

#         elif opc == 9:
        
#         elif opc == 10:

#         opc = menu()
# main()

# class Estrutura_cliente:
#     cod_cliente = 0
#     nome = " "
#     fone =  " "

# class Estrutura_documentos:
#     num_doc = 0.0
#     cod_cliente = 0
#     dia_vencimento = 0
#     dia_pagamento = 0
#     valor = 0.0
#     juros = 0
    

# def menu():
#     print(50*'-=')
#     print('SISTEMA GERENCIADOR DE CLIENTES E DOCUMENTOS') 
#     print('1. Cadastrar clientes')
#     print('2. Relatório de clientes')
#     print('3. Cadastrar documentos')
#     print('4. Relatório de documentos')
#     print('5. Excluir clientes sem documento')
#     print('6. Excluir documentos individuais pelo número')
#     print('7. Excluir documentos por cliente ')
#     print('8. Excluir documentos por período')
#     print('9. Alterar as informações dos clientes')
#     print('10. Mostrar o total de documentos de determinado cliente  ')
#     print('11. Sair') 
#     opcao = int(input('Qual opção deseja? '))
#     print(50*'-=')
#     return opcao

# def cadastrar_clientes(vet_cli): #não pode existir mais que um cliente com o mesmo código.
#     for i in range(1):
#         cadastro_cli = Estrutura_cliente()
#         cadastro_cli.cod_cliente = int(input('Digite o código do cliente: '))
#         cadastro_cli.nome = str(input('Digite o nome do cliente: '))
#         cadastro_cli.fone = str(input('Digite o telefone do cliente: '))
#         vet_cli.append(cadastro_cli)

#     return vet_cli

# def listar_relatorio_de_clientes(vet_cli): #listar todos os clientes cadastrados.
#     print('RELATÓRIO DE CLIENTES.................')
#     print(f'Código do cliente: R$ {vet_cli[i].cod_cliente}')
#     print(f'Nome do cliente: R$ {vet_cli[i].nome}')
#     print(f'Telefone do cliente: R$ {vet_cli[i].fone}')
#     print(\n)

# def cadastrar_documentos(vet_doc): #ao cadastrar um documento, se o dia de pagamento for maior que o dia de vencimento, calcular o campo ‘juros’ do registro documentos (5% sobre o valor original do documento).

# def  listar_relatorio_de_documentos(vet_doc): #listar todos os documentos cadastrados.

# def excluir_clientes_sem_documento(): # um cliente só poderá ser excluído se não existir nenhum documento associado a ele.

# def excluir_documentos_ind_pelo_numero(): #por meio de seu número. Caso o documento não exista, o programa deverá mostrar a mensagem "Documento não encontrado".

# def excluir_documentos_por_cliente(): #o programa deverá informar o código do cliente e excluir todos os seus documentos. Caso o cliente não exista, deverá mostrar a mensagem "Cliente não encontrado".

# def excluir_documentos_por_periodo(): #o programa deverá informar o dia inicial e o dia final e excluir todos os documentos que possuam data de vencimento nesse período.

# def alterar_as_informacoes_dos_clientes(): #só NÃO altere o código do cliente.

# def mostrar_o_total_de_documentos_determinado_cliente(): #Mostrar o total de documentos de determinado cliente.


# def main():
#     vet_doc = [ ] #Declaração do vetor documentos
#     vet_cli = [ ] #Declaração do vetor clientes
#     opc = menu()
#     while opc >= 1 and opc <= 10:
#         if opc == 1:
#             vet_cadastro = cadastrar_produtos(vet_cli)
#             if vet_cli[i].cod_cliente == vet_cli[i].cod_cliente:  #não pode existir mais que um cliente com o mesmo código.
#                 print('Não pode existir mais que um cliente com o mesmo código')
#                 vet_cadastro = cadastrar_produtos(vet_cli)
#             else:
#                 opc = menu()

#         elif opc == 2:
#             listar_relatorio_de_clientes(vet_cli)
        
#         elif opc == 3:
#              cadastrar_documentos(vet_doc)

#         elif opc == 4:

#         elif opc == 5:

#         elif opc == 6:

#         elif opc == 7:

#         elif opc == 8:

#         elif opc == 9:
        
#         elif opc == 10:

#         opc = menu()
# main()

"""####9. (OPCIONAL A IMPLEMENTAÇÃO) Uma empresa prestadora de serviços armazena informações sobre os serviços prestados. Sabe-se que a empresa pode realizar no máximo três serviços diariamente. É de interesse de sua direção manter um histórico mensal (30 dias) sobre os serviços prestados.
A empresa realiza quatro tipos de serviços: 

1) pintura; 

2) jardinagem; 

3) faxina e

4) reforma em geral.

Cada serviço realizado deve ser cadastrado com as seguintes informações: número do serviço, valor do serviço, código do serviço e código do cliente, **numa matriz 30x3 referente a estrutura Servico_prestado**.

Cadastre/digite os quatro tipos de serviços (código e descrição) que a empresa poderá realizar. Para isso, utilize um vetor de quatro posições referente a **estrutura Tipo_servico**.
O programa deverá mostrar o seguinte menu de opções:
1. Cadastrar os tipos de serviços
2. Mostrar todos os tipos de serviço
3. Cadastrar os serviços prestados
4. Mostrar todos os serviços prestados
5. Mostrar os serviços prestados em determinado dia
6. Mostrar os serviços prestados dentro de um intervalo de valor
7. Mostrar um relatório geral (separado por dia), que exiba, inclusive, a descrição do tipo do serviço
8. Sair

**Para a opção 1**: deve-se cadastrar os tipos de serviços oferecidos pela empresa, com código e descrição.

**Para a opção 3**: deve-se considerar que deverão ser cadastrados os serviços prestados ao logo do mês. Em cada dia podem ser cadastrados, no máximo, três serviços prestados.

Utilize uma matriz capaz de armazenar em cada posição todas as informações referentes a um serviço prestado (número, valor, código do serviço, código do cliente). **Cada linha representa um dia do mês**. Dessa maneira, considere a matriz com dimensão 30 × 3.

Solicite o dia em que o serviço foi prestado e as demais informações.
Lembre-se de que a empresa só pode prestar os serviços que já tenham sido cadastrados no vetor de tipo de serviços.

Caso o usuário digite um código de tipo de serviço inválido, o programa deverá mostrar uma mensagem de erro.

Quando o usuário tentar cadastrar mais de três serviços prestados em um mesmo dia, também deverá mostrar uma mensagem de erro.

**Para a opção 5**: o programa deverá receber o dia que se deseja consultar e mostrar os respectivos serviços prestados.

**Para a opção 6**: o programa deverá receber o valor mínimo e o valor máximo e mostrar os serviços prestados que estiverem nesse intervalo.

**Para a opção 7**: o programa deverá mostrar todos os serviços prestados, conforme o exemplo a seguir.

                  DIA 01


No do serviço| Valor do serviço R$| Código do serviço| Descrição| Código do cliente
---|---|---|---|---
100| 200,00| 1| Pintura| 1
150| 100,00| 3| Faxina| 5
201| 640,00| 4| Reforma em geral| 2

                  DIA 02

No do serviço| Valor do serviço R$| Código do serviço| Descrição| Código do cliente
---|---|---|---|---
301| 600,00| 4| Reforma em geral| 3
280| 352,00| 1| Pintura| 2
306| 200,00| 2| Jardinagem| 1
"""

# Por onde começo a programar esse exercício?
# Sempre comece da parte mais simples/talvez a menor e já vai implementando e testando

# Digite seu código aqui

# class Representar_funcionario:
#     nome = ''
#     ende = Representar_endereco()
#     codigo = 0
#     salario = 0.0

# class Representar_endereco:
#     rua = ''
#     numero = 0
#     bairro = ''
#     cidade = ''

# def menu():
#     print(50*'-=')
#     print('Sistema de gerenciamento da escola') 
#     print('1.Cadastrar funcionários')
#     print('2.Visualizar todos os dados')
#     print('3.Sair')
#     opcao = int(input('Qual opção deseja? '))
#     print(50*'-=')
#     return opcao

# def cadastrar_funcionarios(vet_funcionario):
#     for i in range(1):
#         cadastro = Representar_funcionario( )
#         cadastro.nome = str(input('digite o nome do funcionário: '))
#         cadastro.salario = int(input('Digite o salário do funcionário: '))
#         cadastro.codigo = float(input('Digite o código do funcionário: '))
#         cadastro.endereco.rua = str(input('Digite a rua: '))
#         cadastro.endereco.numero = int(input('Digite o número: '))
#         cadastro.endereco.bairro = str(input('Digite o bairro: '))
#         cadastro.endereco.cidade = str(input('Digite a cidade: '))
       
#         vet_funcionario.append(cadastro)
#     return vet_funcionario

# def Visualizar_todos_os_dados(vet_funcionario):
#     print('\nRelação de produtos............................')
#     print('Código\tNome do produto\t\tPreço')
#     for i in range(1):
#         print(vet_funcionario[i].nome, '\n',vet_funcionario[i].salario,'\n',vet_funcionario[i].codigo, '\n',vet_funcionario[i].endereco)
#         print()
        


# def main():
#     vet_funcionario = [ ] #Declaração do vetor
#     opc = menu()
#     while opc >= 1 and opc <= 2:
#         if opc == 1:
#             vet_funcionario = cadastrar_funcionarios(vet_funcionario)
#         elif opc == 2:
#             vet_funcionario = Visualizar_todos_os_dados(vet_funcionario)
        
#         opc = menu()
        
        

# main()