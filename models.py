from django.db import models

# Create your models here.


class Logdb(models.Model):
    verb = models.CharField(blank=False, max_length=5)
    path = models.CharField(blank=False, max_length=50000)
    status = models.IntegerField(default=0)
    duration = models.CharField(blank=False, max_length=15)
    payload = models.JSONField(blank=True)
    header = models.JSONField()
    responses = models.JSONField()
    happened = models.DateTimeField(auto_now_add=True)
