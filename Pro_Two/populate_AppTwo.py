# configuring the things and setting them up

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Pro_Two.settings')

import django
django.setup()

##FAKER SCRIPT

from faker import Faker
from AppTwo.models import Users

fakegen = Faker()

def make_fake(n=20):

    for i in range(n):
        fake_first_name = fakegen.first_name()
        fake_last_name = fakegen.last_name()
        fake_email = fakegen.email()
        p = Users(first_name=fake_first_name, last_name=fake_last_name, email=fake_email)
        p.save()

if __name__ == '__main__':
    print("$$Creating Fake Users...")
    make_fake()
