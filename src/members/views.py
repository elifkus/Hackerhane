from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
from members.models import HsUser


@login_required
def home(request):
    
    return render_to_response('index.html',
                        context_instance=RequestContext(request))
    
class OwnUserUpdateView(UpdateView):
    model = HsUser
    fields = ['email_visible','cell_phone_number','cell_phone_number_visible','full_name', 
                    'nickname','is_student', 'summary', 'reason']
    def get_object(self, queryset=None):
        return HsUser.objects.get(pk=self.request.user.id)
    
    
