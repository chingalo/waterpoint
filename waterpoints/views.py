from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, render
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from users.models import *
from waterpoints.forms import *
from waterpoints.models import *


#description of waterpoints
		
def waterpointDetail(request,user_id):
	#get the current user
	user = Engineer()
	user = Engineer.objects.get(id = user_id )
	if user.login_status == 'log_out':
		message = 'Sorry! Currently you are not log in into this System.'
		context = {'message':message}
		return render(request, 'notlogin.html', context)
	else:
		welcome_info = "Welcome"
		#take form from template
		form = WaterpointRegistration(request.POST)
		message = ""
		#checking if form is completed or not, and taking the action
		if form.is_valid():
			form.save()
			message = "You  have successfull create new water point"
			context = {'message':message,'position':'engineer','user':user,'welcome_info':welcome_info}
			return render (request, 'engineer.html',context)
		else:
			message = "Please fill all information below, for successfull create ner water point"	
			form = WaterpointRegistration()
			context = {'form':form,'message':message,'position':'engineer', 'user':user,'welcome_info':welcome_info}
			return render(request,'waterpointdescription.html',context)
		    
# images for water points
def waterpointPhotos(request):	
	#checking if request method is POST
	if request.method == 'POST':
			
	#taking bounded form
		form = form = Upload_waterpoint_photos(request.POST, request.FILES)
		if form.is_valid():
			#save the form and return successfull upload message
			message = 'ok'
			context = {'message':message}
			form.save()
			return render(request,'test.html',context)

	#return new form if request method is not POST
	else:
		message = 'not yet'
		form = Upload_waterpoint_photos()
		context = {'message':message,'form':form}
		return render(request,'test2.html',context)
		
		
		
		
	
	#taking the form request
	#form = Upload_waterpoint_photos(request.POST, request.FILES)
	#message = form.is_valid()
	#context = {'message':message}
	#return render (request,'test.html',context)
	
	
			
			

