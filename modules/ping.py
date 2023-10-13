from fastapi import APIRouter


router = APIRouter()


@router.get("/")
async def ping():
    print("ping!")
    return {
        "ping": "pong!"
    }
