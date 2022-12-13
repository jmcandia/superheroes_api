from django.db import models

# Create your models here.


class Superhero(models.Model):
    editorial_choices = [('dc', 'DC'),
                         ('marvel', 'Marvel'),
                         ('unknown', 'Unknown')]
    name = models.CharField(max_length=100)
    alter_ego = models.CharField(max_length=200)
    year = models.IntegerField()
    editorial = models.CharField(max_length=10,
                                 choices=editorial_choices,
                                 default='unknown')
