from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb://localhost:27017/todo_db"
client = AsyncIOMotorClient(MONGO_URI)
db = client.todo_db

async def get_database():
    return db
