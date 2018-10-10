from django.db import models
from django.utils import timezone


class TimeSheet(models.Model):
    name = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    hours = models.IntegerField(default=0)
    date_of_work = models.DateTimeField(default=timezone.now)
    date_of_entry = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.date_of_entry = timezone.now()
        self.save()

    def __str__(self):
        return self.name
