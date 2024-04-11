from django.urls import path 
from . import views



urlpatterns = [
    path('', views.courses_list, name="Courses_list"), 
    path('notifications/', views.notification_view, name='notifications'),
    path('course/detail/<int:cid>/', views.course_detial, name="Course_detail"), 
    path('mycourse/', views.my_courses, name="MyCourses"), 
    path('course/sections/<int:cid>/', views.sections, name="Course_section"), 
    path('course/section/lessons/<int:sid>/', views.lesson_list, name="Course_section_lessons"), 
    path('course/section/lessons/lesson/<int:lid>/', views.lesson, name="Lesson"), 
    # path('course/section/lesson/comment/', views.CommentCreateView.as_view(), name="Lesson_comment"), 
]