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
	if not usernamelist :
		message = 'Sorry! Currently you are not log in into this System.'
		context = {'message':message}
		return render(request, 'notlogin.html', context)
	else:
		username = usernamelist[0]
	
	
	#extract password
	passwordlist = loginform.getlist('password')
	if not passwordlist:
		message = 'Sorry! Currently you are not log in into this System.'
		context = {'message':message}
		return render(request, 'notlogin.html', context)
	else:
		password = passwordlist[0]	

	position = ''
		
	#checking if user is system aadministor
	for admin in adminlist:
		if admin.e_mail == username and admin.password == password:
			position = 'admin'
			admin.login_status = 'log_in'
			admin.save()
			user = admin
			 
	#checking if user is district water engineer		
	for engineer in engineerlist:
		if engineer.e_mail == username and engineer.password == password: 
			position = 'engineer'
			engineer.login_status = 'log_in'
			engineer.save()
			user = engineer

	#cheking if user is cowso chairperson
	for chairperson in chairpersonlist:
		if chairperson.e_mail == username and chairperson.password == password:
			user_location=chairperson.physical_location_name
			
			#taking water point to be updated
			waterpoint_update = []
			for waterpoint in waterpointslist:
				if  waterpoint.physical_location_name == user_location:
					waterpoint_update.append(waterpoint)
			position = 'cowso chairperson'
			chairperson.login_status = 'log_in'
			chairperson.save()
			user = chairperson

	#provide list of actons depending on user's position in the system
	if position == 'admin':
		welcome_info = 'Welcome'
		context={'position':'admin','welcome_info':welcome_info,'user':user}
		return render(request, 'users.html' , context)
	elif position == 'engineer':
		welcome_info = 'Welcome'
		context={'position':'engineer','welcome_info':welcome_info,'user':user}
		return render(request, 'users.html' , context)
	elif position == 'cowso chairperson':
		welcome_info = 'Welcome'
		message = 'Please select new status for each water point'
		context={'user_location':user_location,'message':message,'position':'cowso','welcome_info':welcome_info,'user':user, 'waterpoint_update':waterpoint_update}
		#return render(request, 'chairperson.html',context)
		return render(request, 'users.html' , context)
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
	user_district = ''
	user_region = ''	
	message = ''
	warning = ''
	welcome_info = "Welcome"
	
	#check if current user is authorized user or not
	if user.login_status == 'log_out':
		message = 'Sorry! Currently you are not log in into this System.'
		context = {'message':message}
		return render(request, 'notlogin.html', context)
	else:
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
		
			user_district_list = form.getlist('district')
			user_district = user_district_list[0]
		
			user_region_list = form.getlist('region')
			user_region = user_region_list[0]	
	
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
				newuser.district = user_district
				newuser.region = user_region
	
				#saving data
				newuser.save()
	
		context = {'message':message,'position':'admin','user':user,'warning':warning,'welcome_info':welcome_info}
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
	user_district = ''
	user_region = ''
	message = ''
	warning = ''
	welcome_info = "Welcome"
	#check if current user is authorized user or not
	if user.login_status == 'log_out':
		message = 'Sorry! Currently you are not log in into this System.'
		context = {'message':message}
		return render(request, 'notlogin.html', context)
	else:
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
		
			user_district_list = form.getlist('district')
			user_district = user_district_list[0]
		
			user_region_list = form.getlist('region')
			user_region = user_region_list[0]
	
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
			newuser.district = user_district
			newuser.region = user_region
	
			#saving data
			newuser.save()
	
		context = {'message':message ,'user':user,'warning':warning,'welcome_info':welcome_info,'position':'admin' }
		return render(request, 'createChairperson.html', context)	

# back to admin home page	
def adminHome(request, user_id):
	#get user of system:
	user = Administrator()
	user = Administrator.objects.get(id = user_id)
	if user.login_status == 'log_out':
		message = 'Sorry! Currently you are not log in into this System.'
		context = {'message':message}
		return render(request, 'notlogin.html', context)
	else:
		welcome_info = "Welcome"
		context = {'user':user,'welcome_info':welcome_info,'position':'admin'}
		return render(request, 'users.html' , context)
	
#back to District water engineer home page
def enginerHome(request, user_id):
	#get current user
	user = Engineer()
	user = Engineer.objects.get(id = user_id)
	if user.login_status == 'log_out':
		message = 'Sorry! Currently you are not log in into this System.'
		context = {'message':message}
		return render(request, 'notlogin.html', context)
	else:
		welcome_info = "Welcome"
		context = {'welcome_info':welcome_info,'position':'engineer' , 'user':user}
		return render(request, 'users.html' , context)

#thank word for cowso chairperson after updating water point status


# log out function
def log_out(request,user_id,user_e_mail,user_password,user_position):
	#check the position and apply changes on a given user
	
	#for admin to log out
	if user_position == 'admin':
		message = 'log out, admin'
		user = Administrator.objects.get(id = user_id)
		user.login_status = 'log_out'
		user.save()
	
	# for engineer to log out	
	elif user_position == 'engineer':
		message = 'log out, engineer'
		user = Engineer.objects.get(id = user_id)
		user.login_status = 'log_out'
		user.save()	
		
	# for cowso chairperson to log out	
	elif user_position == 'cowso':
		message = 'logout, cowso chairperson'
		user = Chairperson.objects.get(id = user_id)
		user.login_status = 'log_out'
		user.save()
	else:
		message = ''		
	
	return HttpResponseRedirect('/')


#report & summary : summary part in District water engineer interface	
def report_summary_engineer(request, user_id):
	interface = 'engineerSummary'
	#taking current user of system
	user = Engineer()
	user = Engineer.objects.get(id = user_id)
	
	#return values
	welcome_info = 'Welcome'
	context = {'interface':interface,'position':'engineer','welcome_info':welcome_info,'user':user}
	return render (request, 'reports.html' ,context)	

#report & summary : COWSO chairperson part in District water engineer interface	
def cowso_summary_engineer(request, user_id):
	interface = 'cowsoSummaryEngineer'
	#taking current user of system
	user = Engineer()
	user = Engineer.objects.get(id = user_id)
	
	#return values
	welcome_info = 'Welcome'
	context = {'interface':interface,'position':'engineer','welcome_info':welcome_info,'user':user}
	return render (request, 'reports.html' ,context)	

	
#report & summary : COWSO chairperson part in District System admin interface	
def cowso_summary_Admin(request, user_id):
	interface = 'cowsoSummaryAdmin'
	#taking current user of system
	user = Administrator()
	user = Administrator.objects.get(id = user_id)
	
	#return values
	welcome_info = 'Welcome'
	context = {'interface':interface,'position':'admin','welcome_info':welcome_info,'user':user}
	return render (request, 'reports.html' ,context)


#report & summary : COWSO chairperson part in System admin interface		
def engineer_summary_Admin(request, user_id):
	interface = 'engineerSummaryAdmin'
	#taking current user of system
	user = Administrator()
	user = Administrator.objects.get(id = user_id)
	
	#return values
	welcome_info = 'Welcome'
	context = {'interface':interface,'position':'admin','welcome_info':welcome_info,'user':user}
	return render (request, 'reports.html' ,context)
 



	
	
	
