from rest_framework import serializers
from task.models import Task
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
