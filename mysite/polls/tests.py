
import datetime
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Question


# Create your tests here.

class QuestionModelTest(TestCase):

    def test_was_published_recently_with_old_question(self): 
        old_question = Question(pub_date = timezone.now() - datetime.timedelta(days = 2 ) )
        self.assertIs(old_question.was_published_recently(), False )
    
    def test_was_published_recently_with_recent_question(self):
        recent_question = Question(pub_date = timezone.now() + datetime.timedelta(days = 1 ))
        self.assertIs(recent_question.was_published_recently(), True)

    def test_was_published_recently_with_future_question(self):
        future_question = Question(pub_date = timezone.now() + datetime.timedelta(days = 2))
        self.assertIs(future_question.was_published_recently(), False)

   

