import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    phone_number = Column(String(250))
    gender = Column(String(250))

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    description = Column(String(250), nullable=False)
    icons = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    content = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    post_id = Column(Integer, ForeignKey('posts.id'))
    posts = relationship(Post)

class Raection(Base):
    __tablename__ = 'reactions'
    id = Column(Integer, primary_key=True)
    number_of_likes = Column(Integer, nullable=False)
    number_of_dislikes = Column(Integer, nullable=False)
    post_id = Column(Integer, ForeignKey('posts.id'))
    post = relationship(Post)
    comment_id = Column(Integer, ForeignKey('comments.id'))
    comments = relationship(Comment)

class Follower(Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True)
    # follower_user_id = Column(Integer, ForeignKey('users.id'))
    followed_user_id = Column(Integer, ForeignKey('users.id'))
    # follower = relationship(User)
    followed = relationship(User)

    




# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     # the 2 lines below establish the relationship between the address and person tables
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
