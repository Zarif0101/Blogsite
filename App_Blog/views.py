from django.shortcuts import render

# Create your views here.

def Blog_list(request):
    return render(request,'App_Blog/Blog_list.html', context={})