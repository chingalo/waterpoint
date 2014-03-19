from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, render
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from users.models import *
from waterpoints.forms import WaterpointRegistration, WaterpointPhotos
from waterpoints.models import *

#description of waterpoints
		
def waterpointDetail(request):
	#take form from template
	form = WaterpointRegistration(request.POST)
	message = ""
	#checking if form is completed or not
	if form.is_valid():
		form.save()
		message = "You  have successfull create new water point"
		context = {'message':message}
		return render (request, 'test2.html',context)
	else:
		message = "not"	
		form = WaterpointRegistration()
		context = {'form':form,'message':message}
		return render(request,'waterpointdescription.html',context)
		    
		
			

