from django.shortcuts import render

# Create your views here.

from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')
def home(request):
    return render(request, 'login/home.html')