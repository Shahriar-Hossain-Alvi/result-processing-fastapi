from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.authenticated_user import get_current_user
from app.crud_operations.student_service import create_student
from app.db.db import get_db_session
from app.schemas.student_schema import StudentCreateSchema, StudentOutSchema, StudentUpdateSchema
from app.schemas.user_schema import UserOutSchema

router = APIRouter(
    prefix="/students",
    tags=["students"] # for swagger
)


# ensure admin
def ensure_admin(current_user: UserOutSchema):
    if current_user.role.value != "admin":
        raise HTTPException(status_code=403, detail="Unauthorized access")


# create student record
@router.post("/")
async def create_student_record(
        student_data: StudentCreateSchema,
        db: AsyncSession = Depends(get_db_session),
        current_user: UserOutSchema = Depends(get_current_user)
):
    ensure_admin(current_user)

    try:
        return await create_student(db, student_data)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))