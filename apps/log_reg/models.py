from __future__ import unicode_literals
from django.db import models
import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UsersManager(models.Manager):
    def register(self, postData):
        name = postData['name']
        alias = postData['alias']
        email = postData['email']
        dob = postData['dob']
        password = postData['password']
        confirm_password = postData['confirm_password']

        flag = False
        errors = []

        if len(name)< 2:
            flag = True
            errors.append('Name must be at least 2 characters')
        if not name.isalpha():
            flag = True
            errors.append('Name can only contain letters')

        if len(alias)< 2:
            flag = True
            errors.append('Alias must be at least 2 characters')

        if not alias.isalpha():
            flag = True
            errors.append('Alias can only contain letters')

        if not dob:
            flag = True
            errors.append('Date of Birth cannot be blank')

        if not email:
            flag= True
            errors.append('Email field cannot be blank')

        if not EMAIL_REGEX.match(email):
            flag = True
            errors.append('Email format is invalid')

        if not password:
            flag= True
            errors.append('Password field cannot be blank')
        if len(password)< 8:
            flag = True
            errors.append('Password must be at least 8 characters')

        if password != confirm_password:
            flag = True
            errors.append('Password confirmation must match password')
        if flag is False:
            # hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            user = Users.objects.create(name =name, alias=alias, email=email, dob= dob, password=password)
            return (flag, user)


        else:
            return (flag, errors)
            # print Users.objects.all()

    def login(self, postData):
        flag= False
        errors=[]

        try:
            log_user = Users.objects.get(email = postData['email'])
        except self.model.DoesNotExist:
            flag = True
            errors.append('Email does not exist in database')
            return errors
        # hashed = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
        # print hashed
        # print log_user.password
        if postData['password']!= log_user.password:
            flag = True
            errors.append('Password is invalid')
            return errors
        else:
            return False


class Users(models.Model):
    name = models.CharField(max_length= 100)
    alias = models.CharField(max_length= 100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    dob = models.DateTimeField(auto_now= False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UsersManager()
