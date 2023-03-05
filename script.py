from kaggle.api.kaggle_api_extended import KaggleApi
from zipfile import ZipFile
from time import sleep
import pandas as pd
import os
import re


def download_files(url):
    api = KaggleApi()
    api.authenticate()
    path = os.getcwd()
    
    # url do arquivo para download    
    file_name = url
    
    padrao = r'\bdatasets\b'
    match = re.search(padrao, file_name)
    if match:
        palavra =  file_name[match.start()+9:]
        posicao = palavra.find("/")
        palavra2 = palavra[posicao+1:]
    

    # API para fazer o download do dados
    api.dataset_download_files(palavra,  path=path)
    os.chdir(path)
    with ZipFile(palavra2+".zip", 'r') as zip:
        # extraindo todos os arquivos
        print('extraindo todos os arquivos...')
        zip.extractall()
    print("Download Concluido!")
      

# chamando a função com a url do arquivo
download_files("https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020")


dados = pd.read_csv('circuits.csv')
print(dados.head(10))


# Listar e fitrar todos os arquivos no diretório atual
arquivos = os.listdir()
arquivos_csv = [arquivo for arquivo in arquivos if arquivo.endswith('.csv')]

# Imprimir arquivos CSV
print('Arquivos CSV no diretório atual:')
for arquivo in arquivos_csv:
    print(arquivo)
    
    dados = pd.read_csv(arquivo)
    print(dados.head(10))
    sleep(2)
    print('\n')
    



