from django.conf.urls import patterns, url
from django.views.generic.list import ListView
from members.models import HsUser
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from members.views import OwnUserUpdateView


urlpatterns = patterns('',
    url(r'^uyeler/$', login_required(ListView.as_view(
        model=HsUser,
        )), 
        name = 'member-list'
    ),
    url(r'^uyeler/(?P<pk>\d+)/$', login_required(DetailView.as_view(
                                model=HsUser,
                                )),
                       name='show-member'),
    url(r'^degistir/$', login_required(
            OwnUserUpdateView.as_view()),
        name='edit-current-user'),
)