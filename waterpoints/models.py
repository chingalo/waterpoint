from django.db import models

#model for static and dyanamic information 
class Waterpoint(models.Model):
	code_number = models.CharField(max_length = 20)
	water_point_name = models.CharField(max_length = 200)
	physical_location_name = models.CharField(max_length = 200)
	latitude = models.CharField(max_length = 200 , blank = True) 
	longitude = models.CharField(max_length = 200 , blank = True)
	fund = models.CharField(max_length = 200)
	sponsor = models.CharField(max_length = 200)
	
	#choices for water point status
	status_choices=(
	('functioning','fuctioning'),
	('non-functioning','non-functioning'),
	('need to repair','need to repair'),
	)
	status = models.CharField(max_length=200, choices = status_choices , default = 'functioning')
	
	def __unicode__(self): #for pyhton 3 : def __str__(self):
		return self.water_point_name

class Waterpoint_photos(models.Model):
	photos = models.ForeignKey('Waterpoint', on_delete=models.CASCADE)
	image = models.ImageField(upload_to = "waterpoint")
	image_title = models.CharField(max_length = 200)
	
	def __unicode__(self): #for pyhton 3 : def __str__(self):
		return self.image_title

