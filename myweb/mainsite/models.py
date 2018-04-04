from django.db import models
from django.utils import timezone

# Create your models here.

class Iris(models.Model):
    sepal_length = models.FloatField()
    sepal_width = models.FloatField()
    petal_length = models.FloatField()
    petal_width = models.FloatField()
    species = models.CharField(max_length=50)
	
    class Meta:
        ordering = ('species',)
    	
    def __unicode__(self):
	    return self.species
