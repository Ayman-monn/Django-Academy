from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.models import Comment, Post 
from blog.forms import PostCreateForm, PostUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin 




class PostListView(ListView): 
    model = Post 
    template_name = 'posts/posts_list.html'
    paginate_by = 6

    def get_queryset(self):
        query = super().get_queryset()
        q = self.request.GET.get('q', None)
        where = {}
        if q:
            where['title__icontains'] = q
        return query.filter(**where)
    
class UserPostListView(ListView): 
    model = Post 
    template_name = 'posts/posts_list.html'
    paginate_by = 3
    def get_queryset(self):
        query = super().get_queryset()
        q = self.request.GET.get('q', None)
        where = {'author': self.request.user}
        if q:
            where['title__icontains'] = q
        return query.filter(**where)
    


class PostDetailView(DetailView): 
    model = Post 
    template_name = 'posts/post_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView): 
    model = Post 
    form_class = PostCreateForm
    template_name = 'posts/post_create.html'
    success_url = reverse_lazy('Posts_list')
    

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): 
    model = Post 
    form_class = PostUpdateForm
    template_name = 'posts/post_update.html'

    def test_func(self):
        return self.get_object().author == self.request.user

    def get_success_url(self):
        return reverse('Post_detail', kwargs={'pk': self.object.id})


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): 
    model = Post 
    template_name = 'posts/post_delete.html' 
    success_url = reverse_lazy('Posts_list')

    def test_func(self):
        return self.get_object().author == self.request.user



class CommentCreateView(LoginRequiredMixin, CreateView): 
    model = Comment
    fields = ['body','post']
    http_method_names = ['post']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self) -> str:
        return reverse('Post_detail', args=[self.object.post.id])

    



