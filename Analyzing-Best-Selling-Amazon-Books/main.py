import pandas as pd

#data = pd.read_csv('bestsellers.csv')
data = pd.read_csv("Analyzing-Best-Selling-Amazon-Books/bestsellers.csv")

#Exploring the dataset

print(data.head()) #Displays the first 5 rows of the dataset

print(data.shape) #Displays the number of rows and columns in the dataset

print(data.columns) #Displays the column names in the dataset

print(data.describe()) #Displays summary statistics of the dataset

data.drop_duplicates(inplace=True)

#Renaming columns for better clarity
data.rename(columns={"Name": "Title", "Year": "Publication Year", "User Rating": "Rating"}, inplace=True)

#Converting Price Column to float
data['Price'] = data['Price'].astype(float) 

#Analyzing Author Popularity
author_counts = data['Author'].value_counts()
print("Most Popular Authors:\n", author_counts)

#Analyzing average rating by genre
average_rating_by_genre = data.groupby('Genre')['Rating'].mean()
print("Average Rating by Genre:\n", average_rating_by_genre)

#Export top selling authors to csv
author_counts.head(10).to_csv("top_authors.csv")

#Export average rating by genre to csv
average_rating_by_genre.to_csv('average_rating_by_genre.csv')

