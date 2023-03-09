from django.urls import path

from baseinformationapp.views import BaseinformationCreateView

app_name = 'baseinformationapp'

urlpatterns = [
    path('create/', BaseinformationCreateView.as_view(), name='create'),
]