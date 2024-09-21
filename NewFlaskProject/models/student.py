from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base
from .associates import student_group_assoc_table
from .group import Group

class Student(Base):
    __tablename__ = "student"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    age: Mapped[int] = mapped_column()
    address: Mapped[str] = mapped_column(String(250))

    groups: Mapped[list[Group]] = relationship(secondary=student_group_assoc_table)
