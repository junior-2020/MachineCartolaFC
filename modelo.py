# -*- coding: utf-8 -*-

import torch
# https://stackabuse.com/time-series-prediction-using-lstm-with-pytorch-in-python


class LSTM(torch.nn.Module):
    def __init__(self, input_tamanho=4, camada_oculta_tamanho=50, output_tamanho=1):
        super().__init__()
        self.input_tamanho = input_tamanho
        self.camada_oculta_tamanho = camada_oculta_tamanho
        self.lstm = torch.nn.LSTM(input_tamanho, camada_oculta_tamanho)
        self.linear = torch.nn.Linear(camada_oculta_tamanho, output_tamanho)
        self.neuronios_ocultos = (torch.zeros(1, 1, self.camada_oculta_tamanho),
                                  torch.zeros(1, 1, self.camada_oculta_tamanho)
                                  )

    def forward(self, input_seq):
        lstm_output, self.neuronios_ocultos = self.lstm(
            input_seq.view(len(input_seq), 1, -1), self.neuronios_ocultos)
        predicoes = self.linear(lstm_output.view(len(input_seq), -1))
        return predicoes[-1]

# class pyTorchModel(torch.nn.Module):
#     def __init__(self, chIn=1, ch=2):
#         super(pyTorchModel, self).__init__()
#         self.layer1 = torch.nn.Sequential(
#             torch.nn.Conv2d(in_channels=chIn,
#                             out_channels=ch*8, kernel_size=7),
#             torch.nn.ReLU(),
#             torch.nn.Conv2d(in_channels=ch*8, out_channels=ch *
#                             16, kernel_size=5, stride=2),
#             torch.nn.ReLU(),
#             # era 16 e 32 no primeiro conjunto de ensaio
#             torch.nn.Conv2d(in_channels=ch*16, out_channels=ch * \
#                             32, kernel_size=3, stride=2),
#             torch.nn.ReLU(),
#             # era 32 e 32 no primeiro conjunto de ensaio
#             torch.nn.Conv2d(in_channels=ch*32, out_channels=ch * \
#                             32, kernel_size=3, stride=2),
#             torch.nn.ReLU(),
#             torch.nn.Conv2d(in_channels=ch*32, out_channels=ch * \
#                             64, kernel_size=3, stride=2),
#             torch.nn.ReLU(),
#             torch.nn.Conv2d(in_channels=ch*64, out_channels=ch * \
#                             64, kernel_size=3, stride=2),
#             torch.nn.ReLU()
#         )
#         self.v = torch.nn.Sequential(
#             torch.nn.Linear(64*ch*1*1, 256),
#             torch.nn.ReLU()
#         )
#         self.fc = torch.nn.Linear(256, 3)
#         self.ch = ch

#     def forward(self, x):
#         x = self.layer1(x)
#         x = x.view(x.size(0), -1)  # 'estica' a imagem em um vetor de features
#         x = self.v(x)
#         x = self.fc(x)

#         x[:, 0] = torch.tanh(x[:, 0])
#         x[:, 1] = torch.sigmoid(x[:, 1])
#         x[:, 2] = torch.sigmoid(x[:, 2])
#         return x

# Rede model02
# class pyTorchModel(torch.nn.Module):
#     def __init__(self,chIn=1,ch=2):
#         super(pyTorchModel,self).__init__()
#         self.layer1 = torch.nn.Sequential(
#             torch.nn.Conv2d(in_channels=chIn,out_channels=ch*8,kernel_size=7),
#             torch.nn.ReLU(),
#             torch.nn.Conv2d(in_channels=ch*8,out_channels=ch*16,kernel_size=5,stride=2),
#             torch.nn.ReLU(),
#         )
#         self.v = torch.nn.Sequential(
#             torch.nn.Linear(43808,256),
#             torch.nn.ReLU()
#         )
#         self.fc = torch.nn.Linear(256,3)
#         self.ch = ch

#     def forward(self,x):
#         x = self.layer1(x)
#         x = x.view(x.size(0),-1)
#         x = self.v(x)
#         x = self.fc(x)

#         x[:,0] = torch.tanh(x[:,0])
#         x[:,1] = torch.sigmoid(x[:,1])
#         x[:,2] = torch.sigmoid(x[:,2])
#         return x


# class pyTorchModel(torch.nn.Module):
#     def __init__(self,chIn=1,ch=2):
#         super(pyTorchModel,self).__init__()
#         self.layer1 = torch.nn.Sequential(
#             torch.nn.Conv2d(in_channels=chIn,out_channels=ch*8,kernel_size=7),
#             torch.nn.ReLU(),
#             torch.nn.Conv2d(in_channels=ch*8,out_channels=ch*16,kernel_size=5,stride=2),
#             torch.nn.ReLU(),
#             torch.nn.Conv2d(in_channels=ch*16,out_channels=ch*32,kernel_size=3,stride=2),    # era 16 e 32 no primeiro conjunto de ensaio
#             torch.nn.ReLU(),
#             torch.nn.Conv2d(in_channels=ch*32,out_channels=ch*32,kernel_size=3,stride=2), # era 32 e 32 no primeiro conjunto de ensaio
#             torch.nn.ReLU(),
#             torch.nn.Conv2d(in_channels=ch*32,out_channels=ch*64,kernel_size=3,stride=2),
#             torch.nn.ReLU(),
#             torch.nn.Conv2d(in_channels=ch*64,out_channels=ch*64,kernel_size=3,stride=2),
#             torch.nn.ReLU()
#         )
#         self.v = torch.nn.Sequential(
#             torch.nn.Linear(64*ch*1*1,256),
#             torch.nn.ReLU()
#         )
#         self.fc = torch.nn.Linear(256,3)
#         self.ch = ch

#     def forward(self,x):
#         x = self.layer1(x)
#         x = x.view(x.size(0),-1)
#         x = self.v(x)
#         x = self.fc(x)

#         x[:,0] = torch.tanh(x[:,0])
#         x[:,1] = torch.sigmoid(x[:,1])
#         x[:,2] = torch.sigmoid(x[:,2])
#         return x
