from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from account.models import Account
from django.contrib import auth
from .models import Campus_Date, Date, Comment_Date, Comment_campus
import datetime

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
    dates = Date.objects.order_by('-id')
    return render(request, 'date_main.html',{'dates':dates})

def date_detail(request, date_id):
    date = get_object_or_404(Date, pk= date_id)
    comments = Comment_Date.objects.filter(post = date_id)
    if request.method == "POST":
        comment = Comment_Date()
        comment.post = date
        comment.contents = request.POST['contents']
        comment.user_id = request.user.id
        comment.save()
    return render(request, 'date_detail.html', {'date':date, 'comments':comments})

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
def date_write_backend(request, user_id):
    today = datetime.date.today()
    yyyy = today.year
    date = Date()
    user = get_object_or_404(Account, pk=user_id)
    if request.method == "POST":
        date.title = request.POST['title']
        date.contents = request.POST['contents']
        date.height = request.POST['height']
        date.weight = request.POST['weight']
        date.MBTI = request.POST['MBTI']
        date.hobby = request.POST['hobby']
        date.user_id = request.user.id
        date.gender = user.gender
        date.age = yyyy - user.birth.year + 1
        date.save()
    return redirect('/date_detail/' + str(date.id))

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

def comment_delete(request, comment_id, date_id):
    try:
        comment = Comment_Date.objects.get(pk=comment_id)
    except Comment_Date.DoesNotExist:
        comment = None
    comment.delete()
    return redirect('/date_detail/' + str(date_id))

#과팅 게시판
def campus_main(request):
    campuses = Campus_Date.objects.order_by('-id')
    return render(request, 'campus_main.html',{'campuses':campuses})

def campus_detail(request):
    return render(request, 'campus_detail.html')

def campus_write(request):
    return render(request, 'campus_write.html', {'persons': range(1, 11), 'months': range(1, 13), 'days': range(1, 60), 'hours': range(0, 24)})

def campus_edit(request,campus_id):
    campus = get_object_or_404(Campus_Date, pk= campus_id)
    return render(request, 'campus_edit.html', {'campus':campus, 'persons': range(1, 11), 'months': range(1, 13), 'days': range(1, 60), 'hours': range(0, 24)})

#과팅 게시판 CRUD 백엔드
def campus_write_backend(request, user_id):
    user = get_object_or_404(Account, pk=user_id)
    campus = Campus_Date()
    if request.method == "POST":
        campus.title = request.POST['title']
        campus.contents = request.POST['contents']
        campus.major = request.POST['major']
        campus.count = request.POST['count']
        campus.month = request.POST['month']
        campus.day = request.POST['day']
        campus.hour = request.POST['hour']
        campus.major = user.major
        campus.gender = user.gender
        campus.user_id = request.user.id
        campus.save()
    return redirect('/campus_detail/' + str(campus.id) + '/' + str(user_id))

def campus_remove(request, campus_id):
    campus = get_object_or_404(Campus_Date, pk= campus_id)
    campus.delete()
    return redirect('/campus_main')

def campus_edit_backend(request, campus_id, user_id):
    campus = get_object_or_404(Campus_Date, pk= campus_id)
    if request.method == "POST":
        campus.title = request.POST['title']
        campus.contents = request.POST['contents']
        campus.major = request.POST['major']
        campus.count = request.POST['count']
        campus.month = request.POST['month']
        campus.day = request.POST['day']
        campus.hour = request.POST['hour']
    return redirect('/campus_detail/' + str(campus_id) + '/' + str(user_id))
 
def campus_detail(request, campus_id, user_id):
    campus = get_object_or_404(Campus_Date, pk= campus_id)
    comments = Comment_campus.objects.filter(post = campus_id)
    user = get_object_or_404(Account, pk=user_id)
    if request.method == "POST":
        comment = Comment_campus()
        comment.post = campus
        comment.contents = request.POST['contents']
        comment.major = user.major
        comment.user_id = request.user.id
        comment.save()
    return render(request, 'campus_detail.html', {'campus':campus,'comments':comments})

def campus_comment_delete(request, comment_id, campus_id,user_id):
    try:
        comment = Comment_campus.objects.get(pk=comment_id)
    except Comment_campus.DoesNotExist:
        comment = None
    comment.delete()
    return redirect('/campus_detail/' + str(campus_id) + '/' + str(user_id))

def mypage(request, user_id):
    user = get_object_or_404(Account, pk=user_id)
    if request.user.is_authenticated:
        print('성공')
        return render(request, 'mypage.html', {'user': user})
