
import pandas as pd
import requests
from bs4 import BeautifulSoup

import warnings
warnings.filterwarnings("ignore")


def get_data():
    """
        Return a dataframe with FIIS (Fundos Imobiliários) coletados da plataforma Funds Explorer
    """

    url = 'https://www.fundsexplorer.com.br/ranking'
    headers = {"User-Agent": "Mozilla/5.0"}
    resposta = requests.get(url, headers)
    soup = BeautifulSoup(resposta.text, 'lxml')
    return soup.find_all('table')[0]


def get_fundos():
    tabela = get_data()
    df = pd.read_html(str(tabela), decimal=',', thousands='.')[0]

    colunas = list(df.columns)

    for coluna in colunas:
        try:
            df[coluna] = df[coluna].str.replace(r"((?!(,|[0-9])).)", '', regex=True)
            df[coluna] = df[coluna].str.replace(',', '.').astype(float)
               
        except:
            continue

    return df.fillna(0)


def get_fundos_symbols():
    """
        Return a list of FIIS
    """
    tabela = get_data()

    df = pd.read_html(str(tabela), decimal=',', thousands='.')[0]

    return list(df['Códigodo fundo'])
