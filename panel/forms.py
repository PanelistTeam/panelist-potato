from django import forms
from .models import Askroom
from .models import Question
from .models import QuestionsVote
from social_django.models import  UserSocialAuth
class AskroomForm(forms.ModelForm):
    class Meta:
        model= Askroom
        fields= ["title", "askroom_type", "public", "time_created","description","created_by","state"]
        def __init__(self,user_id,date, *args, **kwargs):
            super(AskroomForm, self).__init__(*args, **kwargs)
            self.created_by = user_id
            self.time_created=date
            
class QuestionForm(forms.ModelForm):
    class Meta:
        model= Question
        fields= ["askroom_id", "submitted_by",  "time_submitted","content"]
        #fields = ['content']
        widgets = {
            'content': forms.TextInput(attrs={
                'id': 'content'
                
            }),}
        """def __init__(self,user_id,date, *args, **kwargs):
            super(QuestionForm, self).__init__(*args, **kwargs)
            self.submitted_by = user_id
            self.time_created=date
           """ 
            
class QuestionsVoteForm(forms.ModelForm):
    class Meta:
        model= QuestionsVote
        fields= ["question_id",  "value"]
        widgets = {
            'value': forms.TextInput(attrs={
                'value': 'post-text', 
                'required': True, 
                'placeholder': 'Say something...'
            }),}
        """
        def __init__(self,date,user_id, *args, **kwargs):
            super(QuestionForm, self).__init__(*args, **kwargs)
            self.user_id = user_id
            self.time_created=date
"""