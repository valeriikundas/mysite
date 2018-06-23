from django.urls import path
from django.views.defaults import page_not_found

from . import views

app_name = 'blog'
urlpatterns = [
    path('now/', views.NowView.as_view(), name='now'),
    path('posts/', views.PostsView.as_view(), name='posts'),
    path('contact/', views.contact, name='contact'),
    path('post/<int:pk>', views.PostView.as_view(), name='post'),
    path('', views.main, name='main'),
]
