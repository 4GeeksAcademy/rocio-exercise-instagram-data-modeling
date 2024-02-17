import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), unique= True, index=True)
    first_name = Column(String(250))
    last_name = Column(String(250))    
    email = Column(String(250), unique=True, nullable=False)
    password = Column(String(250), unique=True, nullable=False)

class Post(Base):
    __tablename__ = 'post'


    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.id'))

class Comment(Base):
    __tablename__ = 'comment'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250))
    user_id = Column(Integer, ForeignKey('User.id'))
    post_id = Column(Integer, ForeignKey('Post.id'))
    
class Followers(Base):
    __tablename__ = 'followers'


    id = Column(Integer, primary_key= True)
    user_to_id= Column(Integer, ForeignKey('User.id'))
    user_from_id = Column(Integer, ForeignKey('User.id'))

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
