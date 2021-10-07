from calendar import IllegalMonthError
import datetime
from django.test import SimpleTestCase
from .views import AllActivities
from .models import Activity
# Create your tests here.
class GetDatesByDayTestCase(SimpleTestCase):

    def test_non_existent_month(self):
        all_act = AllActivities() 
        try:
            test = all_act.getDatesByDay(1,13,2021)
        except IllegalMonthError:
            self.fail("There is not error handling with non-existen month")
    
    def test_non_existent_day(self):
        all_act = AllActivities()     
        try:
            test = all_act.getDatesByDay(10,10,2021)
        except IllegalMonthError:
            self.fail("There is not error handling with non-existen day")

    def test_negative_year(self):
        all_act = AllActivities()    
        try:
            test = all_act.getDatesByDay(1,10,-2020)
        except ValueError:
            self.fail("There is not error handling with negative year")
    
    def test_leap_year_and_day_29(self):
        all_act = AllActivities()    
        test = all_act.getDatesByDay(6,2,2020)
        self.assertEqual(test,[datetime.date(2020, 2, 1), datetime.date(2020, 2, 8), datetime.date(2020, 2, 15), datetime.date(2020, 2, 22), datetime.date(2020, 2, 29)])        