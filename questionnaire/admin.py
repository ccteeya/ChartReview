from django.contrib import admin

# Register your models here.
from questionnaire.models import Question, Choice, Questionnaire

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 0

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['questionnaire__title']
    list_filter = ['is_checkbox']
    list_display = ('get_questionnaire_title', 'question_text', 'is_checkbox', 'updated', 'get_chioce_count')
    fieldsets = [
        (None, {'fields': ['question_text']}),
        # ('Date information', {'fields': ['updated']}),
    ]
    inlines = [ChoiceInline]

    def has_add_permission(self, request):
        return False


class QuestionnaireAdmin(admin.ModelAdmin):
    search_fields = ['title']
    # list_filter = ['updated']
    list_display = ('title', 'updated')
    fieldsets = [
        (None, {'fields': ['title']}),
        # ('Date information', {'fields': ['updated']}),
    ]
    inlines = [QuestionInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Questionnaire, QuestionnaireAdmin)