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
