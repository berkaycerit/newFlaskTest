from __future__ import annotations
from sqlalchemy import (
    Table,
    Column,
    ForeignKey,
)
from . import (
    Base,
)


student_group_assoc_table = Table(
    "student_group_assoc_table",
    Base.metadata,
    Column(
        "group_id",
        ForeignKey("groups.id"),
        primary_key=True,
    ),
    Column(
        "student_id",
        ForeignKey("student.id"),
        primary_key=True,
    ),
)


lesson_group_assoc_table = Table(
    "lesson_group_assoc_table",
    Base.metadata,
    Column("lesson_id", ForeignKey("lessons.id"), primary_key=True),
    Column("group_id", ForeignKey("groups.id"), primary_key=True),
)