"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from gnuting import views
from django.urls.conf import include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main_logout'),
    path('main/<str:user_id>', views.main_login, name='main'),

    #이상형 게시판 홈페이지
    path('date_main', views.date_main, name='date_main'),
    path('date_detail/<str:date_id>', views.date_detail, name='date_detail'),
    path('date_write', views.date_write, name='date_write'),
    path('date_edit/<str:date_id>', views.date_edit, name='date_edit'),

    #이상형 게시판 백엔드
    path('date_write_backend/<str:user_id>', views.date_write_backend, name='date_write_backend'),
    path('date_remove/<str:date_id>', views.date_remove, name='date_remove'),
    path('comment_delete/<str:comment_id>/<str:date_id>', views.comment_delete, name='comment_delete'),
    path('date_edit_backend/<str:date_id>', views.date_edit_backend, name='date_edit_backend'),
    

    #과팅 게시판 홈페이지
    path('campus_main', views.campus_main, name='campus_main'),
    path('campus_detail/<str:campus_id>/<str:user_id>', views.campus_detail, name='campus_detail'),
    path('campus_comment_delete/<str:comment_id>/<str:campus_id>/<str:user_id>', views.campus_comment_delete, name='campus_comment_delete'),
    path('campus_write', views.campus_write, name='campus_write'),
    path('campus_edit/<str:campus_id>/<str:user_id>', views.campus_edit, name='campus_edit'),

    #과팅 게시판 백엔드
    path('campus_write_backend/<str:user_id>', views.campus_write_backend, name='campus_write_backend'),
    path('campus_remove/<str:campus_id>', views.campus_remove, name='campus_remove'),
    path('campus_edit_backend/<str:campus_id>', views.campus_edit_backend, name='campus_edit_backend'),
    path('mypage/<str:user_id>', views.mypage, name='mypage'),
    path('', include('account.urls')),
]
