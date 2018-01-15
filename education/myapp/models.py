from django.db import models

# Create your models here.

class kinder(models.Model):
	name = models.CharField(max_length = 100)
	divide =  models.CharField(max_length = 100)
	types =  models.CharField(max_length = 100)
	snumber =  models.CharField(max_length = 100)
	address =  models.CharField(max_length = 1000)


class free(models.Model):
	facility =  models.CharField(max_length = 100)
	address = models.CharField(max_length = 100)
	support = models.CharField(max_length = 100)
	telephone = models.CharField(max_length = 100)
	location = models.CharField(max_length = 100)
	opponent = models.CharField(max_length = 100)
	time = models.CharField(max_length = 100)
	day = models.CharField(max_length = 100)


class recycle(models.Model):
	center = models.CharField(max_length = 100)
	road = models.CharField(max_length = 100)
	address = models.CharField(max_length = 100)
	area = models.CharField(max_length = 100)
	vehicle = models.CharField(max_length = 100)
	item = models.CharField(max_length = 100)
	operating = models.CharField(max_length = 100)
	telephone = models.CharField(max_length = 100)