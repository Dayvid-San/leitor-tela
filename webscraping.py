from dataclasses import field
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json


# 1. Pegar conteúdo HTML a partir da URL
url = "https://www.mlb.com/scores"
top10ranking = {}

rankings = {
    '3points': {'field': 'FG3M', 'label': '3PM'},
    'points': {'field': 'FG3M', 'label': '3PM'},
    '3points': {'field': 'FG3M', 'label': '3PM'},
    '3points': {'field': 'FG3M', 'label': '3PM'},
    '3points': {'field': 'FG3M', 'label': '3PM'},
    '3points': {'field': 'FG3M', 'label': '3PM'},
}

def buildrank(type):

    field = rankings[type]['field']
    label = rankings[type]['label']

    ## O cara que dá o click
    driver.find_element_by_xpath(f"Caminho das tags para executar o click")

    ## Pegano o elemento que queremos
    element = driver.find_element_by_xpath('elemento')
    html_content = element.get_attribute('outerHTML')

    print(html_content)


    # . Parsear o conteúdo HTML - BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.find(name='table')

    # . Estruturar conteúdo em um Data frame - Pandas
    df_full = pd.read_html( str(table) )[0].head(10)
    ## Limpando as colunas
    df = df_full[['Nome das colunas']]
    df.columns['Nome das colunas']

    # . Transformar os Dados em um Dicionário de dados próprio

    return df.to_dict('records')



option = Options()
option.headless = True
driver = webdriver.Edge("")

driver.get(url)
time.sleep(10)

for k in rankings:
    top10ranking[k] = buildrank(k)

print(html_content)

driver.quit()
# 5. Converter e salvar em um arquivo JSON
js = json.dumps(top10ranking)
fp = open('ranking.json', 'w')
fp.write(js)
fp.close()

