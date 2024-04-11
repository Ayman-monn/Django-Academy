from django.urls import include, path 
from django.contrib.auth.views import LoginView
from accounts.forms import UserLoginForm
from accounts.views import RegisterView, edit_profile, registration_success



urlpatterns = [
    path('login/', LoginView.as_view(authentication_form=UserLoginForm), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', edit_profile, name='profile'),
    path('register/success/', registration_success, name='register/success'),
    path('', include('django.contrib.auth.urls')), 
]
