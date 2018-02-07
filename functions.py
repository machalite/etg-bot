import requests
# from pprint import pprint
from bs4 import BeautifulSoup


def scrape_gun(url):
    list_gun = []
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

    print("Scraped " + str(len(list_gun)) + " gun(s)\n")
    return list_gun


def scrape_item(url):
    list_item = []
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

    print("Scraped " + str(len(list_item)) + " item(s)\n")
    return list_item


def scrape_gundead(url):
    list_gundead = []
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

    print("Scraped " + str(len(list_gundead)) + " gundead(s)\n")
    return list_gundead


def save_gun(conn, list_gun):
    print("Saving guns...")
    count_ins = 0
    count_upd = 0
    for item in list_gun:
            # collection name: gun
            cursor = conn.gun.find({'name': item.get('name')})
            if cursor.count() == 0:
                conn.gun.insert_one(item)
                count_ins += 1
            else:
                cursor = list(cursor)[0]
                cursor.pop('_id')
                if item != cursor:
                    conn.gun.update_one({"name": item.get('name')}, {
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

    print("Inserted " + str(count_ins) + " gun(s)")
    print("Updated " + str(count_upd) + " gun(s)\n")


def save_item(conn, list_item):
    print("Saving items...")
    count_ins = 0
    count_upd = 0
    for item in list_item:
            # collection name: item
            cursor = conn.item.find({'name': item.get('name')})
            if cursor.count() == 0:
                conn.item.insert_one(item)
                count_ins += 1
            else:
                cursor = list(cursor)[0]
                cursor.pop('_id')
                if item != cursor:
                    conn.item.update_one({"name": item.get('name')}, {
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
    print("Updated " + str(count_upd) + " item(s)\n")


def save_gundead(conn, list_gundead):
    print("Saving gundeads...")
    count_ins = 0
    count_upd = 0
    for item in list_gundead:
            # collection name: gundead
            cursor = conn.gundead.find({'name': item.get('name')})
            if cursor.count() == 0:
                conn.gundead.insert_one(item)
                count_ins += 1
            else:
                cursor = list(cursor)[0]
                cursor.pop('_id')
                if item != cursor:
                    conn.gundead.update_one({"name": item.get('name')}, {
                        "$set": {
                            'image': item.get('image'),
                            'base_health': item.get('base_health'),
                            'description': item.get('description')
                        }
                    })
                count_upd += 1

    print("Inserted " + str(count_ins) + " gundead(s)")
    print("Updated " + str(count_upd) + " gundead(s)\n")
