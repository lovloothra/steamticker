#Steam Ticker Lib - Lov Loothra

import urllib2
import re

def read_names(src):
    return re.findall('class=\\\\"market_listing_item_name\\\\" style=\\\\"color: #;\\\\">(.*?)<\\\\/span>', src)

def read_prices(src):
    return re.findall('&#36;(.*?) USD', src)

def get_prices(query):
    query = query.replace(" ", "+").replace("&", "%26").replace("(", "%28").replace(")", "%29")
    src = urllib2.urlopen("http://steamcommunity.com/market/search/render/?query={0}&start=0".format(query)).read()
    return zip(read_names(src), read_prices(src))

def get_price(query):
    try:
        return get_prices(query)[0][1]
    except:
        return False
