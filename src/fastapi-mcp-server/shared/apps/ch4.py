from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/name/{name}")
async def read_name(name: str):
    return f"Hello, {name}!"


class CreateItem(BaseModel):
    id: int
    name: str


@app.post("/api/create")
async def create_item(item: CreateItem):
    return {"id": item.id, "name": item.name}
