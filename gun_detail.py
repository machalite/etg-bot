import requests
from bs4 import BeautifulSoup
page = requests.get("https://enterthegungeon.gamepedia.com/Marine_Sidearm")

list_gun = []

soup = BeautifulSoup(page.content, 'html.parser')
tds = soup.find_all('td')

image = str(list(tds)[1])
gun_type = str(list(tds)[3].text)
q = list(tds)[5].find("img")
quality = q.get("alt")
# print quality
# quality = str(list(tds)[5])
magazine_size = str(list(tds)[7].text)
max_ammo = list(tds)[9]
max_ammo.find("")
print max_ammo
reload_time = str(list(tds)[11].text)
dps = str(list(tds)[13].text)
damage = str(list(tds)[15].text)
fire_rate = str(list(tds)[17].text)
shot_speed = str(list(tds)[19].text)
shot_range = str(list(tds)[21].text)
force = str(list(tds)[23].text)
spread = list(tds)[25].text
sell_price = str(list(tds)[27])
description = str.strip(str(list(tds)[29].text))

list_gun.append({
# 'name' : name,
'type' : gun_type,
'quality' : quality,
'magazine_size' : magazine_size,
'max_ammo' : max_ammo,
'reload_time' : reload_time,
'damage' : damage,
'shot_speed' : shot_speed,
'range' : shot_range,
'force' : force,
'spread' : spread,
'image' : image,
'description' : description,
'dps' : dps,
'fire_rate' : fire_rate,
'sell_price' : sell_price
})
