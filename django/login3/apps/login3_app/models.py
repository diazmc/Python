from __future__ import unicode_literals
from django.db import models
from django.contrib import messages
from django.forms import extras
import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def register(self, post):
        first_name = post['first_name']
        last_name = post['last_name']
        email = post['email'].lower()
        password = post['password'].encode()
        con_password = post['con_password']

        errors = []

        if len(first_name) < 1:
            errors.append('Name cannot be blank')
        
        if len(last_name) < 1:
            errors.append('Alias needs at least 2 characters')

        if not EMAIL_REGEX.match(email):
            errors.append('Email is not valid!')
        
        if len(password) < 5:
            errors.append('Password needs at least 5 characters')
        elif (con_password != password):
            errors.append('Needs to match password')
            
        if not errors:
            if User.objects.filter(email=email).exists():
                errors.append("Email already exists")
            else:
                hashed = bcrypt.hashpw(password, bcrypt.gensalt())
                user = User.objects.create(first_name=first_name, last_name=last_name, email=email, password=hashed)
                return {"status": True, "data": user}

        return {"status": False, "data": errors}            

    def login(self, post):
        login_email = post['login_email'].lower()
        login_password = post['login_password'].encode()
        errors = []
        
        if len(login_email) < 1:
            errors.append("Email cannot be blank")
        elif not EMAIL_REGEX.match(login_email):
            errors.append('Email is not valid!')
            
        if len(login_password) < 1:
            errors.append("Password cannot be blank")

        if not errors:
            user_list = User.objects.filter(email=login_email)
            if user_list:
                # login_hashed = bcrypt.hashpw(login_password, bcrypt.gensalt())
                hashed = user_list[0].password.encode()
                if bcrypt.checkpw(login_password, hashed):
                    return {"status": True, "data": user_list[0]}
                else:
                    errors.append("Incorrect Password")
                
            else:
                errors.append("No user with email")

        return {"status": False, "data": errors}
            
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    objects = UserManager()

class Poke(models.Model):
    pokes = models.IntegerField(default=0)
    pokee = models.ForeignKey(User, related_name="pokee")
    poker = models.ForeignKey(User, related_name="poker") 
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    

