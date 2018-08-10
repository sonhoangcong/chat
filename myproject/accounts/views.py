from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def home(request):
	return render(request, 'accounts/home.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request, 'accounts/login.html',{'error':'Tên đăng nhập hoặc mật khẩu không đúng.'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error':'Tên đăng nhập đã tồn tại'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request,user)
                return redirect('index')
        else:
            return render(request, 'accounts/signup.html', {'error':'Mật khẩu phải khớp với mật khẩu xác nhận'})
    else:
        return render(request, 'accounts/signup.html')

