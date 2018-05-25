from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


from .models import Post

# Create your views here.

def posts(request):
    return render(request, 'blog/posts_new.html', {'posts': Post.objects.order_by('-publication_date')})
    # return render(request, 'blog/posts.html', {'posts': Post.objects.order_by('-publication_date')})

def about(request):
    return render(request, 'blog/about.html')

def main(request):
    return render(request, 'blog/main.html')

def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.views_count += 1
    post.save()
    return render(request, 'blog/post.html', {'post': post})

def projects(request):
    return render(request, 'blog/projects.html')

def contact(request):
    return render(request, 'blog/contact.html')