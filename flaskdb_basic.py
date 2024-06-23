# IN THE flask_db.....py files, we are recreating the
# very simple SQLAlchemy Model from the Udemy course (by Jose Portilla) on Flask that deal with databases
# The difference here is that I want to use MYSQL instead of SQLLite as they do in the Udemy Course

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# This next line is the first and possibly only place I deviate from what Jose does in the Udemy course.
# I Replace his SQLite string with one of my own.
# I also skip -- for now importing the OS module he uses to define the physical location of his SQLlite database file,
# Since I am attempting to use a MYSQL server on my laptop instead

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Naples727575!!@localhost/puppydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

class Puppy(db.Model):
    __tablename__='puppie'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    #Defining the FK relationships to other tables. These are FK...
    #...which correspond to primary keys to other tables.
    toys = db.relationship('Toy', backref='puppy', lazy='dynamic')
    owner = db.relationship('Owner', backref='puppy', uselist=False)

    def __init__ (self,name,age):
        self.name = name
        self.age = age

    def __repr__(self):
            if self.owner:
                return f"\nPuppy name is {self.name} and owner is {self.owner.owner_name}"
            else:
                return f"\nPuppy name is {self.name} and has no owner assigned yet."
    
    def report_toys(self):
        print("Here are my toys!")
        for toy in self.toys:
            print(toy.item_name)
        

class Toy(db.Model):

    __tablename__ = 'toys'

    id = db.Column(db.Integer,primary_key = True)
    item_name = db.Column(db.Text)
    # Connect the toy to the puppy that owns it.
    # We use puppies.id because __tablename__='puppie'
    puppy_id = db.Column(db.Integer,db.ForeignKey('puppie.id'))

    def __init__(self,item_name,puppy_id):
        self.item_name = item_name
        self.puppy_id = puppy_id


class Owner(db.Model):

    __tablename__ = 'owners'

    id = db.Column(db.Integer,primary_key= True)
    owner_name = db.Column(db.Text)
    # We use puppies.id because __tablename__='puppie'
    puppy_id = db.Column(db.Integer,db.ForeignKey('puppie.id'))

    def __init__(self,owner_name,puppy_id):
        self.owner_name = owner_name
        self.puppy_id = puppy_id


