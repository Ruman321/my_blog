from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

#if you specify the link as href="{% url 'blog_app:index' %}, eable the below line
# app_name = 'blog_app' 

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.post_list, name='post_list'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('create/', views.create_post, name='create_post'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('features/', views.features, name='features'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)