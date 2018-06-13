from django.contrib import admin
from panel.models import Askroom
from panel.models import QuestionsVote
from panel.models import Question
# Register your models here.
admin.site.register(Askroom)
admin.site.register(Question)
admin.site.register(QuestionsVote)
