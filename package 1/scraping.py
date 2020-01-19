import pandas as pd
import os
import requests
from bs4 import BeautifulSoup
import re


def web_scraping(url):
    html = requests.get(url).content
    soup = BeautifulSoup(html, "lxml")
    table = soup.find_all('table',{'class':'wikitable sortable mw-datatable'})[0]
    rows = table.find_all('tr')
    rows_parsed = [row.text for row in rows]
    return rows_parsed

def smart_parser(row_text):
    row_text = row_text.replace('\nPopulation\n\n\n', '\nPopulation\n').strip('\n')
    row_text = row_text.replace('\n\n', '\n').strip('\n')
    row_text = row_text.replace('\nPopulation\n% of World\n', '\nPopulation % of World\n').strip('\n')
    row_text = re.sub('\[\d\]', '', row_text)
    return list(map(lambda x: x.strip(), row_text.split('\n')))

def scraping_df(data,colnames):
    df_scrapping = pd.DataFrame(data, columns=colnames)
    df_scrapping['Country(or dependent territory)']=df_scrapping['Country(or dependent territory)'].replace(['\[(.*?)\]','\(([^\)]+)\)'], ['',''], regex=True)
    df_scrapping.columns = ['Rank', 'country','Population',' % of World Population','Date','Source']
    return df_scrapping

def merge_scraping_df(df1,df2,column):
    df_project2=df1.merge(df2, on=column)
    return df_project2

def scrap(df,url):
    rows_dirt = web_scraping(url)
    well_parsed = list(map(lambda x: smart_parser(x), rows_dirt))
    name_columns = well_parsed[0]
    data_scraped = well_parsed[1:]
    df_scrap= scraping_df(data_scraped,name_columns)
    df_final = merge_scraping_df(df,df_scrap,'country')
    return df_final

