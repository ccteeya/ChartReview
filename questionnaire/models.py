from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Questionnaire(models.Model):
    title = models.CharField(max_length=200)

    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE, related_name='questions')
    question_text = models.CharField(max_length=500)
    is_checkbox = models.BooleanField(default=True)

    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question_text

    def get_questionnaire_title(self):
        return self.questionnaire.title

    def get_chioce_count(self):
        return self.choice_set.count()


    get_questionnaire_title.short_description = 'questionnaire'
    get_chioce_count.short_description = 'Total chioce'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=200)

    def __str__(self):
        return self.choice_text


# class Answer(models.Model):
#     user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='user')