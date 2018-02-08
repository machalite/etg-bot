from pymongo import MongoClient
import ConfigParser

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
    result = db['gun'].find({"name": {'$regex': name, '$options': 'i'}}, {"name": 1})
    for gun in result:
        list_name.append(str(gun['name']))
    return list_name


def get_details(db, list_name):
    if(len(list_name) == 1):
        result = db['gun'].find({"_id": id})
    print result

def search_item(db, name):
    list_name = []
    result = db['item'].find({"name": {'$regex': name, '$options': 'i'}}, {"name": 1})
    for gun in result:
        list_name.append(str(gun['name']))
    return list_name


name = raw_input("Search :")
list_name = search_name(db, name)
print list_name
