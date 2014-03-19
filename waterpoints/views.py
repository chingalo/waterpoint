from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, render
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from users.models import *
from waterpoints.forms import WaterpointRegistration
from waterpoints.models import *

#description of waterpoints
def waterpointDetail(request):
	context = {'message': "ok"}
	if request.POST:
	 form = WaterpointRegistration(request.POST)
	 if form.is_valid():
	    form.save()	    
         return render(request, 'test2.html',context)
        else:
		 form = WaterpointRegistration()
		 args = {}
		 args.update(csrf(request))
		 args[ 'form' ] = form
		 return render_to_response('test.html',args)	

