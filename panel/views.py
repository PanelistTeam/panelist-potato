from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login
#from django.forms import modelformset_factory
import datetime
from social_django.models import UserSocialAuth
from panel.models import Askroom
from .forms import AskroomForm
from .forms import QuestionForm
from .forms import QuestionsVoteForm
from panel.models import User
from panel.models import Question
from social_django.models import UserSocialAuth
from panel.models import QuestionsVote
from django.shortcuts import get_object_or_404
from _overlapped import NULL
from .mixins import AjaxFormMixin
import json
from panel.ViewsManager import ViewsManager
from django.core import serializers

#for TOKEN
import jwt,json
from rest_framework import views
from rest_framework.response import Response
from .models import User


Manager = ViewsManager()


def ShowVersions(request, roomID, questionID):

    return render(request, 'panel/ShowVersions.html', {'roomID': roomID, 'questions': Manager.VersionsManager(questionID)})


def home(request):
    return render(request, 'panel/home.html')


def EditQuestion(request, roomID, questionID):
    qst = Question.objects.filter(id=questionID)
    form = QuestionForm(request.POST or None)
    if form.is_valid():

        return render(request, 'panel/EditQuestion.html', {'roomID': roomID, 'question': Manager.EditManager(qst[0], form)})
    return render(request, 'panel/EditQuestion.html', {'roomID': roomID, 'question': qst[0]})


def DeleteQuestion(request, roomID, questionID):
    qst = Question.objects.filter(id=questionID)
    form = QuestionForm(request.POST or None)
    if form.is_valid():
        Manager.DeleteManager(qst[0], form)

    return render(request, 'panel/DeleteQuestion.html', {'roomID': roomID, 'question': qst[0]})


def AddQuestion(request, rid):

    form = QuestionForm(request.POST or None)
    if form.is_valid():
        return render(request, 'panel/AddQuestionForm.html', Manager.AddQManager(rid, form, request))
    return render(request, 'panel/AddQuestionForm.html', {'roomID': rid})


def search(request):
    rooms = Askroom.objects.filter(public='True').order_by('title')

    if request.method == 'POST':
        form = AskroomForm(request.POST or None)
        if form.is_valid():
            context = {'form': Manager.SearchManager(
                form, request), 'rooms': rooms}
            return render(request, 'panel/search.html', context)

    return render(request, 'panel/search.html', {'rooms': rooms})


def ShowQuestions(request, roomID):
    if request.method == 'POST':
        
        if 'IdentifyVote' in request.POST:
            form = QuestionsVoteForm(request.POST or None)
            if form.is_valid():
                Manager.VoteManager(form, request)
        elif 'IdentifyQ' in request.POST:
            form = QuestionForm(request.POST or None)
            if form.is_valid():
                Manager.AddQManager(roomID, form, request)

        elif 'IdentifyEdit' in request.POST:
            qst = Question.objects.filter(
                id=request.POST.get('qID').replace("/", ""))
            form = QuestionForm(request.POST or None)
            if form.is_valid():
                Manager.EditManager(qst[0], form)
        elif 'IdentifyDelete' in request.POST:
            qst = Question.objects.filter(
                id=request.POST.get('qID').replace("/", ""))
            form = QuestionForm(request.POST or None)
            if form.is_valid():
                Manager.DeleteManager(qst[0], form)
    return render(request, 'panel/Questions.html', Manager.ShowQManager(roomID, request))

    def AddUser(request):

        form = UsernameForm(request.POST or None)
        if form.is_valid():
            return render(request, 'panel/AddQuestionForm.html', Manager.AddQManager(rid, form, request))
        return render(request, 'panel/home.html')

    def signup(request):
        return render(request, 'panel/signup.html')