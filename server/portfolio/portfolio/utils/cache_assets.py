import os
from datetime import datetime, timedelta
import pymongo

client = pymongo.MongoClient(os.environ.get('DB_HOST'))
db = client.get_database('portfolio')


def cache_assets(assets, user_id):
    result = db.assets.update_one({'user_id': user_id}, {'$set': {'date': datetime.utcnow(), 'content': assets}})

    if result.modified_count == 0:
        data = {
            'user_id': user_id,
            'date': datetime.utcnow(),
            'content': assets,
        }
        db.assets.insert_one(data)
