from django.db import models
from django.contrib.postgres.fields import ArrayField


class Authors(models.Model):
    fullname = models.CharField(max_length=100, null=False, blank=False)
    born_date = models.DateField(null=True, blank=True)
    born_location = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)


class Quotes(models.Model):
    tags = ArrayField(models.CharField(max_length=250), null=False, blank=False)
    author = models.ForeignKey(Authors, on_delete=models.CASCADE)
    quote = models.TextField(blank=True)
