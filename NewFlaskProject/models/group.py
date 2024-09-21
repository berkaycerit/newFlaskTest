from typing import (
    List,
    Optional,
)
from sqlalchemy import (
    ForeignKey,
    String,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)
from . import (
    Base
)


class Group(Base):
    __tablename__ = "groups"  # Veritabanındaki tablo adı, modelden farklı olabilir

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))

    def __repr__(self):
        return f"<Group name:{self.name}>"