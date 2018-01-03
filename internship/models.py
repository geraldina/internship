from django.db import models
from django.utils import timezone


class Person(models.Model):
    email = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    birthday = models.DateField(blank=False, null=False)
    place = models.CharField(max_length=200)
    education = models.TextField()
    awards = models.TextField()
    experience = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.email
