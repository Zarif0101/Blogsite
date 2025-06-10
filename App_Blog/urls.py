from django.urls import path
from . import views

app_name = 'App_Blog'
urlpatterns = [
    path("", views.Blog_list, name="blog_list"),
    
]