import requests

URL = "https://catalog.onliner.by/sdapi/catalog.api/search/dram"
PARAMS = {"group": 0, "group_limit": 0, "limit": 30, "dramkit[0]": "ddr4dimm", "dramkit[1]": "ddr4sodimm", "dramkit[operation]": "union"}

data = requests.get(URL, params=PARAMS).json()

items = []
for product in data['products']:
    gb = product['description_list'][0]
    gb = gb.replace(" ГБ", "")
    items.append({"name":product['html_url'], "price": product['prices']['price_min']['amount'], "gb": gb, "desc": {product['description_list'][0]}})

items.sort(key=lambda item: float(item['price']))

prices = []
for item in items:
    prices.append({"url": item['name'], 'price': (float(item['price'])/float(item['gb'])), "desc": item['desc']})

prices.sort(key=lambda item: float(item['price']))

