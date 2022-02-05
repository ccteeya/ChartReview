from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from questionnaire.models import Questionnaire,Choice, Answer
from questionnaire.serializers import QuestionnaireSerializer, ChoiceSerializer, AnswerSerializer

class QuestionnaireViewSet(viewsets.ModelViewSet):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer


class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer