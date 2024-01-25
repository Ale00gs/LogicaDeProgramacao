"""
### 1. Crie um programa que carregue o arquivo Vendas.xlsx, por meio da biblioteca Pandas. Calcule e apresente a média da coluna do arquivo 'Valor Unitário'.
"""
import pandas as pd
df1 = pd.read_excel('Vendas.xlsx')
soma = df1['Valor Unitário'].sum()
media = soma / len(df1['Valor Unitário'])
print(f'Média: {media:.2f}')

"""
### 2. Crie um programa que carregue o arquivo Vendas.xlsx, por meio da biblioteca Pandas. Calcule e apresente a quantidade mínima da coluna do arquivo 'Quantidade'.

"""

import pandas as pd
df2 = pd.read_excel('Vendas.xlsx')
qtd_min = df2['Quantidade'].min()
print(f'Quantidade mínima: {qtd_min:.2f}')

"""### 3. Crie um programa que carregue o arquivo Vendas.xlsx, por meio da biblioteca Pandas. Calcule e apresente o valor máximo da coluna do arquivo 'Valor Final'.

"""

import pandas as pd
df3 = pd.read_excel('Vendas.xlsx')
qtd_max_valor = df3['Valor Final'].max()
print(f'Valor máximo: {qtd_max_valor:.2f}')

"""### 4. Crie um programa que carregue o arquivo Propaganda.csv, por meio da biblioteca Pandas. Calcule e apresente o valor máximo da coluna do arquivo 'Jornal'.

"""

import pandas as pd
df4 = pd.read_csv('Propaganda.csv')
qtd_max_jornal = df4['Jornal'].max() 
print(f'Valor máximo da coluna do arquivo jornal: {qtd_max_jornal:.2f}')

"""### 5. Crie um programa que carregue o arquivo Propaganda.csv, por meio da biblioteca Pandas. Gere um histograma, referente a coluna Rádio, utilizando a biblioteca plotly.

"""

import pandas as pd
df5 = pd.read_csv('Propaganda.csv')
import plotly.express as px
fig = px.histogram(df5,x = ['tv' 'Radio' 'Jornal' 'Vendas'])
fig.show()

"""### 6. Crie um programa que carregue o arquivo Propaganda.csv, por meio da biblioteca Pandas. Gere um histograma, referente a coluna TV, utilizando a biblioteca Matplotlib, apresente na cor verde.

"""

import pandas as pd
df5 = pd.read_csv('Propaganda.csv')
import matplotlib.pyplot as plt
plt.hist(df5['TV'], 5, rwidth = 0.8, color = 'red')
plt.title('coluna TV')
# plt.xlabel('nome 1')
# plt.ylabel('nome 2')
plt.show()

qtd_max_jornal_format = qtd_max_jornal.replace('.',',')