# -*- coding: utf-8 -*-

#
import json
import requests
import urllib2
from bs4 import BeautifulSoup

page = requests.get('https://www.wsj.com/')
soup = BeautifulSoup(page.text, 'html.parser')

popular_items_list = soup.find(class_="wsj-popular-container space-bottom-large")
headline_items = popular_items_list.find_all('a')


li = []
for headline_name in headline_items:
     text = headline_name.text
     link = headline_name.get('href')
     all_items = text + ", " + link
     li.append(all_items)
#
# with open('data.txt', 'w') as outfile:
#     json.dump(li, outfile)




import json
file = open("filename.json", "w")
output = {"filename": li}
json.dump(output, file)
file.close()

# import requests
# from bs4 import BeautifulSoup
#
# wsj_site = 'https://www.wsj.com/'
#
# page = requests.get(wsj_site)
#
# soup = BeautifulSoup(page, 'html.parser')
#
# # popular_items_list = soup.find(class_="clearfix wsj_popular_item")
# # headline_items = popular_items_list.find_all('a')
# #
# # for headline_name in headline_items:
# #     print(headline_name.prettify())
#
#
# headline_name = soup.find('div', attrs={'class': 'wsj-popular-container space-bottom-large'})
# headline = headline_name.text
# headlineFinal = headline
# print (headline.prettify())
#
#
