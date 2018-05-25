from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
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
# Create your views here.


def ShowVersions(request, roomID, questionID):
    question = Question.objects.filter(id=questionID)
    i = question[0]
    questionsList = []
    while i is not None:
        questionsList.append(i)
        i = i.previous_version

    print(questionsList)
    for j in questionsList:
        print(j.content)
    return render(request, 'panel/ShowVersions.html', {'roomID': roomID, 'questions': questionsList})


def home(request):
    return render(request, 'panel/home.html')


def SuccessfullSubmission(request, id):
    return render(request, 'panel/SuccessfullSubmission.html', {'roomID': id})


def EditQuestion(request, roomID, questionID):
    qst = Question.objects.filter(id=questionID)
    question = qst[0]

    form = QuestionForm(request.POST or None)
    if form.is_valid():

        newContent = form.save(commit=False)
        newContent.askroom_id = question.askroom_id
        newContent.submitted_by = question.submitted_by
        newContent.score = question.score

        newContent.previous_version = question
        newContent.save()
       # newContent.current_version=newContent
        newContent.save()
        prevq = Question.objects.filter(current_version=question)
        for i in prevq:
            i.current_version = newContent
            i.save()
        #question.askroom_id = None
        question.current_version = newContent
        question.save()

        votes = QuestionsVote.objects.filter(question_id=question.id)

        for i in votes:
            i.question_id = newContent
            i.save()

    return render(request, 'panel/EditQuestion.html', {'roomID': roomID, 'question': question})


def DeleteQuestion(request, roomID, questionID):
    qst = Question.objects.filter(id=questionID)
    question = qst[0]
    print(question)
    print(question.previous_version)
    print(question.current_version)
    form = QuestionForm(request.POST or None)
    if form.is_valid():
        votes = QuestionsVote.objects.filter(question_id=question.id)
        for i in votes:
            i.question_id = None
            i.save()
        questions = Question.objects.filter(current_version=question)
        question.previous_version = None
        question.current_version = None
        question.save()
        print(question.previous_version)
        for i in questions:
            i.current_version = None
            i.previous_version = None
            i.save()
        for i in questions:
            i.delete()
        question.delete()

    return render(request, 'panel/DeleteQuestion.html', {'roomID': roomID, 'question': question})


def AddQuestion(request, rid):
   # question=Questions.objects.filter('askroom_id'==roomID).order_by('score')
    #sd= UserSocialAuth.objects.order_by('id')

    form = QuestionForm(request.POST or None)
    print(form.is_valid())
    print(form.errors)
    if form.is_valid():
        print("--asdas----")
        question = form.save(commit=False)
        #question.submitted_by = request.user.id;
        question.time_submitted = datetime.datetime.now()
        question.askroom_id = Askroom.objects.get(id=rid)
        question.score = 0
        question.submitted_by = UserSocialAuth.objects.get(
            id=request.user.id - 1)

        question.save()
       # question.current_version=question
        question.save()
        # print(UserSocialAuth.objects.get(id=request.user.id-1))
       # print("-------")
        # print(request.user.id)
        context = {'form': question, 'roomID': rid}

        return render(request, 'panel/AddQuestionForm.html', context)
    else:
        return render(request, 'panel/AddQuestionForm.html', {'roomID': rid})
    return render(request, 'panel/Questions.html', {'roomID': rid})


def search(request):
    rooms = Askroom.objects.filter(public='True').order_by('title')

   # for i in rooms:
    #print ("created by:")
    #print (i.created_by)

    return render(request, 'panel/search.html', {'rooms': rooms})


def ShowQuestions(request, roomID):

    questions = Question.objects.filter(
        askroom_id=roomID, current_version__isnull=True).order_by('-score')
    for question in questions:
        score = 0
        votes = QuestionsVote.objects.filter(question_id=question.id)
        for vote in votes:
            score = score + vote.value
        question.score = score
        question.save()

    print(questions)
    print(UserSocialAuth.objects.get(id=request.user.id - 1))
    voting = QuestionsVote.objects.filter(
        user_id=UserSocialAuth.objects.get(id=request.user.id - 1))
    print(voting)
    votingIDs = []
    votingIDs2 = []
    votingValues = []
    # print(questions)
    if(len(questions) > 0):
        for i in voting:
            votingIDs.append(i.question_id)

        if(votingIDs):
            for i in votingIDs:
                votingIDs2.append(i.id)

       # print(votingIDs2)
        # print(votingIDs)
        if request.method == 'POST':
            form = QuestionsVoteForm(request.POST or None)
            print(form.is_valid())
            print(form.errors)
            if form.is_valid():

                # print(form.is_valid())
                score = form.save(commit=False)

       # score.question_id=request.POST.get('question.id')
       # print (request.POST.get('id'))
                qv = QuestionsVote.objects.filter(user_id=UserSocialAuth.objects.get(
                    id=request.user.id - 1), question_id=request.POST.get('question_id'))
                score.user_id = UserSocialAuth.objects.get(
                    id=request.user.id - 1)
                print(qv)
                print(qv is None)
                if(qv is None):
                    score.save()
                else:
                    print("Already voted")
                    qv.delete()
                    score.save()

    return render(request, 'panel/Questions.html', {'questions': questions, 'roomID': roomID, 'voting': votingIDs2})


def addRoom(request):
    user = User.objects.all()
    #room = modelformset_factory(Askrooms, fields=('title', 'my_type','public','description'))
    if request.method == 'POST':
        """
            #room=Askrooms()
            print("Trying")
            room_title= request.POST.get('title')
            #room.my_type= request.Askrooms.get('my_type')
            room_public=request.POST.get('public')
            room_description=request.POST.get('description')

            room_time_created=datetime.datetime.now();
            room_created_by=request.POST.get('user.id');
            roomData=Askrooms(title=room_title,my_type='1',public=room_public,time_created=room_time_created,
                              description=room_description, state='1')   
            roomData.save() 
            #return render(request, 'panel/AddRoomForm.html',{'room':room})    
            return render(request, 'panel/AddRoomForm.html')
else:
    return render(request, 'panel/AddRoomForm.html')
"""
    # print(request.user.id)
    k = request.user.id
   # z=UserSocialAuth.objects.get(id=k)
    asdf = UserSocialAuth.objects.order_by("id")
   # print("----------")
 #   print(z)
   # for i in asdf:
    # print (i.id)
    form = AskroomForm(request.POST or None)
    if form.is_valid():
        room = form.save(commit=False)

        room.created_by = UserSocialAuth.objects.get(id=request.user.id - 1)
        room.time_created = datetime.datetime.now()
        room.save()

        # form.save()

        context = {'form': room}

        return render(request, 'panel/AddRoomForm.html', context)
        # return render(request, 'panel/home.html')
    else:
        return render(request, 'panel/AddRoomForm.html')
