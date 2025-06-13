from django.shortcuts import render
from App_Login.views import pass_change
# Create your views here.

def Blog_list(request):
    return render(request,'App_Blog/Blog_list.html', context={})
