from rest_framework import serializers
from chart.models import Chart, Table

# class TableDetailSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = Table
# #         fields = '__all__'
# #
# #
# # class TableListSerializer(serializers.ModelSerializer):
# #
# #     url = serializers.HyperlinkedIdentityField(view_name="chart:table-detail")
# #     class Meta:
# #         model = Table
# #         fields = [
# #             'id',
# #             'url',
# #             'title',
# #             # 'content',
# #             # 'created',
# #         ]

class ChartSerializer(serializers.HyperlinkedModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name='chart-detail')
    # tables = TableSerializer()
    class Meta:
        model = Chart
        fields = '__all__'

class TableSerializer(serializers.HyperlinkedModelSerializer):
    chart = ChartSerializer(read_only=True)
    chart_id = serializers.IntegerField(write_only=True, allow_null=True, required=False)

    def validate_chart_id(self, value):
        if not Chart.objects.filter(id=value).exists() and value is not None:
            raise serializers.ValidationError("Table with id {} not exists.".format(value))
        return value

    class Meta:
        model = Table
        fields = '__all__'


class TableChartDetailSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='table-detail')
    class Meta:
        model = Table
        fields = [
            'url',
            'title',
        ]


class ChartDetailSerializer(serializers.ModelSerializer):
    tables = TableChartDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Chart
        fields = [
            'id',
            'title',
            'created',
            'tables',
        ]