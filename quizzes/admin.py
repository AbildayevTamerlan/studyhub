from django.contrib import admin
from .models import Subject, Test, Question, Answer, Attempt, UserAnswer


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]
    search_fields = ["name"]


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "subject"]
    search_fields = ["title"]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ["text", "test"]
    search_fields = ["text"]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ["text", "question", "is_correct"]
    search_fields = ["text"]


@admin.register(Attempt)
class AttemptAdmin(admin.ModelAdmin):
    list_display = ["user", "test", "total_questions", "correct_answers", "completed_at"]
    list_filter = ["test", "completed_at"]
    search_fields = ["user__username", "test__title"]


@admin.register(UserAnswer)
class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ["attempt", "question", "answer", "is_correct"]
    list_filter = ["is_correct"]
    search_fields = ["question__text", "answer__text"]
