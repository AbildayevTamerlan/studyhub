from django.urls import path

from .views import home, subjects, subject_tests, take_test, test_result, history

urlpatterns = [
    path("", home, name="home"),
    path("subjects/", subjects, name="subjects"),
    path("subjects/<int:subject_id>/", subject_tests, name="subject_tests"),
    path("tests/<int:test_id>/", take_test, name="take_test"),
    path("tests/<int:test_id>/result/", test_result, name="test_result"),
    path("history/", history, name="history"),
]
