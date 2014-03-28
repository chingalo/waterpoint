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
			warning = "Please fill all information below, for successfull create ner water point"	
			form = WaterpointRegistration()
			context = {'form':form,'warning':warning,'position':'engineer', 'user':user,'welcome_info':welcome_info}
			return render(request,'waterpointdescription.html',context)
		    
# images for water points
def waterpointPhotos(request, user_id):
	#get the current user
	user = Engineer()
	user = Engineer.objects.get(id = user_id )
	welcome_info = "Welcome"
	
	if user.login_status == 'log_out':
		message = 'Sorry! Currently you are not log in into this System.'
		context = {'message':message}
		return render(request, 'notlogin.html', context)
	else:		
						
		#checking if request method is POST
		if request.method == 'POST':
					
		#taking bounded form
			form = form = Upload_waterpoint_photos(request.POST, request.FILES)
			
			if form.is_valid():
				#save the form and return successfull upload message if the form is completely filled
				message = 'successfull upload'
				context = {'message':message,'welcome_info':welcome_info,'position':'engineer', 'user':user,}
				form.save()
				return render(request,'engineer.html',context)	
							
			else:
				#return new form to user if any field is empty
				warning = 'Please fill all fileds in the for for successfull uploading of the image'
				form = Upload_waterpoint_photos()
				context = {'form':form,'warning':warning,'position':'engineer', 'user':user,'welcome_info':welcome_info}
				return render(request,'waterpointphotos.html',context)
				
		#return new form if request method is not POST
		else:
			message = 'File all field below, to upload the image'
			form = Upload_waterpoint_photos()
			context = {'message':message,'form':form, 'position':'engineer', 'user':user,'welcome_info':welcome_info}
			return render(request,'waterpointphotos.html',context)		
			
		
		
		
	
	
	
	
			
			

