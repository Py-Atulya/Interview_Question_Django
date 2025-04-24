from django.contrib import admin
from .models import QuestionModel

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'language', 'question', 'answer')
    list_filter = ('language', 'question')
    search_fields = ('question',)
    ordering = ('language', 'question')
    fieldsets = (
        (None, {'fields': ('language', 'question', 'answer')}),

    )
admin.site.register(QuestionModel, QuestionAdmin)