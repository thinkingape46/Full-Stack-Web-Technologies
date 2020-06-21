# pip install flask-bcrypt
# import Bcrypt
from flask_bcrypt import Bcrypt

# create an instance of Brypt

bcrypt = Bcrypt()

my_password = 'somepassword'

# Create an hash key
my_hask_key = bcrypt.generate_password_hash(my_password)

print("haskey is {a}".format(a=my_hask_key))

# Check whether entered pass is true.

bcrypt_check = bcrypt.check_password_hash(my_hask_key, 'hello')
print("Password Check: {a}".format(a=bcrypt_check))

bcrypt_check = bcrypt.check_password_hash(my_hask_key, 'somepassword')
print("Password Check: {a}".format(a=bcrypt_check))