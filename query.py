from pymongo import MongoClient
import configparser
import pdb
import pprint

config = configparser.ConfigParser()
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


def search_name(name):
    list_name = []
    result = db[MONGO_COLLECTION].find(
        {"name": {'$regex': name, '$options': 'i'}}, {"name": 1})
    for res in result:
        list_name.append(str(res['name']))
    return list_name


def search_gun(name):
    list_name = []
    result = db[MONGO_COLLECTION].find(
        {"name": {'$regex': name, '$options': 'i'}, "class": "Gun"},
        {"name": 1})
    for res in result:
        list_name.append(str(res['name']))
    return list_name


def search_item(name):
    list_name = []
    result = db[MONGO_COLLECTION].find(
        {"name": {'$regex': name, '$options': 'i'}, "class": "Item"},
        {"name": 1})
    for res in result:
        list_name.append(str(res['name']))
    return list_name


def search_gundead(name):
    list_name = []
    result = db[MONGO_COLLECTION].find(
        {"name": {'$regex': name, '$options': 'i'}, "class": "Gundead"},
        {"name": 1})
    for res in result:
        list_name.append(str(res['name']))
    return list_name

def get_results(list_name):
    if(len(list_name) == 1):
        result = db[MONGO_COLLECTION].find_one({"name": list_name[0]})
        return result

    elif(len(list_name) <= 15):
        print ("Found " + str(len(list_name)) + " item(s) that contains '" + name +"'")
        for name in list_name:
            print (name)
    else:
        print ("Found " + str(len(list_name)) + " item(s)")
        print ("Too many result. Please narrow down your search...")


# def get_details():
#     name = raw_input("Search :")
#     list_name = search_name(name)
#
#     if(len(list_name) == 1):
#         result = db[MONGO_COLLECTION].find_one({"name": list_name[0]})
#         # pdb.set_trace()
#         # pprint.pprint(result)
#
#     elif(len(list_name) <= 15):
#         print ("Found " + str(len(list_name)) + " item(s) that contains '" + name +"'")
#         for name in list_name:
#             print (name)
#     else:
#         print ("Found " + str(len(list_name)) + " item(s)")
#         print ("Too many result. Please narrow down your search...")
# #     print result
# get_details()
# print list_name
