from django import forms
from users.models import *

#District Water engineer registration form
class EngineerForm(forms.ModelForm):
	class meta:
		model = Engineer
		
#COWSO chairperson registration form
class ChairpersonForm(forms.ModelForm):
	class meta:
		model = Chairperson
