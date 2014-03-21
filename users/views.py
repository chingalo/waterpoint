from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, render
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from users.models import *
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
			user = admin
			 
	#checking if user is district water engineer		
	for engineer in engineerlist:
		if engineer.e_mail == username and engineer.password == password: 
			position = 'engineer'
			user = engineer

	#cheking if user is cowso chairperson
	for chairperson in chairpersonlist:
		if chairperson.e_mail == username and chairperson.password == password:
			p=chairperson.physical_location_name
			position = 'cowso chairperson'
			user = chairperson

	#provide list of actons depending on user's position in the system
	if position == 'admin':
		welcome_info = 'Welcome'
		context={'position':position,'welcome_info':welcome_info,'user':user}
		return render(request, 'admin.html',context)
	elif position == 'engineer':
		welcome_info = 'Welcome'
		context={'position':position,'welcome_info':welcome_info,'user':user}
		return render(request, 'engineer.html',context)
	elif position == 'cowso chairperson':
		welcome_info = 'Welcome'
		
		context={'p':p,'position':position,'welcome_info':welcome_info,'user':user, 'waterpointslist':waterpointslist}
		return render(request, 'chairperson.html',context)
	else:
		message = 'Incorrect username or password'
		context={'message':message,}
		return render(request, 'login.html',context)	
			
	
#creater District water engineer
def createEngineer(request,user_id):
	#get user of the system
	user = Administrator()
	user = Administrator.objects.get(id = user_id )
	
	#initialize all variables to empty strings
	user_sex = ''
	user_location = ''
	user_telphone_number = '' 
	user_email = ''
	user_password = '' 
	user_address = ''
	user_name = ''
	user_id = ''	
	message = ''
	warning = ''
	welcome_info = "Welcome"
	
	#taking data from regstration form
	if  request.POST :
		form = request.POST
	#retrieve all data from registration
		user_id_list= form.getlist('id')
		user_id = user_id_list[0]
	
		user_name_list = form.getlist('name')
		user_name = user_name_list[0]
	
		user_password_list = form.getlist('password')
		user_password = user_password_list[0]
	
		user_email_list = form.getlist('email')
		user_email = user_email_list[0]
	
		user_telphone_number_list = form.getlist('number')
		user_telphone_number = user_telphone_number_list[0]
	
		user_address_list = form.getlist('address')
		user_address = user_address_list[0]
	
		user_sex_list = form.getlist('sex')		
		user_sex = user_sex_list[0]
	
		if user_sex == '' or user_telphone_number == '' or user_email == '' or user_password == '' or user_name == '' or user_id == '' :
			warning = 'please fill all information in the from for successfull create new District water Engineer'
		else: 
			message = 'You have successful created new District water engineer'
	
	#create object for storing data from registration form
	newuser = Engineer()
	if message :
		
		#add data into object created
		newuser.engineer_id = user_id
		newuser.engineer_name = user_name
		newuser.password = user_password
		newuser.e_mail = user_email
		newuser.telphone_number = user_telphone_number
		newuser.address = user_address
		newuser.sex = user_sex
	
		#saving data
		newuser.save()
	
	context = {'message':message,'user':user,'warning':warning,'welcome_info':welcome_info}
	return render(request, 'createEngineer.html', context)

#create COWSO chairperson	
def createChairperson(request, user_id):
	#get user of system:
	user = Administrator()
	user = Administrator.objects.get(id = user_id )
	
	#initialize all variables to empty strings
	user_sex = ''
	user_location = ''
	user_telphone_number = '' 
	user_email = ''
	user_password = '' 
	user_name = ''
	user_id = ''	
	user_location = ''
	user_address = ''
	message = ''
	warning = ''
	welcome_info = "Welcome"
	#taking data from regstration form
	if  request.POST :
		form = request.POST
	#retrieve all data from registration
		user_id_list= form.getlist('id')
		user_id = user_id_list[0]
	
		user_name_list = form.getlist('name')
		user_name = user_name_list[0]
	
		user_password_list = form.getlist('password')
		user_password = user_password_list[0]
	
		user_email_list = form.getlist('email')
		user_email = user_email_list[0]
	
		user_telphone_number_list = form.getlist('number')
		user_telphone_number = user_telphone_number_list[0]
	
		user_address_list = form.getlist('address')
		user_address = user_address_list[0]
		
		user_location_list = form.getlist('location')
		user_location = user_location_list[0]
	
		user_sex_list = form.getlist('sex')
		user_sex = user_sex_list[0]
	
		if user_sex == '' or user_location == '' or user_telphone_number == '' or user_email == '' or user_password == '' or user_name == '' or user_id == '' :
			warning = 'please fill all information in the from inoreder to create new user'
		else: 
			message = 'You have successful create new COWSO chairperson'	
	
	#create object for storing data from registration form
	newuser = Chairperson()
	if message :
		#add data into object created
		newuser.cowso_id = user_id
		newuser.cowso_chairperson_name = user_name
		newuser.password = user_password
		newuser.e_mail = user_email
		newuser.telphone_number = user_telphone_number
		newuser.physical_location_name = user_location
		newuser.address = user_address
		newuser.sex = user_sex
		#saving data
		newuser.save()
	
	context = {'message':message ,'user':user,'warning':warning,'welcome_info':welcome_info}
	return render(request, 'createChairperson.html', context)	

# back to admin home page	
def adminHome(request, user_id):
	#get user of system:
	user = Administrator()
	user = Administrator.objects.get(id = user_id)
	message = 'welcome'
	context = {'user':user,'message':message}
	return render(request,'admin.html',context)
	
#back to District water engineer home page
def enginerHome(request, user_id):
	#get current user
	user = Engineer()
	user = Engineer.objects.get(id = user_id)
	welcome_info = "Welcome"
	context = {'welcome_info':welcome_info, 'user':user}
	return render(request, 'engineer.html',context)

#thank word for cowso chairperson after updating water point status


# log out function
def log_out(request,user_id,user_e_mail):
	message = "ok"
	context = {'message':message}
	return render (request, 'test.html', context)
	

 



	
