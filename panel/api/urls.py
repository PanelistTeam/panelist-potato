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
from django.urls import path

from panel.api import views

urlpatterns = [
    path('askrooms/', views.askrooms, name='askrooms'),
    path('askroom/<int:room_id>/', views.askroom, name='askroom'),
    path('askrooms/create/', views.create_askroom, name='create_askroom'),
    path('questions/<int:room_id>/', views.questions, name='questions'),
    path('question/<int:question_id>/', views.question, name='question'),
    path('question/add/', views.add_question, name='question'),
    path('votes/<int:user_id>/', views.votes, name='questions'),
    path('vote/<int:question_id>/<int:value>/', views.vote, name='vote')
]
