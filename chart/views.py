from chart.models import Chart, Table
from chart.serializers import TableSerializer, ChartSerializer, ChartDetailSerializer
from rest_framework import generics
from rest_framework import viewsets

class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer


class ChartViewSet(viewsets.ModelViewSet):
    queryset = Chart.objects.all()
    serializer_class = ChartDetailSerializer

    # def get_serializer_class(self):
    #     if self.action=='list':
    #         return ChartSerializer
    #     else:
    #         return ChartDetailSerializer
#
# class ChartList(generics.ListCreateAPIView):
#     queryset = Chart.objects.all()
#     serializer_class = ChartListSerializer

