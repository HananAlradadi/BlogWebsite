
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


 
class CustomUser(AbstractUser):
    id = models.AutoField(primary_key=True) 
    username = models.CharField(max_length=150, unique=True) 
    email = models.EmailField(unique=True)  


class Post (models.Model):
    ID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=250)
    Content = models.TextField()
    Category = models.CharField(max_length=250)
    DatePublished = models.DateField(null=True)
class Comment (models.Model) :
    ID = models.AutoField(primary_key=True)
    Content = models.TextField()
    DatePosted = models.DateField(null=True)
    PostID = models.ForeignKey(Post, default=None, on_delete=models.CASCADE,)
    UserID = models.ForeignKey(CustomUser, default=None, on_delete=models.CASCADE,) 
class Category (models.Model) :
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=250)
