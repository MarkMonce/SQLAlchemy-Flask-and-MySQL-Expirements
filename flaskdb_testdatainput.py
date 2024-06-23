# This script will create some puppies, owners, and toys!
# Note, if you run this more than once, you'll be creating dogs with the same
# name and duplicate owners. The script will still work, but you'll see some
# warnings. Watch the video for the full explanation.
from flaskdb_basic import db,Puppy,Owner,Toy,app

# Create 2 puppies
rufus = Puppy("Rufus", 3)
fido = Puppy("Fido", 3)

# Add puppies to database
with app.app_context():
    db.session.add_all([rufus,fido])
    db.session.commit()

# Check with a query, this prints out all the puppies!
# with app.app_context():
#     print(Puppy.query.all())

# # Grab Rufus from database
# # Grab all puppies with the name "Rufus", returns a list, so index [0]
# # Alternative is to use .first() instead of .all()[0]
with app.app_context():
    rufus = Puppy.query.filter_by(name='Rufus').all()[0]



# # Create an owner to Rufus
john = Owner("Ringo",16)
print (john.owner_name, john.puppy_id)

with app.app_context():
    db.session.add(john)
    db.session.commit()



# # # Give some Toys to Rufus
# with app.app_context():
#     toy1 = Toy('Chew Toy',rufus.id)
#     toy2 = Toy("Ball",rufus.id)

# # # Commit these changes to the database
# with app.app_context():
#     db.session.add_all([jose,toy1,toy2])
#     db.session.commit()

# # Let's now grab rufus again after these additions
with app.app_context():
    rufus = Puppy.query.filter_by(name='Rufus').first()
    print(rufus)

# # Show toys
# with app.app_context():
#     db.session.add(fido)
#     print(fido.report_toys())

# You can also delete things from the database:
with app.app_context():
    find_pup = Puppy.query.filter_by(name = 'Sky').first()
    db.session.delete(find_pup)
    db.session.commit()