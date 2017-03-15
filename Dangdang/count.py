import time
import pymongo

client = pymongo.MongoClient('localhost',27017)
dangdang = client['dangdang']
saveinto_2 = dangdang['info_clean']

while True:
    print(saveinto_2.find().count())
    time.sleep(5)
