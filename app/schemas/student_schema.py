from pydantic import BaseModel, ConfigDict

class StudentBaseSchema(BaseModel):
    name: str
    registration: str
    session: str
    department_id: int
    semester_id: int
    user_id: int


class StudentCreateSchema(StudentBaseSchema):
    pass


class StudentOutSchema(StudentBaseSchema):
    id: int
    model_config = ConfigDict(from_attributes=True)


class StudentUpdateSchema(BaseModel):
    name: str | None = None
    registration: str | None = None
    session: str | None = None
    department_id: int | None = None
    semester_id: int | None = None