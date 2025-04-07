#базовая настройка SQLAlchemy

from typing import Any

from sqlalchemy import MetaData
from sqlalchemy.orm import as_declarative
from sqlalchemy.ext.declarative import declared_attr


metadata = MetaData()


@as_declarative()
class Base:
    '''
    Базовый класс, от которого будут наследоваться остальные классы
    '''

    id: Any
    __name__: str
    metadata = metadata

    


SQLALCHEMY_DATABASE_URL = 'postgresql+psycopg2://postgres:admin@localhost/mandarindb'