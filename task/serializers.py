from rest_framework import serializers
from task.models import Task, Note
from chart.serializers import ChartDetailSerializer
from user.serializers import UserRegisterSerializer

class TaskSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name='chart-detail')
    # tables = TableSerializer()

    chart = ChartDetailSerializer()
    user = UserRegisterSerializer()

    class Meta:
        model = Task
        fields = [
            'id',
            'user',
            'chart',
            'created',
        ]


class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = '__all__'