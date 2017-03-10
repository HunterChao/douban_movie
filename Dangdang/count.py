import time
import pymongo

client = pymongo.MongoClient('localhost',27017)
dangdang = client['dangdang']
saveinto_2 = dangdang['saveinto_2']

while True:
    print(saveinto_2.find().count())
    time.sleep(5)
