from rest_framework.viewsets import ModelViewSet
from .models import Subject, Answer
from .serializers import SubjectSerializer, AnswerSerializer


class SubjectView(ModelViewSet):
    http_method_names = ('get', 'head', 'options')
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()


class AnswerView(ModelViewSet):
    http_method_names = ('get', 'head', 'options')
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()
