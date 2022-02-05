from django.contrib import admin
from chart.models import Chart, Table,Keyword
# Register your models here.
from task.models import Task

class TaskInLine(admin.TabularInline):
    model = Task

    extra = 0

class TableInLine(admin.TabularInline):
    model = Table
    fields = ('title','content', 'created',)
    extra = 0


class TableAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ( 'title',  'updated')
    exclude = ('content',)

    def has_add_permission(self, request):
        return False


class ChartAdmin(admin.ModelAdmin):
    inlines = [TableInLine, TaskInLine]
    search_fields = ['title']
    list_display = ('title', 'patient', 'updated')



class KeywordAdmin(admin.ModelAdmin):
    search_fields = ['keyword']


admin.site.register(Keyword, KeywordAdmin)
admin.site.register(Chart, ChartAdmin)
admin.site.register(Table, TableAdmin)