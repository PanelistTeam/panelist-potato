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

class ViewsManager():
    def VersionsManager(self,questionID):
        question = Question.objects.filter(id=questionID)
        i = question[0]
        questionsList = []
        while i is not None:
            questionsList.append(i)
            i = i.previous_version
        return questionsList
    def EditManager(self,question,form):
        
        newContent = form.save(commit=False)
        newContent.askroom_id = question.askroom_id
        newContent.submitted_by = question.submitted_by
        newContent.score = question.score
        newContent.previous_version = question
        newContent.save()    
        prevq = Question.objects.filter(current_version=question)
        for i in prevq:
            i.current_version = newContent
            i.save()
            print("i:")
            print(i)
            print(i.current_version)
        
        question.current_version = newContent
        question.save()

        votes = QuestionsVote.objects.filter(question_id=question.id)
        
        for i in votes:
            i.question_id = newContent
            i.save()
        return question
    def DeleteManager(self,question,form):
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
    def SearchManager(self, form,request):
        room = form.save(commit=False)            
        room.created_by = UserSocialAuth.objects.get(id=request.user.id - 1)
        room.time_created = datetime.datetime.now()
        roomcheck=Askroom.objects.filter(created_by=room.created_by, title=room.title, description=room.description)           
        if(len(roomcheck)==0):
            room.save()
        else:
            print("Room already exist")

        return room
    def ShowQManager(self,roomID,request):  
        questions = Question.objects.filter(
        askroom_id=roomID, current_version__isnull=True).order_by('-score')
        for question in questions:
            score = 0
            votes = QuestionsVote.objects.filter(question_id=question.id)
            for vote in votes:
                score = score + vote.value
            question.score = score
            question.save()

    
        voting = QuestionsVote.objects.filter(
        user_id=UserSocialAuth.objects.get(id=request.user.id - 1))
    
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
        ReturnDictionary={'questions': questions, 'roomID': roomID, 'voting': votingIDs2}
        return ReturnDictionary    
    def VoteManager(self,form,request):  
          
        score = form.save(commit=False)
        qv = QuestionsVote.objects.filter(user_id=UserSocialAuth.objects.get(
        id=request.user.id - 1), question_id=request.POST.get('question_id'))
        score.user_id = UserSocialAuth.objects.get(
        id=request.user.id - 1)
                
        if(qv is None):
            score.save()
        else:
            print("Already voted")
            qv.delete()
            score.save()   
    def AddQManager(self,roomID,form,request): 
        question = form.save(commit=False)        
        question.time_submitted = datetime.datetime.now()
        question.askroom_id = Askroom.objects.get(id=roomID)
        question.score = 0
        question.submitted_by = UserSocialAuth.objects.get(
            id=request.user.id - 1)
        question.content=request.POST.get('content')
        question.save()    
        context = {'form': question, 'roomID': roomID}
        return context