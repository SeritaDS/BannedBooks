
# Import pandas library
import pandas as pd
import matplotlib.pyplot as plt


pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 10)


# read dataset from excel
bannedbooks= pd.read_excel("banned_books.xlsx")

# Create the pandas DataFrame with column name is provided explicitly
# print dataframe
print(bannedbooks)

