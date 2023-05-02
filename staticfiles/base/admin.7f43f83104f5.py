from django.contrib import admin
from base.models import *

from base.models import Question, Stat


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('puzzle','ans')

class StatAdmin(admin.ModelAdmin):
    list_display = ('user','eye','accuracy')

# Register your models here.
admin.site.register(Question,QuestionAdmin)
admin.site.register(Stat,StatAdmin)
