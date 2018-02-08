def save_gun(conn, list_gun, coll_name):
    print("Saving guns...")
    count_ins = 0
    count_upd = 0
    for item in list_gun:
            cursor = conn[coll_name].find({'name': item.get('name')})
            if cursor.count() == 0:
                conn[coll_name].insert_one(item)
                count_ins += 1
            else:
                cursor = list(cursor)[0]
                cursor.pop('_id')
                if item != cursor:
                    conn[coll_name].update_one({"name": item.get('name')}, {
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
                            'notes': item.get('notes'),
                            'class': "Gun"
                        }
                    })
                count_upd += 1

    print("Inserted " + str(count_ins) + " gun(s)")
    print("Updated " + str(count_upd) + " gun(s)\n")


def save_item(conn, list_item, coll_name):
    print("Saving items...")
    count_ins = 0
    count_upd = 0
    for item in list_item:
            cursor = conn[coll_name].find({'name': item.get('name')})
            if cursor.count() == 0:
                conn[coll_name].insert_one(item)
                count_ins += 1
            else:
                cursor = list(cursor)[0]
                cursor.pop('_id')
                if item != cursor:
                    conn[coll_name].update_one({"name": item.get('name')}, {
                        "$set": {
                            'image': item.get('image'),
                            'quote': item.get('quote'),
                            'quality': item.get('quality'),
                            'type': item.get('type'),
                            'effect': item.get('effect'),
                            'class': "Item"
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
            cursor = conn[coll_name].find({'name': item.get('name')})
            if cursor.count() == 0:
                conn[coll_name].insert_one(item)
                count_ins += 1
            else:
                cursor = list(cursor)[0]
                cursor.pop('_id')
                if item != cursor:
                    conn[coll_name].update_one({"name": item.get('name')}, {
                        "$set": {
                            'image': item.get('image'),
                            'base_health': item.get('base_health'),
                            'description': item.get('description'),
                            'class': "Gundead"
                        }
                    })
                count_upd += 1

    print("Inserted " + str(count_ins) + " gundead(s)")
    print("Updated " + str(count_upd) + " gundead(s)\n")
