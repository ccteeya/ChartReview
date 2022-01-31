from chart.models import Chart, Table, Keyword
from chart.serializers import TableSerializer, ChartSerializer, ChartDetailSerializer, KeywordSerializer
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

    # def get_serializer_class(self):
    #     if self.action=='list':
    #         return ChartSerializer
    #     else:
    #         return ChartDetailSerializer
#
# class ChartList(generics.ListCreateAPIView):
#     queryset = Chart.objects.all()
#     serializer_class = ChartListSerializer

