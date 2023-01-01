"""idealroom URL Configuration

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
from django.urls import path
from . import views


app_name = 'homepage'

#urlpatterns
urlpatterns = [
    path('', views.top, name='top'),#views.py の関数を実行
    path('myroom/', views.myroom, name='myroom'),#views.py の関数を実行
    #path('', views.top),#追加
    path('coordinator/', views.coordinator, name='coordinator'),#増えた
    path('register/', views.register, name='register'),#増えた
    path('aboutus/', views.aboutus, name='aboutus'),#増えた
    path('contact/', views.contact, name='contact'),#増えた
    path('terms_of_service/', views.terms_of_service, name='terms_of_service'),#増えた
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),#増えた
]
