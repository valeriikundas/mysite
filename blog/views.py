from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth.models import User
from django.views import generic
from django.views.defaults import page_not_found

from .models import Post


class AboutView(generic.TemplateView):
    template_name = 'blog/about.html'


# @login_required
def main(request):
    #if not request.user.is_authenticated:
        #return page_not_found(request, "LOL:)")
     #   return redirect('{0}?next={1}'.format(settings.LOGIN_URL, request.path))

    #username = request.POST['username']
    #password = request.POST['password']
    #user = authenticate(request, username=username, password=password)
    #user = User.objects.all()[0]
    #if user:
        #login(request, user)

    return render(request, "blog/main.html")


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
    paginate_by = 10


def projects(request):
    return render(request, 'blog/projects.html')


def contact(request):
    return render(request, 'blog/contact.html')
