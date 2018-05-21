from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('blog/', views.posts, name='posts'),
    path('about/', views.about, name='about'),
    path('view/<int:post_id>', views.view_post, name='view_post'),
    path('', views.main, name='main'),
]
