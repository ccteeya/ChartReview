from rest_framework import serializers
from questionnaire.models import Questionnaire, Question, Choice, Answer


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'

class ChoiceDetailSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='choice-detail')

    class Meta:
        model = Choice
        fields = [
            'id',
            'url',
            'choice_text',

        ]

class QuestionDetailSerializer(serializers.ModelSerializer):
    choices = ChoiceDetailSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = [
            'id',
            'question_text',
            'is_checkbox',
            'choices',
        ]


class QuestionnaireSerializer(serializers.ModelSerializer):
    questions = QuestionDetailSerializer(many=True, read_only=True)
    class Meta:
        model = Questionnaire
        fields = [
            'id',
            'title',
            'questions'
        ]

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'