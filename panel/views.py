from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from django.contrib.auth import login
#from django.forms import modelformset_factory
import datetime
from social_django.models import UserSocialAuth
from panel.models import Askrooms
from .forms import AskroomsForm
from .forms import QuestionsForm
from .forms import QuestionsVotesForm
from panel.models import Users
from panel.models import Questions
from social_django.models import  UserSocialAuth
from panel.models import QuestionsVotes
from django.shortcuts import get_object_or_404
from _overlapped import NULL
# Create your views here.
def home(request):
    return render(request, 'panel/home.html')
def SuccessfullSubmission(request,id):
    return render(request,'panel/SuccessfullSubmission.html',{'roomID':id})

def EditQuestion(request,roomID,questionID):
    qst=Questions.objects.filter(id=questionID)
    question=qst[0]
    
    form= QuestionsForm(request.POST or None)
    if form.is_valid():
           
            newContent=form.save(commit=False)
            newContent.askroom_id=question.askroom_id
            newContent.submitted_by=question.submitted_by
            newContent.score=question.score
            newContent.save()
            question.askroom_id=None
            question.save()
            print(question.id)
            print("+++++++++++")
            print(newContent.id)
            
            votes=QuestionsVotes.objects.filter(question_id=question.id)
            print (votes)
            for i in votes:
                i.question_id=newContent
                i.save()
        
        
    return render(request, 'panel/EditQuestion.html',{'roomID':roomID,'question':question})

def DeleteQuestion(request,roomID,questionID):
    qst= Questions.objects.filter(id=questionID)
    question=qst[0]
   
    form= QuestionsForm(request.POST or None)
    if form.is_valid():        
        votes=QuestionsVotes.objects.filter(question_id=question.id)
        for i in votes:
            i.question_id=None
            i.save()
        question.delete()
    
    
    
    return render(request, 'panel/DeleteQuestion.html',{'roomID':roomID, 'question':question})
def AddQuestion(request,rid):
   # question=Questions.objects.filter('askroom_id'==roomID).order_by('score')
    #sd= UserSocialAuth.objects.order_by('id')
    
    form= QuestionsForm(request.POST or None)
    print(form.is_valid())
    print(form.errors)
    if form.is_valid():
        print("--asdas----")
        question = form.save(commit=False)
        #question.submitted_by = request.user.id;
        question.time_submitted=datetime.datetime.now();
        question.askroom_id=Askrooms.objects.get(id=rid)
        question.score=0
        question.submitted_by=UserSocialAuth.objects.get(id=request.user.id-1)
        question.save()       
        #print(UserSocialAuth.objects.get(id=request.user.id-1))
       # print("-------")
        #print(request.user.id)
        context= {'form': question, 'roomID':rid }
        
        return render(request, 'panel/AddQuestionForm.html', context)
    else:
        return render(request, 'panel/AddQuestionForm.html',{'roomID':rid})
    return render(request, 'panel/Questions.html',{'roomID':rid})
def search(request):
    rooms= Askrooms.objects.filter(public='True').order_by('title')
    
   # for i in rooms:	     
         #print ("created by:")
         #print (i.created_by)
         
  
    return render(request, 'panel/search.html',{'rooms': rooms})
def ShowQuestions(request,roomID):
    #form=QuestionsVotesForm(request.Post or None)
    #questions= Questions.objects.order_by('time_submitted')#filter('askroom_id'==roomID).order_by('score')
    questions= Questions.objects.filter(askroom_id=roomID).order_by('-score') #get(askroom_id = roomID)
    
    for question in questions:
        score=0
        votes=QuestionsVotes.objects.filter(question_id=question.id)
        for vote in votes:
            score=score+vote.value
        question.score=score
        question.save()
   # if request.method == 'POST':
    
    
    voting=QuestionsVotes.objects.filter(user_id=request.user.id)
    
    votingIDs=[]
    votingIDs2=[]
    votingValues=[]
    
    if(len(questions)>0):
        for i in voting:
            votingIDs.append(i.question_id)
        
            votingValues.append(i.value)
        print (votingIDs)
        print(votingIDs[0])
        print(votingIDs[0]!=None)
        if(votingIDs[0]!=None):
            for i in votingIDs:
                votingIDs2.append(i.id)
       
    #print(votingIDs2)
    #print(votingValues)
  
    form=QuestionsVotesForm(request.POST or None)
    if form.is_valid():
        
        #print(form.is_valid())
        score=form.save(commit=False)
        form.clean()
       # score.question_id=request.POST.get('question.id') 
       # print (request.POST.get('id'))
        qv=QuestionsVotes.objects.filter(user_id=request.POST.get('user_id'),question_id=request.POST.get('question_id'))
        if(qv==NULL):
            score.save()
        else:
            print("Already voted")
            qv.delete()
            score.save()
        
    
    return render(request, 'panel/Questions.html',{'questions': questions, 'roomID':roomID, 'voting':votingIDs2})
def addRoom(request):
    user = Users.objects.all()
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
    #print(request.user.id)
    k=request.user.id
   # z=UserSocialAuth.objects.get(id=k)
    asdf=UserSocialAuth.objects.order_by("id")
   # print("----------")
 #   print(z)
   # for i in asdf:
       # print (i.id)
    form= AskroomsForm(request.POST or None)
    if form.is_valid():
        room = form.save(commit=False)
       
      
        room.created_by =UserSocialAuth.objects.get(id=request.user.id-1)
        room.time_created=datetime.datetime.now();
        room.save()
      
        #form.save()
        
        context= {'form': room }
        
        return render(request, 'panel/AddRoomForm.html', context)
    else:
          return render(request, 'panel/AddRoomForm.html')
