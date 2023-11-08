import requests
from bs4 import BeautifulSoup
import datetime
import pandas as pd
import sqlite3

url = 'https://coinmarketcap.com/'

session = requests.session()
response = session.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

result = []
rank = soup.select('.cmc-table__cell--sort-by__rank > div')
name = soup.select('.cmc-table__cell--left.cmc-table__cell--sort-by__name > div')
price = soup.select('.cmc-table__cell--sort-by__price > a')
change = soup.select('.cmc-table__cell--sort-by__percent-change-24-h > div')
market_cap = soup.select('.cmc-table__cell--sort-by__market-cap > div')
volume = soup.select('.cmc-table__cell--right.cmc-table__cell--sort-by__volume-24-h > a')
for i in zip(rank, name, price, change, market_cap, volume):
    result.append(
        {
            'rank': i[0].text,
            'name': i[1].text,
            'price': i[2].text,
            'change': i[3].text,
            'market_cap': i[4].text,
            'volume': i[5].text,
            'reg_date': datetime.datetime.now()
        }
    )

    
df = pd.DataFrame(result)


conn = sqlite3.connect('c:/python_class/hello_db.db')

df.to_sql('coinmarketcap_new', conn, if_exists='append', index=False)

conn.close()
