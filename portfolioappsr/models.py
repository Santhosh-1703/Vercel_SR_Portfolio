from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    description=models.TextField(max_length=200)
    def __str__(self):
        return self.name
    
#Python manage.py makemigrations
#python manage.py migrate
