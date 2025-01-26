import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    UserID = Column(Integer, primary_key=True)
    username = Column(String(32), nullable=False)
    name = Column(String(16), nullable=False)
    email = Column(String(32), nullable=False)
    password = Column(String(16), nullable=False)
    phone = Column(Integer)
    bio = Column(String(250))
    

class Comment(Base):
    __tablename__ = 'Comment'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    CommentID = Column(Integer, primary_key=True)
    UserID = Column(Integer, ForeignKey('User.UserID'))
    text_comment = Column(String(250))
    likes_comment = Column(Integer)
    user = relationship(User)

class Post(Base):
    __tablename__ = 'Post'

    PostID = Column(Integer, primary_key=True)
    UserID = Column(Integer, ForeignKey('User.UserID'))
    MediaID = Column(Integer, ForeignKey('Media.MediaID'))
    likes_count = Column(Integer)
    shares_count = Column(Integer)
    Comments_count = Column(Integer)
    user = relationship(User)

class Media(Base):
    __tablename__ = 'Media'

    MediaID = Column(Integer, primary_key=True)
    PostID = Column(Integer, ForeignKey('Post.PostID'))
    media_type = Column(String)
    media_url = Column(String)
    post = relationship(Post)

class Follower(Base):
    __tablename__ = 'Follower'

    FollowerID = Column(Integer, primary_key=True)
    UserID = Column(Integer, ForeignKey('User.UserID'))
    user = relationship(User)

class Message(Base):
    __tablename__ = 'Message'

    MessageID = Column(Integer, primary_key=True)
    UserID = Column(Integer, ForeignKey('User.UserID'))
    FollowerID = Column(Integer, ForeignKey('Follower.FollowerID'))
    message_type = Column(String)
    user = relationship(User)
    follower = relationship(Follower)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
