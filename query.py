from pymongo import MongoClient
import ConfigParser
import pprint

config = ConfigParser.ConfigParser()
config.read("scrape.conf")
MONGO_USERNAME = config.get('database', 'username')
MONGO_PASSWORD = config.get('database', 'password')
MONGO_HOST = config.get('database', 'host')
MONGO_PORT = int(config.get('database', 'port'))
MONGO_DB_NAME = config.get('database', 'db_name')
MONGO_COLLECTION = config.get('database', 'collection_name')

# connection = MongoClient('localhost', 27017)
connection = MongoClient(MONGO_HOST, MONGO_PORT)
db = connection[MONGO_DB_NAME]
db.authenticate(MONGO_USERNAME, MONGO_PASSWORD)


def search_name(db, name):
    list_name = []
    result = db[MONGO_COLLECTION].find(
        {"name": {'$regex': name, '$options': 'i'}}, {"name": 1})
    for res in result:
        list_name.append(str(res['name']))
    return list_name


def search_gun(db, name):
    list_name = []
    result = db[MONGO_COLLECTION].find(
        {"name": {'$regex': name, '$options': 'i'}, "class": "Gun"},
        {"name": 1})
    for res in result:
        list_name.append(str(res['name']))
    return list_name


def search_item(db, name):
    list_name = []
    result = db[MONGO_COLLECTION].find(
        {"name": {'$regex': name, '$options': 'i'}, "class": "Item"},
        {"name": 1})
    for res in result:
        list_name.append(str(res['name']))
    return list_name


def search_gundead(db, name):
    list_name = []
    result = db[MONGO_COLLECTION].find(
        {"name": {'$regex': name, '$options': 'i'}, "class": "Gundead"},
        {"name": 1})
    for res in result:
        list_name.append(str(res['name']))
    return list_name


def get_details(db):
    name = raw_input("Search :")
    list_name = search_name(db, name)

    if(len(list_name) == 1):
        result = db[MONGO_COLLECTION].find({"name": list_name[0]})
        pprint.pprint(result)
    elif(len(list_name) <= 15):
        print "Found " + str(len(list_name)) + " item(s) that contains '" + name +"'"
        for name in list_name:
            print name
    else:
        print "Found " + str(len(list_name)) + " item(s)"
        print "Too many result. Please narrow down your search..."
#     print result
get_details(db)
# print list_name
