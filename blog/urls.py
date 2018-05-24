from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('bootstrap/', views.bootstrap, name='bootstrap'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('posts/', views.posts, name='posts'),
    path('view/<int:post_id>', views.post, name='post'),
    path('', views.main, name='main'),
]
