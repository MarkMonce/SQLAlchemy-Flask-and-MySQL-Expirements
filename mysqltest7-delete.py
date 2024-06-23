from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the User class based on the Base
Base = declarative_base()
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer)

# Connect to the database (for example a SQLite in-memory database)
engine = create_engine('mysql+pymysql://root:Naples727575!!@localhost/mynewdatabase')
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

print("All users:")
all_users = session.query(User).all()
for user in all_users:
    print(f'ID: {user.id}, Name: {user.name}, Age: {user.age}')

# Assuming a user with ID 1 exists and you want to delete it\
delete_user_id = input('Input the ID of the user to delete:\n')

user_to_delete = session.query(User).filter_by(id=delete_user_id).first()

if user_to_delete:
    # Delete the user
    session.delete(user_to_delete)

    # Commit the transaction
    session.commit()
    print("User deleted successfully")
else:
    print("User not found")

# Optionally, to verify deletion
deleted_user = session.query(User).filter_by(id=1).first()
if deleted_user:
    print("User still in database")
else:
    print("User successfully removed from database")

session.close
