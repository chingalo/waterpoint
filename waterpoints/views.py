from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, render
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from users.models import *
from waterpoints.forms import *
from waterpoints.models import *

#regions with respective districts
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
		code_number = ''
		message = ''
		warning = ''
		name = ''
		source_name = ''
		district = ''
		region = ''
		physical_location_name = ''
		latitude = ''
		longitude = ''
		fund = ''
		sponsor = ''
		if request.POST:
			
			#take form from template
			form = request.POST
		
			#taking values from posted form
			code_number_list = form.getlist('code_number')
			code_number = code_number_list[0]
		
			water_connection_list = form.getlist('name')
			water_connection = water_connection_list[0]
		
			source_name_list = form.getlist('source_name')
			source_name = source_name_list[0]
		
			supply_connectionlist = form.getlist('supply_connection')
			supply_connection = supply_connectionlist[0]
		
			district_list = form.getlist('district')
			district = district_list[0]
		
			region_list = form.getlist('region')
			region = region_list[0]
		
			physical_location_name_list = form.getlist('physical_location_name')
			physical_location_name = physical_location_name_list[0]
		
			latitude_list = form.getlist('latitude')
			latitude = latitude_list[0]
		
			longitude_list = form.getlist('longitude')
			longitude = longitude_list[0]
		
			fund_list = form.getlist('fund')
			fund = fund_list[0]
		
			sponsor_list = form.getlist('sponsor')		
			sponsor = sponsor_list[0]
		
			#checking if form is completed or not, and taking the action
			if code_number == '' or water_connection == '' or source_name == '' or district == '' or region == '' or physical_location_name == '' or latitude == '' or longitude == '' or sponsor == '' or fund == '':
				warning = 'Please fill all information below, for successfull create new water supply connection'
			else:
				message = 'You  have successfull create new water supply connection'	
			#saving the form if all fields have been filled
			if message:
				#create object
				new_water_connection = Waterpoint()
				
				#supply values
				new_water_connection.code_number = 	code_number
				new_water_connection.name = water_connection
				new_water_connection.source_name = source_name
				new_water_connection.supply_connection = supply_connection
				new_water_connection.district = district
				new_water_connection.region = region
				new_water_connection.physical_location_name = physical_location_name
				new_water_connection.latitude = latitude
				new_water_connection.longitude = longitude
				new_water_connection.fund = fund
				new_water_connection.sponsor =  sponsor
				
				#saving form
				new_water_connection.save()
				
		context = {'warning':warning,'message':message,'position':'engineer', 'user':user,'welcome_info':welcome_info}
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
				return render(request,'users.html',context)	
							
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
	if user.login_status == 'log_out':
		message = 'Sorry! Currently you are not log in into this System.'
		context = {'message':message}
		return render(request, 'notlogin.html', context)
	else:
		#taking query dictionary having list of status
		form = request.POST
	
		#extract list of status from a form posted
		statuslist = form.getlist('status')
		status_list_length = len(statuslist)
		waterpoint_update = []
		status = []
	
		#taking list of ststus and correspond status to be updated
		for waterpoint in waterpointslist:
			for status_update in statuslist:
				if  status_update == '':
					statuslist.remove(status_update)
				else:
					if  waterpoint.physical_location_name == user_location:
						waterpoint_update.append(waterpoint)
						status.append(status_update)						
						statuslist.remove(status_update)
	
		#checking if all water point having status and if so save it				
		if len(waterpoint_update) == status_list_length:
			#new object to create new status for a given water point			
			
			
			for waterpoint_updated in waterpoint_update:
				updated = status[0]
				#saving status
				new_waterpoint_status = Waterpoint_status()
				new_waterpoint_status.name = waterpoint_updated
				new_waterpoint_status.status = updated
				new_waterpoint_status.save()
				status.remove(status[0])		
			context = {'position':'cowso','user':user,}	
			return render (request, 'cowsoupdateinfo.html', context)
	
		else:
			#return empty form when no status is supplied
			waterpoint_update = []
			for waterpoint in waterpointslist:
				if  waterpoint.physical_location_name == user_location :
					waterpoint_update.append(waterpoint)
			warning = 'Please make sure you have selected new status for each water point!'
			welcome_info = 'Welcome'
			context={'user_location':user_location,'warning':warning,'position':'cowso','welcome_info':welcome_info,'user':user, 'waterpoint_update':waterpoint_update}
			return render(request, 'users.html',context)


