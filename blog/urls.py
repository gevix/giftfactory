from django.urls import path
from .views import BlogPostView, IndexView, CategoryView, AuthorView


urlpatterns = [
        path('', IndexView.as_view(), name='home'),
        path('author/marie', AuthorView, name='author'),
        path('<slug:slug>', BlogPostView.as_view(), name='blogpost'),
        path('category/<slug:slug>', CategoryView.as_view(), name='category'),

    ]
