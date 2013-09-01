from django.shortcuts import render_to_response
from members.models import HsUser
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    
    return render_to_response('index.html', {'members': None,},
                        context_instance=RequestContext(request))
    
def user_home(request, user_id):
    user = None
    
    try:
        user = HsUser.objects.get(user_id)
    except HsUser.DoesNotExist as e:
        #do nothing
        pass
    
    template = None
    
    if user:
        template = "404.html"
    else:
        template = "show_user.html"
        
    return render_to_response(template, {'user': user,},
                              context_instance=RequestContext(request))