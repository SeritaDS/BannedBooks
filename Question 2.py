# Import pandas library
import pandas as pd
import matplotlib.pyplot as plt


pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 10)


# read dataset from excel
bannedBooks= pd.read_excel("banned_books.xlsx")

# Create the pandas DataFrame with column name is provided explicitly
# print dataframe
print(bannedBooks)

# Organize the data as a LINEAR scatterplot by year and type of Ban
bannedBooks.plot.scatter(x='type_of_ban',y='date_of_challenge_removal',c='DarkBlue')
plt.show()