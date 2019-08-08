import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Post(Base):
    __tablename__ = 'posts'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    likes = Column(Integer, primary_key=True)
    picture = Column(String(250), nullable=False)
    comments = Column(String(250), nullable=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)


class Edits(Base):
        __tablename__ = 'edits'
        id = Column(Integer, primary_key=True)
        bio = Column(String(250), nullable=True)
        website = Column(String(250), nullable=True)
        user_id = Column(Integer, ForeignKey('user.id'))
        user = relationship(User)

class Private(Base):
        __tablename__ = 'privateinfo'
        id = Column(Integer, primary_key=True)
        email = Column(String(250), nullable=True)
        phone = Column(Integer, nullable=True)
        gender = Column(String(250), nullable=True)
        edits_id = Column(Integer, ForeignKey('edits.id'))
        edits = relationship(Edits)

        class Followers(Base):
            __tablename__ = 'followers'
            id = Column(Integer, primary_key=True)
            name = Column(String(250), nullable=True)
            user_id = Column(Integer, ForeignKey('user.id'))
            user = relationship(User)



def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')