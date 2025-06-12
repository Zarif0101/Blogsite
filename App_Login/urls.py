from django.urls import path
from . import views
app_name = 'App_Login'

urlpatterns = [
    path("signup/", views.sign_up, name="signup"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path('profile/', views.profile, name='profile'),
    path('change_profile/', views.user_change, name='user_change'),
]
