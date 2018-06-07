
import pymongo

mongoclient = pymongo.MongoClient("127.0.0.1",username="demo",password="demo",authSource="demo",authMechanism="SCRAM-SHA-1")
db = mongoclient.get_database("demo")
Users= db.get_collection("Users")
