home = /usr/local/bin
include-system-site-packages = false
version = 3.7.3

import sqlite3
import pandas as pd

    def acquisition(file):
        sqlite3.connect('/Users/MIGUEL/Desktop/CLAB1/Ironhack-Module-1-Project---Pipelines-/data/raw/Miguel318.db')
        df_business_info = pd.read_sql_query("SELECT * FROM business_info", df)
        df_personal_info = pd.read_sql_query("SELECT * FROM personal_info", df)
        df_rank_info = pd.read_sql_query("SELECT * FROM rank_info", df)
        df = pd.merge(df_business_info, df_personal_info, on='id'), df_rank_info, on='id'))
        return df.to_csv(file)

    def reading_csv(df):
        df = pd.read_csv(df)
        return df

acquisition('df')

