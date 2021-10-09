from django.test import SimpleTestCase

from ..views import AllActivities

from calendar import IllegalMonthError
import datetime

class GetDatesByDayTestCase(SimpleTestCase):
    
    def setUp(self):
        self.all_act = AllActivities() 
    
    def test_non_existent_month(self):
        """
        Escenario cuando el mes ingresado no existe
        """
        try:
            self.all_act.getDatesByDay(1,13,2021)
        except IllegalMonthError:
            self.fail("There is not error handling with non-existen month")
    
    def test_non_existent_day(self):
        """
        Escenario cuando el numero del dia ingresado no existe
        """  
        try:
            self.all_act.getDatesByDay(10,10,2021)
        except IllegalMonthError:
            self.fail("There is not error handling with non-existen day")

    def test_negative_year(self):
        """
        Escenario cuando el año ingresado es negativo
        """
        try:
            self.all_act.getDatesByDay(1,10,-2020)
        except ValueError:
            self.fail("There is not error handling with negative year")
    
    def test_leap_year_and_day_29(self):
        """
        Escenario cuando el año que se ingresa es biciesto, y el dia ingresado cae 29
        """
        test = self.all_act.getDatesByDay(6,2,2020)
        self.assertEqual(test,[datetime.date(2020, 2, 1), datetime.date(2020, 2, 8), datetime.date(2020, 2, 15), datetime.date(2020, 2, 22), datetime.date(2020, 2, 29)])        
    
    def test_current_date(self):
        """
        Escenario donde se verifica el resultado con la fecha de la prueba como parametro.
        """ 
        test = self.all_act.getDatesByDay(4,10,2021)
        self.assertEqual(test,[datetime.date(2021, 10, 7), datetime.date(2021, 10, 14), datetime.date(2021, 10, 21), datetime.date(2021, 10, 28)])        

