'''
Created on Aug 25, 2013

@author: elif
'''
from django.core.management.base import LabelCommand, CommandError

from datetime import datetime, date
from accounting.models import ExpectedIncome, MonthlyRecurringExpense,ExpectedExpense
from membership.models import Membership, Payment


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
        
        memberships_unpaid = Membership.objects.all().exclude(payment__paid_month=1)
        
        for membership in memberships_unpaid:
            amount = membership.custom_amount or membership.type.monthly_fee_amount
            month_str = Payment.MONTHS[month_int-1][1]
            note = month_str + " ayı aidatı - " + " ".join(membership.users) 
            today = datetime.today()
            expected_date = date(today.year, today.month, 5)
        
            expected_income = ExpectedIncome(amount=amount, note=note, type=1,  
                                        expected_date=expected_date, membership=membership)
            
            expected_income.save()

        recurring_expenses = MonthlyRecurringExpense.objects.all()
        
        for recurring_expense in recurring_expenses:
            
            today = datetime.today()
            expected_date = date(today.year, today.month, 10)
        
            expected_expense = ExpectedExpense(amount=recurring_expense.amount, type=recurring_expense.type,
                                                expected_date=expected_date)
            
            expected_expense.save()
            