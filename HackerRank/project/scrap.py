from bs4 import BeautifulSoup
import requests
url = 'https://www.swiggy.com/order-online-near-me'
response = requests.get(url)
html_taxt = response.content
soup = BeautifulSoup(html_taxt, 'lxml')
hotel = soup.find('a','RestaurantList__RestaurantAnchor-sc-1d3nl43-3 kcEtBq')
name = hotel.find('div','sc-beySbM eLaouz').get_taxt()
category = hotel.find('div','sc-beySbM BEWkR').get_text()
otheronfo = hotel.find('div','sw-restaurant-card-subtext-container').get_taxt()
print(otherinfo)
