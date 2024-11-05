from django.db import models

class Login(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    
    def __str__(self):
        return self.email
    
class Create_ak(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    message = models.TextField()
    
    def __str__(self):
        return self.name
    