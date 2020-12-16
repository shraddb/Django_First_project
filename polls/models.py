from django.db import models

class Employee(models.Model):
	name=models.CharField(max_length=30)
	age=models.IntegerField()
	role=models.CharField(max_length=30)
	salary=models.FloatField()

	def __str__(self):
		return self.name
		