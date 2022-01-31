from django.db import models
from django.utils import timezone




class Chart(models.Model):
    # 病历名
    title = models.CharField(max_length=100)
    # 病人名字
    patient = models.CharField(max_length=30)
    # 创建时间
    created = models.DateTimeField(default=timezone.now)
    # 更新时间
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Table(models.Model):
    chart = models.ForeignKey(
        Chart,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='tables'
    )
    # 表名
    title = models.CharField(max_length=100)
    # 内容
    content = models.TextField()
    # 创建时间
    created = models.DateTimeField(default=timezone.now)
    # 更新时间
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Keyword(models.Model):
    keyword = models.CharField(max_length=100)

    def __str__(self):
        return self.keyword