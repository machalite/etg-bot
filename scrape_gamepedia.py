from pymongo import MongoClient
import ConfigParser
import scrape_save
import scrape

config = ConfigParser.ConfigParser()
config.read("scrape.conf")

# get mongodb connection from scrape.conf
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

url_gun = config.get('URL', 'gun')
url_item = config.get('URL', 'item')
url_gundead = config.get('URL', 'gundead')

list_gun = scrape.scrape_gun(url_gun)
list_item = scrape.scrape_item(url_item)
list_gundead = scrape.scrape_gundead(url_gundead)

scrape_save.save_gun(db, list_gun, MONGO_COLLECTION)
scrape_save.save_item(db, list_item, MONGO_COLLECTION)
scrape_save.save_gundead(db, list_gundead, MONGO_COLLECTION)
