from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud_operations.user_login import login_user
from app.db.db import get_db_session
from app.schemas.jwt_schema import TokenSchema

# login router

router = APIRouter(prefix='/login', tags=['login'])

@router.post("/", response_model=TokenSchema)
async def login(
    payload: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db_session)):
    try:
        return await login_user(db, payload.username, payload.password)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    