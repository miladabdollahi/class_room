from sqlalchemy import Column, Integer, String, DateTime
from db import Base as Model
from datetime import datetime
from managers import UserManager


class User(Model):
    __tablename__ = 'User'

    fields = ('id', 'first_name', 'last_name', 'username')

    id = Column(Integer, primary_key=True)
    first_name = Column(String(70))
    last_name = Column(String(70))
    username = Column(String(35))
    join_date = Column(DateTime, default=datetime.now())

    objects = UserManager()

    def __init__(self, id, first_name, last_name, username):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username

    def get_fullname(self):
        fullname = None
        if self.first_name:
            fullname = self.first_name
        if fullname:
            if self.last_name:
                fullname += ' ' + self.last_name
        else:
            fullname = self.last_name
        return fullname


User.register_manager()

