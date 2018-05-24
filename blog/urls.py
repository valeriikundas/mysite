from django.urls import path
from django.views.defaults import page_not_found

from . import views

app_name = 'blog'
urlpatterns = [
    # path('bootstrap/', views.bootstrap, name='bootstrap'),
    path('about/', views.about, name='about'),
    # path('projects/', views.projects, name='projects'),
    path('posts/', views.posts, name='posts'),
    path('contact/', views.contact, name='contact'),
    path('post/<int:post_id>', views.post, name='post'),
    path('', views.main, name='main'),
]
