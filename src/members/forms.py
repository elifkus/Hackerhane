'''
Created on Sep 9, 2013

@author: elif
'''
from django import forms
from common.forms import ReadOnlyField
from django.forms.models import ModelForm
from members.models import HsUser


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
        

class ExampleForm(forms.Form):
    username = forms.CharField(max_length=30, label="Username")
    email = forms.EmailField(label="Email")


class HsUserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(HsUserForm, self).__init__(*args, **kwargs)
        
        self.fields['email'].widget.attrs['readonly'] = True
 
    
    class Meta:
        model = HsUser
        fields = ('full_name', 'email_visible', 'nickname', 'cell_phone_number', 
                  'cell_phone_number_visible', 'is_student', 'summary', 'reason','id', 'email')
        #exclude = ('email',)
