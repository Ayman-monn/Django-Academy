from django import forms
from blog.models import Post, Comment 
from ckeditor.widgets import CKEditorWidget
from django.utils.translation import gettext as _ 



attrs= {'class': 'form-control'}

class PostCreateForm(forms.ModelForm): 
    class Meta: 
        model = Post
        fields = ['title', 'content', 'image']
        labels = {
            'title': _('Title'),
            'content': _('Content'),
            'image': _('Image'),
        }
        widgets={
            'title':forms.TextInput(attrs=attrs), 
            'content':forms.CharField(widget=CKEditorWidget(attrs=attrs)),
        }




class PostUpdateForm(forms.ModelForm): 
    class Meta: 
        model = Post
        fields = ['title', 'content', 'image']
        labels = {
            'title': _('Title'),
            'content': _('Content'),
            'image': _('Image'),
        }
        widgets={
            'title':forms.TextInput(attrs=attrs), 
            'content':forms.CharField(widget=CKEditorWidget(attrs=attrs)) 
        }