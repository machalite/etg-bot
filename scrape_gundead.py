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

list_gundead = []
url = config.get('URL', 'gundead')
print("Begin scraping " + url)
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
trs = soup.find_all('tr')

for index, tr in enumerate(trs):
    if index == 0:
        continue
    tds = tr.find_all('td')
    if len(tds) < 3:
        break
    img = tds[0].find('img')
    image = str(img.get('src'))
    name = str.strip(str(tds[1].text))
    base_health = str.strip(str(tds[2].text))
    description = str.strip(
        str(tds[3].text.replace(u'\u03a6', '').replace(u'\xd7', '')))

    list_gundead.append({
        'image': image,
        'name': name,
        'base_health': base_health,
        'description': description
    })

print("Scraped " + str(len(list_gundead)) + " item(s)...")

count_ins = 0
count_upd = 0
for item in list_gundead:
        cursor = db.gundead.find({'name': item.get('name')})
        if cursor.count() == 0:
            db.gundead.insert_one(item)
            count_ins += 1
        else:
            cursor = list(cursor)[0]
            cursor.pop('_id')
            if item != cursor:
                db.gundead.update_one({"name": item.get('name')}, {
                    "$set": {
                        'image': item.get('image'),
                        'base_health': item.get('base_health'),
                        'description': item.get('description')
                    }
                })
            count_upd += 1

print("Inserted " + str(count_ins) + " item(s)")
print("Updated " + str(count_upd) + " item(s)")
# for gundead in list_gundead:
#     pprint(gundead)
