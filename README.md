waterpoint
==========
It is python powered django cms website project.
It aims at control and manage all water connections available in The United Republic Of Tanzania, through uses of static and dynamic  informations about these water connections.
These water connections includes kiosk or water point connections,business connections, industrial connections, institutional connections and domestics connections.
These system is work through full participation of user's categories, which are System Administrator, The District Water Engineer, and COWSO chairperson.
But in order to access the system these users must have user-name and password for authentication so that only authorized users can access the system depend on their user's role in system.
The System administrator is responsible to create, control and manage all information concerned water connection,The District Water Engineer, and COWSO chairperson.
The District Water Engineer is responsible  for full registration of water connections and views all all informations or status of water connections in his or her district.
Also The District Water Engineer can views information about COWSO Chairperson in his or her district.
Lastly, COWSO chairperson is responsible to update status of all water connections in his or her village or street.


How to install this site:
====================================
Install virtualenv on your machine and use it to maintain the site.
The following are couple of commands for operating under virtual env:

	#Install python virtualenv
	$ sudo apt-get install python-virtualenv
	
	#Create a virtual environment directory
	$ virtualenv /path/to/virtualenv_dir
	
	#Activating virtual environment(while you're in virtualenv_dir)
	$ source bin/activate
	
	#Deactivating virtual env
	$ deactivate

After creating and activating virtualenv, while inside virtualenv folder,
clone this site's source codes:
	
	$ git https://github.com/chingalo/waterpoint.git

Inside waterpoint directory, install project dependencies inside: deps.txt
	$ cd waterpoint
	$ pip install -r deps.txt
Add database  configurations inside waterpoint/settings.py, your
database configurations should look something similar to this:
	
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.postgresql_psycopg2',
			'HOST': 'localhost',
			'NAME': 'DATABASENAME',
			'USER': 'USERNAME',
			'PASSWORD': 'THESECRETPASSWORD',
			'PORT':'5432',
		}
	}
After configuration sync database( run command: python manage.py syncdb --all) and then run the server( run command: python manage.py runserver ).

Incase of any difficulties in configuration refer to [Django CMS Documentation](http://django-cms.readthedocs.org/en/2.2/getting_started/installation.html)
for more information.
