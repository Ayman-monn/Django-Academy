from django.urls import path 
from blog import views 


urlpatterns = [
    path('posts/', views.PostListView.as_view(), name='Posts_list'), 
    path('myposts/', views.UserPostListView.as_view(), name='MyPosts_list'), 
    path('post/detail/<int:pk>/', views.PostDetailView.as_view(), name='Post_detail'), 
    path('post/create/', views.PostCreateView.as_view(), name='Post_create'), 
    path('post/update/<int:pk>/', views.PostUpdateView.as_view(), name='Post_update'), 
    path('post/delete/<int:pk>/', views.PostDeleteView.as_view(), name='Post_delete'), 
    path('post/create/comment/', views.CommentCreateView.as_view(), name='Comment_create'), 

]
