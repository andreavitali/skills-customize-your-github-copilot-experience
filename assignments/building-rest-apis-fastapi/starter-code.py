from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Book API")


class Book(BaseModel):
    title: str
    author: str
    year: int


books = [
    {"id": 1, "title": "Python Basics", "author": "Ada", "year": 2024},
    {"id": 2, "title": "Web Development", "author": "Grace", "year": 2023},
]


@app.get("/books")
def get_books():
    return books


# TODO: Add a POST endpoint to create a new book
# TODO: Add a GET endpoint to return one book by id
# TODO: Add a PUT endpoint to update an item
# TODO: Add a DELETE endpoint to remove an item
