import uvicorn as uvicorn
from fastapi import FastAPI
from database.book import get_all_books
from routers.recommendation import recommendation_route
from routers.books import books

app = FastAPI()

app.include_router(books.router)
app.include_router(recommendation_route.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}


# @app.get("/book/")
# async def get_books():
#     return get_all_books()

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
