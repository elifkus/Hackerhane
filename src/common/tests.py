from django.test import TestCase
from common.utils import note_from_month_index

# Create your tests here.

class UtilTestCase(TestCase):
    def test_note_from_month_index(self):
        membership = None
        month_int = 3
        
        note = note_from_month_index(month_int, membership)
        
        self.assertEqual(note, 'Mart ayı aidatı - ')
        

