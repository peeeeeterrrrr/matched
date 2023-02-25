from django.urls import path

from accountapp.views import AccountUpdateView, AccountDeleteView, AccountCreateView
from homescreenapp.views import HomeScreenListView

app_name = 'homescreenapp'

urlpatterns = [
    path('homescreen/',HomeScreenListView.as_view(template_name='homescreenapp/homescreen.html'), name='homescreen'),
]
