from adquisition import read_and_merge
from cleaning import clean
from scraping import scrap
from analytics import analysis

def main():
    df = read_and_merge('/Users/MIGUEL/Desktop/CLAB1/Ironhack-Module-1-Project---Pipelines-/data/raw/Miguel318.db')
    df_clean=clean(df,['id', 'realTimeWorth', 'Unnamed: 0', 'Unnamed: 0_x', 'Unnamed: 0_y', 'realTimePosition','lastName'])
    df_scrap = scrap(df_clean,'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population')
    analysis(df_scrap,['position', 'worth BUSD', " worthChange millions USD", 'gender', 'country'])


if __name__== '__main__':
    main()