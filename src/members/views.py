from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from django.views.generic.edit import UpdateView
from members.models import HsUser, WebLink


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
    
    
class OwnUserUpdateView(UpdateView):
    model = HsUser
    fields = ['email_visible','cell_phone_number','cell_phone_number_visible','full_name', 
                    'nickname','is_student', 'summary', 'reason']
    def get_object(self, queryset=None):
        return HsUser.objects.get(pk=self.request.user.id)
    

