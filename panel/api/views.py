import datetime

from django.http import JsonResponse, HttpResponseForbidden, HttpResponseBadRequest

from models import AuthUser
from panel.models import Askroom, Question, QuestionsVote


def askrooms(request):
    rooms = Askroom.objects.filter(public='True')
    askroom_dict = {}
    for room in rooms:
        askroom_dict[room.id] = {
            'title': room.title,
            'type': room.askroom_type,
            'public': room.public,
            'time_created': room.time_created,
            'description': room.description,
            'created_by': room.created_by.id
            if room.created_by is not None else None,
            'state': room.state
        }
    response = {
        'askrooms': askroom_dict
    }
    return JsonResponse(response)


def questions(request, room_id):
    question_list = Question.objects.filter(askroom_id=room_id)
    question_list = [x for x in question_list if x.current_version.id == x.id]
    question_dict = {}
    for question in question_list:
        question_dict[question.id] = {
            'askroom_id': question.askroom_id.id,
            'submitted_by': question.submitted_by.id
            if question.submitted_by is not None else None,
            'time_submitted': question.time_submitted,
            'current_version': question.current_version.id,
            'previous_version': question.previous_version.id
            if question.previous_version is not None else None,
            'score': question.score,
            'content': question.content
        }
    response = {
        'questions': question_dict
    }
    return JsonResponse(response)


def votes(request, user_id):
    vote_list = QuestionsVote.objects.filter(user_id=user_id)
    votes_dict = {}
    for vote in vote_list:
        votes_dict[vote.id] = {
            'question_id': vote.question_id.id,
            'user_id': vote.user_id.id
            if vote.user_id is not None else None,
            'value': vote.value
        }
    response = {
        'votes': votes_dict
    }
    return JsonResponse(response)


def askroom(request, room_id):
    room = Askroom.objects.get(id=room_id)
    askroom_dict = {room.id: {
        'title': room.title,
        'type': room.askroom_type,
        'public': room.public,
        'time_created': room.time_created,
        'description': room.description,
        'created_by': room.created_by.id
        if room.created_by is not None else None,
        'state': room.state
    }}
    response = {
        'askrooms': askroom_dict
    }
    return JsonResponse(response)


def create_askroom(request):
    user = request.POST.get('authuser')
    if user is None:
        return HttpResponseForbidden()
    elif request.method == 'POST':
        askroom_dict = request.POST.get('askroom')
        if askroom_dict is not None:
            room = Askroom(
                title=askroom_dict.get('title'),
                askroom_type=askroom_dict.get('type'),
                public=askroom_dict.get('public'),
                time_created=datetime.datetime.now(),
                description=askroom_dict.get('description'),
                created_by=AuthUser.objects.get(username=user)
            )
            roomcheck = Askroom.objects.filter(
                created_by=room.created_by,
                title=room.title,
                description=room.description
            )
            if len(roomcheck) == 0:
                room.save()
                return JsonResponse({'result': 'success'})
            else:
                return JsonResponse({'result': 'askroom_exists'})
        else:
            return HttpResponseBadRequest()
    else:
        return HttpResponseBadRequest()


def question(request, question_id):
    question_list = Question.objects.filter(current_version=question_id)
    question_dict = {}
    for question in question_list:
        question_dict[question.id] = {
            'askroom_id': question.askroom_id.id,
            'submitted_by': question.submitted_by.id
            if question.submitted_by is not None else None,
            'time_submitted': question.time_submitted,
            'current_version': question.current_version.id,
            'previous_version': question.previous_version.id
            if question.previous_version is not None else None,
            'score': question.score,
            'content': question.content
        }
    response = {
        'questions': question_dict
    }
    return JsonResponse(response)


def add_question(request):
    user = request.POST.get('authuser')
    if user is None:
        return HttpResponseForbidden()
    elif request.method == 'POST':
        question_dict = request.POST.get('question')
        if question_dict is not None:
            question = Question(
                askroom_id=Askroom.objects.get(id=question_dict.get('askroom_id')),
                submitted_by=AuthUser.objects.get(username=user),
                time_submitted=datetime.datetime.now(),
                current_version=None,
                previous_version=None,
                score=0,
                content=question_dict.get('content')
            )
            questioncheck = Question.objects.filter(
                askroom_id=question.askroom_id,
                submitted_by=question.submitted_by,
                content=question.content
            )
            if len(questioncheck) == 0:
                question.save()
                question.current_version = question
                question.save()
                return JsonResponse({'result': 'success'})
            else:
                return JsonResponse({'result': 'askroom_exists'})
        else:
            return HttpResponseBadRequest()
    else:
        return HttpResponseBadRequest()


def vote(request, question_id, value):
    user = request.POST.get('authuser')
    if user is None:
        return HttpResponseForbidden()
    elif request.method == 'POST':
        vote_dict = request.POST.get('vote')
        if vote_dict is not None:
            votecheck = QuestionsVote.objects.filter(
                question_id=Question.objects.get(id=vote_dict.get('question_id')),
                user_id=AuthUser.objects.get(username=user)
            )
            if len(votecheck) == 0:
                vote = QuestionsVote(
                    question_id=Question.objects.get(id=vote_dict.get('question_id')),
                    user_id=AuthUser.objects.get(username=user),
                    value=vote_dict.get('value')
                )
                vote.save()
            else:
                vote = votecheck.first()
                vote.value = vote_dict.get('value')
                vote.save()
        else:
            return HttpResponseBadRequest()
    else:
        return HttpResponseBadRequest()