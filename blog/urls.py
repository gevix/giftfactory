from django.urls import path
from .views import BlogPostView, IndexView, CategoryView


urlpatterns = [
        path('', IndexView.as_view(), name='home'),
        path('<slug:slug>', BlogPostView.as_view(), name='blogpost'),
        path('category/<slug:slug>', CategoryView.as_view(), name='category'),


    ]
