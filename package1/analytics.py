import pandas as pd
import numpy as np
import matplotlib.pylab as plt


def graphic_1(df):
    graphic_1 = df['worth BUSD'].hist(bins=100, figsize=(16,8))
    plt.xlabel('Position')
    plt.ylabel('Wealth')
    plt.title("Wealth distribution.png")
    plt.show()
    plt.close()
    plt.savefig("Wealth distribution.png")

def graphic_2(df):
    colors = ['grey', 'mediumvioletred', 'gold', 'orangered', 'yellowgreen', 'r', 'skyblue', 'navy', 'grey', 'black']
    df['country'].value_counts()[:15].plot(kind='bar', width=0.9, figsize=(20, 10), color=colors)
    plt.xlabel('Country (Top 30)')
    plt.ylabel('Number of billionaires')
    plt.title('Number of billionaires per country')
    plt.savefig("Billionaires - Countries")
    plt.savefig("Number of billionaires per country")
    plt.show()
    plt.close()
    plt.savefig("Number of billionaires per country.png")

def analysis(df):
    graphic_1(df)
    graphic_2(df)


