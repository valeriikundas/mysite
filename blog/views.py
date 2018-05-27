from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from django.utils import timezone
from django.core.paginator import Paginator

from .models import Post

# Create your views here.


class AboutView(generic.TemplateView):
    template_name = 'blog/about.html'


class MainView(generic.TemplateView):
    template_name = 'blog/main.html'


class PostView(generic.DetailView):
    model = Post
    template_name = 'blog/post.html'

    def get_object(self):
        object = super().get_object()
        object.views_count += 1
        object.save()
        return object

    def get_queryset(self):
        return Post.objects.filter(publication_date__lte=timezone.now())


class PostsView(generic.ListView):
    model = Post
    template_name = 'blog/posts.html'
    context_object_name = 'posts'
    queryset = Post.objects.filter(
        publication_date__lte=timezone.now()).order_by('-publication_date')
    paginate_by = 1


'''
def posts(request):
    #posts = Post.objects.filter(publication_date__lte=timezone.now()).order_by('-publication_date')
    posts = Post.objects.all()
    page = request.GET.get('page', 1)
    #page = 2

    paginator = Paginator(posts, 2)
    posts = paginator.get_page(page)

    return render(request, 'blog/posts.html', {'posts': posts})
'''


def projects(request):
    return render(request, 'blog/projects.html')


def contact(request):
    return render(request, 'blog/contact.html')
