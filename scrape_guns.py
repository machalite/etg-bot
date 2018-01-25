import requests
# from pprint import pprint
from bs4 import BeautifulSoup
from pymongo import MongoClient

MONGO_USERNAME = 'heroku_m8nk6xx5'
MONGO_PASSWORD = 'fi03i0rubg1i7l94pk05iegn5b'
connection = MongoClient('ds113358.mlab.com', 13358)
db = connection['heroku_m8nk6xx5']

# connection = MongoClient('localhost', 27017)
# db = connection['gungeon']

db.authenticate(MONGO_USERNAME, MONGO_PASSWORD)

list_gun = []
url = "https://enterthegungeon.gamepedia.com/Guns"
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

for item in list_gun:
        cursor = db.gun.find({'name': item.get('name')})
        if cursor.count() == 0:
            db.gun.insert_one(item)
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

print("Scraped " + str(len(list_gun)) + " item(s)")
# for gun in list_gun:
#     pprint(gun)
