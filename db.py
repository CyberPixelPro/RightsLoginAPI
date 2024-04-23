from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
import string, random

db = MongoClient(
    "mongodb+srv://Rgcmusicbot:rgcxd@cluster0.aip5wiz.mongodb.net/?retryWrites=true&w=majority"
).testdb.login


async def is_user_exist(email: str, password: str):
    user = await db.find_one({"email": email})
    if not user:
        return False

    if user["password"] == password:
        token = await get_new_token(email)
        return token
    else:
        return False


async def get_new_token(email: str):
    token = "".join(random.choices(string.ascii_letters + string.digits, k=10))
    await db.update_one({"email": email}, {"$set": {"token": token}})
    return token


async def is_token_exist(token: str): # Check if token exists in the database
    user = await db.find_one({"token": token})
    if not user:
        return False
    return True
