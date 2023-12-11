from django.urls import path
from . import views

urlpatterns = [
    path('blogdetails/<int:ID>/', views.blogdetails, name='blogdetails'),
    path('',views.home , name= 'home'),
    path('usres',views.usres , name='usres'),
    path('comments',views.comments, name='comments'),
    path('blogs',views.blogs,name='blogs'),
    path('categories',views.categories,name='categories')
    
]