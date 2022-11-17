
import pandas as pd
import requests
from bs4 import BeautifulSoup

import warnings
warnings.filterwarnings("ignore")


def get_fundos():



    """
        Return a dataframe with FIIS (Fundos Imobiliários) coletados da plataforma Funds Explorer
    """

    url = 'https://www.fundsexplorer.com.br/ranking'
    agent = {"User-Agent":"Mozilla/5.0"}
    resposta = requests.get(url, headers= agent)
    soup = BeautifulSoup(resposta.text, 'lxml')
    tabela = soup.find_all('table')[0]
    
    df = pd.read_html(str(tabela), decimal = ',', thousands= '.')[0]
    
    colunas = list(df.columns)

    for coluna in colunas:
        try:
            df[coluna] = df[coluna].str.replace('R','')
            df[coluna] = df[coluna].str.replace('$','')
            df[coluna] = df[coluna].str.replace('.','')
            df[coluna] = df[coluna].str.replace('%','')
            df[coluna] = df[coluna].str.replace(',','.').astype(float)
        
            
        except:
          continue
    
    return df


