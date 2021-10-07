from calendar import month
from django.test import TestCase
from django.test import SimpleTestCase
from django.test import TransactionTestCase

from gymTeachers.models import Teacher

from .models import Activity
from .views import AllActivities
from gymServices.models import Service
from AdmSchedule.models import Schedule
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
        selected_service = Service.objects.get(id=1)
        selected_teacher = Teacher.objects.get(person_id=1)
        selected_schedule = Schedule.objects.last()
        new_Act = Activity.objects.create( capacity = 10, 
                            dayofweek = 5,
                            dayofmonth = 10,

                            startime = datetime.time(10, 30, 00), 
                            endtime = datetime.time(11, 30, 00),

                            service = selected_service, 
                            teacher = selected_teacher,
                            schedule = selected_schedule                   
                        )
    
    def no_time_day_overlap(self):
        all_act = AllActivities()
        startTime = "8:30"
        endTime = "9:30"
        day = 1
        test = all_act.checkOverlap(startTime, endTime,day)
        self.assertIs(test, False)

    def time_overlap_no_day_overlap(self):
        all_act = AllActivities()
        startTime = "10:30"
        endTime = "11:30"
        day = 1
        test = all_act.checkOverlap(startTime, endTime,day)
        self.assertIs(test, False)
    
    def time_day_overlap(self):
        all_act = AllActivities()
        startTime = "10:30"
        endTime = "11:30"
        day = 5
        test = all_act.checkOverlap(startTime, endTime,day)
        self.assertIs(test, True)