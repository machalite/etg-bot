import requests
# from pprint import pprint
from bs4 import BeautifulSoup
from pymongo import MongoClient

# MONGO_USERNAME = 'root'
# MONGO_PASSWORD = ''

connection = MongoClient('localhost', 27017)
db = connection['gungeon']
# # db.authenticate(MONGO_USERNAME, MONGO_PASSWORD)

list_gundead = []
page = requests.get("https://enterthegungeon.gamepedia.com/Cult_of_the_Gundead")
soup = BeautifulSoup(page.content, 'html.parser')
trs = soup.find_all('tr')

for index, tr in enumerate(trs):
    if index == 0:
        continue
    tds = tr.find_all('td')
    if len(tds) < 3:
        break
    name = str.strip(str(tds[1].text))
    base_health = str.strip(str(tds[2].text))
    description = str.strip(str(tds[3].text.replace(u'\u03a6', '').replace(u'\xd7', '')))

    list_gundead.append({
        'name': name,
        'base_health': base_health,
        'description': description
    })

for item in list_gundead:
        cursor = db.gundead.find({'name': item.get('name')})
        if cursor.count() == 0:
            db.gundead.insert_one(item)
        else:
            # print "berhasil"
            cursor = list(cursor)[0]
            cursor.pop('_id')
            if item != cursor:
                db.gundead.update_one({"name": item.get('name')}, {
                    "$set": {
                        'base_health': item.get('base_health'),
                        'description': item.get('description')
                    }
                })

# for gundead in list_gundead:
#     pprint(gundead)
