from sqlalchemy import Column, Integer, Text, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.dialects import mysql
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine(
    "mysql+mysqlconnector://root:root@localhost/pyramid?charset=utf8mb4")
Session = sessionmaker()
Base = declarative_base(bind=engine)


class Note(Base):
    __tablename__ = 'notes'
    id = Column(Integer, primary_key=True)
    title = Column(Text)
    text = Column(Text)
    user_id = Column(Integer, ForeignKey('users.id'))

    def __init__(self, title, text, user_id):
        self.title = title
        self.text = text
        self.user_id = user_id

    def __repr__(self):
        return "<Note('%s','%s','%s')>" % (self.title, self.text, self.user_id)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    password = Column(Text)

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def __repr__(self):
        return "<User('%s','%s')>" % (self.name, self.password)


Base.metadata.create_all(engine)
