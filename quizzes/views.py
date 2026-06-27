from django.shortcuts import render, get_object_or_404

from quizzes.models import Subject, Test


def home(request):
   return render(request, "home.html")

def subjects(request):
    context = {"subjects": Subject.objects.all()}
    return render(request, "subjects.html", context)


def subject_tests(request, subject_id):
   subject = get_object_or_404(Subject, pk=subject_id)
   context = {
      "subject": subject,
      "tests": subject.tests.all()
      }
   return render(request, "subject_tests.html", context)

def take_test(request, test_id):
   test = get_object_or_404(Test, pk=test_id)
   context = {
      "test": test,
      "questions": test.questions.all()
   }
   return render(request, "take_test.html", context)

def test_result(request, test_id):
   context = {
      "test": get_object_or_404(Test, pk=test_id)
   }
   return render(request, "test_result.html", context)