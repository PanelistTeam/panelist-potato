# Generated by Django 2.0.5 on 2018-06-03 13:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Askroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('askroom_type', models.IntegerField(blank=True, null=True)),
                ('public', models.NullBooleanField()),
                ('time_created', models.DateTimeField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=840, null=True)),
                ('state', models.IntegerField(blank=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, db_column='created_by', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Privilege',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('askroom_id', models.ForeignKey(blank=True, db_column='askroom_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='panel.Askroom')),
                ('user_id', models.ForeignKey(blank=True, db_column='user_id', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_submitted', models.DateTimeField(blank=True, null=True)),
                ('score', models.IntegerField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=840, null=True)),
                ('content', models.CharField(blank=True, max_length=840, null=True)),
                ('askroom_id', models.ForeignKey(blank=True, db_column='askroom_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='panel.Askroom')),
                ('current_version', models.ForeignKey(blank=True, db_column='current_version', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='current_version+', to='panel.Question')),
                ('previous_version', models.ForeignKey(blank=True, db_column='previous_version', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='previous_version+', to='panel.Question')),
                ('submitted_by', models.ForeignKey(blank=True, db_column='submitted_by', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionsVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(blank=True, null=True)),
                ('question_id', models.ForeignKey(blank=True, db_column='question_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='panel.Question')),
                ('user_id', models.ForeignKey(blank=True, db_column='user_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
