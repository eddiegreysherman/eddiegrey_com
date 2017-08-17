from blog.common.database import Database
from faker import Faker

Database.initialize()

fake = Faker()

print(fake.name())

for x in range(10):
     Database.insert('users', {
         "username": "user{}".format(x),
         "fullname": fake.name()
     })


