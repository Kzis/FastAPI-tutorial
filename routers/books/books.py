from fastapi import APIRouter

router = APIRouter(
    prefix="/book",
    tags=["Book"],
    responses={404: {"message": "Not found"}}
)

book_db = [
    {
        "title": "The C Programming",
        "price": 720
    },
    {
        "title": "Learn Python the Hard Way",
        "price": 870
    },
    {
        "title": "JavaScript: The Definitive Guide",
        "price": 1369
    },
    {
        "title": "Python for Data Analysis",
        "price": 1394
    },
    {
        "title": "Clean Code",
        "price": 1500
    },
]


@router.get("/")
async def get_books():
    return book_db
