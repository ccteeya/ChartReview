from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from questionnaire.models import Questionnaire,Choice
from questionnaire.serializers import QuestionnaireSerializer, ChoiceSerializer

class QuestionnaireViewSet(viewsets.ModelViewSet):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer


class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer