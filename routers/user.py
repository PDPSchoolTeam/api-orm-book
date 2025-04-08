from fastapi import APIRouter
from schemas.base import BaseResponse
from models.user import User

router = APIRouter(
    prefix="/users"
)


@router.get("", response_model=BaseResponse)
async def read_users():
    ...


@router.post("", response_model=BaseResponse)
async def create_user(user: User):
    ...


@router.put("", response_model=BaseResponse)
async def update_user(user: User, user_id: int, ):
    ...


@router.delete("", response_model=BaseResponse)
async def delete_user(user_id: int):
    ...
