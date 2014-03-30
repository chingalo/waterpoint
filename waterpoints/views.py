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
			message = "Please fill all information below, for successfull create new water point"	
			form = WaterpointRegistration()
			context = {'form':form,'message':message,'position':'engineer', 'user':user,'welcome_info':welcome_info}
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
			form = Upload_waterpoint_photos(request.POST, request.FILES)
			
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
			
		
#update water point status
def update_waterpoint(request, user_id, user_location):	
	waterpointslist = Waterpoint.objects.all()
	list_empty = False
	value = 0;	
	#taking user and check if he or she authorized user in the system
	user = Chairperson()
	user = Chairperson.objects.get(id = user_id)
	
	#taking query dictionary having list of status
	form = request.POST
	
	#extract list of status from a form posted
	statuslist = form.getlist('status')
	
#cheking if all waterpoint has not been filled and return new form for updating status:	
	for x in range(len(statuslist)):
		if statuslist[x] == '':
			list_empty = True
			break
	#prepare and send new form	
	if list_empty == True:
		waterpoint_update = []
		for waterpoint in waterpointslist:
			if  waterpoint.physical_location_name == user_location :
				waterpoint_update.append(waterpoint)
		warning = 'Please make sure you have selected new status for each water point!'
		welcome_info = 'Welcome'
		context={'user_location':user_location,'warning':warning,'position':'cowso','welcome_info':welcome_info,'user':user, 'waterpoint_update':waterpoint_update}
		return render(request, 'chairperson.html',context)
	else:
		#taking water points from database which have to be updated its status:
		waterpoint_update = []
		status = []
		
		for waterpoint in waterpointslist:
			if  waterpoint.physical_location_name == user_location and statuslist[value] != '' :
				#save the status
				waterpoint.status = statuslist[value]
				waterpoint.save()
				waterpoint_update.append(waterpoint)			 
				value = value + 1		
			else:
				value = value + 1
			
		context = {'position':'cowso','user':user,}	
		return render (request, 'cowsoupdateinfo.html', context)
