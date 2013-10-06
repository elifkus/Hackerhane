'''
Created on Sep 12, 2013

@author: elif
'''
from django.conf.urls import url, patterns
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from accounting.models import Transaction
from accounting.views import JSONListView, grid_handler, grid_config
from django.views.generic.base import TemplateView


urlpatterns = patterns('',
    url(r'^$', login_required(ListView.as_view(
        model=Transaction,
        queryset=Transaction.objects.order_by("-realized_date"),
        )), 
        name = 'transaction-list'
    ),
    url(r'^json$', login_required(JSONListView.as_view(
        model=Transaction,
        queryset=Transaction.objects.order_by("-realized_date"),
        )), 
        name = 'transaction-list-json'
    ),
    url(r'^2$', TemplateView.as_view(template_name="accounting/transaction_list2.html")),
    url(r'^examplegrid/$', grid_handler, name='grid_handler'),
    url(r'^examplegrid/cfg/$', grid_config, name='grid_config'),
)