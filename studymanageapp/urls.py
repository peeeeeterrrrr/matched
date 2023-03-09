from django.urls import path

from studymanageapp.views import MyclassListView

app_name = 'studymanageapp'

urlpatterns = [
    path('myclasslist/<int:pk>',MyclassListView.as_view(), name='myclasslist'),
]