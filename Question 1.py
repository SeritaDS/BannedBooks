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

# Please provide a list of the top 3 banned books and how often they show up (percentage).

print(bannedBooks['authors'].value_counts().nlargest(3))
print("Percentage of Books")
bookOnePercent= (41/2552) * 100
print(bookOnePercent)
bookTwoPercent= (29/2552) * 100
print(bookTwoPercent)
bookThreePercent= (24/2552) * 100
print(bookThreePercent)
