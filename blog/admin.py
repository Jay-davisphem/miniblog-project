from django.contrib import admin

# Register your models here.
from .models import Blogger, Comment, Commenter, Post
reg = (Blogger, Comment, Commenter, Post)
for i in reg:
    admin.site.register(i)

