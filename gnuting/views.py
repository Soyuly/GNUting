from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from account.models import Account
from django.contrib import auth
from .models import Campus_Date, Date

# Create your views here.

#로그인이 안되었을때 main 홈페이지
def main(request):
    return render(request, 'main.html')

#로그인 후 main
@login_required
def main_login(request, user_id):
    user = get_object_or_404(Account, pk=user_id)
    if request.user.is_authenticated:
        print('성공')
        return render(request, 'main.html', {'user': user})

#이상형 게시판
def date_main(request):
    dates = Date.objects.all()
    return render(request, 'date_main.html',{'dates':dates})

def date_detail(request, date_id):
    date = get_object_or_404(Date, pk= date_id)
    return render(request, 'date_detail.html', {'date':date})

def date_write(request):
    mbti = ["ISTJ", "ISFJ", "INFJ", "INTJ", "ISTP", "ISFP", "INFP", "INTP",
            "ESTP", "ESFP", "ENFP", "ENTP", "ESTJ", "ESFJ", "ENFJ", "ENTJ"]
    return render(request, 'date_write.html', {'heights': range(140, 191), 'weights':range(30,110), 'mbti': mbti})

def date_edit(request, date_id):
    mbti = ["ISTJ", "ISFJ", "INFJ", "INTJ", "ISTP", "ISFP", "INFP", "INTP",
            "ESTP", "ESFP", "ENFP", "ENTP", "ESTJ", "ESFJ", "ENFJ", "ENTJ"]
    date = get_object_or_404(Date, pk= date_id)
    return render(request,'date_edit.html',{'date':date, 'heights': range(140, 191), 'weights':range(30,110), 'mbti': mbti})

#이상형 게시판 CRUD 백엔드
def date_write_backend(request):
    date = Date()
    if request.method == "POST":
        date.title = request.POST['title']
        date.contents = request.POST['contents']
        date.height = request.POST['height']
        date.weight = request.POST['weight']
        date.MBTI = request.POST['MBTI']
        date.hobby = request.POST['hobby']
        date.save()
    return redirect('date_detail/' + str(date.id))

def date_remove(request, date_id):
    date = get_object_or_404(Date, pk= date_id)
    date.delete()
    return redirect('/date_main')

def date_edit_backend(request, date_id):
    date = get_object_or_404(Date, pk= date_id)
    if request.method == "POST":
        date.title = request.POST['title']
        date.contents = request.POST['contents']
        date.height = request.POST['height']
        date.weight = request.POST['weight']
        date.MBTI = request.POST['MBTI']
        date.hobby = request.POST['hobby']
        date.save()
    return redirect('/date_detail/' + str(date.id))   

def campus_main(request):
    campuses = Campus_Date.objects.all()
    return render(request, 'campus_main.html',{'campuses':campuses})


def campus_detail(request):
    return render(request, 'campus_detail.html')


def campus_write(request):
    return render(request, 'campus_write.html', {'persons': range(1, 11), 'months': range(1, 13), 'days': range(1, 60), 'hours': range(0, 24)})

def campus_edit(request,campus_id):
    campus = get_object_or_404(Campus_Date, pk= campus_id)
    return render(request, 'campus_edit.html', {'campus':campus, 'persons': range(1, 11), 'months': range(1, 13), 'days': range(1, 60), 'hours': range(0, 24)})


def campus_write_backend(request):
    campus = Campus_Date()
    if request.method == "POST":
        campus.title = request.POST['title']
        campus.contents = request.POST['contents']
        campus.major = request.POST['major']
        campus.count = request.POST['count']
        campus.month = request.POST['month']
        campus.day = request.POST['day']
        campus.hour = request.POST['hour']
        campus.save()
    return redirect('/campus_detail/' + str(campus.id)) 

def campus_remove(request, campus_id):
    campus = get_object_or_404(Campus_Date, pk= campus_id)
    campus.delete()
    return redirect('/campus_main')

def campus_edit_backend(request, campus_id):
    campus = get_object_or_404(Campus_Date, pk= campus_id)
    if request.method == "POST":
        campus.title = request.POST['title']
        campus.contents = request.POST['contents']
        campus.major = request.POST['major']
        campus.count = request.POST['count']
        campus.month = request.POST['month']
        campus.day = request.POST['day']
        campus.hour = request.POST['hour']
        campus.save()
    return redirect('/campus_detail/' + str(campus.id))  
 
def campus_detail(request, campus_id):
    campus = get_object_or_404(Campus_Date, pk= campus_id)
    return render(request, 'campus_detail.html', {'campus':campus})

def mypage(request, user_id):
    user = get_object_or_404(Account, pk=user_id)
    if request.user.is_authenticated:
        print('성공')
        return render(request, 'mypage.html', {'user': user})
