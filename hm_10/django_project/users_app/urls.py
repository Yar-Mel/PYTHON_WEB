from django.urls import path
from . import views

app_name = "users_app"

urlpatterns = [
    path('signup/', views.signup_user, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/<username>/', views.profile, name='profile'),
]
