import sqlite3
import pandas as pd


def read_sql_table(path,table):
    df = sqlite3.connect(path)
    df_table = pd.read_sql_query('SELECT * FROM '+table,df)
    return df_table

def read_and_merge(path):
    df_business_info = read_sql_table(path, 'business_info')
    df_personal_info = read_sql_table(path, 'personal_info')
    df_rank_info = read_sql_table(path, 'rank_info')
    df4 = pd.merge(df_business_info, df_personal_info, on=['id', 'id'])
    df_dirt = pd.merge(df4, df_rank_info, on=['id', 'id'])
    df_dirt.to_csv('/Users/MIGUEL/Desktop/CLAB1/Ironhack-Module-1-Project---Pipelines-/data/df_dirt.csv', index=False)
    return df_dirt

