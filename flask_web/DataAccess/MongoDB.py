import pymongo

class mongodb:

    def __init__(self,host="127.0.0.1",username="demo",password="demo",dename="demo"):
        mongoclient = pymongo.MongoClient("127.0.0.1", username="demo", password="demo", authSource="demo",
                                          authMechanism="SCRAM-SHA-1")
        self.db = mongoclient.get_database(dename)


    def getdb(self):
        return self.db

    def getCollection(self,collectionName):
        return self.db.get_collection(collectionName)


