from django import forms
from courses.models import Comment 
from ckeditor.widgets import CKEditorWidget
from django.utils.translation import gettext as _ 



attrs = {'class':'form-control', 'required':True}


class CommentForm(forms.ModelForm): 
    class Meta: 
        model = Comment
        fields = ['body']
        labels = {
            'body': _('Body') 
        }
        widgets={
            'body': forms.CharField(widget=CKEditorWidget(attrs=attrs))
        }
        
