from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.CharField(max_length=100)
    created_date = models.DateTimeField('date created', auto_now=True)
    publication_date = models.DateTimeField('date published')
    views_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

