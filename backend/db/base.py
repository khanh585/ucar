import re
from typing import Any

from sqlalchemy.ext.declarative import as_declarative, declared_attr

PATTERN_GENERATE_TABLE_NAME = r"(?<!^)(?=[A-Z])"


@as_declarative()
class Base:
    id: Any
    __name__: str
    __table_args__ = {"schema": "ucar-01"}

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return re.sub(PATTERN_GENERATE_TABLE_NAME, "_", cls.__name__).lower()
