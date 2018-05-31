import datetime

from django.test import TestCase, Client
from django.utils import timezone
from django.urls import reverse

from .models import Post

# Create your tests here.

class PostModelTests(TestCase):

    def test_not_published_post_should_not_be_shown(self):
        """
        Post that has publishe_date after now should not be shown
        """
        time = timezone.now() + datetime.timedelta(days=10)
        future_post = Post(publication_date=time)
        
        client = Client()
        response = client.get(reverse('blog:posts'))

        self.assertIs(response.status_code, 200)
        self.assertIs(len(response.context['posts']), 0)

    
        
