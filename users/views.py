from django.shortcuts import render, redirect

from users.api.serializers import UserSerializers
from .models import AbstractUser
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def index_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Login gagal. Silakan periksa kembali username dan password Anda.')
        else:
            messages.error(request, 'Username tidak ditemukan.')

    return render(request, 'auth/login.html')

def index_register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(username=username, password=password)
                u = User.objects.get(id=user.id)
                abs_user = AbstractUser()
                abs_user.user = u
                abs_user.first_name = first_name
                abs_user.last_name = last_name
                abs_user.name = f"{first_name} {last_name}"
                abs_user.save()
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Username sudah digunakan. Silakan pilih username lain.')
        else:
            messages.error(request, 'Password dan konfirmasi password tidak cocok.')
    
    return render(request, 'auth/register.html')

def logout(request):
    if request.method == 'POST':
        request.session.clear()
        return redirect('home')

def index_profile(request):
    user = request.user
    abs_user = AbstractUser.objects.get(user=user)
    srz = UserSerializers(abs_user, many=False)
    if request.method == 'POST':
        abs_user_edit = AbstractUser.objects.get(user=user)
        abs_user_edit.first_name = request.POST.get('first_name')
        abs_user_edit.last_name = request.POST.get('last_name')
        abs_user_edit.name = request.POST.get('name')
        if request.FILES.get('foto'):
            abs_user_edit.foto = request.FILES.get('foto')
        abs_user_edit.save()
        return redirect('profile')
    context = {
        "user": srz.data,
    }
    return render(request, 'user/profile.html', context=context)