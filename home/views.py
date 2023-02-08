from django.shortcuts import render

from django.shortcuts import render
from .forms import InputForm


# Create your views here.

from django.http import HttpResponse



def hello(request,*args,**kwargs):
    print(args,kwargs)
    print(request.user)
    return render(request,"index.html")


def home_view(request):
    context ={}
    context['form']= InputForm()
    return render(request, "home.html", context)

# listings/views.py

