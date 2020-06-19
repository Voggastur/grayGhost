import pymongo
import os

MONGODB_URI = os.getenv('MONGO_URI')
DBS_NAME = "myTestDB"
COLLECTION_NAME = "myFirstMDB"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e

conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

#coll.update_many({'nationality': 'american'}, {'$set': {'hair_colour': 'maroon'}})

#documents = coll.find({'occupation': 'writer'})

#new_doc = {'first': 'terry', 'last': 'pratchett', 'dob': '28/04/1948', 'gender': 'm', 'hair_colour': 'not much', 'occupation': 'writer', 'nationality': 'english'}

#coll.insert(new_doc)

#new_docs = [{'first': 'terry', 'last': 'pratchett', 'dob': '28/04/1948', 'gender': 'm', 'hair_colour': 'not much', 'occupation': 'writer', 'nationality': 'english'}, {'first': 'george', 'last': 'rr martin', 'dob': '20/09/1948', 'gender': 'm', 'hair_colour': 'maroon', 'occupation': 'writer', 'nationality': 'american'}]

#coll.insert_many(new_docs)

#documents = coll.remove({'nationality': 'american'})

#coll.update_one({'nationality': 'american'}, {'$set': {'hair_colour': 'maroon'}})

#documents = coll.find({'nationality': 'american'})

documents = coll.find()

for doc in documents:
    print(doc)
