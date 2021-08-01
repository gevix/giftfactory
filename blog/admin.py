from django.contrib import admin
from .models import BlogPost, Button, Category


class ButtonTabularInline(admin.StackedInline):
    model = Button


class BlogPostAdmin(admin .ModelAdmin):
    inlines = [ButtonTabularInline]

    class Meta:
        model = BlogPost


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Category)

