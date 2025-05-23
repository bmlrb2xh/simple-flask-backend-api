from app.models.model_base import ModelBase

import datetime
from sqlalchemy import Column, Integer, String, DateTime

class Users(ModelBase):
    __tablename__ = 'Users'
    id = Column('ID', Integer, primary_key = True, autoincrement = True)
    name = Column('Name', String(64), nullable = False)
    password = Column('Password', String(128), nullable = False)
    age = Column('Age', Integer, nullable = False)
    info = Column('Info', String(256), nullable = True)
    date_created = Column('DateCreated', DateTime, nullable = False, default = datetime.datetime.now)
    date_updated = Column('DateUpdated', DateTime, nullable = False, default = datetime.datetime.now, onupdate = datetime.datetime.now)

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'password': self.password,
            'age': self.age,
            'info': self.info,
            'date_created': str(self.date_created),
            'date_updated': str(self.date_updated)
        }
