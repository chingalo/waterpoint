from django.db import models
import datetime
from django.utils import timezone

#model for static and dyanamic information 
class Waterpoint(models.Model):
	code_number = models.CharField(max_length = 20)
	name = models.CharField(max_length = 200)
	source_name = models.CharField(max_length = 200)
	#water supply connection type
	supply_connection_category = (
	('waterpoint','waterpoint'),
	('domestic','domestic'),
	('business','business'),
	('institutional','institutional'),
	('industrial','industrial'),
	)	
	supply_connection = models.CharField(max_length=200, choices = supply_connection_category , default = 'waterpoint')
	district = models.CharField(max_length = 200, blank = True)
	region = models.CharField(max_length = 200, blank = True)
	physical_location_name = models.CharField(max_length = 200)
	latitude = models.CharField(max_length = 200 , blank = True) 
	longitude = models.CharField(max_length = 200 , blank = True)
	fund = models.CharField(max_length = 200)
	sponsor = models.CharField(max_length = 200)
		
	def __unicode__(self): #for pyhton 3 : def __str__(self):
		return self.name
		
#model for photos upload
class Waterpoint_photos(models.Model):
	photos = models.ForeignKey('Waterpoint', on_delete=models.CASCADE)
	image = models.ImageField(upload_to = "waterpoint" )
	image_title = models.CharField(max_length = 200)
	
	def __unicode__(self): #for pyhton 3 : def __str__(self):
		return self.image_title

#model for status of a given water point		
class Waterpoint_status(models.Model):
	name = models.ForeignKey('Waterpoint', on_delete=models.CASCADE)
	status = models.CharField(max_length = 200)
	status_date_update = models.DateTimeField(default=timezone.now)
	
	def __unicode__(self): #for pyhton 3 : def __str__(self):
		return self.status
	
