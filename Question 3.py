# Import pandas library
import pandas as pd
import matplotlib.pyplot as plt


pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 10)


# read dataset from excel
bannedBooks = pd.read_excel("banned_books.xlsx")

# Create the pandas DataFrame with column name is provided explicitly
# print dataframe
print(bannedBooks)


# print the most unique entries in the banned books using the built in .unique function. 

print("Most Unique Titles found using .unique")
print(pd.unique(bannedBooks['title']))