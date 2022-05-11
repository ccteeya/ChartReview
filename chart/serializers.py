from rest_framework import serializers
from chart.models import Chart, Table, Keyword, UsersKeyword, UsersKeywordGroup

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


class KeywordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Keyword
        fields = '__all__'


class UserKeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersKeyword
        fields = '__all__'


# class UserKeywordDetailSerializer(serializers.ModelSerializer):
#     url = serializers.HyperlinkedIdentityField(view_name='userkeyword-detail')
#     class Meta:
#         model = UsersKeyword
#         fields = '__all__'

class UsersKeywordGroupSerializer(serializers.ModelSerializer):
    keywords = UserKeywordSerializer(many=True, read_only=True)

    class Meta:
        model = UsersKeywordGroup
        fields = [
            'id',
            'name',
            'user',
            'keywords',
        ]
