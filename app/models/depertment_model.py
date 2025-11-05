from app.db.base import Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Integer, String

# Department = id, name

class Department(Base):
    __tablename__ = "departments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    dept_name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True) # TODO: all department names must be unique and lowercased department_name = department_name.strip().lower()

    # TODO: add relationship with student
    # TODO: add relationship with subject