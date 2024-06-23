from sqlalchemy import create_engine, Column, Integer, String, text
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import SQLAlchemyError

Base = declarative_base()


engine = create_engine('mysql+pymysql://root:Naples727575!!@localhost/mynewdatabase')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer)

#PRINTING CURRENT LIST OF USERS BEFORE INSERT
print("All users:")
all_users = session.query(User).all()
for user in all_users:
    print(f'ID: {user.id}, Name: {user.name}, Age: {user.age}')

#For test purposes, you can use the following lines to prompt the user for input to be added to the database
new_user_name = input('Input New UserName\n')
new_user_age = input('Input New User Age:\n')
#Or just use the hardcoded values here...


new_user = User(name=new_user_name, age=new_user_age)

session.add(new_user)

# PRINTING UPDATED LIST OF USERS AFTER INSERT
print("All users:")
all_users = session.query(User).all()
for user in all_users:
    print(f'ID: {user.id}, Name: {user.name}, Age: {user.age}')

session.commit()
session.close
