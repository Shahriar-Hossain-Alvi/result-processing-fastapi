from app.db.base import Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Integer, String

## Tables
# 1. students table = id, name, roll, registration, session, dept
# 2. results table = id, student_id, subject_id, semester_id, assignmet_mark, midterm_mark, final_mark, class_test_mark, total_mark grade(GPA)
# 3. semester = id, name, number
# 4. subject = id, name, subject_code, semester_id, dept_id, credits


class Semester(Base):
    __tablename__ = "semesters"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    semester_name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)

    semester_number: Mapped[int] = mapped_column(Integer, nullable=False, unique=True)

    # TODO: add relationship with subjects