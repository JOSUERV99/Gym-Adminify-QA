from django.test import TestCase

from ..views import AllActivities

from ..models import Activity
from gymServices.models import Service
from AdmSchedule.models import Schedule
from gymTeachers.models import Teacher
from gymPersons.models import Person
from gymTeachers.models import Teachercategory

import datetime

class CheckOverlap(TestCase):

    @classmethod
    def setUp(self):
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
            dayofweek = 1,
            dayofmonth = 1,

            startime = datetime.time(10, 30, 00), 
            endtime = datetime.time(11, 30, 00),

            service = selected_service, 
            teacher = selected_teacher,
            schedule = selected_schedule                   
        )
        
        # end setup
    
    def test_no_time_day_overlap(self):
        """
        1- Escenario donde no choca ni el día ni la hora
        """
        all_act = AllActivities()
        
        startTime = "8:30"
        endTime = "10:29"
        day = 2
        
        test =  all_act.checkOverlap(startTime, endTime, day)
        
        self.assertTrue(test) # no debería haber overlap

    def test_time_overlap_no_day_overlap(self):
        """
        2- Escenario donde las horas chocan pero en diferente fecha
        """
        startTime = "10:30"
        endTime = "11:30"
        day = 2
        test =  all_actall_act.checkOverlap(startTime, endTime, day)
        self.assertFalse(test) # no debería haber overlap
    
    def test_day_overlap_no_time_overlap(self):
        """
        3- Escenario donde choca el día pero no la hora
        """
        all_act = AllActivities()
        
        startTime = "8:30"
        endTime = "10:29"
        day = 2
        
        test = all_act.checkOverlap(startTime, endTime, day)
        
        self.assertFalse(test) # no debería haber overlap

    def test_without_activities(self):
        """
        4- Escenario donde no hay actividades
        """
        all_act = AllActivities()
        
        Activity.objects.filter(id=1).delete()
        
        startTime = "10:30"
        endTime = "11:30"
        day = 1
        
        test = all_act.checkOverlap(startTime, endTime, day)
        
        self.assertFalse(test) # hay overlap

    def test_no_overlap_time_edge(self):
        """
        5- Escenario donde choca el día y no la hora, 
        pero la hora de inicio del set up y la hora fin del test es la misma 
        """
        all_act = AllActivities()
        
        startTime = "8:30"
        endTime = "10:30"
        day = 1
        
        test = all_act.checkOverlap(startTime, endTime, day)
        
        self.assertFalse(test) # no debería haber overlap
    
    def test_time_day_overlap(self):
        """
        6- Escenario donde choca el día y la hora
        """
        all_act = AllActivities()
        startTime = "10:30"
        endTime = "11:30"
        day = 5
        
        test = all_act.checkOverlap(startTime, endTime, day)
        
        self.assertTrue(test) # hay overlap