from django.contrib import admin
from panel.models import Askrooms
from panel.models import QuestionsVotes
from panel.models import Questions
# Register your models here.
admin.site.register(Askrooms)
admin.site.register(Questions)
admin.site.register(QuestionsVotes)