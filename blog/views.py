from django.shortcuts import render

from .models import CustomUser

# Create your views here.
from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
# Create your views here.
from django.conf import settings
from .models import Comment
from .models import Category
from .models import Post

User = settings.AUTH_USER_MODEL

def home (request) :
    # index
    return render(request ,'index.html' )

def usres (request) :
    return render(request ,'users.html' , {'allUser' : CustomUser.objects.all} )
def comments (request) :
    return render(request ,'comments.html' , {'allcomments' : Comment.objects.all} )
def blogs (request) :
    return render(request ,'blogs.html', {'allPost' : Post.objects.all})
def blogdetails (request, ID) :
    blog = get_object_or_404(Post, pk=ID)
    return render(request, 'blogdetails.html', {'blog': blog})
def categories (request) :
    return render(request ,'categories.html' , {'allcategories' : Category.objects.all} )
