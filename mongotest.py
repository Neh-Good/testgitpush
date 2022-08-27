import pymongo
client = pymongo.MongoClient("mongodb+srv://neh_good:sonaneha1205@cluster0.318mv6w.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"neha",
    "email":"dbi001_neha@iimnagpur.ac.in",
    "surname":"agrawal"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)