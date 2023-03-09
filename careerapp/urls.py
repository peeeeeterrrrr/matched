from django.urls import path

from careerapp.views import CareerCreateView

app_name = 'careerapp'

urlpatterns = [
    path('create/', CareerCreateView.as_view(), name='create'),
]