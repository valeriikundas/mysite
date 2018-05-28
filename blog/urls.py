from django.urls import path
from django.views.defaults import page_not_found

from . import views

app_name = 'blog'
urlpatterns = [
    path('about/', views.AboutView.as_view(), name='about'),
    # path('projects/', views.projects, name='projects'),
    path('posts/', views.PostsView.as_view(), name='posts'),
    path('contact/', views.contact, name='contact'),
    path('post/<int:pk>', views.PostView.as_view(), name='post'),
    path('', views.main, name='main'),
    #path('', views.MainView.as_view(), name='main'),
]
