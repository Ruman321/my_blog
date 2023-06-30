from django.urls import path
from . import views

#if you specify the link as href="{% url 'blog_app:index' %}, eable the below line
# app_name = 'blog_app' 

urlpatterns = [
    path('login_user/', views.login_user, name='login'),
    path('logout_user/', views.logout_user, name='logout'),
    path('register_user/', views.register_user, name='register'),
]