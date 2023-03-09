from django.urls import path

from scholarshipapp.views import ScholarshipCreateView

app_name = 'scholarshipapp'

urlpatterns = [
    path('create/', ScholarshipCreateView.as_view(), name='create'),
]