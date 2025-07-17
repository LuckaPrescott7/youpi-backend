from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class AdminUser(Base):
    __tablename__ = "admin_users"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)

class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String)
    email = Column(String)
    message = Column(Text)

class Newsletter(Base):
    __tablename__ = "newsletter"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)

class Blog(Base):
    __tablename__ = "blogs"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(Text)

class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True)
    blog_id = Column(Integer, ForeignKey("blogs.id"))
    name = Column(String)
    content = Column(Text)
