from django.contrib import admin
from django.contrib.auth.models import User
from task.models import Task
import django
# from django.contrib.auth.admin import UserAdmin
# Register your models here.
class TaskInLine(admin.TabularInline):
    model = Task
    extra = 0


# class UserAdmin(admin.ModelAdmin):


class UserAdmin(django.contrib.auth.admin.UserAdmin):
    inlines = [TaskInLine]
    list_display = ('username', 'is_superuser')
    exclude = ('groups','first_name','last_name', 'is_staff', 'date_joined','user_permissions', 'last_login')
    fieldsets = [
        (None, {'fields': ['username', 'password', 'is_superuser']}),]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)