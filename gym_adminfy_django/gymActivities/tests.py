from django.test import TestCase

# from .models import Activity
# from .views import AllActivities

import datetime

# Create your tests here.
# class GetDatesByDayTestCase(TestCase):

#     def test_animals_can_speak(self):
#         """Animals that can speak are correctly identified"""
#         # all_act = AllActivities() 
#         # all_act.getDatesByDay()
#         # self.assertEqual(lion.speak(), 'The lion says "roar"')
#         self.assertEqual('The cat says "roar"', 'The cat says "meow"')
        
class CheckOverlap(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Activity.objects.create(dayofweek = 5,startime = datetime.time(10, 30, 00),endtime = datetime.time(11, 30, 00))
        pass
    
    def dia_fecha_negativos(self):
        #all_act = AllActivities()
        startTime = datetime.time(10, 30, 00)
        endTime = datetime.time(11, 30, 00)
        day = 5
        # print(all_act.checkOverlap(startTime, endTime,day))
        # self.assertIs(all_act.checkOverlap(startTime, endTime,day), True)