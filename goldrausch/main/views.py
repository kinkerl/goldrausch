from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render, render_to_response, get_object_or_404
from django.conf import settings
from django.utils.translation import ugettext as _
from django.utils import translation
from main.models import Agent, Task

def index(request):
	c = {
	}
	ret = RequestContext(request,c)
        return render_to_response('main/index.html', ret)


def update(request, boardid, eventid, statuscode, secret):
	print "incomming %s %s %s %s" %(boardid, eventid, statuscode, secret)
	ret = RequestContext(request,{})

	agent = get_object_or_404(Agent, code=boardid)
	if not agent.secret == secret:
	        return render_to_response('main/error.xml', ret)		
	task = get_object_or_404(Task, code=eventid)
	task.status = statuscode
	task.save()
        return render_to_response('main/response.xml', ret)


def overview(request):
	agent_list = Agent.objects.all()
	ret = RequestContext(request, {'agent_list':  agent_list})
	return render(request, 'main/overview.xml', ret, content_type="application/xml")


