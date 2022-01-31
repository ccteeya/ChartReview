from django.contrib import admin
from task.models import Task, Note
from chart.models import Chart
# Register your models here.


# class ChartInLine(admin.TabularInline):
#     model = Chart
#     extra = 0
#
# class TaskAdmin(admin.ModelAdmin):
#     search_fields = ['id']
#
#     inlines = [ChartInLine]



admin.site.register(Task)
admin.site.register(Note)