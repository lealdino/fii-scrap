
import pandas as pd
import requests
import re
from bs4 import BeautifulSoup

import warnings
warnings.filterwarnings("ignore")


def get_fundos():
    """
        Return a dataframe with FIIS (Fundos Imobiliários) coletados da plataforma Funds Explorer
    """

    url = 'https://www.fundsexplorer.com.br/ranking'
    agent = {"User-Agent": "Mozilla/5.0"}
    resposta = requests.get(url, headers=agent)
    soup = BeautifulSoup(resposta.text, 'lxml')
    tabela = soup.find_all('table')[0]

    df = pd.read_html(str(tabela), decimal=',', thousands='.')[0]

    colunas = list(df.columns)

    for coluna in colunas:
        try:
            if coluna not in ['Setor', 'Códigodo fundo']:
                df[coluna] = df[coluna].apply(
                    lambda s: re.sub(r'[R$.%]', r'', str(s))
                )
                df[coluna] = df[coluna].apply(
                    lambda s: re.sub(r',', r'.', str(s))).astype(float)

        except:
            continue

    return df


def get_fundos_symbols():
    """
        Return a list of FIIS
    """

    url = 'https://www.fundsexplorer.com.br/ranking'
    agent = {"User-Agent": "Mozilla/5.0"}
    resposta = requests.get(url, headers=agent)
    soup = BeautifulSoup(resposta.text, 'lxml')
    tabela = soup.find_all('table')[0]

    df = pd.read_html(str(tabela), decimal=',', thousands='.')[0]

    return list(df['Códigodo fundo'])
