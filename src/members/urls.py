from django.conf.urls import patterns, url
from django.views.generic.list import ListView
from members.models import HsUser
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
    url(r'^uyeler/$', login_required(ListView.as_view(
        model=HsUser,
        )), 
        name = 'member-list'
    ),
)