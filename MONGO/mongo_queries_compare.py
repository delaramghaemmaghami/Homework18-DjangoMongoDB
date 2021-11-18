from pymongo import MongoClient

client = MongoClient("localhost", 27017)

db = client.homework18

collection = db.custumerInfos

tehran_average = collection.aggregate([{"$match": {"location.state": "تهران"}}, {
    "$group": {"_id": "$location.state", "averageAge": {"$avg": "$dob.age"}}}])

tehran_ave = 0

for i in tehran_average:
    tehran_ave = i['averageAge']

compare_with_tehran_ave = collection.aggregate(
    [{"$group": {"_id": "$location.state", "averageAge": {"$avg": "$dob.age"}}},
     {"$addFields": {"tehranAverage": tehran_ave}}])

for i in compare_with_tehran_ave:
    print(i)
