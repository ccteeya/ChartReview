from django.db import models
from django.utils import timezone
# Create your models here.
from chart.models import Chart
from django.contrib.auth.models import User

class Task(models.Model):

    chart = models.ForeignKey(
        Chart,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='tasks'
    )

    user = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='tasks'
    )

    done = models.BooleanField(
        default=False
    )


    # 创建时间
    created = models.DateTimeField(default=timezone.now)
    # 更新时间
    updated = models.DateTimeField(auto_now=True)


class Note(models.Model):

    content = models.TextField()

    task = models.ForeignKey(
        Task,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='notes'
    )

    # 创建时间
    created = models.DateTimeField(default=timezone.now)
    # 更新时间
    updated = models.DateTimeField(auto_now=True)
