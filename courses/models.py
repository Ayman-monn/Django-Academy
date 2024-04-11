from django.db import models
from django.contrib.auth.models import User 
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import gettext_lazy as _ 
from django.db.models.signals import post_save 


class Course(models.Model):
    name = models.CharField(_('Name'),max_length=155)
    name_en = models.CharField(_('Name_en'),max_length=155, blank=True, null=True)

    image = models.ImageField(_('Image'),upload_to='courses/')
    price = models.FloatField(_('Price')) 
    short_description = models.TextField(_('Short_description')) 
    short_description_en = models.TextField(_('Short_description_en'),blank=True, null=True) 
    description = models.TextField(_('Description'))
    description_en = models.TextField(_('Description_en'), blank=True, null=True)
    info = models.TextField(_('Info'))
    info_en = models.TextField(_('Info_en'),blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self) -> str:
        return self.name 
    class Meta:
        verbose_name = _('Course')
        verbose_name_plural = _('Courses')


class Section(models.Model): 
    name = models.CharField(_('Name') ,max_length=155) 
    name_en = models.CharField(_('Name_en') ,max_length=155, blank=True, null=True) 

    # relational fields 
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 
    class Meta:
        verbose_name = _('Section')
        verbose_name_plural = _('Sections')


    
    def __str__(self): 
        return self.name 
    

class Lesson(models.Model): 
    name = models.CharField(_('Name'),max_length=155) 
    name_en = models.CharField(_('Name_en'),max_length=155, blank=True, null=True) 
    description = models.TextField(_('Description'),max_length=500, null=True, blank=True) 
    description_en = models.TextField(_('Description_en'),max_length=500, null=True, blank=True) 
    video = models.FileField(_('Video'),upload_to='lessons/') 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 

    # relational fields 
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    class Meta:
        verbose_name = _('Lesson')
        verbose_name_plural = _('Lessons')

    def __str__(self): 
        return self.name 
    

class Comment(models.Model): 
    body = RichTextUploadingField(_('Body')) 
    # relational fields
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE) 
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    to_user = models.CharField(max_length=100, null=True)


    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 
    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')

    def __str__(self): 
        return self.lesson.name + '>' + self.user.username 
    


class StudentCourses(models.Model):     
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    course = models.ForeignKey(Course, on_delete=models.CASCADE) 
    amount_paid = models.FloatField(blank=True, null=True) 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 


class Notification(models.Model): 
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True) 
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True)
    from_user = models.ForeignKey(User, on_delete=models.CASCADE)
    to_user = models.CharField(max_length=100, null=True) 
    is_seen = models.BooleanField(default=False) 

    created_at = models.DateTimeField(auto_now_add=True, null=True) 
    updated_at = models.DateTimeField(auto_now=True, null=True) 
    class Meta: 
        ordering = ['-created_at', 'is_seen']
    def __str__(self): 
        return self.from_user.username



def create_notication(sender, instance, created, **kwargs): 
    if created: 
        Notification.objects.create(
            lesson= instance.lesson,
            comment = instance, 
            from_user = instance.user,
            to_user = instance.to_user
        )
post_save.connect(create_notication, sender=Comment)



