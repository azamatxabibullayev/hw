from django.db import models


# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    year = models.IntegerField()
    location = models.CharField(max_length=255)

    class Meta:
        db_table = 'School'

    def __str__(self):
        return self.name


class PrivateSchool(models.Model):
    name = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    year = models.IntegerField()
    location = models.CharField(max_length=255)

    class Meta:
        db_table = 'PrivateSchool'

    def __str__(self):
        return self.name
