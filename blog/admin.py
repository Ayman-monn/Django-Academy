from django.contrib import admin
from blog.models import Post, Comment 


@admin.register(Post) 
class PostAdmin(admin.ModelAdmin): 
    list_display = ['title','author', 'id']
    list_select_related = ['author']



@admin.register(Comment) 
class CommentAdmin(admin.ModelAdmin): 
    list_display = ['body', 'user', 'post', 'id']
    list_select_related = ['user', 'post']

