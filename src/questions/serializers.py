from rest_framework.serializers import ModelSerializer
from . import models


class AnswerChainSerializer(ModelSerializer):
    class Meta:
        model = models.Answer
        fields = ('id', 'title', 'slug', 'content')


class AnswerSerializer(ModelSerializer):
    answer_chain = AnswerChainSerializer(many=True)

    class Meta:
        model = models.Answer
        fields = ('id', 'title', 'slug', 'content', 'answer_chain')


class SubjectAnswerSerializer(ModelSerializer):

    class Meta:
        model = models.Answer
        fields = ('id', 'title', 'slug', 'content')


class SubjectSerializer(ModelSerializer):
    answers = SubjectAnswerSerializer(many=True)

    class Meta:
        model = models.Subject
        fields = ('id', 'title', 'answers')
