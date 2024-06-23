#As we had to do in the flaskdb-createtable.py, we need to ALSO import that app object from flaskdb_basic.py

from flaskdb_basic import db, Puppy, app

my_puppy = Puppy('Sky', 3) ##No need for app_context, here becase we are simply creating a new objet as defined in flaskdb_basic.py

with app.app_context(): ##CANNOT EXECUTE COMMANDS TO THE DATABASE WITHOUT THE app_context!!!!
    db.session.add(my_puppy)
    db.session.commit()
    db.session.close


with app.app_context():
    #NOTE: With simple queries, you do not need to open a session since you are not making changes to the database
    all_puppies = Puppy.query.all()
    # #I Get back a list (ie array) off Puppy objects, called "all_puppies"
    # #And I can iterate throug that list
    for dog in all_puppies:
        print(dog.name )
        # print('\n')
    # #I can reference any object and its attributes by using an index if the all_puppies object list
    print("\nGets a puppy by an index eg (all_puppies[num].name) : " + all_puppies[0].name)

    # #And....I can run very precise queries to return just a single object that references a specifc record in the database
    #some_puppy = Puppy.query.get(2)
    another_puppy = db.session.get(Puppy, 2)
    #print("\nGets a puppy with the query.get() command: " + some_puppy.name+"\n")
    print("\nMore modern version of a query: " + another_puppy.name)

#To delete all dogs named "sky" --- Sorry Sky
with app.app_context():
     
    delete_puppies = Puppy.query.filter_by(name = 'Sky')
    for dog in delete_puppies:
        print('\n' + dog.name + " will be deleted. So sorry, Sky. :-(\n")
        db.session.delete(dog)
        db.session.commit()

# To update a specific record

with app.app_context():
    some_puppy = db.session.get(Puppy, 2)
    print(some_puppy.name + "\'s age was " + str(some_puppy.age))
    some_puppy.age = some_puppy.age + 1
    print(some_puppy.name + "\'s age is now " + str(some_puppy.age) + "\n")
    db.session.commit()
    db.session.close()


