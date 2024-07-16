from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from django.contrib.auth import authenticate,login,logout
from .forms import LoginForm, UserRegistrationForm

# Create your views here.
class Home(LoginRequiredMixin, generic.TemplateView):
    login_url = 'login' 
    template_name = 'account/home.html'


class Login(generic.View):
   
    def get(self,*args, **kwargs):
        form = LoginForm()
        context = {
            'form': form
        }
        return render(self.request,'account/login.html', context )

    def post(self, *args, **kwargs):
        form = LoginForm(self.request.POST)
        if form.is_valid():
            user = authenticate(
                self.request,
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )
            if user:
                login(self.request, user)
                return redirect('home')
            else:
                messages.warning(self.request, "Wrong credentials")
                return redirect('login')

        context = {
            'form': form
        }
        return render(self.request,'account/login.html', context )
    

class Logout(generic.View):
    def get(self, *args, **kwargs):
        logout(self.request)
        return redirect('login')
    

class Registration(generic.CreateView):
    template_name = 'account/registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')