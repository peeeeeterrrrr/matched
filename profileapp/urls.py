from django.urls import path

from profileapp.views import ProfileView
from studymanageapp.views import MyclassListView

app_name = 'profileapp'

urlpatterns = [
    path('profile/<int:pk>',ProfileView.as_view(), name='profile'),
]