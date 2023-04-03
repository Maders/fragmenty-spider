from pymongo import MongoClient

mongo_uri = "mongodb://localhost:27017"
client = MongoClient(mongo_uri)
db = client['fragmenty']
collection = db['numbers']

# Update all documents
result = collection.update_many(
    {},
    [
        {
            "$set": {
                "minimumBidInUSD": {
                    "$substr": ["$minimumBidInUSD", 1, {"$subtract": [{"$strLenCP": "$minimumBidInUSD"}, 1]}]
                }
            }
        }
    ]
)

print(f"Updated {result.modified_count} documents")
