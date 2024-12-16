from bs4 import BeautifulSoup
import pandas as pd
import requests

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')
print(soup)

soup.find('table')

soup.find_all('table', class_= 'wikitable sortable')

# there are 2 table, print the first one only
table = soup.find_all('table')[1]
print(table)

# storing header into world_titles
world_titles = table.find_all('th')

world_table_titles = [title.text.strip() for title in world_titles]
print(world_table_titles)

df = pd.DataFrame(columns = world_table_titles)

# extracting raw data
column_data = table.find_all('tr')

for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]

    length = len(df)
    df.loc[length] = individual_row_data

# putting data into actual csv file
# putting index = false to remove auto indexing while saving in csv format 
df.to_csv(r'<enter pathname>/<filename or folder name>.csv', index=Flase)
