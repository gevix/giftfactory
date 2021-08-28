from django.urls import path
from .views import BlogPostView, IndexView, CategoryView, AuthorView, about_view


urlpatterns = [
        path('', IndexView.as_view(), name='home'),
        path('about', about_view, name='about'),
        path('author/marie', AuthorView.as_view(), name='author'),
        path('<slug:slug>', BlogPostView.as_view(), name='blogpost'),
        path('category/<slug:slug>', CategoryView.as_view(), name='category'),

    ]
