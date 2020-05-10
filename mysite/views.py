from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from . import cleanse as c
def landing(request):
	return render(request,"welcome.html")

class SignUp(generic.CreateView):
  form_class = UserCreationForm
  success_url = reverse_lazy('login')
  template_name = 'signup.html'

def reset(request):
	c.cleanProjects()
	return HttpResponse("Wiped all projects")