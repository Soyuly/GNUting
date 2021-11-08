from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from account.models import Account
from django.contrib import auth
from .models import Campus_Date

# Create your views here.


def main(request):
    return render(request, 'main.html')


@login_required
def main_login(request, user_id):
    user = get_object_or_404(Account, pk=user_id)
    if request.user.is_authenticated:
        print('성공')
        return render(request, 'main.html', {'user': user})

def date_main(request):
    return render(request, 'date_main.html')

def date_detail(request):
    return render(request, 'date_detail.html')

def date_write(request):
    mbti = ["ISTJ", "ISFJ", "INFJ", "INTJ", "ISTP", "ISFP", "INFP", "INTP",
            "ESTP", "ESFP", "ENFP", "ENTP", "ESTJ", "ESFJ", "ENFJ", "ENTJ"]
    return render(request, 'date_write.html', {'heights': range(140, 191), 'mbti': mbti})


def campus_main(request):
    return render(request, 'campus_main.html')


def campus_detail(request):
    return render(request, 'campus_detail.html')


def campus_write(request):
    return render(request, 'campus_write.html', {'persons': range(1, 11), 'months': range(1, 13), 'days': range(1, 60), 'hours': range(0, 24)})


def create_campus(request):
    campus = Campus_Date()
    campus.title = request.POST['title']
    campus.contents = request.POST['contents']
    campus.major = request.POST['major']
    campus.month = request.POST['month']
    campus.day = request.POST['day']
    campus.hour = request.POST['hour']
    campus.save()
    return render(request, 'campus_write.html')


def mypage(request, user_id):
    user = get_object_or_404(Account, pk=user_id)
    if request.user.is_authenticated:
        print('성공')
        return render(request, 'mypage.html', {'user': user})
