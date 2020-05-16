from django.db import models
from django.core import validators

# Create your models here.

class Users(models.Model):

    #if you don't have the string representation then you will see user as the
    #name in admin site for each user.
    def __str__(self):
        return self.first_name + " " + self.last_name

    first_name = models.CharField(max_length=30, validators=[validators.MinLengthValidator(0)])
    last_name = models.CharField(max_length=20, validators=[validators.MinLengthValidator(0)])
    email = models.EmailField(max_length=254, unique=True, validators=[validators.validate_email]) #don't forget the unique thing
