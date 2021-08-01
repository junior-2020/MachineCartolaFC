import pandas as pd
import numpy as np
import random as rd
import matplotlib.pyplot as plt
import clustering_script


########################################################################################################################################################################
'''
Aquisição dos dados e visualização dos gráficos da base de dados que será utilizada
'''
########################################################################################################################################################################
# from locale import atof, setlocale, LC_NUMERIC

# setlocale(LC_NUMERIC, '')
# f = lambda x: atof(x)


dados = pd.read_csv('atletaspontuacao.csv', sep=',', converters={'Id':int, 'Atleta_id':int, 'Rodada_id': int})
#, 'Pontos':f, 'Preço':f, 'Variação':f, 'Média':f })

print("Imprimindo as primeiras entradas dos dados: \n", dados.head())

print("Fazendo a descrição estatística dos dados: \n", dados.describe(include='float64'))


pontuacaoAtleta = 'Pontos'
precoAtleta = 'Preço'
mediaAtleta = 'Média'
variacaoAtleta = 'Variação'
# partidasJogadas = 'jogos_num'
# scoutId = 'scout'
# qtdeScout = 'qtde_scout'
# clubeId = 'clube_id'
# posicaoId = 'posicao_id'
atletaId = 'Atleta_id'
rodadaId = 'Rodada_id'


# Fazendo os gráficos para visualização

dados_eixo_x_atleta = dados[[atletaId, pontuacaoAtleta, precoAtleta, mediaAtleta, rodadaId]]
print("Imprimindo os dados selecionados: \n", dados_eixo_x_atleta)

# plt.scatter(dados_eixo_x_atleta[rodadaId], dados_eixo_x_atleta[pontuacaoAtleta], c='black')
# plt.scatter(dados_eixo_x_atleta[rodadaId], dados_eixo_x_atleta[mediaAtleta], c='red')
# plt.xlabel('Número da rodada')
# plt.ylabel('Pontuação do atleta(b) / Media(r)')
# plt.show()


plt.scatter(dados_eixo_x_atleta[precoAtleta], dados_eixo_x_atleta[mediaAtleta], c='black')
plt.xlabel('Preço do atleta')
plt.ylabel('Média do atleta')
plt.show() # Bom gráfico!


plt.scatter(dados_eixo_x_atleta[mediaAtleta], dados_eixo_x_atleta[pontuacaoAtleta], c='black')
plt.xlabel('Média do atleta')
plt.ylabel('Pontuação do atleta')
plt.show() # Bom gráfico!

# atletas_unicos = dados_eixo_x_atleta.groupby(atletaId)
# cor = (rd.random(), rd.random(), rd.random())
# print(atletas_unicos.shape)
ids_passadas = []


from cycler import cycler

plt.rc('axes', prop_cycle=(cycler('color', ['r', 'g', 'b', 'y', 'c', 'k']) *
                           cycler('linestyle', ['-', '--', ':', '-.'])))
plt.figure()
for id in dados_eixo_x_atleta[atletaId]:
    if id not in ids_passadas:
        atleta_atual = dados_eixo_x_atleta[dados_eixo_x_atleta[atletaId] == id]
        plt.plot(atleta_atual[rodadaId], atleta_atual[pontuacaoAtleta])
        ids_passadas.append(id)
        if len(ids_passadas) > 50:
            break
plt.xlabel('Número da rodada')
plt.ylabel('Pontuação de cada atleta')
plt.show()


# for index, linha in dados_eixo_x_scout.iterrows():
#     if linha[scoutId] == 'PI':
#         print(dados_eixo_x_atleta.at[index, mediaAtleta])
        

########################################################################################################################################################################
'''
Aplicação do algoritmo de clustering para classificar e agrupar os dados
'''
########################################################################################################################################################################


clusters_atletas = clustering_script.Clusters(dados)
# print(clusters_atletas.dados)
clusters_atletas.formar_clusters()
# clusters_atletas.plotar_clusters()
contador = 0

for i in dados_eixo_x_atleta:
    if dados_eixo_x_atleta[dados_eixo_x_atleta[rodadaId] == 13]:
        contador += 1
        print(contador)

