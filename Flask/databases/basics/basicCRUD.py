# Created to make CRUD operations.

from basic import db, Puppy

# Create a new entry to the database.

my_puppy = Puppy('Rufus', 4)

db.session.add(my_puppy)
db.session.commit()

# Read the database.
all_puppies = Puppy.query.all()
print(all_puppies)

# Selection by ID
puppy_one = Puppy.query.get(1)
print(puppy_one.name)

# Filers.
# Select puppies by name.
# Below line proudces some SQL code for us.
puppy_franky = Puppy.query.filter_by(name='Franky')

# puppies printing will follow __repr__ method, i.e string representation of the Class.
print(puppy_franky.all())


# Update
first_puppy = Puppy.query.get(1)
first_puppy.age = 10
# add
db.session.add(first_puppy)
db.session.commit()

# Delete.
second_puppy = Puppy.query.get(2)
db.session.delete(second_puppy)
db.session.commit()

all_puppies = Puppy.query.all()
print(all_puppies)