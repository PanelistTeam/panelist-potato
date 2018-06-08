from django.contrib.auth import login
import datetime
from panel.models import Askroom
from .forms import QuestionForm
from .forms import QuestionsVoteForm
from panel.models import User
from panel.models import Question
from panel.models import QuestionsVote
from django.contrib.auth import  authenticate
from django.http import  JsonResponse


class ViewsManager():
    def SignUpManager(self, form, request):
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(request, user)

    def ChooseFormManager(self, request, roomID, checkPOST):
        requestCatcher = request.POST

        requestTranslator = request.POST.get('data1')
        print(requestTranslator)
        tmp = ""
        for j in requestTranslator:
            if(j != "[" and j != "]"):
                tmp += j
        dictData = eval(tmp)
        if 'IdentifyVote' in dictData:
            print("IV")
            form = QuestionsVoteForm(dictData or None)
            if form.is_valid():

                return JsonResponse(self.VoteManager(form, dictData), safe=False)
        elif 'IdentifyQ' in dictData:
            print("IQ")
            form = QuestionForm(request.POST or None)
            if form.is_valid():
                return JsonResponse(self.AddQManager(roomID, form, dictData), safe=False)

        elif 'IdentifyEdit' in dictData:
            print("IE")
            qst = Question.objects.filter(
                id=dictData['question_id'])
            form = QuestionForm(dictData or None)
            if form.is_valid():
                return JsonResponse(self.EditManager(qst[0], form, dictData['content']), safe=False)
        elif 'IdentifyDelete' in dictData:
            print("ID")
            qst = Question.objects.filter(
                id=dictData['question_id'])
            print(dictData['question_id'])
            form = QuestionForm(dictData or None)
            if form.is_valid():
                return JsonResponse(self.DeleteManager(qst[0]), safe=False)

    def VersionsManager(self, questionID):
        question = Question.objects.filter(id=questionID)
        i = question[0]
        questionsList = []
        while i is not None:
            questionsList.append(i)
            i = i.previous_version
        return questionsList

    def EditManager(self, question, form, content):
        print(content)
        newContent = form.save(commit=False)
        newContent.askroom_id = question.askroom_id
        newContent.submitted_by = question.submitted_by
        newContent.score = question.score
        newContent.time_submitted = question.time_submitted
        newContent.content = content
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
        requestCatcher = request.POST
        print(request.POST)
        requestTranslator = request.POST.get('data1')
        print(requestTranslator)
        tmp = ""
        for j in requestTranslator:
            if(j != "[" and j != "]"):
                tmp += j
        dictData = eval(tmp)
        if('IdentifyAddRoom' in dictData):
            room = form.save(commit=False)
            room1 = {}
            room.created_by = User.objects.get(id=dictData['created_by'])
            room.time_created = datetime.datetime.now()
            room.description = dictData['description']
            room.title = dictData['title']
            room.public = dictData['public']
            roomcheck = Askroom.objects.filter(
                created_by=room.created_by, title=room.title, description=room.description)
            if(len(roomcheck) == 0):
                room.save()
            else:
                print("Room already exist")
            room1['created_by'] = room.created_by
            room1['time_created'] = room.time_created
            room1['title'] = dictData['title']
            room1['public'] = dictData['public']
            room1['description'] = dictData['description']
            return list(room1)
        else:
            return(self.RemoveRManager(dictData['askroom_id']))

    def RemoveRManager(self, roomID):
        questions = Question.objects.filter(askroom_id=roomID)
        for question in questions:
            print(question)
            votes = QuestionsVote.objects.filter(question_id=question.id)
            for vote in votes:
                vote.delete()
                print(vote)

            question.previous_version = None
            question.current_version = None
            question.save()

        for question in questions:
            question.delete()

        print(roomID)

        room = Askroom.objects.filter(id=roomID)

        room.delete()

    def ShowQManager(self, roomID, request):
        questions = Question.objects.filter(
            askroom_id=roomID, current_version__isnull=True).order_by('-score', '-time_submitted')
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

    def VoteManager(self, form, dictData):

        score = form.save(commit=False)

        qv = QuestionsVote.objects.filter(user_id=User.objects.get(
            id=dictData['user_id']), question_id=dictData['question_id'])
        score.user_id = User.objects.get(
            id=dictData['user_id'])
        score.value = dictData['voting']

        if(qv is None):
            score.save()
        else:
            print("Already voted")
            qv.delete()
            score.save()
        score1 = Question.objects.filter(id=score.question_id.id).values()
        print(list(score1))
        return list(score1)

    def AddQManager(self, roomID, form, dictData):

        question = form.save(commit=False)
        question.time_submitted = datetime.datetime.now()
        question.askroom_id = Askroom.objects.get(id=roomID)
        question.score = 0
        question.submitted_by = User.objects.get(
            id=dictData['created_by'])
        question.content = dictData['content']
        qstn = Question.objects.filter(submitted_by=User.objects.get(
            id=dictData['created_by']), content=dictData['content'])

        if(len(qstn) == 0):
            question.save()
        else:
            print("Already posted")
        question1 = Question.objects.filter(id=question.id).values()
        # question.save()
       # context = {'form': question, 'roomID': roomID}
        print(list(question1))
        return list(question1)
