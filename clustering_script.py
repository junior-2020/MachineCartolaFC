import pandas as pd
import numpy as np
import random as rd
import matplotlib.pyplot as plt


class Clusters():
    def __init__(self, dados, K=15):
        self.K = K
        self.dados = dados

        self.pontuacaoAtleta = 'Pontos'
        self.precoAtleta = 'Preço'
        self.mediaAtleta = 'Média'
        self.variacaoAtleta = 'Variação'
        self.atletaId = 'Atleta_id'
        self.rodadaId = 'Rodada_id'

    # def __str__(self):
    #     super().__str__()
    #     return self.dados

    def formar_clusters(self):
        ########################################################################################################################################################################
        '''
        Seleção do numéro de aglomerados (clusters) e centróides de cada aglomerado
        '''
        ########################################################################################################################################################################

        # K = 15

        centroides = (self.dados.sample(self.K))
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

        ########################################################################################################################################################################

        # Aqui funciona
        ########################################################################################################################################################################

        diff = 1
        j = 0

        while(diff > 1):
            XD = self.dados
            i = 1
            for index1, row_c in centroides.iterrows():
                ED = []
                for index2, row_d in XD.iterrows():
                    d1 = (row_c[self.mediaAtleta]-row_d[self.mediaAtleta])**2
                    d2 = (row_c[self.precoAtleta]-row_d[self.precoAtleta])**2
                    d = np.sqrt(d1+d2)
                    ED.append(d)
                self.dados[i] = ED
                i = i+1

            C = []
            for index, row in self.dados.iterrows():
                min_dist = row[1]
                pos = 1
                for i in range(self.K):
                    if row[i+1] < min_dist:
                        min_dist = row[i+1]
                        pos = i+1
                C.append(pos)
            self.dados["Cluster"] = C
            Centroids_new = self.dados.groupby(["Cluster"]).mean()[
                [self.precoAtleta, self.mediaAtleta]]
            if j == 0:
                diff = 1
                j = j+1
            else:
                diff = (Centroids_new[self.precoAtleta] - centroides[self.precoAtleta]).sum() + (
                    Centroids_new[self.mediaAtleta] - centroides[self.mediaAtleta]).sum()
                print(diff.sum())
            centroides = self.dados.groupby(["Cluster"]).mean()[
                [self.precoAtleta, self.mediaAtleta]]

        self.centroides = centroides
        # print(dados_eixo_x)

    def plotar_clusters(self):
        plt.scatter(self.dados[self.mediaAtleta],
                    self.dados[self.precoAtleta], c='black')
        plt.scatter(self.centroides[self.mediaAtleta],
                    self.centroides[self.precoAtleta], c='red')
        plt.xlabel('Média do atleta')
        plt.ylabel('Preço do atleta')
        plt.show()
