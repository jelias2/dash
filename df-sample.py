import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings("ignore", message="numpy.dtype size changed")
warnings.filterwarnings("ignore", message="numpy.ufunc size changed")

years=["1980","1981","1982","1983","1984","1985","1986","1987","1988","1989",'1990',"1991","1992","1993","1994","1995","1996","1997","1998","1999","2000",
"2001","2002","2003","2004","2005","2006","2007","2008","2009","2010"]


df = pd.read_csv('populationbycountry19802010millions.csv')
df.reset_index(inplace=True)
df.set_index("countries", inplace=True)
df.drop(["index"])
available_countries = df.index.unique()
#print available_countries
for country in available_countries:
    if country == "Vietnam":
        odf = df[df.index == "Vietnam"]
        print( odf.iloc[0,:])

    #trace = {'x': odf['YEAR'], 'y': odf['QUANTITY'], name=fund}
#print(df.index) ##prints out all the countries
# r = 0
# for counter ,value in enumerate( df.index) :
# #     if i == 'Sri Lanka':
# #         print (df.iloc[r,:])
# #     r += 1
#     print( counter)
#
# print(df.iloc[1,2])
# #print(df.rows)
