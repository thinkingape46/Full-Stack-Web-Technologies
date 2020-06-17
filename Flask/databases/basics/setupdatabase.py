# import db and puppy from basic.py which is in the same folder.
from basic import db, Puppy

# setup database.
# Usually we do not create a seperate py to create a database, it will be handled through command line tools (easier?)
# Convers the model class into a database table.
db.create_all()

# Create new entries.

# A new entry for the puppy Sammy through a new instance of Puppy class.
sam = Puppy('Sammy', 3)

# for Franky
frank = Puppy('Franky', 6)

print(sam.id)
print(frank.id)
# About two statement shall return None, because we didn't define them while creating the class.

# Add puppy objects to the database.
# db.session.add_all([sam, frank])

# We can also add the objects seperately.
db.session.add(sam)
db.session.add(frank)

# To save the changes to the database.
db.session.commit()

# ids will be create when we all the objects to the database.
print(sam.id)
print(frank.id)