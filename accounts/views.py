from django.http import HttpResponseRedirect
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import redirect, render
from django.urls import resolve, reverse
from django.views.generic import CreateView
from accounts.forms import UserRegisterForm, ProfileForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


class RegisterView(CreateView): 
    form_class = UserRegisterForm 
    template_name = 'registration/register.html'

    def get_success_url(self) -> str:
        login(self.request, self.object) 
        return reverse('register/success')

@login_required
def edit_profile(request): 
    if request.method == 'POST': 
        form = ProfileForm(request.POST ,instance=request.user) 
        if form.is_valid(): 
            form.save()
            return redirect('profile')
        
    else: 
        form = ProfileForm(instance=request.user)
        return render(request,'profile.html', {
            'form':form
        })

from django.utils.deprecation import MiddlewareMixin

class UserRestrictionMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            current_url = resolve(request.path_info).url_name
            # if current_url.startswith('login') or current_url.startswith('register'):
            if current_url== 'login' or current_url == 'register':
                return redirect('Courses_list')

def registration_success(request):
    return render(request, 'success_register.html')