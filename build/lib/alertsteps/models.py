from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

#Post is the name of the db table 
#Writes into db as sql, super convenient!
class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField() #unrestricted char length
	date_posted = models.DateTimeField(default=timezone.now) #could use auto_now_add=True
	author = models.ForeignKey(User, on_delete=models.PROTECT) #one-to-many relationship, Users can post many while each post has 1 author

	def __str__(self): #"__dunder__" method, allows sql queries to return the title
		return self.title