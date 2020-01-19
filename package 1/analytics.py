import pandas as pd
import numpy as np
import matplotlib.pylab as plt


def graphic_1(df, col1):
    graphic_1 = df[col1].hist(bins=100, figsize=(16,8))
    plt.xlabel('Position')
    plt.ylabel('Wealth')
    plt.title("Wealth distribution.png")
    plt.show()
    plt.close()
    plt.savefig("Wealth distribution.png")

def graphic_2(df, list_of_columns):
    graphic_2 = df.plot(list_of_columns[0], list_of_columns[1], kind="scatter")
    plt.show()
    plt.close()
    plt.savefig("Scatter Wealth distribution.png")


def graphic_3(df, col1, col3):
    graphic_3 = df.plot(col1, col3, kind="scatter")
    plt.show()
    plt.close()
    plt.savefig("Scatter worth change.png")


def graphic_4(df, col4, col5):
    graphic_4 = df.groupby(col4)[col5].sum().sort_values(ascending=False)/100
    gender = ['Male', 'Female', 'None']
    colors = ['skyblue', 'grey', 'white']
    graphic_4.plot(kind='pie', labels = gender, colors = colors, startangle=45, shadow=False, figsize=(16,8),  autopct='%.2f%%')
    plt.title('Wealth comparison between genders')
    plt.show()
    plt.close()
    plt.savefig("Wealth comparison between genders.png")

list_of_columns = ['position', 'worth BUSD', " worthChange millions USD", 'gender', 'country']
def analysis(df, list_of_columns):
    graphic_1(df, list_of_columns[1])
    graphic_2(df, list_of_columns[0], list_of_columns[1])
    graphic_3(df, 'position', " worthChange millions USD")
    graphic_4(df, 'gender', 'country')

