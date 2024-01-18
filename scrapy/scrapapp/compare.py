import pandas as pd


poke = pd.read_csv("D:\\scrapy\\scrapy\\scrapapp\\excel\\namelist.csv")

# for read a particular column
# for index, row in poke.iterrows():
#     print(row[['Name','State','Country']])


data_in_file = poke.loc[poke['Name']=='sany']
# name_in_file = data_in_file['Name'].values[0]
# state_in_file = data_in_file['State'].values[0]
# country_in_file = data_in_file['Country'].values[0]
if data_in_file.empty:
    print("empty")
else:
    print("code issue")