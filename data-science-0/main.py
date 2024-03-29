#!/usr/bin/env python
# coding: utf-8

# # Desafio 1
# 
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
# 
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


black_friday = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# In[3]:


# Padronizando: 
pucharse_padronizada = (black_friday['Purchase'] - black_friday['Purchase'].mean()) / black_friday['Purchase'].std()

# normalizando:
pucharse_normalizada = ((black_friday['Purchase'] - black_friday['Purchase'].min()) /
                    (black_friday['Purchase'].max() - black_friday['Purchase'].min()))


# ## Questão 1
# 
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[4]:


def q1():
    return black_friday.shape


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# In[5]:


def q2():
    quantidade = black_friday[(black_friday['Gender'] == 'F') & (black_friday['Age']=='26-35')].shape[0]
    return quantidade


# ## Questão 3
# 
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# In[6]:


def q3():
    quantidade = len(black_friday['User_ID'].unique())
    return quantidade


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[7]:


def q4():
    quantidade = len(black_friday.dtypes.unique())
    return quantidade


# ## Questão 5
# 
# Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[8]:


def q5():
    linhas_nulas = black_friday[(black_friday['Product_Category_2'].isna()) | (black_friday['Product_Category_3'].isna())].shape[0]
    linhas_totais = black_friday.shape[0]

    percentual = linhas_nulas/linhas_totais
    return float(percentual)


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[9]:


def q6():
    quantidade = max(black_friday.isna().sum())
    return quantidade


# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[10]:


def q7():
    valor = black_friday['Product_Category_3'].mode()
    return float(valor)


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[11]:


def q8():
    media = pucharse_normalizada.mean()
    return float(media)


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# In[12]:


def q9():
    quantidade = len(pucharse_padronizada[(pucharse_padronizada > -1) & (pucharse_padronizada < 1)])
    return quantidade


# ## Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[13]:


def q10():
    regra = black_friday[(black_friday['Product_Category_2'].isna()) & (~black_friday['Product_Category_3'].isna())].shape[0]
    if regra == 0:
        return True
    else:
        return False

