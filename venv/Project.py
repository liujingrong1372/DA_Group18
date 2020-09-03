import pandas as pd
import xlrd
import matplotlib.pyplot as plt
import numpy

country = [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]  # To call out the whole countries of Europe which consist of 11 columns
row = [121]  # Start reading the excel file from row 241
df = pd.read_excel('IMVA.xlsx', sheet_name='IMVA', usecols=country)  # to read the excel file
pd.set_option('display.max_columns', 29)  # to preview the whole 18 columns, if delete there will be semi colons
pd.set_option('display.max_rows', 241)  # to preview the whole of 241 rows, if delete it wont preview the whole 241 rows

ranges = (df.iloc[121:241, :29])  # start from rows 121 to 241 and from column 19 to 29
calculated = (df.iloc[121:241, :29].sum(axis=0))  # Sum of whole value from 121-241 & from column 19-29
top3 = (df.iloc[121:241, :29].sum(axis=0).nlargest(3))  # Print out top 3 largest value country using n.largest

print(ranges)
print(calculated)
print(top3.index)

ax = calculated[[' United Kingdom ', ' Germany ', ' Scandinavia ']].plot(kind='bar', title="Top 3 Country In Europe", figsize=(10,10), legend=True, fontsize=12)


plt.show()


