import csv
import datetime

from django.utils import timezone

from polls.models import Question, Choice

def run():
    print("=== Polls Loader")

    Choice.objects.all().delete()
    Question.objects.all().delete()
    print("=== Objects deleted")

    with open('scripts/dj4e_batch.csv') as f:
        reader = csv.reader(f)
        next(reader)  # Advance past the header

        for row in reader:
            question_text, *choice_text_list = row
            q = Question(question_text=question_text, pub_date=timezone.now())
            q.save()
            for choice_text in choice_text_list:
                q.choice_set.create(choice_text=choice_text)
            print(q)
            for choice in q.choice_set.all():
                print(f' * {choice}')
    print("=== Load Complete")
