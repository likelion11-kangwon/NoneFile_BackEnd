# post.py
from fastapi import APIRouter

router = APIRouter()


@router.get('/post')
async def post():
    return {
        "post": "test"
    }
