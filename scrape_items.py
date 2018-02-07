import requests
# from pprint import pprint
from bs4 import BeautifulSoup
from pymongo import MongoClient
import ConfigParser

config = ConfigParser.ConfigParser()
config.read("scrape.conf")

# get mongodb connection from scrape.conf
MONGO_USERNAME = config.get('database', 'username')
MONGO_PASSWORD = config.get('database', 'password')
MONGO_HOST = config.get('database', 'host')
MONGO_PORT = int(config.get('database', 'port'))
MONGO_DB_NAME = config.get('database', 'db_name')

# connection = MongoClient('localhost', 27017)
connection = MongoClient(MONGO_HOST, MONGO_PORT)
db = connection[MONGO_DB_NAME]
db.authenticate(MONGO_USERNAME, MONGO_PASSWORD)

# begin scraping
list_item = []
url = config.get('URL', 'item')
print("Begin scraping " + url)
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
trs = soup.find_all('tr')

for index, tr in enumerate(trs):
    if index == 0:
        continue
    tds = tr.find_all('td')

    img = tds[0].find('img')
    image = str(img.get('src'))
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
        'image': image,
        'name': name,
        'quote': quote,
        'quality': quality,
        'type': type,
        'effect': effect
    })

print("Scraped " + str(len(list_item)) + " item(s)...")
print("Begin updating database...")

# begin updating database
count_ins = 0
count_upd = 0
for item in list_item:
        # collection name: item
        cursor = db.item.find({'name': item.get('name')})
        if cursor.count() == 0:
            db.item.insert_one(item)
            count_ins += 1
        else:
            cursor = list(cursor)[0]
            cursor.pop('_id')
            if item != cursor:
                db.item.update_one({"name": item.get('name')}, {
                    "$set": {
                        'image': item.get('image'),
                        'quote': item.get('quote'),
                        'quality': item.get('quality'),
                        'type': item.get('type'),
                        'effect': item.get('effect')
                    }
                })
            count_upd += 1

print("Inserted " + str(count_ins) + " item(s)")
print("Updated " + str(count_upd) + " item(s)")
# for item in list_item:
#     pprint(item)
