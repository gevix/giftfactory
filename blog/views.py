# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import BlogPost, Category


class IndexView(ListView):
    model = BlogPost
    template_name = 'blog/index.html'


class BlogPostView(DetailView):
    model = BlogPost
    template_name = 'blog/post.html'


class CategoryView(DetailView):
    model = Category
    template_name = 'blog/category.html'


class AuthorView(ListView):
    model = BlogPost
    template_name = 'blog/author.html'

# Create your views here.
