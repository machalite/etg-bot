import requests
# from pprint import pprint
from bs4 import BeautifulSoup
from pymongo import MongoClient

# MONGO_USERNAME = 'root'
# MONGO_PASSWORD = ''

MONGO_USERNAME = 'heroku_m8nk6xx5'
MONGO_PASSWORD = 'fi03i0rubg1i7l94pk05iegn5b'
connection = MongoClient('ds113358.mlab.com', 13358)
db = connection['heroku_m8nk6xx5']

# connection = MongoClient('localhost', 27017)
# db = connection['gungeon']
db.authenticate(MONGO_USERNAME, MONGO_PASSWORD)

list_item = []
url = "https://enterthegungeon.gamepedia.com/Items"
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
                        'image': item.get('image'),
                        'quote': item.get('quote'),
                        'quality': item.get('quality'),
                        'type': item.get('type'),
                        'effect': item.get('effect')
                    }
                })

print("Scraped " + str(len(list_item)) + " item(s)")
# for item in list_item:
#     pprint(item)
