from django import forms
from waterpoints.models import Waterpoint, Waterpoint_photos

class WaterpointRegistration(forms.ModelForm):
	class Meta:
		model = Waterpoint
		

