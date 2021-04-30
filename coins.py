import requests
import app

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'b9c373fc-8124-41fb-8395-f389458efb7b',
}

params = {
  'start':'1',
  'limit':'100',
  'convert':'USD'
}

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'


json = requests.get(url, params=params, headers=headers).json()

coins = json['data']

items = []  #list of dictionaries containing real-time data from CoinMarketCap API

def up_down(percentage): #to showcase percentage-change with appropriate symbols
  if float(percentage) >= 0:
    return '▲ '+ str(percentage)
  elif float(percentage)< 0:
    return '▼ '+ str(percentage)[1:]

for objects in coins: #traversing through the json file and appending the dictionary containing necessary data to the items list
    items.append(
        {
            'rank': objects['cmc_rank'],
            'name': objects['name'],
            'symbol': objects['symbol'],
            'price': format(round(objects['quote']['USD']['price'],2) , ","),
            'percentage_change_1h_int': round(objects['quote']['USD']['percent_change_1h'], 2),
            'percentage_change_1h_str': up_down(round(objects['quote']['USD']['percent_change_1h'], 2)) ,
            'percentage_change_24h_int': round(objects['quote']['USD']['percent_change_24h'], 2),
            'percentage_change_24h_str': up_down(round(objects['quote']['USD']['percent_change_24h'], 2)),
            'percentage_change_7d_int': round(objects['quote']['USD']['percent_change_7d'], 2),
            'percentage_change_7d_str': up_down(round(objects['quote']['USD']['percent_change_7d'], 2)),
            'percentage_change_30d_int': round(objects['quote']['USD']['percent_change_30d'], 2),
            'percentage_change_30d_str': up_down(round(objects['quote']['USD']['percent_change_30d'], 2)),
            'percentage_change_60d_int': round(objects['quote']['USD']['percent_change_60d'], 2),
            'percentage_change_60d_str': up_down(round(objects['quote']['USD']['percent_change_60d'], 2)),
            'percentage_change_90d_int': round(objects['quote']['USD']['percent_change_90d'], 2),
            'percentage_change_90d_str': up_down(round(objects['quote']['USD']['percent_change_90d'], 2)),
            'market_cap_str': format((round((float(objects['quote']['USD']['market_cap'])/float(10**9)), 2)), ","),
            'market_cap_int': objects['quote']['USD']['market_cap'],
            'circulating_supply': format(objects['circulating_supply'], ",")
        }
    )

#To obtain the x and y values from the top 5 cryptocurrencies
labels1, values1, labels2, values2 = [],[],[],[]
for x1 in range(5):
    labels1.append(items[x1]['name'])
for y1 in range(5):
    values1.append(items[y1]['percentage_change_90d_int'])
for x2 in range(5):
    labels2.append(items[x2]['name'])
for y2 in range(5):
    values2.append(items[y2]['market_cap_int'])
