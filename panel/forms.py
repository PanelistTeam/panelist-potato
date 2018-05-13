from django import forms
from .models import Askrooms
from .models import Questions
class AskroomsForm(forms.ModelForm):
    class Meta:
        model= Askrooms
        fields= ["title", "my_type", "public", "time_created","description","social_created_by","state"]
        def __init__(self,user_id,date, *args, **kwargs):
            super(AskroomsForm, self).__init__(*args, **kwargs)
            self.created_by = user_id
            self.time_created=date
            
class QuestionsForm(forms.ModelForm):
    class Meta:
        model= Questions
        fields= ["askroom_id", "submitted_by",  "time_submitted"]
        def __init__(self,user_id,date, *args, **kwargs):
            super(QuestionsForm, self).__init__(*args, **kwargs)
            self.submitted_by = user_id
            self.time_created=date