"""
Nome do Arquivo: main.py
Descrição: Calcular a média dos valores obtidos em uma base de dados que se encontra em um arquivo .zip.
Autor : Everton Diniz Silva
Data Criação: 30/11/2024
Versão: 1.0 
"""

#Bibliotecas utilizadas:
import zipfile
from pathlib import Path
import numpy as np


#Variáveis Globais:
ListaDeDados = []
DadosIncompatíveis = []

#Definir caminho da pasta e do arquivo:
CaminhoArquivo = Path(__file__).parent /'base_dados'/'Arquivo.zip'
CaminhoPasta = Path(__file__).parent /'base_dados'


#Função para descompactar arquivo e obter dados: 
def decompactar_dado():

    #Decompactar arquivo .zip:
    with zipfile.ZipFile(f'{CaminhoArquivo}', 'r') as ArquivoZip:    
        arquivos = ArquivoZip.namelist()
        
        #Interar sobre os arquivos existente e selecionar o arquivo de interesse:
        for arquivo in arquivos:

            if arquivo ==  'data.txt':
                DadosTxt = arquivo
            
                #Abrir dados disponiveis em arquivo txt:
                DadosEmBytes = ArquivoZip.read(DadosTxt)

                #formatar e listar dados:
                DadosForm = DadosEmBytes.decode("utf-8").split(" ")

                return DadosForm   

            else:
                print(f'Arquivo "data.txt" não foi encontrado em: " {CaminhoPasta} "')  
                return 'ARQUIVO NÃO ENCONTRADO' 
           
         

#Função para obter lista com os dados formatados e calcular a média dos valores obtidos: 
def listar_dados(dado):

    #Interar sobre os dados obtidos e acrescentar em uma lista no fomato numérico inteiro:
    for d in dado:
        #Atribuir dado numérico em lista:
        if d.isnumeric():
            ListaDeDados.append(int(d))

        #Dados incompatíveis:
        else:
            DadosIncompatíveis.append(d)  

    #Calcular média dos valores da lista:
    MédiaDados = f'{np.mean(ListaDeDados).tolist():.6f}'
   
    #Retornar resultados da função:
    return MédiaDados, len(ListaDeDados), DadosIncompatíveis       


#Chamadas das funções: 

DadoForm = decompactar_dado()

if DadoForm != 'ARQUIVO NÃO ENCONTRADO':

    media = listar_dados(DadoForm)

    #Apresentação dos resultados:

    texto = 'Calculo da média dos valores obtido atravéz do arquivo data.txt:'

    print(f'{"-"*len(texto)}{"-"*5}')
    print(f'\n{texto}\n')
    print(f'Total de valores existente: {media[1]} ')
    print(f'Média calculada: {media[0]} ')
    print(f'Dados incompativeis para os calculos: {media[2]}\n')
    print(f'{"-"*len(texto)}{"-"*5}')

