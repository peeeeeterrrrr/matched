from django.urls import path

from classmatchapp.views import MatchingListView

app_name = 'classmatchapp'

urlpatterns = [
    path('matchinglist/<int:pk>',MatchingListView.as_view(), name='matchinglist'),
]