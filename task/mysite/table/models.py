from django.db import models

# Create your models here.
class Employee(models.Model):
	name = models.CharField(max_length=30)

	class Meta:
		db_table = 'Employee'

class Department(models.Model):
	name = models.CharField(max_length=30)

	class Meta:
		db_table = 'Department'

class Project(models.Model):
	name = models.CharField(max_length=30)
	employees = models.ManyToManyField(Employee)

	class Meta:
		db_table = 'Project'
