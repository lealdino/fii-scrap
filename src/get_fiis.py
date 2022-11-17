import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np
import yfinance as yf
from datetime import  datetime
from datetime import timedelta



def get_fiis():

    url = 'https://www.fundsexplorer.com.br/ranking'
    agent = {"User-Agent":"Mozilla/5.0"}
    resposta = requests.get(url, headers= agent)
    soup = BeautifulSoup(resposta.text, 'lxml')
    tabela = soup.find_all('table')[0]
    df = pd.read_html(str(tabela), decimal = ',', thousands= '.')[0]
    

    df['Preço Atual'] = df['Preço Atual'].str.replace('R','')
    df['Preço Atual'] = df['Preço Atual'].str.replace('$','')
    df['Preço Atual'] = df['Preço Atual'].str.replace('.','')
    df['Preço Atual'] = df['Preço Atual'].str.replace(',','.').astype(float)

    df['Dividendo'] = df['Dividendo'].str.replace('R','')
    df['Dividendo'] = df['Dividendo'].str.replace('$','')
    df['Dividendo'] = df['Dividendo'].str.replace('.','')
    df['Dividendo'] = df['Dividendo'].str.replace(',','.').astype(float)

    df['PatrimônioLíq.'] = df['PatrimônioLíq.'].str.replace('R','')
    df['PatrimônioLíq.'] = df['PatrimônioLíq.'].str.replace('$','')
    df['PatrimônioLíq.'] = df['PatrimônioLíq.'].str.replace('.','')
    df['PatrimônioLíq.'] = df['PatrimônioLíq.'].str.replace(',','.').astype(float)

    df['VPA'] = df['VPA'].str.replace('R','')
    df['VPA'] = df['VPA'].str.replace('$','')
    df['VPA'] = df['VPA'].str.replace('.','')
    df['VPA'] = df['VPA'].str.replace(',','.').astype(float)

    #DY 3 Acumulado
    df['DY (3M)Acumulado'] = df['DY (3M)Acumulado'].str.replace(',','.')
    df['DY (3M)Acumulado'] = df['DY (3M)Acumulado'].str.replace('%','').astype(float)

    df['DY (6M)Acumulado'] = df['DY (6M)Acumulado'].str.replace(',','.')
    df['DY (6M)Acumulado'] = df['DY (6M)Acumulado'].str.replace('%','').astype(float)

    df['DY (12M)Acumulado'] = df['DY (12M)Acumulado'].str.replace(',','.')
    df['DY (12M)Acumulado'] = df['DY (12M)Acumulado'].str.replace('%','').astype(float)

    df['DY (3M)Média'] = df['DY (3M)Média'].str.replace(',','.')
    df['DY (3M)Média'] = df['DY (3M)Média'].str.replace('%','').astype(float)

    df['DY (6M)Média'] = df['DY (6M)Média'].str.replace(',','.')
    df['DY (6M)Média'] = df['DY (6M)Média'].str.replace('%','').astype(float)

    df['DY Ano'] = df['DY Ano'].str.replace(',','.')
    df['DY Ano'] = df['DY Ano'].str.replace('%','').astype(float)

    df['Variação Preço'] = df['Variação Preço'].str.replace(',','.')
    df['Variação Preço'] = df['Variação Preço'].str.replace('%','').astype(float)
    df['DividendYield'] = df['DividendYield'].str.replace(',','.')
    df['DividendYield'] = df['DividendYield'].str.replace('%','').astype(float)

    df['Rentab.Período'] = df['Rentab.Período'].str.replace('.','')
    df['Rentab.Período'] = df['Rentab.Período'].str.replace(',','.')
    df['Rentab.Período'] = df['Rentab.Período'].str.replace('%','').astype(float)

    df['Rentab.Acumulada'] = df['Rentab.Acumulada'].str.replace('.','')
    df['Rentab.Acumulada'] = df['Rentab.Acumulada'].str.replace(',','.')
    df['Rentab.Acumulada'] = df['Rentab.Acumulada'].str.replace('%','').astype(float)

    df['DYPatrimonial'] = df['DYPatrimonial'].str.replace(',','.')
    df['DYPatrimonial'] = df['DYPatrimonial'].str.replace('%','').astype(float)

    df['VariaçãoPatrimonial'] = df['VariaçãoPatrimonial'].str.replace(',','.')
    df['VariaçãoPatrimonial'] = df['VariaçãoPatrimonial'].str.replace('%','').astype(float)

    df['Rentab. Patr.no Período'] = df['Rentab. Patr.no Período'].str.replace(',','.')
    df['Rentab. Patr.no Período'] = df['Rentab. Patr.no Período'].str.replace('%','').astype(float)

    df['VacânciaFinanceira'] = df['VacânciaFinanceira'].str.replace(',','.')
    df['VacânciaFinanceira'] = df['VacânciaFinanceira'].str.replace('%','').astype(float)

    df['VacânciaFísica'] = df['VacânciaFísica'].str.replace(',','.')
    df['VacânciaFísica'] = df['VacânciaFísica'].str.replace('%','').astype(float)

    df['Rentab. Patr.Acumulada'] = df['Rentab. Patr.Acumulada'].str.replace('.','')
    df['Rentab. Patr.Acumulada'] = df['Rentab. Patr.Acumulada'].str.replace(',','.')
    df['Rentab. Patr.Acumulada'] = df['Rentab. Patr.Acumulada'].str.replace('%','').astype(float)


    df['DY (12M)Média'] = df['DY (12M)Média'].str.replace('.','')
    df['DY (12M)Média'] = df['DY (12M)Média'].str.replace(',','.')
    df['DY (12M)Média'] = df['DY (12M)Média'].str.replace('%','').astype(float)

    
    return df