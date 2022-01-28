from django.shortcuts import render
from chart.models import Chart, Table
# from chart.serializers import TableSerializer, ChartSerializer, ChartDetailSerializer
from rest_framework import generics
from task.serializers import TaskSerializer
from rest_framework import viewsets
from task.models import Task
# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = self.queryset
        user_id = self.request.query_params.get('userId', None)
        if user_id is not None:
            queryset = queryset.filter(user__id=user_id)
        return queryset