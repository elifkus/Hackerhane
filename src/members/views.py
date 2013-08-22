from django.shortcuts import render, render_to_response
from members.models import HsUser
from django.template.context import RequestContext

def home(request):
    users = HsUser.objects.all()
    return render_to_response('index.html', {'members': users,},
                        context_instance=RequestContext(request))
