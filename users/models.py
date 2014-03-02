from django.db import models

#model for all users of system includes COWOSO_Chairpeson, district_water_engineer, system administrator
class Administrator(models.Model):
	admin_id = models.CharField(max_length = 20)
	admin_name = models.CharField(max_length = 200)
	password = models.CharField(max_length = 200)
	e_mail = models.EmailField(max_length = 200)
	telphone_number =  models.CharField(max_length = 20)
	address =  models.CharField(max_length = 200, blank = True)
	sex = models.CharField(max_length = 6)
	
	def __unicode__(self): #for pyhton 3 : def __str__(self):
		return self.admin_name

class Engineer(models.Model):
	engineer_id = models.CharField(max_length = 20)
	engineer_name = models.CharField(max_length = 200)
	password = models.CharField(max_length = 200)
	e_mail = models.EmailField(max_length = 200)
	telphone_number = models.CharField(max_length = 20)
	address =  models.CharField(max_length = 200, blank = True)
	sex = models.CharField(max_length = 6)
	
	def __unicode__(self): #for pyhton 3 : def __str__(self):
		return self.engineer_name

class Chairperson(models.Model):
	cowso_id = models.CharField(max_length = 20)
	cowso_chairperson_name = models.CharField(max_length = 200)
	password = models.CharField(max_length = 200)
	e_mail = models.EmailField(max_length = 200)
	telphone_number =  models.CharField(max_length = 20)
	address =  models.CharField(max_length = 200, blank = True)
	physical_location_name = models.CharField(max_length = 200)
	sex = models.CharField(max_length = 6)
	
	def __unicode__(self): #for pyhton 3 : def __str__(self):
		return self.cowso_chairperson_name
