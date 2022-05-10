#!/usr/bin/env python
# coding: utf-8

# # QUANTIDADE DE TINTA PARA PINTAR UMA PAREDE
# 

# In[18]:


# Incerir a largura e altura da parede e a taxa de perda da tinta.
lar = float(input('Largura da parede:')) 
alt = float(input('Altura da parede:'))  
Tperda = float(input('Taxa de perda:'))

#Transformar a perda em porcentagem
Tp =Tperda/100 +1 

#Calcular a área a ser pintada
área = lar*alt

#Exibir as dimesões e área da parede, e a taxa de perda da tinta
print('Sua parede tem dimensao de {}m X {}m e área de {}m² com perda de {}%.'.format(lar,alt,área,Tperda)) 

#Calcular o volume de tinta a ser utilizado na pintura
tinta =área*Tp/2

#Exibir a quantidade de tinta para pintar a parede já com a taxa de perda
print('Com esta taxa de perda você irá precisar de {}Litros de tinta para pintar a parede'.format(tinta))


# In[ ]:




