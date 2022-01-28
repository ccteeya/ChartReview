from django.contrib import admin
from chart.models import Chart, Table
# Register your models here.
from task.models import Task

class TaskInLine(admin.TabularInline):
    model = Task

    extra = 0

class TableInLine(admin.TabularInline):
    model = Table
    fields = ('title', 'created',)
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







admin.site.register(Chart, ChartAdmin)
admin.site.register(Table, TableAdmin)