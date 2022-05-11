from chart.models import Chart, Table, Keyword, UsersKeywordGroup,UsersKeyword
from chart.serializers import TableSerializer, ChartSerializer, ChartDetailSerializer, KeywordSerializer, UsersKeywordGroupSerializer, UserKeywordSerializer
from rest_framework import generics
from rest_framework import viewsets

class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

class ChartViewSet(viewsets.ModelViewSet):
    queryset = Chart.objects.all()
    serializer_class = ChartDetailSerializer

class KeywordViewSet(viewsets.ModelViewSet):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer

class UsersKeywordGroupViewSet(viewsets.ModelViewSet):
    queryset = UsersKeywordGroup.objects.all()
    serializer_class = UsersKeywordGroupSerializer

    def get_queryset(self):
        queryset = self.queryset
        user_id = self.request.query_params.get('userId', None)
        if user_id is not None:
            queryset = queryset.filter(user = user_id)
        return queryset



class UserKeywordViewSet(viewsets.ModelViewSet):
    queryset = UsersKeyword.objects.all()
    serializer_class = UserKeywordSerializer


