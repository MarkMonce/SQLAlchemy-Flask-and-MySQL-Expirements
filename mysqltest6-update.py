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

print("All users before update:")
all_users = session.query(User).all()
for user in all_users:
    print(f'ID: {user.id}, Name: {user.name}, Age: {user.age}')

# Get User Input for the User to Update
user_update_id = input("Enter the ID of the user you want to change: ")


user_to_update = session.query(User).filter_by(id=user_update_id).first()

if user_to_update:
    # Update the user's name and/or age8
    user_to_update.name = input("New User Name:\n")
    user_to_update.age = input("New User Age:\n")

    # Commit the transaction
    session.commit()
    print(f"Updated User: {user_to_update.name}, Age: {user_to_update.age}")
else:
    print("User not found")

# Optionally, to show that the update was committed
# updated_user = session.query(User).filter_by(id=1).first()
# if updated_user:
#     print(f"User after update: {updated_user.name}, Age: {updated_user.age}")
# else:
#     print("User not found after attempting update")
print("All users after update:")
all_users = session.query(User).all()
for user in all_users:
    print(f'ID: {user.id}, Name: {user.name}, Age: {user.age}')

session.close