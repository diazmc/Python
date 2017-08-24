from __future__ import unicode_literals
from django.db import models
from django.contrib import messages

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def register(self, post):
        first_name = post['first_name']
        last_name = post['last_name']
        email = post['email']
        password = post['password']
        con_password = post['con_password']

        errors = []


        if len(first_name) < 1:
            errors.append('Name cannot be blank')
        
        if len(last_name) < 1:
            errors.append('Alias needs at least 2 characters')

        if len(password) < 5:
            errors.append('Password needs at least 5 characters')

        if not EMAIL_REGEX.match(email):
            errors.append('Email is not valid!')
        
        if (con_password != password):
            errors.append('Needs to match password')

        if User.objects.filter(email=email).exists():
            errors.append("Email already exists")
            
        if not errors:
            user = User.objects.create(first_name=first_name, last_name=last_name, email=email, password=password)
            return {"status": True, "data": user}
        else:
            return {"status": False, "data": errors}            

    def login(self, post):
        login_email = post['login_email']
        login_password = post['login_password']
        user_login = User.objects.filter(email=login_email)
        errors = []
        
        if len(login_email) < 1:
            errors.append("Email cannot be blank")
            
        if len(login_password) < 1:
            errors.append("Password cannot be blank")

        if user_login[0].password != login_password:
            errors.append("Incorrect password")
        
        if not user_login:
            errors.append("Email does not exist")

        if not errors:
            user = User.objects.filter(email=login_email, password=login_password)
            return {"status": True, "data": user}

        else:
            return {"status": False, "data": errors}
            
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    objects = UserManager()