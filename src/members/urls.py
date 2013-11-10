from django.conf.urls import patterns, url
from django.views.generic.list import ListView
from members.models import HsUser
from django.contrib.auth.decorators import login_required
from members.views import update_own_user
from members import views
from django.views.generic.base import TemplateView
from members.forms import ExampleForm



urlpatterns = patterns('',
    url(r'^uyeler/$', login_required(ListView.as_view(
        queryset=HsUser.objects.all().exclude(email='kasa@istanbulhs.org'),
        )), 
        name = 'member-list'
    ),
    url(r'^uyeler/(?P<pk>\d+)/$', login_required(views.view_user),
                       name='show-member'),
    url(r'^degistir/$', login_required(
            update_own_user),
        name='edit-current-user'),
    url(r'^example/$', TemplateView.as_view(template_name="example.html"), {'form': ExampleForm()}),
) 