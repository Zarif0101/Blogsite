from django.contrib import admin
from django.urls import path, include
from BlogSite import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('App_Login.urls')),
    path('blog/', include('App_Blog.urls')),
    path('', views.Index, name='Index'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)