#report & summary : water connection part in District water engineer interface
def water_connection_summary_engineer(request, user_id):
	interface = 'engineerWaterConections'
	waterconnectionlist = []
	
	#taking current user of system
	user = Engineer()
	user = Engineer.objects.get(id = user_id)
	
	#taking all water connections from database
	waterpointlist_database = Waterpoint.objects.all()
	
	#cheching is current user has logged in in the system
	if user.login_status == 'log_out':
		message = 'Sorry! Currently you are not log in into this System.'
		context = {'message':message}
		return render(request, 'notlogin.html', context)
	else:
		#select all water connections in a given district
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
	
		#return values
		welcome_info = 'Welcome'
		context = {'interface':interface,'industrial_connection':industrial_connection,'institutional_connection':institutional_connection,'business_connection':business_connection,'domestic_connection':domestic_connection,'waterpoint_connection':waterpoint_connection,'position':'engineer','welcome_info':welcome_info,'user':user}
		return render (request, 'reports.html' ,context)
	


#report & summary : water connection part in System admin interface
def water_connection_summary_admin(request, user_id):
	interface = 'waterconnectionSummaryAdmin'
	#taking current user of system
	user = Administrator()
	user = Administrator.objects.get(id = user_id)
	
	#cheching is current user has logged in in the system
	if user.login_status == 'log_out':
		message = 'Sorry! Currently you are not log in into this System.'
		context = {'message':message}
		return render(request, 'notlogin.html', context)
	else:
	
		#taking all water point from the system:
		waterpointlist_database = Waterpoint.objects.all()
		#separate water connection in their categories
		waterpoint_connection = []
		domestic_connection = []
		business_connection = []
		institutional_connection = []
		industrial_connection = []
		for waterconnection in waterpointlist_database:
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
		water_connections_total = len(waterpointlist_database)
		
		#return values
		welcome_info = 'Welcome'
		context = {'interface':interface,'water_connections_total':water_connections_total,'industrial_connection_no':industrial_connection_no,'institutional_connection_no':institutional_connection_no,'business_connection_no':business_connection_no,'domestic_connection_no':domestic_connection_no,'waterpoint_connection_no':waterpoint_connection_no,'position':'admin','welcome_info':welcome_info,'user':user}
		return render (request, 'reports.html' ,context)	
	
	
# to view all detail concerned a given water connection
def water_connection_DetailsFromEngineer(request, user_id,water_connection_id):
	#taking current user of the system
	user = Engineer()
	user = Engineer.objects.get(id = user_id)
	#cheching is current user has logged in in the system
	if user.login_status == 'log_out':
		message = 'Sorry! Currently you are not log in into this System.'
		context = {'message':message}
		return render(request, 'notlogin.html', context)
	else:	

		#taking queried water connetion form data base
		water_connection = Waterpoint()
		water_connection = Waterpoint.objects.get(id = water_connection_id)
	
		#taking all images from database
		imagelist_database = Waterpoint_photos.objects.all()
	
		#select images for a given water point
		imagelist = []
		for image in imagelist_database:
			if image.photos == water_connection:
				imagelist.append(image)
	
	
		#taking all status form database
		statuslist_database = Waterpoint_status.objects.all()
	
		#taking status for a given water point
		statuslist = []
		for status in statuslist_database:
			if status.name == water_connection:
				statuslist.append(status)
	
		#return values
		welcome_info = "Welcome"
		detail = 'water_connection_engineer'
		context = {'detail':detail,'water_connection':water_connection,'imagelist':imagelist,'statuslist':statuslist,'water_connection':water_connection,'position':'engineer','welcome_info':welcome_info,'user':user,}
		return render(request, 'moredetails.html',context)	
				
