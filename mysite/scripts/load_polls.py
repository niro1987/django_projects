import csv
import os

from django.utils import timezone
from polls.models import Choice, Question


def run():
    dt = timezone.now()
    
    Choice.objects.all().delete()
    Question.objects.all().delete()
    
    folder = os.path.dirname(os.path.relpath(__file__))
    filename = os.path.join(folder, "batch_polls.csv")
    print(filename)
    
    with open(filename, "r", encoding="utf-8") as f_in:
        reader = csv.reader(f_in)
        
        for row in reader:
            print(row)
            
            if len(row) < 2: continue
            q = Question(
                question_text = row[0],
                pub_date = dt,
            )
            q.save()
            
            for choice in row[1:]:
                c = Choice(
                    question=q,
                    choice_text = choice,
                    votes = 0,
                )
                c.save()
