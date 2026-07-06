from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from quizzes.models import Subject, Test, Question, Answer, Attempt, UserAnswer


def home(request):
    return render(request, "home.html")


def subjects(request):
    context = {"subjects": Subject.objects.all()}
    return render(request, "subjects.html", context)


def subject_tests(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    context = {"subject": subject, "tests": subject.tests.all()}
    return render(request, "subject_tests.html", context)


@login_required
def take_test(request, test_id):
    test = get_object_or_404(Test, pk=test_id)

    if request.method == "POST":
        attempt = Attempt.objects.create(user=request.user, test=test)
        correct_answers = 0

        for question in request.POST:
            if question.startswith("question_"):
                selected_answer = request.POST[question]
                answer = get_object_or_404(Answer, pk=selected_answer)

                if answer.is_correct:
                    correct_answers += 1

                UserAnswer.objects.create(
                    attempt=attempt,
                    question=answer.question,
                    answer=answer,
                    is_correct=answer.is_correct,
                )

        total_questions = test.questions.count()

        attempt.total_questions = total_questions
        attempt.correct_answers = correct_answers
        attempt.completed_at = timezone.now()
        attempt.save()  # insert the changes into database

        return render(request, "test_result.html", {"test": test, "attempt": attempt})
    else:
        context = {"test": test, "questions": test.questions.all()}
        return render(request, "take_test.html", context)


def test_result(request, test_id):
    context = {"test": get_object_or_404(Test, pk=test_id)}
    return render(request, "test_result.html", context)


@login_required
def history(request):
    attempts = request.user.attempts.all()
    return render(request, "history.html", {"attempts": attempts})
