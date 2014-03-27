from django import forms
from waterpoints.models import Waterpoint, Waterpoint_photos

class WaterpointRegistration(forms.ModelForm):
	class Meta:
		model = Waterpoint
		
class Upload_waterpoint_photos(forms.ModelForm):
	class Meta:
		model = Waterpoint_photos
		fields = ('photos','image_title','image')
