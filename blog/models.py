from django.db import models
from datetime import datetime


class Category(models.Model):
    slug = models.SlugField(max_length=50)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class BlogPost(models.Model):
    date = models.DateField(auto_now=True)
    slug = models.SlugField(max_length=200)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='static/blog')
    description = models.TextField(max_length=5000)
    category = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return self.title


class Button(models.Model):
    url = models.URLField(max_length=50)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='static/blog')
    description = models.TextField(max_length=2000)
    blogPostRelated = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
