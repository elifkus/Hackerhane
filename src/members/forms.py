'''
Created on Sep 9, 2013

@author: elif
'''
from django import forms

class SignUpForm(forms.Form):
    full_name = forms.CharField(max_length=64)
    email = forms.CharField(max_length=255)
    cell_phone_number = forms.CharField(max_length=16)
    is_student = forms.BooleanField()

    def save(self, user):
        user.full_name = self.cleaned_data['full_name']
        user.email = self.cleaned_data['email']
        user.cell_phone_number = self.cleaned_data['cell_phone_number']
        user.is_student = self.cleaned_data['is_student']
        user.save()