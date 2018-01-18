import requests
# from pprint import pprint
from bs4 import BeautifulSoup
from pymongo import MongoClient

# MONGO_USERNAME = 'root'
# MONGO_PASSWORD = ''

connection = MongoClient('localhost', 27017)
db = connection['gungeon']
# db.authenticate(MONGO_USERNAME, MONGO_PASSWORD)

list_item = []
page = requests.get("https://enterthegungeon.gamepedia.com/Items")
soup = BeautifulSoup(page.content, 'html.parser')
trs = soup.find_all('tr')

for index, tr in enumerate(trs):
    if index == 0:
        continue
    tds = tr.find_all('td')

    name = str.strip(str(tds[1].text))
    type = str.strip(str(tds[2].text))
    quote = str.strip(str(tds[3].text))

    q = tds[4].find('img')
    quality = q.get("alt")
    if "S" in quality:
        quality = "S"
    elif "A" in quality:
        quality = "A"
    elif "B" in quality:
        quality = "B"
    elif "C" in quality:
        quality = "C"
    elif "D" in quality:
        quality = "D"
    else:
        quality = "-"

    effect = str.strip(str(tds[5].text))

    list_item.append({
        'name': name,
        'quote': quote,
        'quality': quality,
        'type': type,
        'effect': effect
    })

for item in list_item:
        cursor = db.item.find({'name': item.get('name')})
        if cursor.count() == 0:
            db.item.insert_one(item)
        else:
            cursor = list(cursor)[0]
            cursor.pop('_id')
            if item != cursor:
                db.item.update_one({"name": item.get('name')}, {
                    "$set": {
                        'quote': item.get('quote'),
                        'quality': item.get('quality'),
                        'type': item.get('type'),
                        'effect': item.get('effect')
                    }
                })

# for item in list_item:
#     pprint(item)
