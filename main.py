import pymongo
import pandas as pd
import json
client= pymongo.MongoClient("mongodb://localhost:27017")
df = pd.read_csv("Twitterproject.csv")
data=df.to_dict(orient = "records")
print(data)
db = client["Twitterscrappingproject"]
print(db)
db.Twitterproject.insert_many(data)


