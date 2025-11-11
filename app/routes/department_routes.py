from fastapi import APIRouter, Depends, HTTPException
from app.core.authenticated_user import get_current_user
from app.crud_operations.department_service import create_department, get_departments
from app.models.user_model import UserRole
from app.schemas.department_schema import DepartmentCreateSchema, DepartmentOutSchema
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.db import get_db_session
from app.schemas.user_schema import UserOutSchema


router = APIRouter(
    prefix="/departments",
    tags=["departments"] # for swagger
)


@router.post("/")
async def create_new_department(
    department_data: DepartmentCreateSchema, 
    db: AsyncSession = Depends(get_db_session),
    current_user: UserOutSchema = Depends(get_current_user)
    ):
    # if current_user.role != UserRole.ADMIN:
    if current_user.role.value != "admin":
        raise HTTPException(status_code=403, detail="Only admin can create a new department")
    print("DEPARTMENT DATA", department_data)
    try:
       return await create_department(db, department_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/", response_model=list[DepartmentOutSchema])
async def get_all_departments(
    db: AsyncSession = Depends(get_db_session),
    current_user: UserOutSchema = Depends(get_current_user)
    ):
    try: 
        return await get_departments(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))