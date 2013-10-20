'''
Created on Oct 13, 2013

@author: elif
'''
from django.core.management.base import NoArgsCommand

from members.models import ExistingMemberInformation, HsUser


class Command(NoArgsCommand):
    '''
    Command for generating users from existing users
    '''
    def handle_noargs(self, **options):
        existing_user_infos = ExistingMemberInformation.objects.all()
        
        for existing_info in existing_user_infos:
            HsUser.objects.create_user(existing_info.email, existing_info.cell_phone_number, 
                                       existing_info.is_student or False, 
                                       password=None,
                                       full_name=existing_info.full_name, is_active=True)
            existing_info.delete()
        