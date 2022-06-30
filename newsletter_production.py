import finnhub
import csv, time #pip install finnhub-python
from datetime import datetime, date, timedelta

clients = {'binaghiignacio@gmail.com' : ['BTC-USD','ETH'] ,'thomasbinaghi@gmail.com' : ['BTC-USD', 'AAPL', 'BNB']} # Creating a database simulation


api_key = 'calsj2iad3ife6c6atu0'
finnhub_client = finnhub.Client(api_key)
all_news = finnhub_client.general_news('general', min_id=0)

most_recent_news = []
customized_news = []

"""
# Retrieving all news
for i in all_news:
    most_recent_news.append([i["headline"], i['image'], i['summary'], i['url']]) # Retrieving key information

for i in most_recent_news[:4]: # Only outputting the necessary information seperated
    for x in i:
        print(x)
    print(' ')
"""
today = date.today() # Getting Today's Date
yesterday = str(datetime.today() - timedelta(days=1))[:10] # Getting Yesterday's date

for email,assets in clients.items(): # Iterating through client emails and assets
    total_custom_news = []
    for i in assets:
        print(i)
        custom_news = finnhub_client.company_news(i, _from=yesterday, to=today)[:2] # Getting asset info from the last 24 hrs and only adding 2 of each source
        for i in custom_news:
           total_custom_news.append([i["headline"], i['image'], i['summary'], i['url']]) # Appending news information by each asset

            # Thomas i know it looks weird that their assets show up with the last included but its on purpose bc its incrementing
    print(total_custom_news)