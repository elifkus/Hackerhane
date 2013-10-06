'''
Created on Sep 12, 2013

@author: elif
'''
from django.conf.urls import url, patterns
from django.contrib.auth.decorators import login_required
from accounting.views import grid_handler, grid_config
from django.views.generic.base import TemplateView


urlpatterns = patterns('',
    url(r'^$', login_required(TemplateView.as_view(template_name="accounting/transaction_list.html")), name='transaction-list'),
    url(r'^transaction-grid/$', login_required(grid_handler), name='grid_handler'),
    url(r'^transaction-grid/cfg/$', login_required(grid_config), name='grid_config'),
)