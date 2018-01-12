from django.db import models

# Create your models here.

class kinder(models.Model):
	kname = models.CharField(max_length = 100)
	city = models.CharField(max_length = 100)
	pnumber= models.CharField(max_length = 100)
	tnumber = models.CharField(max_length = 100)
	address =  models.CharField(max_length = 100)
	tel = models.CharField(max_length = 100)
	classnum = models.CharField(max_length = 100)
	cctvnum = models.CharField(max_length = 100)
	commute = models.CharField(max_length = 100)

class free(models.Model):
	facility =  models.CharField(max_length = 100)
	address = models.CharField(max_length = 100)
	support = models.CharField(max_length = 100)
	telephone = models.CharField(max_length = 100)
	location = models.CharField(max_length = 100)
	opponent = models.CharField(max_length = 100)
	time = models.CharField(max_length = 100)


class recycle(models.Model):
	center = models.CharField(max_length = 100)
	address = models.CharField(max_length = 100)
	area = models.CharField(max_length = 100)
	vehicle = models.CharField(max_length = 100)
	item = models.CharField(max_length = 100)
	operating = models.CharField(max_length = 100)
	service = models.CharField(max_length = 100)
	telephone = models.CharField(max_length = 100)