#!/usr/bin/env python
# coding: utf-8

# # Análise de Dados com Python
# 
# ### Desafio:
# 
# Você trabalha em uma empresa de telecom e tem clientes de vários serviços diferentes, entre os principais: internet e telefone.
# 
# O problema é que, analisando o histórico dos clientes dos últimos anos, você percebeu que a empresa está com Churn de mais de 26% dos clientes.
# 
# Isso representa uma perda de milhões para a empresa.
# 
# O que a empresa precisa fazer para resolver isso?
# 
# Base de Dados: https://www.kaggle.com/radmirzosimov/telecom-users-dataset

# In[ ]:


#Lógica

#Passo1 - Importar a base de dados

#Passo2 - Visualizar a base de dados

#Passo3 - Tratamento dos dados

#Passo4 - Análise incial

#Passo5 - Análise detalhada dos clientes


# In[30]:


#Passo1 
import pandas as pd
tabela = pd.read_csv('telecom_users.csv')

#Passo2
#display(tabela) <- mostra a tabela referida, no caso, deixaremos para usar essa função após tratar os dados

#Passo3
#coluna inútil
tabela = tabela.drop('Unnamed: 0', axis=1)

#valores reconhecidos de forma errada
tabela['TotalGasto'] = pd.to_numeric(tabela['TotalGasto'], errors='coerce')

#tratar valores vazios
tabela = tabela.dropna(how= 'all', axis=1)
tabela = tabela.dropna(how= 'any', axis=0)
display(tabela)
print(tabela.info())

#Passo4
print(tabela['Churn'].value_counts())
print(tabela['Churn'].value_counts(normalize=True).map('{:.1%}'.format))

#Passo5
get_ipython().system('pip install plotly')
import plotly.express as px

for coluna in tabela.columns:
    
    grafico = px.histogram(tabela, x=coluna, color='Churn')
    grafico.show()








# ### Conclusões e Ações

# - Pessoas com famílias menores têm mais chances de cancelar
#     - Podemos criar um plano família para diminuir a taxa de cancelamento
# 
# - Quanto maior o tempo das pessoas como cliente, menor a taxa de cancelamento
#     - Existe alguma ação promocional trazendo clientes desqualificados 
#     - Podemos pensar em alguns bônus para fidelizar clientes
#     - A 1ª experiência do cliente pode estar sendo muito ruim
# 
# - Estamos com algum problema no serviço de Fibra, a taxa de cancelamento está muito alta
# 
# - Quanto mais serviços o cliente tem, maiores as chances de cancelamento
#     - Podemos criar algum pacote que ofereça mais serviços inclusos
#     
# - Quase todo cancelamento está no contrato mensal 
#     - Podemos oferecer descontos nos contratos anuais
#     
# - Forma de pagamento: evitar boleto eletrônico
#     - Dar desconto nas outras opções
#     
# 
#     

# In[ ]:




