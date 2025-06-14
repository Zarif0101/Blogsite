from django.contrib import admin
from django.urls import path, include
from BlogSite import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('App_Login.urls')),
    path('blog/', include('App_Blog.urls')),
    path('', views.Index, name='Index'),
]
