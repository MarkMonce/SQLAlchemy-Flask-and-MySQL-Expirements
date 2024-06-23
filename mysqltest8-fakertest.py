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


DATABASE_URL = 'mysql+pymysql://root:Naples727575!!@127.0.0.1/mynewdatabase'

# Create a connection to the database
engine = create_engine(DATABASE_URL, echo=True)
# Base.metadata.create_all(engine)  # Create tables based on the Base

Session = sessionmaker(bind=engine)
session = Session()

# Create an instance of Faker to generate fake data
fake = Faker()

i = input("How Many Users?: ")

# Generate and add 10 fake users
for _ in range(int(i)):
    name = fake.name()
    age = fake.random_int(min=18, max=60)
    new_user = User(name=name, age=age)
    session.add(new_user)

# Commit the transactions
session.commit()

print("All users after update:")
all_users = session.query(User).all()
for user in all_users:
    print(f'ID: {user.id}, Name: {user.name}, Age: {user.age}')

session.close()