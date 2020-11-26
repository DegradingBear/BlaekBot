import requests
from bs4 import BeautifulSoup as bs

headers = {'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 OPR/71.0.3770.323"}

def geturl(url):
    html = requests.get(url, headers)
    html = bs(html.content, 'html.parser')
    html = html.find(class_="priceTable__shop")
    newUrl = html.find('a').get('href')
    return newUrl


def getPrice(name):
    name = "+".join(name.split(" "))
    url = f'https://isthereanydeal.com/search/?q={name}'
    html = requests.get(url, headers)
    html = bs(html.content, 'html.parser')
    newurl = f"https://isthereanydeal.com{html.find(class_='card__title').get('href')}"
    html = html.find_all(class_="card-container")[0]
    html = html.find_all(class_="card__row")[2]
    html = html.find_all(class_="numtag__primary")
    html = str(html).split('>')[1].split('<')[0].split('$')[1]
    price = float(html)
    return(price, geturl(newurl))