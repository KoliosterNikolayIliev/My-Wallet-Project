import os
from datetime import datetime
import pymongo

client = pymongo.MongoClient(os.environ.get('DB_HOST'))
db = client.get_database('portfolio')


def cache_assets(assets, user_id):
    current_datetime = datetime.utcnow()
    data = {
        'user_id': user_id,
        'date': current_datetime,
        'content': assets,
    }
    db.assets.insert_one(data)
