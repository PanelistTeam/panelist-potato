"""panelist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url, include
from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import ListView, DetailView

from . import views
from . import views as core_views
#from mysite.core import views as core_views
urlpatterns = [

    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^$', views.home, name='home'),
    url(r'^search/', views.search, name='search'),
    #url(r'^add/', views.addRoom, name='AddRoom'),
    path('ShowQuestions/<int:roomID>/',
         views.ShowQuestions, name='ShowQuestions'),
    path('<int:roomID>/ShowVersions/<int:questionID>/',
         views.ShowVersions, name='ShowQuestion'),
]
