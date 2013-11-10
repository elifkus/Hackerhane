from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from members.models import HsUser, WebLink
from members.forms import HsUserForm
from django.forms.models import inlineformset_factory
import logging 
from django.contrib import messages


logger = logging.getLogger(__name__)

def home(request):
    user = request.user
    
    if user.is_authenticated():
        if user.is_active:
            return render_to_response('index.html',
                        context_instance=RequestContext(request))
        else:
            return render_to_response('not_allowed.html',
                        context_instance=RequestContext(request))
    else:
        return redirect("/accounts/login/")
    
    
def ask_admin(request):
    return render_to_response('not_allowed.html',
                        context_instance=RequestContext(request))
    

def view_user(request, pk):
    user_id = int(pk)
    
    member = None
    links = None
    try:
        member = HsUser.objects.get(id=user_id)
        links = WebLink.objects.filter(user_id=user_id)
    except HsUser.DoesNotExist:
        pass

    return render_to_response('members/hsuser_detail.html',
                              {'object': member,
                               'links': links},
                               context_instance=RequestContext(request))
    

def update_own_user(request):
    
    if request.method == "POST":
        user_form = HsUserForm(request.POST, prefix='user', instance=request.user)
        WebLinkFormset = inlineformset_factory(HsUser, WebLink)
        link_formset = WebLinkFormset(request.POST, request.FILES, instance=request.user, prefix="link")
        
        if user_form.is_valid() and link_formset.is_valid():
            user_form.save()
            link_formset.save()
            
            messages.success(request, 'Bilgileriniz güncellendi.')
            
            return redirect(request.user.get_absolute_url())
        
    else:
        user_form = HsUserForm(instance=request.user, prefix="user")
        WebLinkFormset = inlineformset_factory(HsUser, WebLink)
        link_formset = WebLinkFormset(instance=request.user, prefix="link")
        
    return render_to_response('members/hsuser_form.html',
                                  {'user_form': user_form,
                                   'link_formset': link_formset},
                                  context_instance=RequestContext(request)
                                 ) 

