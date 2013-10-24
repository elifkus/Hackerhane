'''
Created on Sep 12, 2013

@author: elif
'''
from django.conf.urls import url, patterns
from django.contrib.auth.decorators import login_required
from accounting.views import grid_handler, grid_config
from django.views.generic.base import TemplateView
from django.contrib.admin.views.decorators import staff_member_required


urlpatterns = patterns('',
    url(r'^$', staff_member_required(TemplateView.as_view(template_name="accounting/transaction_list.html")), name='transaction-list'),
    url(r'^transaction-grid/$', staff_member_required(grid_handler), name='grid_handler'),
    url(r'^transaction-grid/cfg/$', staff_member_required(grid_config), name='grid_config'),
)