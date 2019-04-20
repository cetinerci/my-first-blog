from django.contrib import admin
from .models import Post

admin.site.register(Post)

# Register your models here.git init Initialized empty Git repository in ~/djangogirls/.git/
from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html', {})
