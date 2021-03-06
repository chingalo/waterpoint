from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, render
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from users.models import *
from waterpoints.models import *

# lists of regions with respective districts
arusha = ['arumeru', 'arusha-city', 'arusha district','longido','monduli', 'ngorongoro']
dar_es_salama = ['ilala', 'kinondoni', 'temeke']
dodoma = ['bahi', 'chamwino', 'chemba','dodoma municipal', 'kondoa', 'kongwa','mpwapwa']
geita = ['bukombe','chato','geita', 'mbongwe', "nyang'hwale"]
iringa = ['iringa district', 'iringa municipal', 'kilolo', 'mafinga town', 'mufindi']
kagera = ['biharamulo', 'bukoba district', 'bukoba municipal','karagwe','kyerwa', 'missenyi','muleba','ngara']
kaskazini_Pemba = ['micheweni', 'wete']
kaskazini_unguja = ['kaskazini A', 'kaskazini B']
katavi = ['mlele', 'mpanda district', 'mpanda town']
kigoma = ['buhigwe', 'kakonko', 'kasulu', 'kasulu town', 'kibondo', 'kigoma district', 'kigoma-ujiji municipal', 'uvinza']
kilimanjaro = ['hai', 'moshi district', 'moshi municipal', 'mwanga', 'rombo', 'same' , 'siha']
kusini_pemba = ['chake chake','mkoani']
kusini_unguja = ['kati', 'kusini']
lindi = ['kilwa', 'lindi district', 'lindi municipal', 'liwale', 'nachingwea', 'ruangwa']
manyara  = ['babati town', 'babati district', 'hanang', 'kiteto', 'mbulu', 'simanjiro']
mara = ['bunda', 'butiama', 'musoma district', 'musoma municipal', 'rorya', 'sengeti', 'tarime']
mbeya = ['chunya', 'ileje', 'kyela', 'mbarali', 'mbeya city', 'mbeya district', 'mbozi', 'momba', 'rungwe', 'tunduma']
mjini_magharibi = ['magharibi', 'mjini']
morogoro = ['gairo', 'kilombero', 'kilosa', 'morogoro district', 'morogoro municipal', 'mvomero', 'ulanga']
mtwara = ['masasi district', 'masasi town', 'mtwara district', 'mtwara municipal', 'nayumbu', 'newala', 'tandahimba']
mwanza = ['ilemela municipal','kwimba', 'mangu', 'misungwi', 'nyamagana municipal', 'sengerema', 'ukerewe']
pwani = ['bagamoyo', 'kibaha district', 'kibaha town', 'kisarawe', 'mafia', 'mkuranga', 'rufiji']
rukwa = ['kalambo','nkasi', 'sumbawanga district','sumbawanga municipal']
ruvuma = ['mbinga', 'songea district','songea municipal', 'tunduru', 'namtumbo', 'nyasa']
shinyanga = ['kahama town', 'kahama', 'kishapu', 'shinyanga district', 'shinyanga municipal']
simiyu = ['bariadi', 'busega', 'itilima', 'maswa', 'meatu']
singida = ['ikungi', 'iramba', 'manyoni', 'mkalama', 'singida district', 'singida municipal']
tabora = ['igunga','kaliua', 'nzega','sikonge', 'tabora municipal', 'urambo',  'uyui']
tanga = ['handeni', 'handeni town', 'kilindi', 'korogwe town' , 'korongwe', 'lushoto', 'muhenza', 'mkinga', 'pangani', 'tanga city']

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
		context = {'message':message,}
		return render(request, 'notlogin.html', context)
	else:
		username = usernamelist[0]
	
	
	#extract password
	passwordlist = loginform.getlist('password')
	if not passwordlist:
		message = 'Sorry! Currently you are not log in into this System.'
		context = {'message':message,}
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
		message = 'Please select new status for each water connection'
		context={'user_location':user_location,'message':message,'position':'cowso','welcome_info':welcome_info,'user':user, 'waterpoint_update':waterpoint_update}
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
				
				#setting region depend on district
				if user_district in arusha :
					newuser.region = "Arusha"
				elif user_district in dar_es_salama:
					newuser.region = "Dar-es-salaam"
				elif user_district in dodoma:
					newuser.region = "Dodoma"
				elif user_district in geita :
					newuser.region = "Geita"
				elif user_district in iringa :
					newuser.region = "Iringa"	
				elif user_district in kagera:
					newuser.region = "Kagera"
				elif user_district in kaskazini_Pemba:
					newuser.region = "Kaskazini Pemba"
				elif user_district in kaskazini_unguja:
					newuser.region = "Kaskazini Unguja"
				elif user_district in katavi:
					newuser.region = "Katavi"	
				elif user_district in kigoma :
					newuser.region = "Kigoma"
				elif user_district in kilimanjaro:
					newuser.region = "Kilimanjaro"
				elif user_district in kusini_pemba:
					newuser.region = "Kusini Pemba"
				elif user_district in kusini_unguja:
					newuser.region = "Kusini Unguja"	
				elif user_district in lindi:
					newuser.region = "Lindi"
				elif user_district in manyara:
					newuser.region = "Manyara"
				elif user_district in mara :
					newuser.region = "Mara"
				elif user_district in mbeya:
					newuser.region = "Mbeya"	
				elif user_district in mjini_magharibi:
					newuser.region = "Mjini Magharibi"
				elif user_district in morogoro:
					newuser.region = "Morogoro"
				elif user_district in mtwara:
					newuser.region = "Mtwara"
				elif user_district in mwanza:
					newuser.region = "Mwanza"	
				elif user_district in pwani:
					newuser.region = "Pwani"
				elif user_district in rukwa:
					newuser.region = "Rukwa"
				elif user_district in ruvuma:
					newuser.region = "Ruvuma"
				elif user_district in shinyanga:
					newuser.region = "Shinyanga"	
				elif user_district in simiyu:
					newuser.region = "Simiyu"
				elif user_district in singida:
					newuser.region = "Singida"
				elif user_district in tabora:
					newuser.region = "Tabora"
				elif user_district in tanga:
					newuser.region = "tanga"	
	
				#saving data
				newuser.save()
	
		context = {'kaskazini_unguja':kaskazini_unguja,'kilimanjaro':kilimanjaro,'kusini_pemba':kusini_pemba,
		'mjini_magharibi':mjini_magharibi,'tanga':tanga,'tabora':tabora,'singida':singida,'simiyu':simiyu,
		'shinyanga':shinyanga,'ruvuma':ruvuma,'rukwa':rukwa,'pwani':pwani,'mwanza':mwanza,'mtwara':mtwara,
		'mbeya':mbeya,'mara':mara,'manyara':manyara,'lindi':lindi,'kusini_unguja':kusini_unguja,
		'kigoma':kigoma,'katavi':katavi,'kaskazini_Pemba':kaskazini_Pemba,'kagera':kagera,'iringa':iringa,
		'geita':geita,'dodoma':dodoma,'dar_es_salama':dar_es_salama,'arusha':arusha,'morogoro':morogoro,
		'message':message,'position':'admin','user':user,'warning':warning,'welcome_info':welcome_info}
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
			
			#setting region depend on district
			if user_district in arusha :
				newuser.region = "Arusha"
			elif user_district in dar_es_salama:
				newuser.region = "Dar-es-salaam"
			elif user_district in dodoma:
				newuser.region = "Dodoma"
			elif user_district in geita :
				newuser.region = "Geita"
			elif user_district in iringa :
				newuser.region = "Iringa"	
			elif user_district in kagera:
				newuser.region = "Kagera"
			elif user_district in kaskazini_Pemba:
				newuser.region = "Kaskazini Pemba"
			elif user_district in kaskazini_unguja:
				newuser.region = "Kaskazini Unguja"
			elif user_district in katavi:
				newuser.region = "Katavi"	
			elif user_district in kigoma :
				newuser.region = "Kigoma"
			elif user_district in kilimanjaro:
				newuser.region = "Kilimanjaro"
			elif user_district in kusini_pemba:
				newuser.region = "Kusini Pemba"
			elif user_district in kusini_unguja:
				newuser.region = "Kusini Unguja"	
			elif user_district in lindi:
				newuser.region = "Lindi"
			elif user_district in manyara:
				newuser.region = "Manyara"
			elif user_district in mara :
				newuser.region = "Mara"
			elif user_district in mbeya:
				newuser.region = "Mbeya"	
			elif user_district in mjini_magharibi:
				newuser.region = "Mjini Magharibi"
			elif user_district in morogoro:
				newuser.region = "Morogoro"
			elif user_district in mtwara:
				newuser.region = "Mtwara"
			elif user_district in mwanza:
				newuser.region = "Mwanza"	
			elif user_district in pwani:
				newuser.region = "Pwani"
			elif user_district in rukwa:
				newuser.region = "Rukwa"
			elif user_district in ruvuma:
				newuser.region = "Ruvuma"
			elif user_district in shinyanga:
				newuser.region = "Shinyanga"	
			elif user_district in simiyu:
				newuser.region = "Simiyu"
			elif user_district in singida:
				newuser.region = "Singida"
			elif user_district in tabora:
				newuser.region = "Tabora"
			elif user_district in tanga:
				newuser.region = "tanga"
	
			#saving data
			newuser.save()
	
		context = {'kaskazini_unguja':kaskazini_unguja,'kilimanjaro':kilimanjaro,'kusini_pemba':kusini_pemba,
		'mjini_magharibi':mjini_magharibi,'tanga':tanga,'tabora':tabora,'singida':singida,'simiyu':simiyu,
		'shinyanga':shinyanga,'ruvuma':ruvuma,'rukwa':rukwa,'pwani':pwani,'mwanza':mwanza,'mtwara':mtwara,
		'mbeya':mbeya,'mara':mara,'manyara':manyara,'lindi':lindi,'kusini_unguja':kusini_unguja,
		'kigoma':kigoma,'katavi':katavi,'kaskazini_Pemba':kaskazini_Pemba,'kagera':kagera,'iringa':iringa,
		'geita':geita,'dodoma':dodoma,'dar_es_salama':dar_es_salama,'arusha':arusha,'morogoro':morogoro,
		'message':message ,'user':user,'warning':warning,'welcome_info':welcome_info,'position':'admin' }
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
	waterconnectionlist = []
	cowsolist = []
	cowsofemalelist = []
	cowsomalelist = []
	
	#taking current user of system
	user = Engineer()
	user = Engineer.objects.get(id = user_id)
	
	#taking all water connection and cowso from database
	waterpointlist_database = Waterpoint.objects.all()
	cowsolist_database = Chairperson.objects.all()
	
	#cheching is current user has logged in in the system
	if user.login_status == 'log_out':
		message = 'Sorry! Currently you are not log in into this System.'
		context = {'message':message}
		return render(request, 'notlogin.html', context)
	else:
		# cowso in given district
		for cowso in cowsolist_database:
			if cowso.district == user.district:
				cowsolist.append(cowso)
		for cowso in cowsolist:
			if cowso.sex == 'male':
				cowsomalelist.append(cowso)
			elif cowso.sex == 'female':
				cowsofemalelist.append(cowso)	
			
	#count number of male and female in given district
		malecowso_number = len(cowsomalelist)
		femalecowso_number = len(cowsofemalelist)
		total_cowso = len(cowsolist)
	
		#water connections in given district
		for waterpoint in waterpointlist_database:
			if waterpoint.district == user.district:
				waterconnectionlist.append(waterpoint)
	
		#separate water connection in their categories
		waterpoint_connection = []
		domestic_connection = []
		business_connection = []
		institutional_connection = []
		industrial_connection = []
		for waterconnection in waterconnectionlist:
			if waterconnection.supply_connection == 'waterpoint':
				waterpoint_connection.append(waterconnection)
			elif waterconnection.supply_connection == 'domestic':
				domestic_connection.append(waterconnection)
			elif waterconnection.supply_connection == 'business':
				business_connection.append(waterconnection)
			elif waterconnection.supply_connection == 'institutional':
				institutional_connection.append(waterconnection)
			elif waterconnection.supply_connection == 'industrial':
				industrial_connection.append(waterconnection)
		#count number for water connections		
		waterpoint_connection_no = len(waterpoint_connection)
		domestic_connection_no = len(domestic_connection)
		business_connection_no = len(business_connection)
		institutional_connection_no = len(institutional_connection)	
		industrial_connection_no = len(industrial_connection)
		water_connections_total = len(waterconnectionlist)
	
			
		#return values
		welcome_info = 'Welcome'
		context = {'interface':interface,'water_connections_total':water_connections_total,'industrial_connection_no':industrial_connection_no,'institutional_connection_no':institutional_connection_no,'business_connection_no':business_connection_no,'domestic_connection_no':domestic_connection_no,'waterpoint_connection_no':waterpoint_connection_no,'total_cowso':total_cowso,'femalecowso_number':femalecowso_number,'malecowso_number':malecowso_number,'position':'engineer','welcome_info':welcome_info,'user':user,}
		return render (request, 'reports.html' ,context)	

