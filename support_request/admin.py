from django.contrib.admin import ModelAdmin , register
from .models import AskTheTeacher , AskTheGBT
@register(AskTheTeacher)
class AskTheTeacherAdmin(ModelAdmin):
    ...

@register(AskTheGBT)
class AskTheGBTAdmin(ModelAdmin):
    ...