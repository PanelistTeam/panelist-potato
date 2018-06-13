from django import template
from panel.models import QuestionsVote
register = template.Library()

@register.simple_tag
def checkvote(userid, questionid):
    for questionvote in QuestionsVote.objects.all():
        tempusername = str(questionvote.user_id)
        tempquestionid = str(questionvote.question_id)
        if tempusername == userid and tempquestionid == questionid:
            return questionvote.value