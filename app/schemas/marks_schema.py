from pydantic import BaseModel, ConfigDict
from app.models.subject_model import Subject
from app.schemas.subject_schema import SubjectOutSchema

class MarksBaseSchema(BaseModel):
    assignment_mark: float = 0.0
    class_test_mark: float = 0.0
    midterm_mark: float = 0.0
    final_exam_mark: float = 0.0
    student_id: int
    subject_id: int
    semester_id: int


class MarksCreateSchema(MarksBaseSchema):
    pass


class MarksUpdateSchema(BaseModel):
    assignment_mark: float | None = None
    class_test_mark: float | None = None
    midterm_mark: float | None = None
    final_exam_mark: float | None = None

class MarksResponseSchema(MarksBaseSchema):
    id: int
    total_mark: float
    GPA: float 
    model_config = ConfigDict(from_attributes=True)


class SemesterWiseAllSubjectsMarksResponseSchema(BaseModel):
    semester_id: int
    marks: list[MarksResponseSchema]
    model_config = ConfigDict(from_attributes=True)



class PopulatedMarksResponseSchema(MarksBaseSchema):
    id: int
    total_mark: float
    GPA: float 
    subject: SubjectOutSchema
    model_config = ConfigDict(from_attributes=True)

class SemesterWiseAllSubjectsMarksWithPopulatedDataResponseSchema(BaseModel):
    semester_id: int
    marks: list[PopulatedMarksResponseSchema]
    model_config = ConfigDict(from_attributes=True)