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
    path('date_main', views.date_main, name='date_main'),
    path('date_detail', views.date_detail, name='date_detail'),
    path('date_write', views.date_write, name='date_write'),
    path('campus_main', views.campus_main, name='campus_main'),
    path('campus_detail', views.campus_detail, name='campus_detail'),
    path('campus_write', views.campus_write, name='campus_write'),
    path('mypage/<str:user_id>', views.mypage, name='mypage'),
    path('', include('account.urls')),
]
