from django.contrib import admin
from . models import Category
from . models import Comment
from . models import Post
from . models import CustomUser
# Register your models here.

admin.site.register([Category,Comment,Post,CustomUser])
