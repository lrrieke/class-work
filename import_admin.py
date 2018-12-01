from user import User 
from user import Admin
from user import Privileges

lena = Admin('lena', 'rieke', 'las vegas', 28)
lena_privileges = ['can post', 'can delete post', 'can add user', 'can ban user']

lena.privileges.privileges = lena_privileges

lena.privileges.show_privileges()