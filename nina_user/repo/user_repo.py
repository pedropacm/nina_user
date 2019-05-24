import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
 
Base = declarative_base()

engine = create_engine('sqlite:///:memory:')
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)

session = DBSession()

class UserRepo:

	def __init__(self):
		# Create all tables in the engine. This is equivalent to "Create Table"
		# statements in raw SQL.
		Base.metadata.create_all(engine)
		

	def save(self, user):
		session.add(user)
		session.commit()
		return session.query(User).filter(
			User.name == user.name,
			User.email == user.email,
			User.password == user.password).first()

	def find_by_email(self, email):
		return session.query(User).filter(User.email == email).first()		

	def find_by_id(self, user_id):
		return session.query(User).filter(User.id == user_id).first()

 
class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
