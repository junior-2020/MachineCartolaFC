import pandas as pd
import numpy as np
import random as rd
import matplotlib.pyplot as plt

from locale import atof, setlocale, LC_NUMERIC

setlocale(LC_NUMERIC, '')

########################################################################################################################################################################
'''
Aquisição dos dados e visualização dos gráficos da base de dados que será utilizada
'''
########################################################################################################################################################################

f = lambda x: atof(x)


dados = pd.read_csv('Dados_xls_CartolaFC_teste_1.csv', sep=';', converters={'pontos_num':f, 'preco_num':f, 'variacao_num': f, 'media_num':f })

print(dados.head())

print(dados.describe(include='float64'))


pontuacaoAtleta = 'pontos_num'
precoAtleta = 'preco_num'
mediaAtleta = 'media_num'
partidasJogadas = 'jogos_num'
scoutId = 'scout'
qtdeScout = 'qtde_scout'
clubeId = 'clube_id'
posicaoId = 'posicao_id'

dados_eixo_x_scout = dados[[scoutId, qtdeScout]]

# Fazendo os gráficos para visualização

print(dados_eixo_x_scout)

plt.scatter(dados_eixo_x_scout[scoutId], dados_eixo_x_scout[qtdeScout], c='black')
plt.xlabel('Tipo de Scout')
plt.ylabel('Quantidade do scout')
plt.show()

dados_eixo_x_atleta = dados[[pontuacaoAtleta, precoAtleta, partidasJogadas]]
print(dados_eixo_x_atleta)

plt.scatter(dados_eixo_x_atleta[partidasJogadas], dados_eixo_x_atleta[pontuacaoAtleta], c='black')
plt.xlabel('Partidas jogadas')
plt.ylabel('Pontuação do atleta')
plt.show()


dados_eixo_x_atleta = dados[[mediaAtleta, posicaoId]]
print(dados_eixo_x_atleta)

plt.scatter(dados_eixo_x_atleta[posicaoId], dados_eixo_x_atleta[mediaAtleta], c='black')
plt.xlabel('Posição em campo')
plt.ylabel('Média do atleta')
plt.show()

'''
Este gráfico merece estudo, parece promissor
'''

plt.scatter(dados_eixo_x_atleta[mediaAtleta], dados_eixo_x_scout[qtdeScout], c='black')
plt.xlabel('Média do atleta')
plt.ylabel('Quantidade do scout')
plt.show()

# for index, linha in dados_eixo_x_scout.iterrows():
#     if linha[scoutId] == 'PI':
#         print(dados_eixo_x_atleta.at[index, mediaAtleta])
        


########################################################################################################################################################################
'''
Seleção do numéro de aglomerados (clusters) e centróides de cada aglomerado
'''
########################################################################################################################################################################

# K = 3

# centroides = (dados_eixo_x.sample(K))
# plt.scatter(dados_eixo_x[rendaAnual], dados_eixo_x[valorEmprestimo], c='black')
# plt.scatter(centroides[rendaAnual], centroides[valorEmprestimo], c='red')
# plt.xlabel('Renda Anual')
# plt.ylabel('Valor Empréstimo (em milhares)')
# plt.show()

# print(dados_eixo_x)

########################################################################################################################################################################
'''
Associação dos pontos ao centroide mais próximo e recalculando os centroides
'''
########################################################################################################################################################################

# Não funciona
########################################################################################################################################################################

# diferenca = 1
# j = 0

# while diferenca != 0:
#     dados_xd = dados_eixo_x
#     i = 1
#     for index1, linha_c in centroides.iterrows():
#         dados_ed = []
#         for index2, linha_d in dados_xd.iterrows():
#             distancia1 = (linha_c[rendaAnual] - linha_d[rendaAnual]) ** 2
#             distancia2 = (linha_c[valorEmprestimo] - linha_d[valorEmprestimo]) ** 2
#             distanciaHipotenusa = np.sqrt(distancia1 + distancia2)

#             dados_ed.append(distanciaHipotenusa)

#         print(f' A variável i é {i}')
#         print(dados_eixo_x[1])
#         dados_eixo_x[i] = dados_ed
#         i += 1

#     dados_c = []

#     diferenca = 0

# print(type(dados_eixo_x))
# print()


#     for index, linha in dados_eixo_x.iterrows():
#         distancia_minima = linha[1]
#         posicao = 1
#         for i in range(K):
#             if linha[i+1] < distancia_minima:
#                 distancia_minima = linha[i+1]
#                 posicao = i+1
#         dados_c.append(posicao)

########################################################################################################################################################################
########################################################################################################################################################################

#Aqui funciona
########################################################################################################################################################################



# diff = 1
# j=0

# while(diff!=0):
#     XD=dados_eixo_x
#     i=1
#     for index1,row_c in centroides.iterrows():
#         ED=[]
#         for index2,row_d in XD.iterrows():
#             d1=(row_c["ApplicantIncome"]-row_d["ApplicantIncome"])**2
#             d2=(row_c["LoanAmount"]-row_d["LoanAmount"])**2
#             d=np.sqrt(d1+d2)
#             ED.append(d)
#         dados_eixo_x[i]=ED
#         i=i+1

#     C=[]
#     for index,row in dados_eixo_x.iterrows():
#         min_dist=row[1]
#         pos=1
#         for i in range(K):
#             if row[i+1] < min_dist:
#                 min_dist = row[i+1]
#                 pos=i+1
#         C.append(pos)
#     dados_eixo_x["Cluster"]=C
#     Centroids_new = dados_eixo_x.groupby(["Cluster"]).mean()[["LoanAmount","ApplicantIncome"]]
#     if j == 0:
#         diff=1
#         j=j+1
#     else:
#         diff = (Centroids_new['LoanAmount'] - centroides['LoanAmount']).sum() + (Centroids_new['ApplicantIncome'] - centroides['ApplicantIncome']).sum()
#         print(diff.sum())
#     centroides = dados_eixo_x.groupby(["Cluster"]).mean()[["LoanAmount","ApplicantIncome"]]

# print(dados_eixo_x)
    
# plt.scatter(dados_eixo_x[rendaAnual], dados_eixo_x[valorEmprestimo], c='black')
# plt.scatter(centroides[rendaAnual], centroides[valorEmprestimo], c='red')
# plt.xlabel('Renda Anual')
# plt.ylabel('Valor Empréstimo (em milhares)')
# plt.show()