from django.test import TestCase
from django.db import connections

# Create your tests here.
class DbConnTest(TestCase):

    def test_db_connection(self):
        result = False

        db_con = connections['default']
        cursor = db_con.cursor()
        print("Cursor:", cursor)
        if cursor:
            result = True

        self.assertEqual(result, True, "Cannot connect to Database")
    
        




