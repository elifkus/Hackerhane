'''
Created on Oct 23, 2013

@author: elif
'''

from django import template
register = template.Library()

@register.simple_tag
def get_field_label(instance, field_name):
    """
    Returns verbose_name for a field.
    """
    return instance._meta.get_field(field_name).verbose_name.title()