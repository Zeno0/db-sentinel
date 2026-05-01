from django.db import models

# Create your models here.
class QueryStat(models.Model):
    query = models.TextField()
    calls = models.IntegerField()
    total_exec_time = models.FloatField()
    mean_exec_time = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
