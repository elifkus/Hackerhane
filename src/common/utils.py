'''
Created on Oct 24, 2013

@author: elif
'''
from django.utils.dates import MONTHS

def note_from_month_index(month_number, membership):
    month_str = MONTHS[month_number]
    note = month_str + " ayı aidatı - " 
    
    if membership:
        note+= str(membership)
        
    return note        


def note_from_month(month, membership):
    month_int = month.month
    return note_from_month_index(month_int, membership)