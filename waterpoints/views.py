from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, render
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from users.models import *
from waterpoints.forms import WaterpointRegistration
from waterpoints.models import *

#description of waterpoints
		
def waterpointDetail(request,user_id):
	#get the current user
	user = Engineer()
	user = Engineer.objects.get(id = user_id )
	
	#take form from template
	form = WaterpointRegistration(request.POST)
	message = ""
	#checking if form is completed or not, and taking the action
	if form.is_valid():
		form.save()
		message = "You  have successfull create new water point"
		context = {'message':message,'user':user}
		return render (request, 'test2.html',context)
	else:
		message = "not"	
		form = WaterpointRegistration()
		context = {'form':form,'message':message, 'user':user}
		return render(request,'waterpointdescription.html',context)
		    
# images for water points
def waterpointPhotos(request):
	#retrieve all from imageupload form
	form = request.POST
	
	#retrieve image form form	
	imagelist = form.getlist('image') 
	
	
	message = 'ok'
	context = {'message':message,'result':imagelist}
	return render (request, 'test2.html',context)
	
	
			
			

