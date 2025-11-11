from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models import Department
from app.schemas.department_schema import  DepartmentCreateSchema, DepartmentOutSchema


async def create_department(
        db: AsyncSession, 
        department_data: DepartmentCreateSchema
    ):
    lowercase_department_name = department_data.department_name.lower().strip()

    # check for existing department
    statement = select(Department).where(Department.department_name == lowercase_department_name)
    result = await db.execute(statement)
    is_exist = result.scalar_one_or_none()

    if(is_exist):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Department already exist")

    new_department = Department(department_name=lowercase_department_name)
    
    db.add(new_department)  # add the new_department to db(session)
    await db.commit()
    await db.refresh(new_department) # refresh the object(get the new data)

    return {
        "message": f"new_department created successfully. ID: {new_department.id}"
    }

async def get_departments(db: AsyncSession):
    statement = select(Department)
    result = await db.execute(statement)

    return result.scalars().all()