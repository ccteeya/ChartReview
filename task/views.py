from task.serializers import TaskSerializer, NoteSerializer
from rest_framework import viewsets
from task.models import Task, Note
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


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def get_queryset(self):
        queryset = self.queryset
        task_id = self.request.query_params.get('taskId', None)
        if task_id is not None:
            queryset = queryset.filter(task__id=task_id)
        return queryset