#report & summary : COWSO chairperson part in District water engineer interface	
def cowso_summary_engineer(request, user_id):
	interface = 'cowsoSummaryEngineer'
	cowsolist = []
	cowsofemalelist = []
	cowsomalelist = []
	
	#taking current user of system
	user = Engineer()
	user = Engineer.objects.get(id = user_id)
	
	#cheching is current user has logged in in the system
	if user.login_status == 'log_out':
		message = 'Sorry! Currently you are not log in into this System.'
		context = {'message':message}
		return render(request, 'notlogin.html', context)
	else:	
		#taking all COWSO from database
		cowsolist_database = Chairperson.objects.all()
	
		# cowso in given district
		for cowso in cowsolist_database:
			if cowso.district == user.district:
				cowsolist.append(cowso)
		for cowso in cowsolist:
			if cowso.sex == 'male':
				cowsomalelist.append(cowso)
			elif cowso.sex == 'female':
				cowsofemalelist.append(cowso)
	
		#return values
		welcome_info = 'Welcome'
		context = {'interface':interface,'cowsomalelist':cowsomalelist ,'cowsofemalelist':cowsofemalelist,'cowsolist':cowsolist,'position':'engineer','welcome_info':welcome_info,'user':user}
		return render (request, 'reports.html' ,context)	



	
