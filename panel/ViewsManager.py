from django.contrib.auth import login
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
from django.core import serializers
from django.contrib.auth import login, authenticate
from django.http import HttpResponse, JsonResponse
import json
class ViewsManager():
    def SignUpManager(self,form,request):
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(request, user)
    def ChooseFormManager(self, request, roomID,checkPOST):
        z=request.POST
        print(z)
        print(z['data1'])
        temp=request.POST.get('data1')
        k=""
        for j in temp:
            if(j!="[" and j!="]" ):
                k+=j
        temp1=eval(k)
        if 'IdentifyVote' in temp1:
            print("IV")
            form = QuestionsVoteForm(temp1 or None)
            if form.is_valid():
                z=JsonResponse(self.VoteManager(form, temp1),safe=False)
                print(z)                
                return z
        elif 'IdentifyQ' in temp1:
            print("IQ")
            form = QuestionForm(request.POST or None)
            if form.is_valid():
                return JsonResponse(self.AddQManager(roomID, form, temp1),safe=False)

        elif 'IdentifyEdit' in temp1:
            print("IE")
            qst = Question.objects.filter(
                id=temp1['question_id'])
            form = QuestionForm(temp1 or None)
            if form.is_valid():
                return JsonResponse(self.EditManager(qst[0], form),safe=False)
        elif 'IdentifyDelete' in temp1:
            print("ID")
            qst = Question.objects.filter(
                id=temp1['question_id'])
            print(temp1['question_id'])
            form = QuestionForm(temp1 or None)
            if form.is_valid():
                return JsonResponse(self.DeleteManager(qst[0]),safe=False)

    def VersionsManager(self, questionID):
        question = Question.objects.filter(id=questionID)
        i = question[0]
        questionsList = []
        while i is not None:
            questionsList.append(i)
            i = i.previous_version
        return questionsList

    def EditManager(self, question, form):

        newContent = form.save(commit=False)
        newContent.askroom_id = question.askroom_id
        newContent.submitted_by = question.submitted_by
        newContent.score = question.score
        newContent.time_submitted=question.time_submitted
        newContent.previous_version = question
        contentVerify = Question.objects.filter(
            content=newContent.content, previous_version=newContent.previous_version)
        if(len(contentVerify) == 0):
            newContent.save()
            prevq = Question.objects.filter(current_version=question)
            for i in prevq:
                i.current_version = newContent
                i.save()

            question.current_version = newContent
            question.save()

            votes = QuestionsVote.objects.filter(question_id=question.id)

            for i in votes:
                i.question_id = newContent
                i.save()
        # return question
        else:
            print("Already edited")

    def DeleteManager(self, question):
        votes = QuestionsVote.objects.filter(question_id=question.id)
        for i in votes:
            i.delete()
        questions = Question.objects.filter(current_version=question)
        question.previous_version = None
        question.current_version = None
        question.save()

        for i in questions:
            i.current_version = None
            i.previous_version = None
            i.save()
        for i in questions:
            i.delete()
        question.delete()

    def SearchManager(self, form, request):
        print(request.POST)
        room = form.save(commit=False)
        room1 = {}
        room.created_by = User.objects.get(id=request.user.id)
        room.time_created = datetime.datetime.now()
        roomcheck = Askroom.objects.filter(
            created_by=room.created_by, title=room.title, description=room.description)

        if(len(roomcheck) == 0):
            room.save()
        else:
            print("Room already exist")
        room1['created_by'] = room.created_by
        room1['time_created'] = room.time_created
        room1['title'] = request.POST.get('title')
        room1['description'] = request.POST.get('description')
        return list(room1)

    def ShowQManager(self, roomID, request):
        questions = Question.objects.filter(
            askroom_id=roomID, current_version__isnull=True).order_by('-score','-time_submitted')
        for question in questions:
            score = 0
            votes = QuestionsVote.objects.filter(question_id=question.id)
            for vote in votes:
                score = score + vote.value
            question.score = score
            question.save()

        voting = QuestionsVote.objects.filter(
            user_id=User.objects.get(id=request.user.id))

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
        ReturnDictionary = {'questions': questions,
                            'roomID': roomID, 'voting': votingIDs2}
        return ReturnDictionary

    def VoteManager(self, form, temp1):
       
        score = form.save(commit=False)
        print(score)
        #score.value=temp1['value']
        qv = QuestionsVote.objects.filter(user_id=User.objects.get(
            id=temp1['user_id']), question_id=temp1['question_id'])
        score.user_id = User.objects.get(
            id=temp1['user_id'])
        score.value=temp1['voting']
        print(score)
        if(qv is None):
            score.save()
        else:
            print("Already voted")
            qv.delete()
            score.save()
        score1=Question.objects.filter(id=score.question_id.id).values()
        print(list(score1))
        return list(score1)
    def AddQManager(self, roomID, form, temp1):
        question = form.save(commit=False)
        question.time_submitted = datetime.datetime.now()
        question.askroom_id = Askroom.objects.get(id=roomID)
        question.score = 0
        question.submitted_by = User.objects.get(
            id=temp1['social_created_by'])
        question.content = temp1['content']
        qstn = Question.objects.filter(submitted_by=User.objects.get(
            id=temp1['social_created_by']), content=temp1['content'])
       
        if(len(qstn) == 0):
            question.save()
        else:
            print("Already posted")
        question1=Question.objects.filter(id=question.id).values()
        # question.save()
       # context = {'form': question, 'roomID': roomID}
        print(list(question1))
        return list(question1)
