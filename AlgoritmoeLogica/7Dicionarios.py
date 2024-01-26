# Dicionário é uma lista com um "rótulo"
# É muito bom para armazenar informações que 
# precisam de algum tipo de identificador. Vamos ver no exemplo.
# Ex: E-mails de gerentes de loja

emails_gerentes = {
    "Iguatemi": "iguatemi@gmail.com",
    "Plaza": "plaza@gmail.com",
    "Barra": "barra@gmail.com,"
}

# --- EXERCÍCIO 1 ---------------------
# Se eu quiser descobrir qual o e-mail do shopping "Iguatemi"

email = emails_gerentes['Iguatemi']
print(email)

# --- EXERCÍCIO 2 ---------------------
# Se eu quiser adicionar um shopping novo

emails_gerentes['Leblon'] = "leblon@gmail.com"
print(emails_gerentes)

# --- EXERCÍCIO 3 ---------------------
# Se eu quiser descobrir todos os shopping que temos?

# forma 1: fazer um for
for shopping in emails_gerentes:
    print(shopping)

# forma 2: dicionario.keys()
print(emails_gerentes.keys())

# --- EXERCÍCIO 4 ---------------------
# Se eu quiser todos os e-mails?

# forma 1: fazer um for
for shopping in emails_gerentes:
    print(emails_gerentes[shopping])

# forma 2: dicionarios.values
print(emails_gerentes.values())

# --- EXERCÍCIO 5 ---------------------
# Retirar um shopping

removido = emails_gerentes.pop("Iguatemi")
print(f'O shopping "{removido}" foi removido.')

print(emails_gerentes)

# --- EXERCÍCIO 6 ---------------------
# Verificar se um Shopping existe:

if "Iguatemi" in emails_gerentes:
    print("Tem sim")
else:
    print("Tem não")