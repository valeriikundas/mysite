from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from django.utils import timezone

from .models import Post

# Create your views here.


class AboutView(generic.TemplateView):
    template_name = 'blog/about.html'


class MainView(generic.TemplateView):
    template_name = 'blog/main.html'


class PostView(generic.DetailView):
    model = Post
    template_name = 'blog/post.html'

    def get_queryset(self):
        return Post.objects.filter(publication_date__lte=timezone.now())


def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.views_count += 1
    post.save()
    return render(request, 'blog/post.html', {'post': post})


class PostsView(generic.ListView):
    template_name = 'blog/posts.html'
    context_object_name = 'posts'
    model = Post

    def get_queryset(self):
        """
        return the last 3 published posts
        """
        return Post.objects.filter(publication_date__lte=timezone.now()).order_by('-publication_date')[:5]


def projects(request):
    return render(request, 'blog/projects.html')


def contact(request):
    return render(request, 'blog/contact.html')
