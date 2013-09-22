'''
Created on Sep 12, 2013

@author: elif
'''
from django.conf.urls import url, patterns
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from accounting.models import Transaction
from accounting.views import JSONListView


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
)