#report & summary : COWSO chairperson part in District System admin interface	
def cowso_summary_Admin(request, user_id):
	interface = 'cowsoSummaryAdmin'
	#taking current user of system
	user = Administrator()
	user = Administrator.objects.get(id = user_id)
	
	#cheching is current user has logged in in the system
	if user.login_status == 'log_out':
		message = 'Sorry! Currently you are not log in into this System.'
		context = {'message':message}
		return render(request, 'notlogin.html', context)
	else:
		#taking all COWSO chaiperson from database
		cowsolist =Chairperson.objects.all();
	
		#separete COWSO chairperson depend on their gender or sex
		cowsomalelist = []
		cowsofemalelist = []
		for cowso in cowsolist:
			if cowso.sex == 'male':
				cowsomalelist.append(cowso)
			else:
				cowsofemalelist.append(cowso)	
		#counting COWSO chairperson
		cowsomale_no = len(cowsomalelist)
		cowsofemale_no = len(cowsofemalelist)
		cowso_total = len(cowsolist)
	 
		#return values
		welcome_info = 'Welcome'
		context = {'interface':interface,'cowso_total':cowso_total,'cowsofemale_no':cowsofemale_no,'cowsomale_no':cowsomale_no,'position':'admin','welcome_info':welcome_info,'user':user}
		return render (request, 'reports.html' ,context)


