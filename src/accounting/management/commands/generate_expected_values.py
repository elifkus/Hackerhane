'''
Created on Aug 25, 2013

@author: elif
'''
from django.core.management.base import LabelCommand, CommandError
from datetime import datetime, date
from accounting.models import ExpectedIncome, MonthlyRecurringExpense,ExpectedExpense
from membership.models import Membership
from calendar import monthrange
from django.utils.dates import MONTHS


class Command(LabelCommand):
    '''
    Command for generating expected income and expenses
    '''
    def handle_label(self, label, **options):
        month_int = None
        
        try:
            month_int = int(label)
        except ValueError as  e:
            self.stderr.write("Argument supplied is not an integer")
            raise CommandError(e)
        __unused_weekday, last_day = monthrange(2013, month_int)
        memberships_unpaid = Membership.objects.all().exclude(feepayment__paid_month__range=(date(2013, month_int, 1), date(2013, month_int, last_day)))
        
        for membership in memberships_unpaid:
            amount = membership.custom_amount or membership.type.monthly_fee_amount
            #TODO: Fix this use django date format
            month_str = MONTHS[month_int]
            
            note = month_str + " ayı aidatı - " + str(membership)
            today = datetime.today()
            expected_date = date(today.year, month_int, 1)
        
            expected_income = ExpectedIncome(amount=amount, note=note, type_id=1,  
                                        expected_date=expected_date)
            
            expected_income.save()

        recurring_expenses = MonthlyRecurringExpense.objects.all()
        
        for recurring_expense in recurring_expenses:
            
            today = datetime.today()
            expected_date = date(today.year, month_int, recurring_expense.day_of_occurrence)
        
            expected_expense = ExpectedExpense(amount=recurring_expense.amount, type=recurring_expense.type,
                                                expected_date=expected_date)
            
            expected_expense.save()
            