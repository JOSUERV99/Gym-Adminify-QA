from django.test import TestCase
from django.test import SimpleTestCase

from .views import AllActivities

from .models import Activity
from gymServices.models import Service
from AdmSchedule.models import Schedule
from gymTeachers.models import Teacher
from gymPersons.models import Person
from gymTeachers.models import Teachercategory

from calendar import IllegalMonthError, month
from datetime import datetime

class CheckOverlap(TestCase):

    @classmethod
    def setUpTestData(cls):
        # initialices the objects needed for the activity test
        Schedule.objects.create(
            month = 5,
            year = 2021
        )
        
        Service.objects.create(
            name = "Yoga",
            description = "Clases de yoga",            
            hourfee = 10.5
        )
        
        Person.objects.create(
            name = "Ericka",
            phone = 88888888,
            mail = "ericka@gmail.com",
            identification = "117870177"
        )
        
        Teachercategory.objects.create(
            name = "Principal"
        )
        
        # saves foreigns keys for the class Teacher and Activity  
        selected_person = Person.objects.get(id=1)
        selected_teacher_category = Teachercategory.objects.get(id=1)
        selected_service = Service.objects.get(id=1)
        
        Teacher.objects.create(
            person = selected_person ,
            teachercategory = selected_teacher_category,
        )
        
        selected_teacher = Teacher.objects.get(person_id=1)
        selected_schedule = Schedule.objects.last()
        
        Activity.objects.create(
            capacity = 10, 
            dayofweek = 5,
            dayofmonth = 10,

            startime = datetime.time(10, 30, 00), 
            endtime = datetime.time(11, 30, 00),

            service = selected_service, 
            teacher = selected_teacher,
            schedule = selected_schedule                   
        )
        # end setup
        
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
class GetDatesByDayTestCase(SimpleTestCase):
    
    def setUp(self):
        self.all_act = AllActivities() 
    
    def test_non_existent_month(self):
        try:
            self.all_act.getDatesByDay(1,13,2021)
        except IllegalMonthError:
            self.fail("There is not error handling with non-existen month")
    
    def test_non_existent_day(self):   
        try:
            self.all_act.getDatesByDay(10,10,2021)
        except IllegalMonthError:
            self.fail("There is not error handling with non-existen day")

    def test_negative_year(self):  
        try:
            self.all_act.getDatesByDay(1,10,-2020)
        except ValueError:
            self.fail("There is not error handling with negative year")
    
    def test_leap_year_and_day_29(self):
        test = self.all_act.getDatesByDay(6,2,2020)
        self.assertEqual(test,[datetime.date(2020, 2, 1), datetime.date(2020, 2, 8), datetime.date(2020, 2, 15), datetime.date(2020, 2, 22), datetime.date(2020, 2, 29)])        
    
    def test_current_date(self):  
        test = self.all_act.getDatesByDay(4,10,2021)
        self.assertEqual(test,[datetime.date(2021, 10, 7), datetime.date(2021, 10, 14), datetime.date(2021, 10, 21), datetime.date(2021, 10, 28)])        

