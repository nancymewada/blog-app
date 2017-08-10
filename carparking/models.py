# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
'''
class Ticket(models.Model):
	ticketstatus = (('1','active'),
					('2','expired'),
					('3','duplicate')
				)
	id =  models.AutoField(primary_key=True)
	car = models.ForeignKey(Car,null=True,blank=True)
	status = models.CharField(max_length=10, choices=ticketstatus, null=True, blank=True)
	entrytime = models.DateField(null=True, blank=True)
	exittime = models.DateField(null=True, blank=True)
	parkingslot = models.ForeignKey(Parkinglot)

class Parkinglot(models.Model):
	car = models.ForeignKey(Car, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

class Car(models.Model):
	question = models.ForeignKey(Parkinglot, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
'''