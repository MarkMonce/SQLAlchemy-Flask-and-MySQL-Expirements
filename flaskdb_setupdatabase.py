# THIS FILE CONNECTS TO THE flask_basic.py file which is what I'm doing in the IMPORT command below....
# I Had to add the app object to the import so I could use the 'app.app_context' later, which is 
# Different from the Udemy video. I am using MYSQL and the Udemy video uses SQLite


from flaskdb_basic import db, Puppy, Toy, Owner, app

#This should create the tables in the flask_basic.py
#IMPORTANT: THIS COMMAND MUST APPEAR WITHIN THE app.app_context() context
# ALSO, specific to the db.creat_all() command, it is more common to use Flask-migrate at the command line to do this
# Flask-migrate will then keep a running record of the datase lifecycle; 
# Flask uses a subset of "Alembic", which can be thought of as a version-control system for databases.

with app.app_context():    
    db.create_all()

# Creating objects to be inserted into the DB
sam = Puppy('Samuel', 9)
frank = Puppy('Franklin', 15)


# OPTIONAL: Print back to the console to prove the objects do not exist because the 'id'
# field will only exist AFTER the data is inserted into the database in the next few lines of code

print(sam.id)
print(frank.id)

# Here is a key differentiation from what the Udemy course has these two commands as standalone
#
# db.session.add_all([sam,frank])
# db.session.commit()


# However, when I ran them, they failed, and the error said I needed to add the "with app.app_context() command"
# And after several tries, you can see what I came up with and it works

with app.app_context():
    db.session.add_all([sam,frank])
    db.session.commit()
    db.session.close
    
    # ----------OPTIONAL ADDITIONAL EXAMPLE CALLS TO THE ORM OBJECT(IE MODEL or TABLE)------------
    # -- OPTIONAL Print the Ids of the records that did not exist in the database until the previous commands
    # -- were executed
    print(sam.id)
    print(frank.id)

    #Now I can query the table by using the query method (See flaskdb_crud.py to see this done again)
    all_puppies = Puppy.query.all()
    #I Get back a list (ie array) off Puppy objects, called "all_puppies"
    #And I can iterate throug that list
    for dog in all_puppies:
        print(dog)
        # print('\n')
    #I can reference any object and its attributes by using an index if the all_puppies object list
    print(all_puppies[1].name)

    #And....I can run very precise queries to return just a single object that references a specifc record in the database
    some_puppy = Puppy.query.get(12)
    print(some_puppy.name)

 

