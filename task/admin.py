from django.contrib import admin
from task.models import Task, Note
from chart.models import Chart
# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    # search_fields = ['done']
    list_filter=('chart', 'user', 'done')
    list_display = ('chart', 'user', 'done')


admin.site.register(Task, TaskAdmin)
admin.site.register(Note)