from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base,declared_attr
from sqlalchemy.orm import sessionmaker
from config import SqliteConfig


class Model(object):

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    def serialize(self):
        data = {}
        for f in getattr(self, 'fields'):
            data[f] = getattr(self, f)
        return data

    @classmethod
    def register_manager(cls):
        getattr(cls, 'objects').contribute_to_class(cls)


engine = create_engine(SqliteConfig.database_url,echo=True)

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base(cls=Model)