from django.shortcuts import render

# Create your views here.


def date_write(request):
    mbti = ["ISTJ","ISFJ","INFJ","INTJ","ISTP","ISFP","INFP","INTP","ESTP","ESFP","ENFP","ENTP","ESTJ","ESFJ","ENFJ","ENTJ"]
    return render(request, 'date_write.html',{'heights' : range(140,191), 'mbti':mbti})

def campus_write(request):
    return render(request, 'campus_write.html',{'persons':range(1,11), 'months':range(1,13), 'days':range(1,60), 'hours':range(0,24)})

def mypage(request):
    return render(request, 'mypage.html')