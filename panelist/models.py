from django.db import models


class Users(models.Model):
    display_name = models.CharField(max_length=126)
    full_account = models.NullBooleanField()
    member_since = models.DateTimeField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)

class Askrooms(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    my_type = models.IntegerField(blank=True, null=True) 
    public = models.NullBooleanField()
    time_created = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=840, blank=True, null=True)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)

class Questions(models.Model):
    askroom_id = models.ForeignKey('Askrooms', models.DO_NOTHING, db_column='askroom_id', blank=True, null=True)
    submitted_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='submitted_by', blank=True, null=True)
    time_submitted = models.DateTimeField(blank=True, null=True)
    current_version = models.ForeignKey('self', models.DO_NOTHING, db_column='current_version', blank=True, null=True)
#   Conflict in DB   
#    previous_version = models.ForeignKey('self',related_name='previous_version', models.DO_NOTHING, db_column='previous_version', blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=840, blank=True, null=True)
    content = models.CharField(max_length=840, blank=True, null=True)  

class QuestionsVotes(models.Model):
    question_id = models.ForeignKey('Questions', models.DO_NOTHING, db_column='question_id', blank=True, null=True)
    user_id = models.ForeignKey('Users', models.DO_NOTHING, db_column='user_id', blank=True, null=True)
    value = models.NullBooleanField()

class Privileges(models.Model):
    user_id = models.ForeignKey('Users', models.DO_NOTHING, db_column='user_id', blank=True, null=True)
    askroom_id = models.ForeignKey('Askrooms', models.DO_NOTHING, db_column='askroom_id', blank=True, null=True)
    access_level = models.IntegerField(blank=True, null=True)