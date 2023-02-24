import motor.motor_asyncio
from info import AUTH_CHANNEL, DATABASE_URI

class Fsub_DB:

    def __init__(self):
        self.client = motor.motor_asyncio.AsyncIOMotorClient(DB_URI)
        self.db = self.client["Fsub_DB"]
        self.col = self.db[str(FORCE_SUB_CHANNEL)]

    async def add_user(self, userid, first_name, username, date):
        await self.col.insert_one({"id": str(userid), "first_name": first_name, "username": username, "date": date})

    async def get_user(self, userid):
        return await self.col.find_one({"id": str(userid)})

    async def get_all_users(self):
        return await sel.col.find().to_list(None)

    async def delete_user(self, userid):
        await self.col.delete_one({"id": str(userid)})

    async def purge_all(self):
        await self.col.delete_many({})

    async def total_users(self):
        return await self.col.count_documents({})
