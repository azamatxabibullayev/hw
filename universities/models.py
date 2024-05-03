from django.db import models


# Create your models here.

class University(models.Model):
    name = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    year = models.IntegerField()
    location = models.CharField(max_length=255)

    class Meta:
        db_table = 'University'

    def __str__(self):
        return self.name


class PrivateUniversity(models.Model):
    name = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    year = models.IntegerField()
    location = models.CharField(max_length=255)

    class Meta:
        db_table = 'PrivateUniversity'

    def __str__(self):
        return self.name
