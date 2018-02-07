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
list_gun = []
url = config.get('URL', 'gun')
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
    quote = str.strip(str(tds[2].text.replace(u'\u2026', '')))

    q = tds[3].find('img')
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

    gun_type = str.strip(str(tds[4].text))
    magazine_size = str.strip(str(tds[5].text))

    ammo_capacity = str.strip(str(tds[6].text))
    if not ammo_capacity:
        ammo_capacity = "-"

    damage = str.strip(str(tds[7].text))
    fire_rate = str.strip(str(tds[8].text))
    reload_time = str.strip(str(tds[9].text))
    shot_speed = str.strip(str(tds[10].text))
    shot_range = str.strip(str(tds[11].text))
    force = str.strip(str(tds[12].text))
    spread = str.strip(str(tds[13].text))
    notes = str.strip(str(tds[14].text))

    list_gun.append({
        'image': image,
        'name': name,
        'quote': quote,
        'quality': quality,
        'type': gun_type,
        'magazine_size': magazine_size,
        'ammo_capacity': ammo_capacity,
        'damage': damage,
        'fire_rate': fire_rate,
        'reload_time': reload_time,
        'shot_speed': shot_speed,
        'range': shot_range,
        'force': force,
        'spread': spread,
        'notes': notes,
    })

print("Scraped " + str(len(list_gun)) + " item(s)...")

# begin updating database
count_ins = 0
count_upd = 0
for item in list_gun:
        # collection name: gun
        cursor = db.gun.find({'name': item.get('name')})
        if cursor.count() == 0:
            db.gun.insert_one(item)
            count_ins += 1
        else:
            cursor = list(cursor)[0]
            cursor.pop('_id')
            if item != cursor:
                db.gun.update_one({"name": item.get('name')}, {
                    "$set": {
                        'image': item.get('image'),
                        'quote': item.get('quote'),
                        'quality': item.get('quality'),
                        'type': item.get('type'),
                        'magazine_size': item.get('magazine_size'),
                        'ammo_capacity': item.get('ammo_capacity'),
                        'damage': item.get('damage'),
                        'fire_rate': item.get('fire_rate'),
                        'reload_time': item.get('reload_time'),
                        'shot_speed': item.get('shot_speed'),
                        'range': item.get('range'),
                        'force': item.get('force'),
                        'spread': item.get('spread'),
                        'notes': item.get('notes')
                    }
                })
            count_upd += 1

print("Inserted " + str(count_ins) + " item(s)")
print("Updated " + str(count_upd) + " item(s)")
# for gun in list_gun:
#     pprint(gun)
