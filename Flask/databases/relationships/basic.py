# Create entries into the table.
# First let's import models from models.py
# Write the script so it's meant to be run once.

from models import db, Puppy, Owner, Toy

# Create some puppy objects.

rufus = Puppy('Rufus')
sammy = Puppy('Sammy')

# Add puppies to the database.
# Can also use add_all([rufus, sammy])
db.session.add_all([rufus, sammy])

db.session.commit()

# Check if the puppies are added to the database.

############# PRINT FUNCTION ################
print(Puppy.query.all())

# grad Rufus from the database.
# we filer by name, and by using "first()"; we are grabbing the first.
# If we wish to grab all of the items in the list use ".all()"; and then if you want the first of it use indexing ".all()[0]"
rufus = Puppy.query.filter_by(name='Rufus').first()

# Create owner object
jose = Owner('Jose', rufus.id)

# Give toys to Rufus.

toy1 = Toy('Chew Toy', rufus.id)
toy2 = Toy('Ball', rufus.id)

db.session.add_all([jose, toy1, toy2])
db.session.commit()

# Now we have commited some changes to table again, lets grab Rufus again and print the changes.
rufus = Puppy.query.filter_by(name='Rufus').first()

# Rufus now has a owner and two toys.
############# PRINT FUNCTION ################
print(rufus)
print(rufus.report_toys())
