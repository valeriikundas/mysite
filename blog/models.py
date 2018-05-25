from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.CharField(max_length=100, blank=True)
    created_date = models.DateTimeField('date created', auto_now=True)
    publication_date = models.DateTimeField(
        'date published', blank=True, null=True)
    views_count = models.IntegerField(default=0, blank=True)
    image_url = models.URLField(blank=True)
    tags = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)

    def is_published(self):
        return self.publication_date != None and self.publication_date <= timezone.now()
    is_published.boolean = True


class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
