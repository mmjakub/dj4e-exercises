import datetime

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Question

class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        '''
        was_published_recently() return False for questions with future pub_date
        '''
        time = timezone.now() + datetime.timedelta(days=1)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
    def test_was_published_recently_with_old_question(self):
        '''
        was_published_recently() return False for questions older than a day
        '''
        time = timezone.now() + datetime.timedelta(days=-1)
        question = Question(pub_date=time)
        self.assertIs(question.was_published_recently(), False)
    def test_was_published_recently_with_recent_question(self):
        '''
        was_published_recently() return True for questions newer than a day
        '''
        time = timezone.now() + datetime.timedelta(days=-1, seconds=1)
        question = Question(pub_date=time)
        self.assertIs(question.was_published_recently(), True)
        
def create_question(question_text, days=-1):
    '''
    Create a question published at `days` offset from now
    '''
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        '''
        If there are no questions show a message instead
        '''
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No polls are available.')
        self.assertQuerySetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        '''
        Questions published in the past are displayed
        '''
        question = create_question('Past question', -1)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerySetEqual(
                response.context['latest_question_list'], [question])

    def test_future_question(self):
        '''
        Questions published in the future are not displayed
        '''
        question = create_question('Future question', 1)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, 'No polls are available.')
        self.assertQuerySetEqual(response.context['latest_question_list'], [])

    def test_two_past_questions(self):
        '''
        Multiple questions can appear on index
        '''
        q1 = create_question('Q1', -1)
        q2 = create_question('Q2', -2)
        res = self.client.get(reverse('polls:index'))
        self.assertQuerySetEqual(
                res.context['latest_question_list'], [q1, q2])

    def test_six_past_questions(self):
        '''
        No more than five questions are displayed
        '''
        questions = [create_question(f'Q{i}', -i) for i in range(1, 7)]
        not_displayed = questions.pop() 
        res = self.client.get(reverse('polls:index'))
        self.assertQuerySetEqual(
                res.context['latest_question_list'], questions)

class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        '''
        Detail page for feature question is not found
        '''
        q = create_question('Future', 1)
        res = self.client.get(reverse('polls:detail', args=(q.id,)))
        self.assertEqual(res.status_code, 404)
    def test_past_question(self):
        '''
        Detail view for published question contains qestion text
        '''
        q = create_question('Past', -1)
        res = self.client.get(reverse('polls:detail', args=(q.id,)))
        self.assertContains(res, q.question_text)
