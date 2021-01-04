from django.db import models
from django.utils.translation import ugettext_lazy as _


class Answer(models.Model):
    title = models.CharField(max_length=256, verbose_name=_('Вопрос или ответ оператора'))
    slug = models.CharField(max_length=24, blank=True, null=True, verbose_name=_('Короткое название'))
    content = models.TextField(blank=True, null=True, verbose_name=_('Текст'))
    answer_chain = models.ManyToManyField('self', blank=True, symmetrical=False, verbose_name='Связка ответов')

    class Meta:
        verbose_name = _('Ответ')
        verbose_name_plural = _('Ответы')

    def __str__(self):
        return self.slug


class Subject(models.Model):
    title = models.CharField(max_length=256, verbose_name=_('Тема'))
    answers = models.ManyToManyField(Answer, blank=True, symmetrical=False, verbose_name='Связать с другими ответами:')

    class Meta:
        verbose_name = _('Тема')
        verbose_name_plural = _('Темы')

    def __str__(self):
        return self.title
