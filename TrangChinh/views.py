from django.shortcuts import render, redirect
from .models import NhatKy
from django.http import HttpResponseRedirect
from .forms import RegistrationForm
from .forms import LoginForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
# Create your views here.

def list(request):
    Data = {"NhatKys": NhatKy.objects.all().order_by("-date")}
    return render(request, "templates1.html", Data)
def post(request, id):
    post = NhatKy.objects.get(id=id)
    return render(request, "templates2.html", {"post": post})
def register(request):
    form = RegistrationForm() 
    if request.method == 'POST':
        form = RegistrationForm(request.POST) 
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/login')
    return render(request, 'templates4.html', {'form': form})
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)  
               
                return redirect('/')  
            else:
             
                error_message = "Đăng nhập không hợp lệ. Vui lòng thử lại."
                return render(request, 'templates3.html', {'form': form, 'error_message': error_message})
    else:
        form = LoginForm()
    return render(request, 'templates3.html', {'form': form})
def logout_view(request):
    logout(request)
    return redirect('/login')
