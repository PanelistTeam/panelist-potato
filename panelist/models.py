from django.db import  models
from django.contrib.auth.models import User
from social_django.models import  UserSocialAuth
"""class User(models.Model):
    display_name = models.CharField(max_length=126)
    full_account = models.NullBooleanField()
    member_since = models.DateTimeField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
"""


class Askroom(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    askroom_type = models.IntegerField(blank=True, null=True) 
    public = models.NullBooleanField()
    time_created = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=840, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, db_column='created_by', blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    
    
class Question(models.Model):
    askroom_id = models.ForeignKey('Askroom', on_delete=models.CASCADE, db_column='askroom_id', blank=True, null=True)
    submitted_by = models.ForeignKey(User, on_delete=models.SET_NULL, db_column='submitted_by', blank=True, null=True)
    time_submitted = models.DateTimeField(blank=True, null=True)
    current_version = models.ForeignKey('self', models.DO_NOTHING, db_column='current_version', blank=True, null=True, related_name='current_version+')
    previous_version = models.ForeignKey('self', models.DO_NOTHING, db_column='previous_version', blank=True, null=True, related_name='previous_version+')
    score = models.IntegerField(blank=True, null=True)
    content = models.CharField(max_length=840, blank=True, null=True)

    def __str__(self):
        return self.content
    
    
class QuestionsVote(models.Model):
    question_id = models.ForeignKey('Question', on_delete=models.CASCADE, db_column='question_id', blank=True, null=True)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, db_column='user_id', blank=True, null=True)
    value= models.IntegerField(blank=True, null=True) 


class Privilege(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id', blank=True, null=True)
    askroom_id = models.ForeignKey('Askroom', on_delete=models.CASCADE, db_column='askroom_id', blank=True, null=True)
    access_level = models.IntegerField(blank=True, null=True)
    
    
    
    
    
    
   



