from django.shortcuts import render, redirect, get_object_or_404
from .models import Account
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError

# Create your views here.


def login(request):
    return render(request, 'login.html')


def login_backend(request):
    username = request.POST['id']
    password = request.POST['password']
    user = auth.authenticate(request, username=username, password=password)
    if user is not None:
        auth.login(request, user)
        print(user.id)
        return redirect('main/'+str(request.user.id))
    else:
        error = 1
        print(error)
        return render(request, 'login.html', {'error': error})


def logout_backend(request):
    auth.logout(request)
    return redirect('main_logout')


def signup(request):
    return render(request, 'sign_up.html')


def signup_backend(request):
    if request.method  == 'POST':
        account = Account()
        account.name = request.POST['name']
        account.nickname = request.POST['nickname']
        account.major = request.POST['major']
        account.birth = request.POST['birth']
        account.gender = request.POST['gender']

        if User.objects.filter(username=request.POST['id']).exists():
            error = 1
            return render(request, 'sign_up.html', {'error': error})
            
        account.user = User.objects.create_user(
        username=request.POST['id'], password=request.POST['password'])
        account.save()
        print('회원가입')
    user = auth.authenticate(
        request, username=request.POST['id'], password=request.POST['password'])

    if account is not None:
        auth.login(request, user)
        return redirect('/main/'+str(request.user.id))
    else:
        error = 1
        return render(request, 'login.html', {'error': error})


def edit_account_backend(request, user_id):
    user = get_object_or_404(Account, pk=user_id)
    if request.method == "POST":
        user.name = request.POST['name']
        user.nickname = request.POST['nickname']
        user.major = request.POST['major']
        user.birth = request.POST['birth']
        user.gender = request.POST['gender']
        user.save()
    return redirect('/mypage/'+str(user_id))


def edit_account(request, user_id):
    user = get_object_or_404(Account, pk=user_id)
    return render(request, 'edit_account.html', {'user': user})
