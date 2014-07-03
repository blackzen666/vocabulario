#from django.template.loader import get_template
#from django.template import Context
#from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime


def addVocabulario(request):
	now = datetime.datetime.now()
	#t = get_template('current_datetime.html')
	#html = t.render(Context({'current_datetime': now}))
	#html = "<html><body>La hora es %s.</body></htm>"%now
	#return HttpResponse(html)
	return render_to_response('vocabularios.html',)#{'current_datetime': now})
