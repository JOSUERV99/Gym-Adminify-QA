from django.test import TestCase
from views import AllActivities
# Create your tests here.
class GetDatesByDayTestCase(TestCase):

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        all_act = AllActivities() 
        all_act.getDatesByDay()
        self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')