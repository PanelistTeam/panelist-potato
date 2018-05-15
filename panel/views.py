from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from lazysignup.decorators import allow_lazy_user
from django.http import HttpResponse
from django.contrib.auth import login
#from django.forms import modelformset_factory
import datetime
from social_django.models import UserSocialAuth
from panel.models import Askrooms
from .forms import AskroomsForm
from .forms import QuestionsForm
from panel.models import Users
from panel.models import Questions
from django.shortcuts import get_object_or_404
# Create your views here.
def home(request):
    return render(request, 'panel/home.html')

def Score(request, roomID, questionID):
    questions= Questions.objects.filter(id=questionID)
    return render(request,'panel/Score.html', 'question':questions)
def AddQuestion(request,roomID):
   # question=Questions.objects.filter('askroom_id'==roomID).order_by('score')
    
    form= QuestionsForm(request.POST or None)
    if form.is_valid():
        question = form.save(commit=False)
        #question.submitted_by = request.user.id;
        question.time_submitted=datetime.datetime.now();
        question.askroom_id=Askrooms.objects.get(id=roomID)
        question.score=0
        question.save()       
        print(roomID)
        context= {'form': question, 'id':roomID }
        
        return render(request, 'panel/AddQuestionForm.html', context)
    else:
        return render(request, 'panel/AddQuestionForm.html')
    return render(request, 'panel/Questions.html')
def search(request):
    rooms= Askrooms.objects.order_by('title')
    print ("WTF")
    for i in rooms:
	     print (i.id)
  
    return render(request, 'panel/search.html',{'rooms': rooms})
def ShowQuestions(request,roomID):
    #questions= Questions.objects.order_by('time_submitted')#filter('askroom_id'==roomID).order_by('score')
    questions= Questions.objects.filter(askroom_id=roomID) #get(askroom_id = roomID)
    #user = Users.objects.all()
   # print (questions.get('askroom_id)'))
    for i in questions:
        print(i.id)
        print (i.askroom_id)
        #if(i.askroom_id== roomID):
         #   print("TRUE")
        #else:
         #   print ("FALSE")
        
        #print (i.askroom_id);
    return render(request, 'panel/Questions.html',{'questions': questions, 'id':roomID})
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
    
    
    form= AskroomsForm(request.POST or None)
    if form.is_valid():
        room = form.save(commit=False)
        room.social_created_by = request.user.id;
        room.time_created=datetime.datetime.now();
        room.save()
        print( UserSocialAuth.get_social_auth('google', 26))
        print ("Sth\n")
        print (request.user)
        print (request.user.id)
        #form.save()
        
        context= {'form': room }
        
        return render(request, 'panel/AddRoomForm.html', context)
    else:
          return render(request, 'panel/AddRoomForm.html')
