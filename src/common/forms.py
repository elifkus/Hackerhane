'''
Created on Sep 10, 2013

@author: elif
'''
from django import forms
from django.utils.html import escape
from django.utils.safestring import mark_safe
from django.forms.util import flatatt


class ReadOnlyWidget(forms.Widget):
    def render(self, name, value, attrs):
        final_attrs = self.build_attrs(attrs, name=name)
        if hasattr(self, 'initial'):
            value = self.initial
            return mark_safe("<p %s>%s</p>" % (flatatt(final_attrs), escape(value) or ''))

    def _has_changed(self, initial, data):
        return False

class ReadOnlyField(forms.Field):
    widget = ReadOnlyWidget
    def __init__(self, widget=None, label=None, initial=None, help_text=None):
        super(type(self), self).__init__(self, label=label, initial=initial, 
            help_text=help_text, widget=widget)
        self.widget.initial = initial

    def clean(self, value):
        return self.widget.initial
    