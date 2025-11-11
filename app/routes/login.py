from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud_operations.user_login import login_user
from app.db.db import get_db_session
from app.schemas.jwt_schema import TokenSchema
from app.schemas.login_Schema import LoginSchema

# login router

router = APIRouter(prefix='/login', tags=['login'])

@router.post("/", response_model=TokenSchema)
async def login(payload: LoginSchema, db: AsyncSession = Depends(get_db_session)):
    try:
        return await login_user(db, payload.username, payload.password)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    