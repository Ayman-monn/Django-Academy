import re
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from academy_project import settings
from courses.forms import CommentForm
from .models import Course, Notification, Section, Lesson, Comment, StudentCourses
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required 
from django.views.generic import CreateView


@login_required
def notification_view(request):
    notifications = Notification.objects.select_related('lesson', 'comment', 'from_user').filter(to_user=request.user.username) 
    for noti in notifications:
        noti.is_seen = True
        noti.save() 

    return render(request, 'notification.html')

def courses_list(request):
    query = request.GET.get('query', '')
    where = {}
    if query: 
        where['name__icontains'] = query
        courses = Course.objects.filter(**where) 
    else: 
        courses = Course.objects.all() 
    return render(request, 'index.html',{
        'courses':courses
    })

def course_detial(request, cid): 
    course = Course.objects.get(pk=cid) 


    return render(request, 'course_detail.html',{
        'course':course, 
        'public_key': settings.STRIPE_PUBLIC_KEY
    })


@login_required 
def my_courses(request): 
    courses = StudentCourses.objects.select_related('user', 'course').filter(user=request.user) 
    return render(request, 'courses/my_courses.html', {
        'courses':courses
    })

@login_required
def sections(request, cid):
    course = Course.objects.get(pk=cid) 
    student = StudentCourses.objects.filter(user_id = request.user.id, course_id = course.id)
    if not student: 
        return redirect('Courses_list')
    sections = Section.objects.select_related('course').filter(course=cid) 
    return render(request, 'courses/sections.html', {
        'sections':sections,
        'course_name':course.name,
        'course_name_en':course.name_en
    })


@login_required
def lesson_list(request, sid): 
    course = Course.objects.get(section=sid) 
    student = StudentCourses.objects.filter(user_id = request.user.id, course_id = course.id)
    if not student: 
        return redirect('Courses_list')
    lessons = Lesson.objects.select_related('section').filter(section=sid)
    return render(request, 'courses/lessons_list.html',{
        'lessons':lessons,
        'course_id': course.id,
        'course_name': course.name,
        'course_name_en': course.name_en,
    })

def find_username(body):
    search = re.search('(@)([A-z0-9]+\S[^\W])', body)
    if search:
        return search.group(2)
    else: 
        return False
    


@login_required
def lesson(request, lid): 
    course = Course.objects.get(lesson=lid) 
    student = StudentCourses.objects.filter(user_id = request.user.id, course_id = course.id)
    if not student: 
        return redirect('Courses_list')
    lesson = Lesson.objects.get(pk=lid)
    if request.method =='POST':
        form =CommentForm(request.POST)
        new_comment = form.save(commit=False)
        body = request.POST.get('body')
        username = find_username(body)
        if User.objects.filter(username=username).exists(): 
            new_comment.to_user= username 
        else: 
            new_comment.to_user= 'admin' 
        new_comment.body = body
        new_comment.user = request.user 
        new_comment.lesson = Lesson.objects.get(id=lid)
        new_comment.save() 
        return HttpResponseRedirect(request.path_info)
    else:
        form = CommentForm()
    return render(request, 'courses/lesson.html', {
        'lesson':lesson, 
        'form':form  
    })


    

# class CommentCreateView(CreateView): 
#     model = Comment 
#     form_class = CommentForm
#     http_method_names = ['post']

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         lesson = Lesson.objects.get(pk= self.request.POST.get('lid'))
#         form.instance.lesson = lesson 
#         return super().form_valid(form)
    
#     def get_success_url(self) -> str:
#         return reverse('Lesson', args=[self.object.lesson.id])