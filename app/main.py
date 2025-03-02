from fastapi import FastAPI, HTTPException, Depends
from motor.motor_asyncio import AsyncIOMotorClient
from .models import Todo
from .schemas import TodoSchema
from .database import get_database
from bson import ObjectId

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to Todo API"}

@app.post("/todos/")
async def create_todo(todo: TodoSchema, db=Depends(get_database)):
    new_todo = await db.todos.insert_one(todo.dict())
    return {"id": str(new_todo.inserted_id), **todo.dict()}

@app.get("/todos/")
async def get_todos(db=Depends(get_database)):
    todos = await db.todos.find().to_list(length=100)
    return [{"id": str(todo["_id"]), **todo} for todo in todos]

@app.put("/todos/{id}")
async def update_todo(id: str, todo: TodoSchema, db=Depends(get_database)):
    result = await db.todos.update_one({"_id": ObjectId(id)}, {"$set": todo.dict()})
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"id": id, **todo.dict()}

@app.delete("/todos/{id}")
async def delete_todo(id: str, db=Depends(get_database)):
    result = await db.todos.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "Todo deleted successfully"}
