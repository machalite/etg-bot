import requests
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
            'class': "Gun"
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
            'effect': effect,
            'class': "Item"
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
            'description': description,
            "class": "Gundead"
        })

    print("Scraped " + str(len(list_gundead)) + " gundead(s)\n")
    return list_gundead
