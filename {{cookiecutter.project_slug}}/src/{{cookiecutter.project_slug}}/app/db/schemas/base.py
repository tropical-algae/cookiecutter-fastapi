from typing import Any, Generic, TypeVar

from pydantic import BaseModel
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import as_declarative

BaseModelType = TypeVar("BaseModelType", bound=BaseModel)


@as_declarative()
class Base(Generic[BaseModelType]):
    id: Any
    __name__: str

    # Generate __tablename__ automatically
    @declared_attr  # type: ignore
    def __tablename__(cls) -> str:  # noqa
        return cls.__name__.lower()

    def trans(self) -> BaseModelType:  # type: ignore
        pass
