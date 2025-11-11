from pydantic import BaseModel, ConfigDict


class DepartmentCreateSchema(BaseModel):
    department_name: str

class DepartmentOutSchema(BaseModel):
    id: int 
    department_name: str

    model_config = ConfigDict(from_attributes=True)