from django.contrib import admin
from openpyxl import Workbook
from django.http import HttpResponse
# Register your models here.
from questionnaire.models import Question, Choice, Questionnaire, Answer

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 0

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['questionnaire__title']
    list_filter = ['is_checkbox']
    list_display = ('get_questionnaire_title', 'question_text', 'is_checkbox', 'updated')
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


class AnswerAdmin(admin.ModelAdmin):
    actions = ['export_as_excel']
    list_filter = ('user', 'question')
    list_display = ('user', 'question', 'answer')

    def export_as_excel(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='application/msexcel')
        response['Content-Disposition'] = f'attachment; filename={meta}.xlsx'
        wb = Workbook()
        ws = wb.active
        ws.append(field_names)
        for obj in queryset:
            for field in field_names:
                data = [f'{getattr(obj, field)}' for field in field_names]
            row = ws.append(data)
        wb.save(response)
        return response

    export_as_excel.short_description = 'Export excel'
admin.site.register(Question, QuestionAdmin)
admin.site.register(Questionnaire, QuestionnaireAdmin)
admin.site.register(Answer, AnswerAdmin)