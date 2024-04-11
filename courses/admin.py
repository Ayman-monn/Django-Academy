from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest
from .models import Course, Notification, Section, Lesson, Comment, StudentCourses
from django.db.models import Count 


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin): 
    list_display = ['name', 'image', 'price', 'section_count', 'lesson_count'] 
    list_per_page = 30
    
    def section_count(self, obj): 
        return obj.section_count
    
    def lesson_count(self, obj): 
        return obj.lesson_count

    def get_queryset(self, request):
        query = super().get_queryset(request)
        query = query.annotate(
            section_count=Count('section', distinct=True),
            lesson_count =Count('lesson', distinct=True)
            )
        return query
@admin.register(Section)
class SectionAdmin(admin.ModelAdmin): 
    list_display = ['name', 'course', 'lesson_count'] 
    list_select_related = ['course']
    list_filter = ['course']
    list_per_page = 30

    def lesson_count(self, obj): 
        return obj.lesson_count 
    

    def get_queryset(self, request):
        query = super().get_queryset(request)
        query = query.annotate(lesson_count=Count('lesson', distinct=True))
        return query
        
@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin): 
    list_display = ['name', 'course', 'section', 'comment_count'] 
    list_select_related = ['course', 'section']
    list_filter = ['course', 'section']
    list_per_page = 30 

    def comment_count(self, obj): 
        return obj.comment_count

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        query = super().get_queryset(request)
        query = query.annotate(
            comment_count=Count('comment', distinct=True)
        )
        return query

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin): 
    list_display = ['lesson', 'user','to_user', 'created_at']  
    list_select_related = ['user', 'lesson'] 
    list_per_page = 30 


@admin.register(StudentCourses)
class StudentCoursesAdmin(admin.ModelAdmin): 
    list_display=['user', 'course']
    list_select_related = ['user', 'course']
    list_per_page = 30  

    # def has_add_permission(self, request: HttpRequest) -> bool:
    #     return False
    # def has_change_permission(self, request: HttpRequest, obj: Any | None = ...) -> bool:
    #     return False 
    # def has_delete_permission(self, request: HttpRequest, obj: Any | None = ...) -> bool:
    #     return False


@admin.register(Notification) 
class NotificationAdmin(admin.ModelAdmin): 
    list_display = ['from_user', 'to_user', 'lesson','comment', 'is_seen', 'created_at']
    list_select_related = ['from_user', 'lesson', 'comment']
    list_editable = ['is_seen']
    

    

