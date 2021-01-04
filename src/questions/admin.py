from django.contrib import admin
from . import models


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(models.Subject)
admin.site.register(models.Answer, AnswerAdmin)
