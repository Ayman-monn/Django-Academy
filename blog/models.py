from django.db import models
from django.contrib.auth.models import User 
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models.signals import post_save



class Post(models.Model): 
    title = models.CharField(max_length=155)
    image = models.ImageField(upload_to='posts/', null=True)
    content = RichTextUploadingField() 
    
    author = models.ForeignKey(User, on_delete=models.PROTECT) 
    slug = models.SlugField() 

    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 

    
    def save(self, *args, **kwargs):
        if not self.slug: 
            self.slug = slugify(self.title) 
        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ('-created_at', )

        
    def __str__(self) -> str:
        return self.title 
    


class Comment(models.Model): 
    body = models.TextField() 

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_comment') 
    post = models.ForeignKey(Post, on_delete=models.CASCADE) 

    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 


    def __str__(self): 
        return self.body     
    


