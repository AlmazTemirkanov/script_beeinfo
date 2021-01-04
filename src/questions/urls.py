from django.urls import path, include
from rest_framework import routers
from .views import SubjectView, AnswerView


router = routers.DefaultRouter(trailing_slash=True)
router.register(r'subjects', SubjectView, basename='subjects')
router.register(r'answers', AnswerView, basename='answers')

urlpatterns = [
    path('', include(router.urls)),
]
