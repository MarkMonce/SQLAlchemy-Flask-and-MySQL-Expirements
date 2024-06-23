from sqlalchemy import create_engine, Column, Integer, String, text
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import SQLAlchemyError


Base = declarative_base()
# Assuming engine is already created and Base is declared
engine = create_engine('mysql+pymysql://root:Naples727575!!@localhost/mynewdatabase')
Session = sessionmaker(bind=engine)
session = Session()

# Define the User class based on Base
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer)

# Querying all users
print("All users:")
all_users = session.query(User).all()
for user in all_users:
    print(f'ID: {user.id}, Name: {user.name}, Age: {user.age}')

# Querying users with a specific hardcoded name
print('Hardcoded user is named John Doe')
print('Updating user John Doe\n')
john_doe_users = session.query(User).filter(User.name == 'John Doe').all()
print('--------------------------------\n')
print('Change comments in script to use user inputs for searches.....')
print('--------------------------------\n')

# #Or Prompt the script user for an ID
# search_id = input("Input ID of user to search:\n")
# john_doe_users = session.query(User).filter(User.id == search_id).all()

# #Or Prompt the script user for the age to search
# age_search = input('Input the desired user age(s)\n')
# john_doe_users = session.query(User).filter(User.age == age_search).all()

# # OR Prompt the script user for the name of the user
# username_search = input('Input the name of the user to search\n')
# john_doe_users = session.query(User).filter(User.name == username_search).all()

for user in john_doe_users:
    print(f'ID: {user.id}, Name: {user.name}, Age: {user.age}')

# Don't forget to close the session when done
session.close()