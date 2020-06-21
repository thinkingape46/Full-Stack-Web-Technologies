# pip install Werkzeug
# import Werkzeug.

from werkzeug.security import generate_password_hash, check_password_hash

# No need to create an object.

my_password = 'somepassword'

hashed_pass = generate_password_hash(my_password)

print(hashed_pass)

werkzeug_check = check_password_hash(hashed_pass, 'hello')
print("Password Check: {a}".format(a=werkzeug_check))

werkzeug_check = check_password_hash(hashed_pass, 'somepassword')
print("Password Check: {a}".format(a=werkzeug_check))