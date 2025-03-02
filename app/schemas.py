from pydantic import BaseModel
class TodoSchema(BaseModel):
    title: str
    description: str
    priority: int
    completed: bool
