from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, render
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from users.models import *
from users.forms import EngineerForm, ChairpersonForm
from waterpoints.models import *



#authorization of users login into the system
def authorize(request):
	#retrive all water points in the system
	waterpointslist = Waterpoint.objects.all()
	
	#retrieve list all system administrators, District water engineers and cowso chairperson
	adminlist = Administrator.objects.all()
	engineerlist = Engineer.objects.all()
	chairpersonlist = Chairperson.objects.all()
	
	#taking username and password from login form
	loginform = request.POST
	
	#extract username
	usernamelist = loginform.getlist('username')
	username = usernamelist[0]
	
	#extract password
	passwordlist = loginform.getlist('password')
	password = passwordlist[0]
	
	position = ''
		
	#checking if user is system aadministor
	for admin in adminlist:
		if admin.e_mail == username and admin.password == password:
			position = 'admin'
			 
	#checking if user is district water engineer		
	for engineer in engineerlist:
		if engineer.e_mail == username and engineer.password == password: 
			position = 'engineer'

	#cheking if user is cowso chairperson
	for chairperson in chairpersonlist:
		if chairperson.e_mail == username and chairperson.password == password:
			p=chairperson.physical_location_name
			position = 'cowso chairperson'

	#provide list of actons depending on user's position in the system
	if position == 'admin':
		message = 'welcome System adminstrator'
		context={'position':position,'message':message,'username':username, 'password':password}
		return render(request, 'admin.html',context)
	elif position == 'engineer':
		message = 'welcome District engineer'
		context={'position':position,'message':message,'username':username, 'password':password}
		return render(request, 'engineer.html',context)
	elif position == 'cowso chairperson':
		message = 'welcome cowso chairperson '
		
		context={'p':p,'position':position,'message':message,'username':username, 'password':password, 'waterpointslist':waterpointslist}
		return render(request, 'chairperson.html',context)
	else:
		message = 'Incorrect username or password'
		context={'message':message,}
		return render(request, 'login.html',context)	
			
	
#creater District water engineer
def createEngineer(request):
	message = request.POST
	context = {'message':message}
	return render(request, 'createEngineer.html', context)

#create COWSO chairperson	
def createChairperson(request):
	message = request.POST
	context = {'message':message}
	return render(request, 'createChairperson.html', context)	
