from django.db import models
from django.conf import settings


class Subject(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Test(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE
    )  # many tests belong to one subject

    def __str__(self):
        return self.title


class Question(models.Model):
    text = models.TextField()
    test = models.ForeignKey(
        Test, on_delete=models.CASCADE
    )  # many questions belong to one test

    def __str__(self):
        return self.text[:50]


class Answer(models.Model):
    text = models.TextField()
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE
    )  # many answers belong to one question
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text[:50]


class Attempt(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )  # many attempts belong to one user
    test = models.ForeignKey(
        Test, on_delete=models.CASCADE
    )  # many attempts belong to one test
    score = models.FloatField(null=True, blank=True)
    correct_answers = models.PositiveIntegerField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user} — {self.test}"


class UserAnswer(models.Model):
    attempt = models.ForeignKey(
        Attempt, on_delete=models.CASCADE
    )  # many user answers belong to one attempt
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE
    )  # many user answers belong to one question
    answer = models.ForeignKey(
        Answer, on_delete=models.CASCADE
    )  # many user answers belong to one answer
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.attempt} — {self.question}"
