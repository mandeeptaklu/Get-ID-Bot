from pymongo import MongoClient
from config import Config

client = MongoClient(Config.MONGO_URI)
db = client['ID_Finder_Bot']
users_col = db['users']

def save_user(user_id):
    if not users_col.find_one({"user_id": user_id}):
        users_col.insert_one({"user_id": user_id})

def get_all_users():
    # .find() ek cursor deta hai, use list mein convert karo
    return list(users_col.find({}))


