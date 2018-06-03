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
from django.views.decorators.csrf import csrf_exempt
# For sign up
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

Manager = ViewsManager()


def ShowVersions(request, roomID, questionID):

    return render(request, 'panel/ShowVersions.html', {'roomID': roomID, 'questions': Manager.VersionsManager(questionID)})


def home(request):
    return render(request, 'panel/home.html')


@csrf_exempt
def search(request):
    rooms = Askroom.objects.filter(public='True').order_by('title')

    if request.method == 'POST':
        form = AskroomForm(request.POST or None)
        if form.is_valid():
            context = {'form': Manager.SearchManager(
                form, request), 'rooms': rooms}
            return JsonResponse(Manager.SearchManager(
                form, request), safe=False)

    return render(request, 'panel/search.html', {'rooms': rooms})

@csrf_exempt
def ShowQuestions(request, roomID):
    if request.method == 'POST':
        return Manager.ChooseFormManager(request, roomID,request.POST)
        
    print("Test")
    return render(request, 'panel/Questions.html', Manager.ShowQManager(roomID, request))


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            Manager.SignUpManager(form, request)
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