#report & summary : COWSO chairperson part in System admin interface		
def engineer_summary_Admin(request, user_id):
	interface = 'engineerSummaryAdmin'
	#taking current user of system
	user = Administrator()
	user = Administrator.objects.get(id = user_id)
	#cheching is current user has logged in in the system
	if user.login_status == 'log_out':
		message = 'Sorry! Currently you are not log in into this System.'
		context = {'message':message}
		return render(request, 'notlogin.html', context)
	else:
		#taking list of all District Water Engineer From database
		engineerlist = Engineer.objects.all();
	
		#separete engineeer depend on gender or sex
		engineermalelist = []
		engineeerfemalelist = []
		for engineer in engineerlist:
			if engineer.sex == 'male':
				engineermalelist.append(engineer)
			else:
				engineeerfemalelist.append(engineer)
	
		#counting engineers
		engineeermale_no = len(engineermalelist)
		engineeerfemale_no = len(engineeerfemalelist)
		engineeer_total = len(engineerlist)		
				
		#return values
		welcome_info = 'Welcome'
		context = {'interface':interface,'engineeer_total':engineeer_total,'engineeerfemale_no':engineeerfemale_no,'engineeermale_no':engineeermale_no,'position':'admin','welcome_info':welcome_info,'user':user}
		return render (request, 'reports.html' ,context)
 


#to view all details for a given COWSO chairperson if query is from District water Engineer
def cowso_DetailsFromEngineer(request, user_id,cowso_id):
	#taking current user of the system
	user = Engineer()
	user = Engineer.objects.get(id = user_id)
	
	#cheching is current user has logged in in the system
	if user.login_status == 'log_out':
		message = 'Sorry! Currently you are not log in into this System.'
		context = {'message':message}
		return render(request, 'notlogin.html', context)
	else:
		#taking requested cowso from database
		cowso = Chairperson()
		cowso = Chairperson.objects.get(id = cowso_id)
	
		#return values
		welcome_info = "Welcome"
		detail = 'cowso_engineer'
		context = {'detail':detail,'position':'engineer','welcome_info':welcome_info,'user':user,'cowso':cowso}
		return render(request, 'moredetails.html',context)



#To view all details for a given District water engineer 
def engineer_DetailsFromAdmin(request, user_id,engineer_id):
	
	#return values
	welcome_info = "Welcome"
	context = {'position':'admin','welcome_info':welcome_info,'user':user}
	return render(request, 'moredetails.html',context)

#to view all details for a given COWSO chairperson if query is from admin
def cowso_DetailsFromAdmin(request, user_id,engineer_id):
	
	#return values
	welcome_info = "Welcome"
	context = {'position':'admin','welcome_info':welcome_info,'user':user}
	return render(request, 'moredetails.html',context)
















	
	
	
