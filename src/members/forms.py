'''
Created on Sep 9, 2013

@author: elif
'''
from django import forms
from common.forms import ReadOnlyField


class SignupForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        
        if not self.initial:
            self.email = forms.CharField(max_length=256, required=True)
        else:
            self.fields['email'].widget.attrs['readonly'] = True
            
    full_name = forms.CharField(max_length=64)
    email = ReadOnlyField()
    cell_phone_number = forms.CharField(max_length=16)
    is_student = forms.BooleanField(required=False)

    def save(self, user):
        user.full_name = self.cleaned_data['full_name']
        user.email = self.cleaned_data['email']
        user.cell_phone_number = self.cleaned_data['cell_phone_number']
        user.is_student = self.cleaned_data['is_student']
        user.save()
        

