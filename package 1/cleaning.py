import pandas as pd
import numpy as np
import datetime

def drop(df, list_of_columns):
    df1 = df.drop(list_of_columns, axis=1)
    return df1

def repla_cols(df, col1, col2):
    df[col1].replace({"BUSD": ' '})
    df[col2].replace('na', '0.0', regex=True, inplace=True)
    df[col1].replace('[BUSD]+$', '', regex=True, inplace=True)
    df[col2].replace('[millions USD]+$', '', regex=True, inplace=True)
    df[col2].astype('float').astype('int')
    df[col2].astype('float').astype('int')
    return df

def rename2(df):
    df2 = df.rename(columns={'worth':'worth BUSD', 'worthChange':' worthChange millions USD'})
    return df2

def wrangling_gender(df, column):
    df[column].replace('[M]+$', 'Male', regex=True, inplace=True)
    df[column].replace('[F]+$', 'Female', regex=True, inplace=True)
    df[column].astype('object').astype('str')
    return df


def age_wrangling(df, column):
    df[column].replace('[years old]+$', '', regex=True, inplace=True)
    df[column].fillna(str(-2019), inplace=True)
    current_year = datetime.datetime.today().year
    age = []
    for i in df[column]:
        if len(str(i)) == 4:
            age.append(str(current_year - int(i)))
        else:
            age.append(i)
    df[column] = age
    return df

def non_values(df, column):
    df[column].replace('None', np.nan, regex=True, inplace=True)
    df2 = df.drop(df[df[column].isnull()].index).reset_index(drop=True)
    return df2

def capitalize_column(df):
    df1 = df.apply(lambda x: x.astype(str).str.capitalize())
    return df1

def clean(df,list_of_columns):
    df_drop = drop(df, list_of_columns)
    df_replace = repla_cols(df_drop, 'worth', 'worthChange')
    df_rename = rename2(df_replace)
    df_wrangling_gender = wrangling_gender(df_rename, 'gender')
    df_wrangling_age = age_wrangling(df_wrangling_gender,'age')
    df_wrangling_country = non_values(df_wrangling_age, 'country')
    df_capitalize = capitalize_column(df_wrangling_country)
    return df_capitalize
