from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from faker import Faker

# Define the Base class for declarative table definitions
Base = declarative_base()

# Define the User class
class User(Base):
    __tablename__ = 'users2'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer)

# Replace 'username', 'password', 'server', 'dbname' with your actual MySQL credentials
DATABASE_URL = 'mysql+pymysql://root:Naples727575!!@127.0.0.1/mynewdatabase'

# Create a connection to the database
engine = create_engine(DATABASE_URL, echo=True)
Base.metadata.create_all(engine)  # Create tables based on the Base

engine.dispose